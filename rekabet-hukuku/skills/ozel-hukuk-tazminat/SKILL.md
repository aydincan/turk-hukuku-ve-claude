---
name: ozel-hukuk-tazminat
description: "Kartel veya hâkim durum ihlalinden zarar gören tarafın üç kata kadar tazminat (m.58) talebini, zarar ve illiyet ispatını, zamanaşımını ve görevli mahkemeyi değerlendirmek istendiğinde kullanılır."
---

# Rekabet İhlalinden Özel Hukuk Tazminatı (m.57-58)

## Görev
Rekabet ihlali nedeniyle zarar gören teşebbüs veya tüketicinin 4054 m.57-58 kapsamında tazminat (üç kata kadar) talebini kurgulamak; zarar, illiyet ve kusur ispatını, zamanaşımını ve usul boyutunu yönetmek.

## Soğuk başlangıç (intake)
- İddia edilen ihlal: kartel (fiyat tespiti), dışlayıcı kötüye kullanma, başka m.4/m.6 ihlali mi?
- Rekabet Kurulu'nun ihlali tespit eden kesinleşmiş bir kararı var mı (follow-on) yoksa bağımsız dava mı (stand-alone)?
- Zarar türü: fazladan ödenen fiyat (overcharge), kâr kaybı, pazardan dışlanma?
- İhlal/zararın öğrenilme tarihi ve dava açılabilirlik durumu?

## Denetim şeması
1. **Hukuki temel (m.57)** — rekabeti sınırlayan davranışlarla zarar verenler, zarar görenin zararını tazminle yükümlüdür; sorumluluk haksız fiil esaslarına dayanır (TBK m.49 vd. ile birlikte okunur).
2. **Üç kat tazminat (m.58)** — zarar görenin gerçek zararı yanında, kartel/anlaşma sonucu ortaya çıkan zararda mahkeme, zarar görenin talebiyle, verilen zararın üç katına kadar tazminata hükmedebilir; bu caydırıcı bir özel hukuk yaptırımıdır.
3. **Unsurlar** — hukuka aykırılık (ihlalin varlığı), kusur, zarar ve illiyet bağı ispatlanmalı. Follow-on davada kesinleşmiş Kurul kararı ihlali güçlü biçimde ortaya koyar; zarar miktarı ve illiyet yine ispat gerektirir.
4. **Zararın hesabı** — fiyat farkı (but-for fiyat), kâr kaybı; iktisadi modelleme ve bilirkişi devreye girer. Geçişkenlik (passing-on) savunması değerlendirilir.
5. **Zamanaşımı** — haksız fiil zamanaşımı kuralları (TBK m.72: zararın ve failin öğrenilmesinden itibaren kısa süre, her hâlde uzun süre) çerçevesinde; Kurul kararının kesinleşmesinin zamanaşımına etkisi dikkatle değerlendirilir.
6. **Görev/yetki** — uyuşmazlık ticari nitelikteyse asliye ticaret mahkemesi; dava şartı arabuluculuk (ticari uyuşmazlık) ihtimali kontrol edilir.

## Çıktı modülleri
- Follow-on / stand-alone yol kararı.
- Zarar kalemleri ve hesap yöntemi taslağı.
- Üç kat tazminat talebi gerekçesi.
- Zamanaşımı ve görev/yetki + arabuluculuk kontrol listesi.

## Plugin bağlamı

Bu beceri `rekabet-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
