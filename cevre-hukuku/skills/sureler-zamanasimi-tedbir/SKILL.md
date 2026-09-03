---
name: sureler-zamanasimi-tedbir
description: "Dava açma süreleri, idari para cezası tahsil/karar zamanaşımı, tazminatta zamanaşımı ile yürütmenin durdurulması ve ihtiyati tedbir taleplerinin zamanlamasında; telafisi güç zararın önlenmesi için acil koruma gerektiğinde kullan."
---

# Süreler, Zamanaşımı ve İhtiyati Tedbir

## Görev
Çevresel uyuşmazlıkta tüm süre ve zamanaşımı eşiklerini hesaplamak; telafisi güç/imkânsız zararı önlemek için yürütmenin durdurulması ve ihtiyati tedbir taleplerini doğru zamanda hazırlamak.

## Soğuk başlangıç (intake)
1. Hangi işlem/karar/fiil söz konusu; tebliğ/ilan/öğrenme tarihi nedir?
2. Talep idari mi (iptal/tam yargı) yoksa özel hukuk mu (tazminat/el atma)?
3. Devam eden ve telafisi güç bir zarar (geri dönüşü olmayan tahribat) var mı?
4. Daha önce idari başvuru/itiraz yapıldı mı; süre durduran bir işlem var mı?

## Denetim şeması
1. **İdari dava süresi**: İptal ve tam yargı davalarında kural süre 60 gündür (2577 sayılı İYUK m.7); ÇED ve izin işlemlerinde ilan/askı ve öğrenme tarihinin tespiti kritiktir. İYUK m.11 kapsamında idari başvuru süreyi durdurabilir.
2. **İdari yaptırım zamanaşımı**: İdari para cezalarında 5326 sayılı Kabahatler Kanunu m.20 (soruşturma) ve m.21 (yerine getirme) zamanaşımı süreleri uygulanır; süre dolmuşsa ceza verilemez/tahsil edilemez.
3. **Özel hukuk zamanaşımı**: Haksız fiil tazminatında TBK m.72 — zarar ve failin öğrenilmesinden itibaren 2 yıl ve her hâlde 10 yıl; fiil aynı zamanda suç ise daha uzun ceza zamanaşımı uygulanır. Devam eden (sürekli) kirlilikte zamanaşımının başlangıcı tartışmalıdır, fiil devam ettikçe yeniden işlemeye başlayabilir.
4. **Acil koruma**: İdari yargıda yürütmenin durdurulması (İYUK m.27 — açıkça hukuka aykırılık + telafisi güç zarar); adli yargıda ihtiyati tedbir (HMK m.389) ve delil tespiti (HMK m.400). Çevresel tahribatın geri döndürülemezliği "telafisi güç zarar" ölçütünü güçlü kılar.
5. **Ara sonuç**: Tüm süreler tek takvimde toplanır; en yakın eşik ve acil tedbir ihtiyacı kırmızı işaretlenir.

## Çıktı modülleri
- Süre ve zamanaşımı takvimi (idari + özel hukuk)
- Süre başlangıcı/durması analizi
- Yürütmenin durdurulması / ihtiyati tedbir talebi taslağı
- Delil tespiti başvuru iskeleti

## Plugin bağlamı

Bu beceri `cevre-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
