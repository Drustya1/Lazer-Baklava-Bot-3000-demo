# Glass Bridge Duel

## Oyun Özeti
Glass Bridge Duel, iki oyunculu, gerilim dolu bir beceri ve hafıza oyunudur. Oyuncular, devasa bir uçurumun iki yakası arasında uzanan 20 sıralı cam bloktan oluşan bir köprüde ilerler. Her sırada yan yana duran iki cam panelden yalnızca biri sağlam, diğeri ise kırılgandır. Oyuncular, hangisinin güvenli olduğunu tahmin ederek sırayla ileri atlar. Doğru seçim onları bir sonraki sıraya taşırken, yanlış seçim oyuncuyu köprünün altındaki keskin kazıklara düşürür ve oyunu kaybettirir.

## Tema ve Atmosfer
* **Tema:** Distopik bir ölüm oyunu arenası; neon ışıklar, gerilimli müzikler ve dramatik sunumlarla desteklenir.
* **Atmosfer:** Her sıçrayışta artan kalp atış sesleri, seyirci tezahüratları ve camın hafif gıcırdaması gibi ses efektleriyle gerilim yükselir.
* **Görsel Stil:** Cam paneller ışığı kırarak hafif parlamalar yapar. Zemin aşağıda karanlık, sisli ve kazıklarla doludur. Oyuncuların kıyafetleri farklı renklerde ve futuristik çizgilere sahiptir.

## Bileşenler
* 20 sıra boyunca uzanan, her sırada 2 cam panel içeren köprü.
* Oyuncu avatarları (Oyuncu A ve Oyuncu B) ve onların konum göstergeleri.
* Seyirci hologramları veya ekranları (atmosfer için).
* Panel dayanıklılığına dair gizli veri tablosu (sadece oyun motoru tarafından bilinir).
* Skor/istatistik panosu: başarılı tahmin sayısı, kalan sağlam panel sayısı, tur sayısı.
* Gerilim müziği, düşüş animasyonları ve cam kırılma efektleri.

## Kurulum
1. Oyun başlarken 20 sıradan oluşan köprü rastgele hazırlanır. Her sırada bir panel "Sağlam" diğeri "Kırılgan" olarak işaretlenir.
2. Oyuncular köprünün başında yan yana başlar.
3. Oyun, başlangıç oyuncusunu rastgele seçer veya oyuncular anlaşır.

## Oynanış Yapısı
* Oyun turlarla ilerler; her tur bir oyuncunun hamlesini içerir.
* Oyuncular sırayla seçtikleri panelin üzerine atlar.
* Oyuncu sağlam panele atlarsa bir sonraki sıraya geçer ve hamle sırası diğer oyuncuya geçer.
* Oyuncu kırılgan panele atlarsa panel kırılır, oyuncu aşağıya düşer ve kaybeder. Diğer oyuncu oyunu kazanır.
* Eğer bir oyuncu 20. sırayı da geçer ve uçurumun karşı tarafına ulaşırsa, o oyuncu oyunu kazanır.

## Oyun Döngüsü
1. **Gözlem:** Oyuncu, önündeki iki paneli inceler (görsel fark bulunmaz).
2. **Karar:** Oyuncu hangi panelin sağlam olabileceğine karar verir. Taktiksel olarak önceki seçimlere göre olasılık hesabı yapabilir.
3. **Hamle:** Seçilen panel üzerine atlanır.
4. **Geri Bildirim:** Panel sağlam ise oyuncu yeni sırada kalır ve tur biter. Panel kırılırsa düşüş animasyonu ve ses efektleri oynatılır.
5. **Devam:** Diğer oyuncu için 1. adıma dönülür.

## İki Kişilik Dinamikler
* Oyuncuların hamle sırası önemlidir. İlk oyuncu risk alırken ikinci oyuncu bilgi toplar.
* Her sağlam panel keşfedildiğinde bilgi her iki oyuncu için de açığa çıkar. Sonraki oyuncu bu bilgiden yararlanabilir.
* Eğer bir oyuncu düşerse diğer oyuncu otomatik olarak kazanır. Eğer bir oyuncu köprüyü tamamlarsa rakibi kaybetmiş sayılır.
* İki oyuncunun da hafızasını test eder: Eğer ilk oyuncu bir sıradaki sağlam paneli bulur ancak geri adım atmak zorunda kalırsa (örneğin opsiyonel zorluklar eklenirse) diğer oyuncu bu bilgiyi kullanabilir.

## Opsiyonel Kurallar ve Modlar
* **Zaman Baskısı:** Her hamle için 10 saniyelik süre; süre dolarsa oyuncu panik atlayış yapar ve rastgele bir panel seçilir.
* **İpucu Jetonu:** Her oyuncuya oyunun başında birer ipucu jetonu verilir. Kullanıldığında oyun motoru seçilen sırada hangi panelin sağlam olduğunu ışıkla kısaca gösterir.
* **Ekip Çalışması Modu:** Oyuncular aynı anda ilerler, ancak farklı kulvarlarda. Bir oyuncu düşerse oyun kaybedilir; kazanmak için iki oyuncunun da karşıya ulaşması gerekir.
* **Rekabet Puanları:** Köprünün kaçıncı sırasında düştüğünüze göre puan verilir. 10 tur sonunda en yüksek puanlı oyuncu kazanır.

## Dijital Uygulama Notları
* **Fizik Motoru:** Panel kırılma animasyonları ve düşüş efektleri için fizik tabanlı simülasyon (ör. Unity veya Unreal Engine).
* **Panel Durumu Verisi:** 20x2 boyutlu bir dizi; `true` sağlam, `false` kırılgan.
* **Sıra Yönetimi:** Tur sistemi; aktif oyuncu değişimi için basit bir boolean.
* **Çok Oyuncu Desteği:** Yerel iki oyuncu (aynı klavye/gamepad) veya çevrimiçi sıra tabanlı oynanış.
* **Ses Tasarımı:** Panik müziği, nabız efekti, cam çatlama, düşüş çığlığı.
* **Arayüz:** Panel seçim göstergeleri, kalan ipucu sayısı, tur sayacı.

## Kazanma ve Kaybetme
* **Kazanma:** Bir oyuncu köprünün sonuna ulaşırsa veya rakibi düşerse kazanır.
* **Kaybetme:** Kırılgan panele basıldığında gerçekleşir.
* **Beraberlik:** Yoktur. Opsiyonel modlarda eşzamanlı düşüş durumunda son sıraya kadar ilerleyen kazanır veya tekrar oynanır.

## Anlatı ve İlerleme
* Her başarılı geçiş, hikâyede oyuncuların popülerliğini arttırır; sonraki turlarda seyirci baskısı artar.
* Kazanılan oyunlarla yeni kıyafetler, müzikler veya atmosfer efektleri açılabilir.

## Ses ve Görsel İpuçları
* Sağlam panel üzerinde kısa süreli bir titreşim ve hafif beyaz parıltı gösterilebilir.
* Kırılgan panel seçildiğinde önce ince çatlak sesleri, ardından dramatik kırılma efekti oynatılır.

## Test ve Dengeleme Önerileri
* Panel dağılımı tamamen rastgele; ancak aynı kulvardaki sağlam panel sayısının 3’ten fazla uzamasını engelleyen bir kural eklenebilir.
* Yeni oyuncular için öğretici bölüm: İlk iki sıra garantili sağlam panellerle başlar, ardından gerçek oyuna geçilir.

## Genişletme Fikirleri
* Farklı köprü uzunlukları (ör. 15 sıra hızlı mod, 25 sıra uzman modu).
* Özel beceriler: "Cam Dinleyicisi" yeteneği ile oyuncu camın titreşimine bakarak ipucu alır.
* Seyirci bahis sistemi: Çevrimiçi modda izleyiciler hangi oyuncunun kazanacağına dair oy verebilir.

