---
name: tasima-sozlesmesi-taslak
description: "Taşıma, taşıma işleri komisyonculuğu veya lojistik/depolama hizmet sözleşmesi hazırlanması, mevcut sözleşmenin riskli/geçersiz şartlar yönünden incelenmesi ve emredici hükümlere uyumun denetlenmesi gerektiğinde kullanılır."
---

# Taşıma ve Lojistik Sözleşmesi Taslağı

## Görev
Taşıma/forwarding/lojistik sözleşmesi taslağı üretmek veya mevcut sözleşmeyi emredici hükümler, sorumluluk dağılımı ve risk yönünden incelemek.

## Soğuk başlangıç (intake)
1. Sözleşme tipi: tek seferlik taşıma, çerçeve taşıma, forwarding mi, depolama+taşıma karması mı?
2. Taşıma iç mi sınır aşan mı; CMR uygulanacak mı?
3. Taraflar: gönderen/yük sahibi mi, taşıyıcı mı, komisyoncu mu temsil ediliyor?
4. Özel ihtiyaçlar: değer beyanı, sigorta, tehlikeli madde, teslim süresi taahhüdü var mı?

## Denetim şeması
1. **Emredici çerçeve:** Sınır aşan karayolunda CMR m.41 — sorumluluğu CMR aleyhine değiştiren şartlar batıldır. İç taşımada TTK m.854 ve m.886 — sorumluluğu hafifleten anlaşmalar sınırlı; kasıt/pervasızlık için sorumsuzluk geçersiz.
2. **Esaslı maddeler:** Taşıma konusu eşya ve güzergâh, teslim/varma süresi, ücret ve ödeme, yükleme-boşaltma yükümlülüğü (m.852 vd.), belge düzenleme.
3. **Sorumluluk maddeleri:** Sorumluluk sınırı (TTK m.882 / CMR m.23) sözleşmeyle taşıyıcı lehine düşürülemez; değer beyanıyla (m.880) artırılabilir. Gecikme tazminatı tavanına dikkat.
4. **Sigorta:** Taşıyıcı mali sorumluluk sigortası (CMR sigortası) ve emtia/nakliyat sigortası ayrımı; sigorta yaptırma yükümlüsü ve rücu (TTK m.1472 halefiyet).
5. **Forwarder klozları:** Sabit ücret kararlaştırılırsa taşıyıcı gibi sorumluluk doğacağı (m.926) açıkça öngörülmeli; aksi halinde komisyon yapısı netleştirilmeli.
6. **Yan klozlar:** Hapis hakkı (TTK m.891), demuraj/bekleme ücreti, mücbir sebep, uygulanacak hukuk ve yetki/tahkim.
7. **Ara sonuç:** Geçersiz/asimetrik şartların ayıklanması ve dengeli risk dağıtımı.

## Çıktı modülleri
- Madde madde sözleşme taslağı ([doldurulacak] yer tutucularıyla).
- Geçersiz/riskli şart raporu (CMR m.41 / TTK m.854 süzgeci).
- Sorumluluk ve sigorta klozları için alternatif lafızlar.

## Plugin bağlamı

Bu beceri `tasima-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
