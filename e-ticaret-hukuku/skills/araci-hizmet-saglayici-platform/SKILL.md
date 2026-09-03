---
name: araci-hizmet-saglayici-platform
description: "Pazar yeri veya platform işleten ya da platformda satış yapan tarafın 6563 m.9 kapsamındaki aracı sorumluluğu, uyar-kaldır ve ETAHS yükümlülüklerinin değerlendirilmesi gerektiğinde kullanılır."
---

# Aracı Hizmet Sağlayıcı ve Platform Sorumluluğu

## Görev
Pazar yeri/platform (aracı hizmet sağlayıcı) ile platformda satış yapan hizmet sağlayıcı arasındaki sorumluluk dağılımını ve 7416 sayılı Kanunla gelen ETAHS yükümlülüklerini değerlendirmek.

## Soğuk başlangıç (intake)
- Müvekkil platform mu (ETAHS) yoksa platform satıcısı mı (ETHS)?
- Platformun yıllık net işlem hacmi ve işlem sayısı hangi eşik bandında?
- Uyuşmazlık konusu: üçüncü kişi içeriği/hak ihlali mi, reklam/indirim sınırı mı, ödeme/komisyon mu?
- Hak sahibinin bildirimi (uyar-kaldır) yapıldı mı?

## Denetim şeması
1. Genel kural (6563 m.9): aracı hizmet sağlayıcı, hizmet sunduğu içeriği kontrol etmek ve hukuka aykırılığı araştırmakla yükümlü değildir; kural olarak başkalarına ait içerikten sorumlu tutulmaz.
2. Uyar-kaldır: 5651 ve 6563 çerçevesinde hak ihlali iddiası usulüne uygun bildirildiğinde platform makul sürede gereğini yapmazsa sorumluluğu doğabilir; fikri mülkiyet ihlallerinde özel bildirim-kaldırma mekanizması işler.
3. ETAHS kademeli yükümlülükleri (7416 değişiklikleri): net işlem hacmine göre "elektronik ticaret aracı hizmet sağlayıcı", "büyük" ve "çok büyük" ETAHS kategorileri; reklam ve indirim bütçesi sınırları, kendi markalı ürün satış kısıtları, lisans alma ve lisans bedeli, veri taşınabilirliği ve eşit muamele yükümlülükleri devreye girer.
4. Sözleşmesel dağılım: ETAHS-ETHS arasındaki aracılık sözleşmesinde sorumluluk, komisyon, fikri haklar ve cezai şart denetlenir.
5. Yaptırım: 6563 m.12 idari para cezaları ve faaliyet durdurma/erişim engelleme riskleri.
İspat yükü: bildirimin usulüne uygunluğu hak sahibinde, gereğinin yapıldığı platformdadır.
Ara sonuç: kategori + tetiklenen yükümlülükler + sorumluluk eşiği.

## Çıktı modülleri
- ETAHS kategori ve yükümlülük haritası.
- Uyar-kaldır prosedürü ve cevap taslağı.
- Aracılık sözleşmesi risk notu.

## Plugin bağlamı

Bu beceri `e-ticaret-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
