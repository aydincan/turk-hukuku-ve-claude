---
name: hesap-maddi-hata-denetimi
description: "Tazminat, alacak, faiz, kıdem-ihbar veya değer hesabı içeren raporlarda aritmetik doğruluğu, faiz başlangıcı ve oranını, birim-tarih tutarlılığını ve ıslah-zamanaşımı kesişimini kontrol etmek istendiğinde kullanılır."
---

# Hesap ve Maddi Hata Denetimi

## Görev
Hesap içeren raporlarda sayısal sonucu yeniden üretmek: aritmetik, faiz, birim ve tarih tutarlılığını denetleyip maddi hataları somut rakamla göstermek; yanlış kalemin doğru karşılığını önermek.

## Soğuk başlangıç (intake)
- Hesabın türü nedir (işçilik alacağı, tazminat, alacak/faiz, taşınmaz değeri vb.)?
- Hesaba esas alınan dönem, oran ve birimler raporda açık mı?
- Faiz türü (yasal/avans/temerrüt) ve başlangıç tarihi gösterilmiş mi?
- Davada ıslah veya zamanaşımı def'i var mı?

## Denetim şeması
1. **Aritmetik yeniden üretim:** Ara toplamlar ve nihai rakam kalem kalem yeniden hesaplanır; her sapma somut farkıyla yazılır. Birim (TL/USD), oran (%) ve tarih tutarlılığı kontrol edilir.
2. **Faiz denetimi:** Faiz türü dava ve borç niteliğine uygun mu; başlangıç tarihi temerrüt/dava/olay tarihiyle örtüşüyor mu; oran ve yürürlük tarihi doğru mu? Ticari işlerde avans faizi ile yasal faiz ayrımına dikkat edilir.
3. **Zamanaşımı-ıslah kesişimi:** Zamanaşımı def'i varsa hesaplanan kalemlerin zamanaşımına uğrayan kısmı ayrıştırılır. Islahla artırılan miktarın zamanaşımı yönünden ayrı değerlendirilmesi gerekir; rapor bunu gözetmemişse hata kalemidir.
4. **Veri tabanı denetimi:** Asgari ücret, kıdem tavanı, faiz oranı gibi parametreler yürürlük tarihiyle ve resmî kaynağıyla doğrulanır; eski/yanlış parametre kullanımı maddi hatadır.
5. **Ara sonuç:** Maddi/hesap hatası tamamlanabilir nitelikte olduğundan kural olarak **ek rapor** ile düzeltme istenir (HMK m.281); hata yöntemden kaynaklanıyorsa yeni heyete gidilir.

## Çıktı modülleri
- Kalem kalem doğru/yanlış karşılaştırma tablosu (rapordaki / olması gereken / fark).
- Faiz başlangıç-oran-tür denetim notu.
- Zamanaşımı/ıslah etkisinin ayrı dökümü.
- Ek rapor talebine eklenecek düzeltilmiş hesap özeti.

## Plugin bağlamı

Bu beceri `bilirkisi-rapor-inceleme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
