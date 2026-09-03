---
name: rtuk-yayin-denetimi
description: "Radyo, televizyon ve isteğe bağlı yayın hizmetlerinde yayın ilkelerine aykırılık, RTÜK idari para cezaları ve bu kararlara karşı idari dava yolu söz konusu olduğunda kullanılır."
---

# RTÜK Yayın Denetimi ve İdari Yaptırımlar

## Görev
6112 sayılı Kanun kapsamında yayın hizmeti ilkelerine aykırılığı değerlendirmek, RTÜK idari yaptırımlarının hukuka uygunluğunu denetlemek ve idari dava yolunu kurgulamak.

## Soğuk başlangıç (intake)
1. Yayın hangi mecrada (TV/radyo/isteğe bağlı/internet yayını) çıktı?
2. İddia edilen ihlal hangi yayın ilkesine ilişkin (m.8)?
3. RTÜK kararı tebliğ edildi mi, tebliğ tarihi ne?
4. Müvekkil medya hizmet sağlayıcı mı, şikâyetçi izleyici mi?

## Denetim şeması
1. **Yayın ilkeleri (m.8)**: İnsan onuru, özel hayat, çocukların korunması, tarafsızlık ve doğruluk gibi ilkeler denetlenir. Aykırılık tespiti somut yayın içeriğiyle altlanmalıdır.
2. **Yaptırım rejimi (m.32)**: İhlalin ağırlığına göre uyarı, idari para cezası, program durdurma ve lisans iptaline kadar giden kademeli yaptırımlar uygulanır. Orantılılık ve tekerrür değerlendirilir.
3. **Düzeltme ve cevap (m.18)**: İşitsel-görsel yayında kişilik hakkı ihlaline karşı cevap-düzeltme yolu işler.
4. **Yargı yolu**: RTÜK kararı bir idari işlemdir; 2577 sayılı İYUK uyarınca iptal davası idari yargıda açılır. Dava süresi tebliğden itibaren altmış gündür (İYUK m.7); yürütmenin durdurulması talep edilebilir (İYUK m.27).
5. **Ara sonuç**: İşlemin yetki-şekil-sebep-konu-maksat unsurlarından biri sakatsa iptal; orantısız yaptırımda hukuka aykırılık doğar.

## Çıktı modülleri
- Yayın ilkesi-ihlal altlama tablosu
- İdari yaptırıma karşı iptal dava dilekçesi iskeleti (İYUK)
- Yürütmenin durdurulması talebi gerekçesi

## Plugin bağlamı

Bu beceri `basin-medya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
