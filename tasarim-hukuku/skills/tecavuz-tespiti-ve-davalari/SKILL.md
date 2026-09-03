---
name: tecavuz-tespiti-ve-davalari
description: "Tasarım hakkına tecavüz fiillerinin SMK m.81 ve m.149-150 çerçevesinde tespiti, açılacak davaların ve taleplerin belirlenmesi; üçüncü kişinin tasarımı taklit/kullanım iddiası karşısında strateji kurulması gerektiğinde kullanılır."
---

# Tecavüz Tespiti ve Davaları

## Görev
Tasarım hakkına tecavüzü tespit etmek ve uygun davaları/talepleri belirlemek: hangi fiil tecavüzdür, hangi talepler ileri sürülür, husumet kime yöneltilir ve hükümsüzlük def'i nasıl karşılanır.

## Soğuk başlangıç (intake)
1. Korunan tasarım tescilli mi, tescilsiz mi; sicil/koruma durumu nedir?
2. Tecavüz iddia edilen fiil nedir (üretim, satış, ithalat, ticari kullanım, depolama)?
3. Karşı ürün görselleri ile korunan tasarım görselleri yan yana var mı?
4. Karşı taraf tasarımın hükümsüzlüğünü ileri sürebilir mi (önceki tasarım var mı)?

## Denetim şeması
1. Tecavüz fiilleri (SMK m.81/1): Tasarım sahibinin izni olmadan tasarımı kullanma; özellikle aynısının veya genel izlenim itibarıyla ayırt edilemeyenin üretimi, piyasaya sürülmesi, satışı, ithali, ticari amaçla elde bulundurulması/kullanılması. Tescilsizde ayrıca kopyalama unsuru aranır (m.57/2).
2. Koruma kapsamı karşılaştırması (SMK m.57): "Bilgilenmiş kullanıcı"da bıraktığı genel izlenim aynı/ayırt edilemez ise tecavüz vardır. Karşılaştırma görsel ve bütünseldir; seçenek özgürlüğü darsa benzerlik eşiği yükselir.
3. Önceki kullanım / tüketilme: Sessiz kalma yoluyla hak kaybı (SMK m.81/3 ve genel hükümler), hakkın tüketilmesi (m.152) ve ön kullanım hakkı (m.81/2'ye bağlı durumlar) savunma olarak değerlendirilir.
4. Talepler (SMK m.149): Tecavüzün tespiti, durdurulması (men), giderilmesi (ref), maddi ve manevi tazminat, el koyma, ürünler/araçlar üzerinde mülkiyet/imha/şekil değiştirme, kararın ilanı. İhtiyati tedbir için m.159 ve HMK m.389 vd.
5. Hükümsüzlük def'i (SMK m.81/2): Tecavüz davasında davalı, tasarımın hükümsüz olduğunu def'i olarak ileri sürebilir; hükümsüzlük tespitiyle tecavüz iddiası düşer. Bu nedenle dava açmadan önce kendi tasarımınızın geçerliliğini test edin.
6. Görev/yetki (SMK m.156): FSHHM; yetki davalının yerleşim yeri veya tecavüzün işlendiği yer.

## Çıktı modülleri
- Yan yana görsel karşılaştırma ve genel izlenim analizi.
- Talep matrisi (tespit/men/ref/tazminat/el koyma/imha/ilan) ve dayanak maddeler.
- Hükümsüzlük riski değerlendirmesi ve dava açma kararı notu.

## Plugin bağlamı

Bu beceri `tasarim-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
çalışır; bir konu eklentinin dışına taştığında ilgili başka eklentiyi işaret eder,
aksi hâlde bu eklentinin uygun bir sonraki becerisini önerir.

## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar; mahkeme (Yargıtay / Danıştay /
  Anayasa Mahkemesi / Bölge Adliye Mahkemesi / Bölge İdare Mahkemesi), daire, **esas ve
  karar numarası**, tarih ve doğrulanabilir kaynak ile verilir
  (ör. `karararama.yargitay.gov.tr`, `karararama.danistay.gov.tr`,
  `kararlarbilgibankasi.anayasa.gov.tr`, `mevzuat.gov.tr`, UYAP Emsal).
  **Model hafızasından karar numarası ÜRETME.** Emin olunmayan her künye `[doğrulanacak]`
  olarak işaretlenir.
- **Mevzuat** madde / fıkra / bent ile gösterilir (ör. "TBK m.49/1", "HMK m.114/1-ç").
- **Doktrin** yalnızca kullanıcı kaynağı sağladığında veya lisanslı canlı erişim
  belgelendiğinde kullanılır; yazar, eser, baskı ve sayfa ile.
- Varsayımlar açıkça **"varsayım"** diye işaretlenir; sahte kesinlik üretilmez.
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
