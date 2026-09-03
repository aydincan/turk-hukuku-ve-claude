---
name: tam-yargi-davasi
description: "İdarenin işlem veya eyleminden doğan maddi-manevi zararın tazmini için tam yargı davasını ve idarenin kusurlu/kusursuz sorumluluk rejimini değerlendirmek amacıyla kullanılır; zarar gören kişiye tazminat aranacağında başvurulur."
---

# Tam Yargı Davası ve İdarenin Sorumluluğu

## Görev
İdarenin işlem/eyleminden doğan zararın tazmini için tam yargı davasını kurgulamak ve idarenin sorumluluk türünü (hizmet kusuru / kusursuz sorumluluk) belirlemek. İYUK m.2/1-b ve Anayasa m.125/son ekseninde çalışır.

## Soğuk başlangıç (intake)
1. Zarar bir idari işlemden mi, idari eylemden mi (fiili faaliyet/ihmal) doğuyor?
2. Zararın türü (maddi/manevi) ve miktarı belirlenebiliyor mu; belgeleri var mı?
3. Zarar tarihi ve idarenin zarara yol açan davranışı ne zaman öğrenildi?
4. İYUK m.13 ön başvurusu (eylemlerde) yapıldı mı?

## Denetim şeması
1. **Sorumluluğun kaynağı.** İşlemden doğan zararda iptal + tazmin birlikte istenebilir; eylemden doğan zararda İYUK m.13 uyarınca **önce idareye başvuru** zorunludur (eylemin/zararın öğrenilmesinden itibaren bir yıl ve her halde beş yıl içinde).
2. **Sorumluluk türü.** (a) **Hizmet kusuru:** hizmetin kötü işlemesi, geç işlemesi veya hiç işlememesi. (b) **Kusursuz sorumluluk:** risk ilkesi ve fedakârlığın denkleştirilmesi (sosyal risk dâhil belirli hallerde). Kusursuz sorumlulukta kusur aranmaz, illiyet ve zarar yeterlidir.
3. **Unsurlar.** Zarar (gerçek, kesin, kişisel), idareye yüklenebilir davranış ve **illiyet bağı**. İlliyeti kesen mücbir sebep, beklenmeyen hal, zarar görenin/üçüncü kişinin ağır kusuru sorumluluğu kaldırabilir veya azaltabilir.
4. **Süre.** İşlemden doğan tazminatta dava süresi iptal davası süresine bağlanır (İYUK m.7, m.12); eylemde m.13 başvurusu üzerine ret/zımni ret sonrası dava süresi işler.
5. **İspat.** Re'sen araştırma (İYUK m.20) geçerli olsa da zarar ve illiyeti davacı ortaya koymalı; tazminat hesabında bilirkişi sıkça devreye girer.
6. **Ara sonuç.** Sorumluluk türü + unsurların karşılanma durumu + talep edilebilir tazminat kalemleri (maddi/manevi, faiz başlangıcı).

## Çıktı modülleri
- Sorumluluk türü ve gerekçesi.
- Unsur (zarar/illiyet/yüklenebilirlik) değerlendirme tablosu.
- İYUK m.13 başvuru dilekçesi taslağı (eylem halinde).
- Tazminat kalemleri ve faiz talebi notu.

## Plugin bağlamı

Bu beceri `idare-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
