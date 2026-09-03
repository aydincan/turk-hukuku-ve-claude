---
name: hapis-infaz-rejimi
description: "Hapis cezasının kapalı/açık kurum rejimi, açığa ayrılma şartları, çağrı ve infaza başlama usulü ile nakil işlemlerini değerlendirmek gerektiğinde kullanılır."
---

# Hapis Cezası İnfaz Rejimi ve Açık Kuruma Ayrılma

## Görev
Hapis cezasının fiziki infaz rejimini belirlemek: çağrı ve infaza başlama, kapalı/açık kurum ayrımı, açığa ayrılma şartları ve nakil/gözlem süreçleri.

## Soğuk başlangıç (intake)
- Hükümlüye çağrı kâğıdı tebliğ edildi mi; kendiliğinden teslim mi olacak?
- Ceza miktarı ve suç tipi açık kuruma doğrudan ayrılmaya uygun mu?
- Sağlık, yaş, kadın/çocuk hükümlü gibi özel durum var mı?
- Tutuklu olarak hâlihazırda kapalı kurumda mı?

## Denetim şeması
1. İnfaza başlama: kesinleşen ilam Cumhuriyet Başsavcılığınca infaza verilir; hükümlüye çağrı kâğıdı çıkarılır (5275 m.19-20). Belirli hâllerde doğrudan yakalama emri düzenlenir. Ara sonuç: infaza giriş usulü.
2. Kurum türü: kural olarak kapalı kuruma alınma; ancak doğrudan açık kuruma ayrılma şartlarını taşıyanlar (kısa ceza, belirli suç dışı tipler) açık kuruma alınır (5275 m.14 ve Açık Ceza İnfaz Kurumlarına Ayrılma Yönetmeliği).
3. Açığa ayrılma: kapalı kurumdaki hükümlünün, koşullu salıverilmeye kalan süre ve iyi hâl şartıyla açık kuruma ayrılması; idare ve gözlem kurulu kararı (5275 m.89, m.14) belirleyicidir. İspat: iyi hâl ve disiplin sicili kurum kayıtlarıyla.
4. Nakil ve gözlem: gözlem ve sınıflandırma (5275 m.23), güvenlik ve disiplin gerekçeli nakiller; hükümlünün talebi veya idare kararıyla.
5. Özel rejimler: kadın, çocuk ve hasta hükümlüler için ayrı düzenlemeler; hastalık nedeniyle infazın ertelenmesi ayrı bir beceride değerlendirilir.
6. İtiraz: ayırma/nakil işlemine karşı infaz hâkimliği yolu (4675 sayılı Kanun). İlkesel içtihat karararama.yargitay.gov.tr, künye `[doğrulanacak]`.
7. Ara sonuç: kurum türü + açığa ayrılma uygunluğu + usul takvimi.

## Çıktı modülleri
- Rejim ve kurum türü tablosu.
- Açığa ayrılma şart kontrol listesi.
- Nakil/itiraz başvuru tetiği.

## Plugin bağlamı

Bu beceri `infaz-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
