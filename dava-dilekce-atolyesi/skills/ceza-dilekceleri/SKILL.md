---
name: ceza-dilekceleri
description: "Suç duyurusu/şikâyet, katılma talebi, tahliye-itiraz ve esas hakkında savunma gibi ceza muhakemesi dilekçelerini CMK çerçevesinde hazırlamak gerektiğinde kullanılır."
---

# Ceza Muhakemesi Dilekçeleri (CMK)

## Görev
Soruşturma ve kovuşturma evrelerinde mağdur/şüpheli/sanık vekilliğine uygun dilekçeleri üretmek: şikâyet/suç duyurusu, katılma, koruma tedbirine itiraz ve savunma dilekçeleri.

## Soğuk başlangıç (intake)
- Hangi evre: soruşturma mı, kovuşturma mı?
- Müvekkil mağdur/müşteki mi, şüpheli/sanık mı, katılan mı?
- Şikâyete bağlı suç mu, şikâyet süresi (TCK m.73 — 6 ay) işliyor mu?
- Tutuklama/adli kontrol gibi bir koruma tedbiri var mı?

## Denetim şeması
1. Şikâyet/suç duyurusu (CMK m.158): Cumhuriyet başsavcılığına yazılır; suça konu vakıalar, deliller ve fail bilgileri. Şikâyete bağlı suçlarda TCK m.73 — fiilin ve failin öğrenilmesinden itibaren 6 ay; süre geçerse şikâyet hakkı düşer.
2. Katılma (CMK m.237-239): Suçtan zarar gören, kovuşturmada katılma talep eder; davaya katılma kararı verilirse haklar genişler.
3. Koruma tedbirine itiraz (CMK m.267-271): Tutuklama, adli kontrol ve diğer hâkim/mahkeme kararlarına itiraz; süre kural olarak yedi gün (m.268). Salıverilme talebi (m.104) her zaman mümkündür.
4. Savunma/esas hakkında beyan: İddianamedeki (m.170) suç vasıflandırmasını tartışın; suç genel teorisi katmanlarına göre (tipiklik, hukuka aykırılık, kusurluluk) savunmayı kurun; lehe deliller ve TCK m.21/22 kast-taksir ayrımı.
5. Delil değerlendirme: Hukuka aykırı delil yasağı (CMK m.206/2, m.217/2; Anayasa m.38/6). Ara sonuç: evre ve sıfata uygun dilekçe, süre içinde hazır.

## Çıktı modülleri
- İlgili ceza dilekçesi taslağı (şikâyet/katılma/itiraz/savunma)
- Süre uyarısı (şikâyet 6 ay, itiraz 7 gün)
- Delil ve tanık listesi
- Talep bloğu (soruşturma işlemi/salıverilme/beraat vb.)

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
