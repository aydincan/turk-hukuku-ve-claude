---
name: enerji-yatirim-epc-finansman
description: "Santral/altyapı yatırımlarında EPC ve O&M sözleşmeleri, proje finansmanı, teminat yapısı, hukuki durum tespiti ve izin-onay zinciri kurulurken kullanılır."
---

# Enerji Yatırımı, EPC ve Proje Finansmanı

## Görev
Enerji yatırım projesinin sözleşmesel ve finansal mimarisini kurmak; EPC/O&M risk dağılımını, proje finansmanı teminat paketini ve izin-onay zincirini denetleyerek kapanışa hazır hale getirmek.

## Soğuk başlangıç (intake)
1. Proje tipi, kapasite ve gelişim aşaması (önlisans/lisans/inşa)?
2. EPC modeli: anahtar teslim mi, ölçüye bağlı mı; tek/çok yüklenici?
3. Finansman: özkaynak/borç oranı, kreditör, teminat beklentisi?
4. Kritik izinler (ÇED, bağlantı, mülkiyet/irtifak, imar) tamam mı?

## Denetim şeması
1. **İzin-onay zinciri**: Lisans/önlisans, ÇED kararı, bağlantı ve sistem kullanım anlaşmaları, mülkiyet/irtifak ve gerekirse 6446 m.19 kamulaştırma; eksik halka projeyi durdurur, tamamlanma takvimine bağlanır.
2. **EPC sözleşmesi**: TBK eser sözleşmesi (m.470 vd.) zemininde anahtar teslim bedel, iş programı, gecikme cezası (cezai şart, TBK m.182), performans testleri ve geçici/kesin kabul; ayıp ve garanti (TBK m.474 vd.) ile teminat süresi.
3. **Teminat paketi**: Avans/performans/bakım teminat mektupları, sigorta (inşaat all-risk, üçüncü kişi mali mesuliyet) ve liquidated damages; kreditör lehine alacak ve hesap rehinleri, lisans üzerinde rehin/şerh imkânı.
4. **Risk tahsisi**: Mevzuat değişikliği, kur, gecikme ve mücbir sebep maddeleri EPC, PPA ve kredi sözleşmeleri arasında tutarlı olmalı (back-to-back); çelişki kreditör için kabul edilemez boşluk doğurur.
5. **Direct agreement / step-in**: Kreditörün lisans ve kilit sözleşmelere müdahale (step-in) ve devir hakları; EPDK izni gereken pay/kontrol değişiklikleri kontrol edilir.

İdari işlem boyutunda iptal riskleri İYUK, sözleşmesel uyuşmazlıklar TBK/tahkim kapsamında ayrı izlenir.

## Çıktı modülleri
- İzin-onay ve kapanış ön koşulları (CP) kontrol listesi.
- EPC/O&M risk dağılım matrisi.
- Teminat paketi ve back-to-back tutarlılık raporu.

## Plugin bağlamı

Bu beceri `enerji-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
