---
name: arsa-payi-kat-irtifaki
description: "Bağımsız bölümlere bağlanan arsa paylarının hatalı/dengesiz olması, kat irtifakı kurulması ya da iskân sonrası kat mülkiyetine geçiş gerektiğinde; arsa payı düzeltme davası ve KMK kuruluş işlemleri için kullanılır."
---

# Arsa Payı Düzeltimi, Kat İrtifakı ve Kat Mülkiyetine Geçiş

## Görev
Bağımsız bölümlere bağlı arsa payı ilişkisini doğru kurmak: kat irtifakı/kat mülkiyetinin kuruluşunu denetlemek ve bağımsız bölümün değeriyle orantısız (hatalı) arsa paylarının düzeltilmesi davasını yürütmek.

## Soğuk başlangıç (intake)
- Yapıda kat irtifakı mı, kat mülkiyeti mi kurulu; yoksa hiç kurulmamış mı (cins tashihi/iskân durumu)?
- Arsa payları bağımsız bölümlerin değeriyle orantılı mı; hangi bölüm lehine/aleyhine sapma var?
- Düzeltme talebi tüm malikleri mi etkiliyor; yönetim planı ve proje mevcut mu?
- İskân (yapı kullanma izni) alındı mı; kat mülkiyetine geçiş için belgeler tam mı?

## Denetim şeması
1. **Kavram**: Kat irtifakı, henüz tamamlanmamış yapıda bağımsız bölümler üzerinde ileride kat mülkiyeti kurulmak üzere arsa payına bağlı kurulan irtifaktır (634 sayılı KMK m.2, m.3, m.10). Kat mülkiyeti ise tamamlanmış yapıda bağımsız bölüm üzerindeki tam mülkiyettir.
2. **Arsa payının niteliği**: Her bağımsız bölüme, değeriyle orantılı arsa payı özgülenir (KMK m.3/2). Arsa payı bağımsız bölümden ayrı devredilemez, ona bağlı (bütünleyici) gider.
3. **Arsa payı düzeltimi**: Arsa payları, bağımsız bölümlerin değeriyle oransızsa, her kat maliki/irtifak sahibi hâkimden düzeltme isteyebilir (KMK m.3/son'a göre, projedeki değerler esas alınarak). Dava, oransızlığın değerleme (bilirkişi) ile ortaya konmasına dayanır ve tüm bağımsız bölüm maliklerine husumet yöneltilir.
4. **Kat mülkiyetine geçiş**: Yapı tamamlanıp yapı kullanma izni (iskân) alınınca, kat irtifakı kat mülkiyetine çevrilir (KMK m.14, m.12'deki belgelerle). Resen veya malik talebiyle tapuda dönüşüm yapılır.
5. **Kuruluş belgeleri (KMK m.12)**: Mimari proje, yapı kullanma izni, yönetim planı ve liste; eksiklik kuruluşu engeller.
6. **Ara sonuç**: Oransız paylar düzeltme davasıyla projedeki değerlere göre yeniden belirlenir; tamamlanan yapıda kat irtifakı kat mülkiyetine dönüştürülür.

## Çıktı modülleri
- Arsa payı düzeltme dava dilekçesi iskeleti (oransızlık iddiası, değerleme, husumet listesi).
- Kat mülkiyetine geçiş belge kontrol listesi (proje, iskân, yönetim planı).
- Görev/yetki notu: sulh hukuk mahkemesi (KMK Ek m.1; HMK m.4), taşınmazın yeri.

## Plugin bağlamı

Bu beceri `gayrimenkul-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
