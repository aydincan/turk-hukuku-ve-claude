---
name: girisim-yapilanmasi-cap-table
description: "Bir girişimin şirket tipini (AŞ tercihi), ortaklık yapısını, pay defteri ve cap table mantığını, hangi yatırım aşamasında olduğunu ve uygulanacak çerçeveyi ayırt etmek için kullanılır; sonraki tüm yatırım ve sözleşme adımlarının zeminini kurar."
---

# Girişim Yapılanması ve Cap Table Temeli

## Görev
Girişimi doğru şirket tipi, doğru ortaklık yapısı ve okunabilir bir cap table üzerine oturtmak; yatırım aşamasını teşhis edip hangi alt-beceriye geçileceğini belirlemek.

## Soğuk başlangıç (intake)
1. Şirket tipi nedir (AŞ / Ltd. / henüz kurulmadı) ve neden?
2. Hangi aşamadasınız: kuruluş, pre-seed, seed, Seri A+ veya çıkış?
3. Mevcut pay dağılımı, kurucu sayısı ve varsa opsiyon havuzu nedir?
4. Kim temsil ediliyor: girişimci/kurucular mı, yatırımcı mı?
5. Yurtdışı holding (ör. flip) düşünülüyor mu; yoksa tamamen Türkiye mi?

## Denetim şeması
1. Tip tercihi: Yatırım alacak girişim kural olarak AŞ (TTK m.329 vd.) olmalı; imtiyazlı pay (m.478-479), kayıtlı sermaye (m.460) ve ESOP esnekliği AŞ'de mümkün. Ltd. ise tür değiştirme TTK m.180-190 ile AŞ'ye dönüştürülür.
2. Kuruluş/sermaye: Asgari ve kayıtlı sermaye TTK m.332 — güncel tutarı olay tarihinden teyit et; tek ortakla AŞ kurulabilir (m.338).
3. Cap table mantığı: Pay defteri (TTK m.499) gerçeği; cap table yönetsel araç. Tam sulandırılmış (fully diluted) tabloda mevcut paylar + tahsis edilmiş/edilmemiş opsiyon havuzu + dönüştürülebilir enstrümanların (SAFE/nota) dönüşüm etkisi gösterilir.
4. Rüçhan ve sulandırma: Her bedelli artırımda rüçhan hakkı m.461; yatırımcı girişi için bu hak yönetilir (mevcut ortakların oran kaybı = sulandırma).
5. Aşama tayini ve yönlendirme: term sheet → enstrüman (SAFE/nota/equity) → SHA/esas sözleşme → ESOP → çıkış. İlgili alt-beceriye geç.
6. İspat/şekil: Pay sahipliği şirkete karşı pay defteri kaydıyla; devir geçerliliği m.490 şekline tabi.

## Çıktı modülleri
- Aşama ve tip teşhis tablosu (madde atıflı).
- Mevcut ve tam sulandırılmış cap table iskeleti (yer tutuculu).
- Hangi alt-beceriye geçileceğini gösteren yol haritası.

## Plugin bağlamı

Bu beceri `girisim-startup-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
