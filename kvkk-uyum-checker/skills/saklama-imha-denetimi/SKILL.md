---
name: saklama-imha-denetimi
description: "Saklama sürelerinin mevzuat dayanağına uygunluğu, imha yöntemleri ve periyodik imha düzeni denetlenirken ya da saklama-imha politikası ve süre matrisi kurulurken kullanılır."
---

# Saklama ve İmha Politikası Denetimi

## Görev
KVKK m.4 (süreyle sınırlılık), m.7 (silme/yok etme/anonim hale getirme) ve İmha Yönetmeliği uyarınca saklama sürelerini, imha yöntemlerini ve periyodik imha düzenini denetlemek; süre matrisini mevzuat dayanağına oturtmak.

## Soğuk başlangıç (intake)
1. Veri kategorisi başına saklama süreleri belirlenmiş mi; dayanağı hangi kanun?
2. Saklama ve İmha Politikası var mı (VERBİS'e kayıtlılar için zorunlu)?
3. İmha hangi ortamlarda, hangi yöntemle yapılıyor (fiziksel, elektronik, bulut)?
4. Periyodik imha tutanağı ve logları tutuluyor mu?

## Denetim şeması
1. **Süre dayanağı testi (m.4/2-d)**: Her kategori için süre, kanuni saklama yükümlülüğü (örn. TTK m.82 ticari defterler, VUK saklama süreleri, iş hukuku zamanaşımları) ve amaç gereği ihtiyaç birlikte değerlendirilerek belirlenmeli; "ihtiyaten süresiz saklama" m.4 ihlalidir.
2. **İmha yükümlülüğünün doğması (m.7)**: İşleme sebebi sona erdiğinde veri re'sen veya talep üzerine silinir/yok edilir/anonim hale getirilir; üç yöntem ortam ve amaca göre seçilir.
3. **Periyodik imha**: İmha Yönetmeliği uyarınca politika sahibi sorumlu, periyodik imhayı azami 6 ayda bir yapar; işlemler kayıt altına alınır ve bu kayıtlar en az 3 yıl saklanır.
4. **Anonimleştirme kontrolü**: Geri döndürülebilen "anonimleştirme" hâlâ kişisel veridir ve KVKK kapsamındadır; tersine mühendislik testi yapılmalı.
5. **Ara sonuç**: Amaç bittiği halde saklamaya devam, hem m.4 ihlali hem TCK m.138 (verileri yok etmeme) riskidir; politika fiili imha kayıtlarıyla uyumlu olmalı.

İspat yükü: İmhanın usulüne uygun yapıldığını veri sorumlusu imha tutanağı ve loglarıyla ispatlar.

## Çıktı modülleri
- Veri kategorisi bazlı saklama süresi matrisi (mevzuat dayanağıyla).
- Saklama ve İmha Politikası uygunluk bulgu listesi.
- Periyodik imha tutanağı ve log şablonu.

## Plugin bağlamı

Bu beceri `kvkk-uyum-checker` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
