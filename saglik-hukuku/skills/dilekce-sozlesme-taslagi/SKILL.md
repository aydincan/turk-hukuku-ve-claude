---
name: dilekce-sozlesme-taslagi
description: "Tıbbi uyuşmazlıkta dava dilekçesi, onam formu, sağlık hizmeti sözleşmesi veya idareye başvuru gibi belgelerin iskeletini üretmek için kullanılır; yer tutucu disipliniyle hazır taslak sağlar."
---

# Dilekçe, Sözleşme ve Başvuru Taslağı

## Görev
Tıbbi uyuşmazlığa uygun usul ve içerikte dilekçe, sözleşme veya başvuru taslağını, doğrulanması gereken her veriyi [doldurulacak] yer tutucuyla işaretleyerek üretmek.

## Soğuk başlangıç (intake)
1. Hangi belge gerekli: dava dilekçesi, idari başvuru, onam formu, hizmet sözleşmesi?
2. Yargı kolu adli mi idari mi; mahkeme/merci belli mi?
3. Taraflar, vekiller ve talep sonucu net mi?
4. Dayanak vakıalar ve deliller listelendi mi?

## Denetim şeması
1. **Belge türü ve usul çerçevesi**: Adli dava → HMK m.119 dava dilekçesi zorunlu unsurları. İdari dava → İYUK m.3 dilekçe unsurları. Onam → Hasta Hakları Yönetmeliği m.15/24-31 içerik standardı.
2. **Dava dilekçesi mimarisi**: Mahkeme, taraflar, dava değeri/harç, açık talep sonucu, vakıaların sıralı anlatımı, hukuki sebepler (TBK m.49/112/502, TCK ilgili maddeler), her vakıanın dayandığı delil (HMK m.119/f.1-e,f).
3. **Talep sonucu**: Maddi tazminat kalemleri (tedavi gideri, iş gücü/destek kaybı), manevi tazminat, faiz başlangıcı ve türü, yargılama gideri ve vekâlet ücreti.
4. **Onam/sözleşme taslağı**: Aydınlatma içeriği (tanı, yöntem, riskler, alternatifler, başarısızlık olasılığı), tarih ve makul süre, imza alanları; sorumluluğu tamamen kaldıran şartların geçersizliği (TBK m.115).
5. **Yer tutucu disiplini**: Tüm tarih, tutar, ad ve teknik veri [doldurulacak] olarak işaretlenir; uydurma veri girilmez.
6. **Ara sonuç**: Zorunlu unsur eksikse dilekçe reddi/HMK m.119/2 süre verme riski; taslakta bu kontrol yapılır.

## Çıktı modülleri
- İstenen belgenin tam taslağı (başlıklı, yer tutuculu)
- Zorunlu unsur kontrol listesi (HMK m.119 / İYUK m.3)
- Talep sonucu ve faiz bloğu
- Doldurulacak veri listesi

## Plugin bağlamı

Bu beceri `saglik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
