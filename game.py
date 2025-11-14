"""Text tabanlı Lazer Baklava Bot 3000 macera oyunu."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


Coordinate = Tuple[int, int]


@dataclass
class RobotState:
    """Lazer Baklava Bot 3000'in oyun boyunca takip edilen özellikleri."""

    position: Coordinate
    lives: int = 3
    energy: int = 10
    baklava_inventory: int = 2
    story_flags: Dict[str, bool] = field(default_factory=dict)

    def lose_life(self) -> None:
        self.lives -= 1

    def gain_life(self) -> None:
        self.lives += 1

    def spend_energy(self, amount: int = 1) -> None:
        self.energy -= amount

    def restore_energy(self) -> None:
        self.energy = 10


class LazerBaklavaGame:
    """Robotun sokaktan kaçıp uzay pistine ulaşmasını sağlayan mini oyun."""

    START_POS: Coordinate = (1, 1)
    EXIT_TILE: str = "X"
    HUMAN_TILES = {"H"}
    DOG_TILES = {"D"}
    BAKLAVA_TILES = {"B"}
    SWITCH_TILES = {"N"}

    MOVE_DELTAS: Dict[str, Coordinate] = {
        "w": (-1, 0),
        "a": (0, -1),
        "s": (1, 0),
        "d": (0, 1),
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    def __init__(self) -> None:
        self.base_map: List[List[str]] = [
            list("##########"),
            list("#S..H...B#"),
            list("#.##.##..#"),
            list("#..D..H..#"),
            list("#B..N..D.#"),
            list("#..##..#.#"),
            list("#..H...#.#"),
            list("#....##..#"),
            list("#..D....X#"),
            list("##########"),
        ]
        self.robot = RobotState(self.START_POS)
        self.reset_game(full_reset=True)

    def reset_game(self, full_reset: bool = False) -> None:
        """Robotun konumunu ve kaynaklarını yeniler."""

        if full_reset:
            # Robotun çantası ve yaşam puanları tamamen sıfırlanır.
            self.robot = RobotState(position=self.START_POS)
            self.map_state = [row[:] for row in self.base_map]
        else:
            self.robot.position = self.START_POS

        self.robot.energy = 10

    # ------------------------------------------------------------------
    # Oyun döngüsü ve yardımcılar
    # ------------------------------------------------------------------
    def run(self) -> None:
        self.print_intro()

        while True:
            self.render()
            command = input(
                "Komut gir (WASD/yön, 'eat', 'baklava', 'quit'): "
            ).strip().lower()

            if command in {"quit", "q"}:
                print("Robot diyarına giden yolculuk bir başka zamana kaldı. Görüşmek üzere!")
                return

            if command in {"eat", "ye"}:
                self.handle_eat_command()
                continue

            if command in {"baklava", "envanter"}:
                self.describe_inventory()
                continue

            if command not in self.MOVE_DELTAS:
                print("Anlaşılamayan komut. WASD veya yön kelimelerini kullanabilirsin.")
                continue

            self.process_move(command)

    def handle_eat_command(self) -> None:
        if self.robot.baklava_inventory <= 0:
            print("Çantanda soğuk baklava kalmamış! Yenilerini sokakta aramalısın.")
            return

        self.robot.baklava_inventory -= 1
        self.robot.gain_life()
        print(
            "Mis gibi soğuk baklavayı mideye indirdin. Canın bir arttı!"
            f" (Toplam can: {self.robot.lives})"
        )

    def describe_inventory(self) -> None:
        print(
            "Çanta durumu:"
            f"\n- Soğuk baklava: {self.robot.baklava_inventory}"
            "\n- Nintendo Switch 2 (EA Sports 2025, Fall Guys, Süper Mario World,"
            " Ateş ve Su, Minecraft Dungeons)"
            "\n- 1.000.000 TL (Mahmut Bey'e uzay bileti için hazır)"
        )

    def process_move(self, command: str) -> None:
        delta = self.MOVE_DELTAS[command]
        new_row = self.robot.position[0] + delta[0]
        new_col = self.robot.position[1] + delta[1]

        if not self.can_move_to((new_row, new_col)):
            print("Titanyum bedeninle bile bu duvardan geçemezsin!")
            return

        self.robot.position = (new_row, new_col)
        self.robot.spend_energy()

        if self.robot.energy <= 0:
            print(
                "Enerjin tükendi! Nintendo Switch 2'yi şarj etmeden bu macera bitmez."
            )
            print("Mahalle en baştan yükleniyor...")
            self.reset_game(full_reset=True)
            return

        tile = self.map_state[new_row][new_col]

        if tile in self.HUMAN_TILES | self.DOG_TILES:
            self.handle_threat(tile)
            return

        if tile in self.BAKLAVA_TILES:
            self.collect_baklava((new_row, new_col))

        if tile in self.SWITCH_TILES:
            self.charge_energy()

        if tile == self.EXIT_TILE:
            self.complete_mission()

    def can_move_to(self, coordinate: Coordinate) -> bool:
        row, col = coordinate
        return self.map_state[row][col] != "#"

    # ------------------------------------------------------------------
    # Oyun olayları
    # ------------------------------------------------------------------
    def handle_threat(self, tile: str) -> None:
        threat = "insan" if tile in self.HUMAN_TILES else "köpek"
        print(
            f"Bir {threat} tarafından yakalandın! Lazer gözlerinle sadece kaçacak bir"
            " açık bulabiliyorsun."
        )
        self.robot.lose_life()

        if self.robot.lives <= 0:
            print(
                "Tüm canlarını kaybettin. Lazer Baklava Bot 3000 yeniden başlatılıyor..."
            )
            self.reset_game(full_reset=True)
        else:
            print(f"Kalan can: {self.robot.lives}. Başlangıç noktasına ışınlanıyorsun.")
            self.reset_game(full_reset=False)

    def collect_baklava(self, coordinate: Coordinate) -> None:
        row, col = coordinate
        self.map_state[row][col] = "."
        self.robot.baklava_inventory += 1
        print(
            "Yerlerdeki gizli tepsiye ulaştın! Çantana bir soğuk baklava daha ekledin."
            f" (Toplam: {self.robot.baklava_inventory})"
        )

    def charge_energy(self) -> None:
        self.robot.restore_energy()
        print(
            "Nintendo Switch 2'yi açtın ve biraz oyun oynadın. Enerjin tavana vurdu!"
            f" (Enerji: {self.robot.energy})"
        )

    def complete_mission(self) -> None:
        print(
            "Mahmut Bey'e 1.000.000 TL'yi teslim ettin. Uzay pisti kapılarını açıyor!\n"
            "Lazer Baklava Bot 3000 artık Mars'taki Robot Diyarına doğru yola çıktı."
        )
        raise SystemExit

    # ------------------------------------------------------------------
    # Görselleştirme ve hikâye metinleri
    # ------------------------------------------------------------------
    def print_intro(self) -> None:
        print(
            """
================== LAZER BAKLAVA BOT 3000 ==================
Boy: 15 cm | Malzeme: Paslanmaz titanyum | Gözler: Kahverengi lazer
Çanta: Soğuk baklava (2 adet), Nintendo Switch 2, 1.000.000 TL
Enerji: 1 milyon yıl dayanabilen piller (ama oyunda 10 birimlik enerji ile başlıyorsun)
Görev: İnsanlardan ve köpeklerden kaç, uzay pistine ulaş ve Mars'taki Robot Diyarına git!

Kontroller: WASD veya UP/DOWN/LEFT/RIGHT yaz.
"eat" komutu çantandaki bir soğuk baklavayı yiyip +1 can verir.
"baklava" komutu envanteri gösterir.
===========================================================
            """
        )

    def render(self) -> None:
        printable_rows: List[str] = []
        for r_idx, row in enumerate(self.map_state):
            rendered_row: List[str] = []
            for c_idx, tile in enumerate(row):
                if (r_idx, c_idx) == self.robot.position:
                    rendered_row.append("R")
                elif tile == "#":
                    rendered_row.append("#")
                elif tile == "X":
                    rendered_row.append("🚀")
                elif tile in self.HUMAN_TILES:
                    rendered_row.append("H")
                elif tile in self.DOG_TILES:
                    rendered_row.append("D")
                elif tile in self.BAKLAVA_TILES:
                    rendered_row.append("🥮")
                elif tile in self.SWITCH_TILES:
                    rendered_row.append("🎮")
                else:
                    rendered_row.append(".")
            printable_rows.append("".join(rendered_row))

        stats = (
            f"Can: {self.robot.lives} | Enerji: {self.robot.energy}"
            f" | Çantadaki soğuk baklava: {self.robot.baklava_inventory}"
        )

        print("\n".join(printable_rows))
        print(stats)


def main() -> None:
    game = LazerBaklavaGame()
    try:
        game.run()
    except SystemExit:
        pass


if __name__ == "__main__":
    main()
