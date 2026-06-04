---
name: layiha-ve-mutalaada-atif-duzeni
description: "Dava dilekçesi, cevap, istinaf/temyiz layihası veya hukuki mütalaa yazılırken; mevzuat-içtihat-doktrin atıflarının metin içi yerleşimini ve hukuki sebep bildirimini düzenlemek için kullanılır."
---

# Layiha ve Mütalaada Atıf Düzeni

## Görev
Bir layiha veya mütalaada atıfları, usul kurallarına ve okunabilirliğe uygun biçimde yerleştirmek; hukuki sebebi doğru bildirmek ve dayanakları izlenebilir kılmak.

## Soğuk başlangıç (intake)
- Belge türü: dava dilekçesi, cevap, replik/düplik, istinaf, temyiz, mütalaa mı?
- Yargı kolu hangisi (HMK, CMK, İYUK)?
- Talep sonucu hangi norma dayanıyor; hukuki sebepler listesi hazır mı?
- Atıf yoğunluğu metni boğuyor mu?

## Denetim şeması
1. **Hukuki sebep bildirimi** — HMK m.119/1-(g): dava dilekçesinde dayanılan hukuki sebepler gösterilir (hâkimin hukuku resen uygulaması saklı — iura novit curia). Mevzuat madde/fıkra ile bildirilir; eksik/yanlış hukuki niteleme tek başına hak kaybı doğurmaz ama atıf disiplinli olmalı.
2. **Vakıa-delil-hukuk ayrımı** — Vakıalar (HMK m.119/1-(e)) ayrı, deliller (m.119/1-(f)) vakıaya bağlı, hukuki sebepler ayrı bölümde; atıf yalnızca hukuk kısmında yoğunlaşır, vakıaya delil gösterilir.
3. **Atıf yerleşimi** — Mevzuat metin içinde "(TBK m.49)" parantezi ile; içtihat ana metinde ilke + künye, yoğunsa dipnotta; doktrin destekleyici olarak ölçülü kullanılır. Layiha içtihat yığını değil, argüman taşır.
4. **İçtihat seçimi** — Lehe ve güncel, mümkünse İBK/HGK; tek daire kararı "yerleşik" diye sunulmaz. Aleyhe yerleşik içtihat varsa öngörülüp karşılanır.
5. **Mütalaada katman dürüstlüğü** — Mütalaa kesinlik derecesini dürüstçe yansıtır ("kuvvetle muhtemel / tartışmalı"); bağlayıcı kural ile yazar görüşü ayrılır; risk açıkça yazılır.
6. **Doğrulama işaretleri** — Teyit edilmemiş künyeler `[doğrulanacak]`, eksik bilgi `[doldurulacak]`; taslak bu işaretlerle teslim edilebilir, sahte numarayla değil.

## Çıktı modülleri
- Belgenin hukuki sebepler bölümü taslağı (madde atıflı).
- İçtihat yerleşim planı (ana metin/dipnot).
- Atıf yoğunluğu/okunabilirlik notu.
- `[doğrulanacak]` / `[doldurulacak]` işaret listesi.

## Plugin bağlamı

Bu beceri `atif-turk-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
