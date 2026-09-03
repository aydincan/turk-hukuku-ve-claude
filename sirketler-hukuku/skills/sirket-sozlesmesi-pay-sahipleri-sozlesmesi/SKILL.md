---
name: sirket-sozlesmesi-pay-sahipleri-sozlesmesi
description: "Esas/şirket sözleşmesi maddeleri ile şirket dışı pay sahipleri sözleşmesi (SHA) hükümleri kurgulanırken; emredici TTK sınırları, imtiyaz, sürükleme-birlikte satış, veto ve uyum konularını denetlemek için kullanılır."
---

# Esas Sözleşme ve Pay Sahipleri Sözleşmesi

## Görev
Şirket içi anayasayı (esas/şirket sözleşmesi) ve ortaklar arası dış sözleşmeyi (SHA) TTK'nın emredici sınırları içinde kurgulamak; tarafların kontrol, çıkış ve koruma mekanizmalarını geçerli biçimde yerleştirmek.

## Soğuk başlangıç (intake)
1. Düzenlenecek belge esas/şirket sözleşmesi mi, dış pay sahipleri sözleşmesi mi?
2. Kontrol/yönetim dengesi nasıl (kurucu, yatırımcı, çoğunluk-azınlık)?
3. İstenen mekanizmalar: imtiyaz, veto, sürükleme/birlikte satış, önalım, vesting?
4. Hükümler şirkete karşı mı (esas sözleşme) yoksa sadece taraflar arası mı (SHA) işleyecek?
5. Şirket AŞ mi Ltd. mi; tipe bağlılık (m.340) sınırı dikkate alındı mı?

## Denetim şeması
1. Esas sözleşme sınırı: AŞ'de tipe bağlılık ve emredici hükümler (m.340) — esas sözleşme ancak kanunun açıkça izin verdiği yerde sapabilir; Ltd. m.579. Kanunun izin vermediği imtiyaz/sınırlama esas sözleşmeye konsa da geçersiz.
2. İmtiyaz: Oyda imtiyaz m.479 (sınırlar ve istisnalar); kâr payı/tasfiye payı imtiyazı; imtiyazlı pay sahipleri özel kurulu m.454.
3. Devir sınırlaması (bağlam): m.491-493 (AŞ); Ltd.'de devir onayı m.595. SHA'daki önalım/önerilen alım yalnızca taraflar arası borç doğurur, payın devrini şirkete karşı geçersiz kılmaz (ayni etki için esas sözleşme/bağlam gerekir).
4. SHA tipik hükümleri: sürükleme (drag-along), birlikte satış (tag-along), veto/olumlu oy konuları, bilgi alma, vesting/ters vesting, çıkmazda (deadlock) çözüm. Bunlar TBK kapsamında geçerli; cezai şart (TBK m.179) ve fesih sonuçları eklenir.
5. Uyum/çatışma: SHA ile esas sözleşme çelişirse şirkete karşı esas sözleşme; taraflar arası SHA. Oy sözleşmeleri geçerli ama oy hakkının payla bütünlüğü ilkesi (m.434) ve dürüstlük sınırı.
6. Ltd. özgü: ek ödeme/yan edim yükümlülükleri esas sözleşmede öngörülebilir (m.603-606).
7. İspat/şekil: Esas sözleşme değişikliği genel kurul + tescil; SHA yazılı, gerekirse imza onaylı.

## Çıktı modülleri
- Esas/şirket sözleşmesi madde taslakları (emredici sınır notlu).
- SHA hüküm seti (drag/tag/veto/vesting, cezai şart) taslağı.
- Esas sözleşme-SHA uyum/çatışma matrisi.

## Plugin bağlamı

Bu beceri `sirketler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
