---
name: durustluk-dilekce-modulleri
description: "TMK m.2/m.3/m.4/m.6'ya dayanan bir dava, cevap veya layiha gerekçesi yazılırken; dürüstlük/kötüye kullanma/iyiniyet/ispat argümanını dilekçe diline dökmek ve yer tutucularla taslaklamak için kullanılır."
---

# Başlangıç Hükümleri Dilekçe ve Gerekçe Modülleri

## Görev
Başlangıç hükümlerine dayanan bir argümanı (dürüstlük, hakkın kötüye kullanılması, iyiniyet, hakkaniyet, ispat yükü) dilekçe/layiha gerekçesine uygun, altlamalı ve atıf disiplinli bir metne dönüştürmek.

## Soğuk başlangıç (intake)
- Metin kim için: dava dilekçesi, cevap, replik-düplik, istinaf gerekçesi mi?
- Hangi başlangıç hükmü argümanın merkezinde (m.2/1, m.2/2, m.3, m.4, m.6, m.7)?
- Hangi somut vakıalar bu hükmün şartlarını karşılıyor; karşı argüman ne?
- Talep sonucu (asıl talep) nedir ve başlangıç hükmü onu nasıl destekliyor/savunuyor?

## Denetim şeması
1. **Asıl talebe bağla** — Başlangıç hükmü tek başına talep sonucu olmaz; önce asıl talep (HMK m.119/1-ğ: açık talep sonucu) yazılır, başlangıç hükmü onun hukuki sebebi/savunması olarak konumlandırılır.
2. **Hukuki sebep — HMK m.119/1-g** — İlgili madde fıkra/bent ile gösterilir (ör. "TMK m.2/2 — hakkın açıkça kötüye kullanılması yasağı"); hâkim hukuku re'sen uygular ama dayanak açıkça anılır.
3. **Vakıa-şart altlaması** — Hükmün her şartı (ör. m.2/2 için çelişkili davranış + yaratılan güven + açıklık) somut vakıaya bağlanır; her vakıa için delil (HMK m.119/1-f) gösterilir, `[doldurulacak]` yer tutucularıyla eksik bilgi işaretlenir.
4. **İspat şeridi** — TMK m.6 dağılımına göre hangi vakıayı kimin ispatlayacağı; karine varsa (m.3, m.7) aksini ispat yükünün karşı tarafta olduğu vurgulanır.
5. **Karşı argüman karşılama** — "Davalı/davacı … ileri sürebilirse de …" kalıbıyla rakip okuma açıkça çürütülür; özellikle "açıklık" eşiği ve özen ölçütü tartışılır.
6. **Atıf hijyeni** — Mevzuat madde/fıkra ile; içtihat yalnızca ilke + `[doğrulanacak]` künye (mahkeme/daire/E./K./T.). Karar numarası uydurulmaz; abartılı kesinlik ("kesin kazanırız") yerine olasılık dürüstçe nitelenir.

## Çıktı modülleri
- Talep sonucu + başlangıç hükmünün konumu (sebep/savunma).
- Hukuki sebep bloğu (madde/fıkra).
- Vakıa→şart altlama paragrafları + delil bağı + `[doldurulacak]`.
- İspat şeridi ve karşı argüman/çürütme + `[doğrulanacak]` içtihat yeri.

## Plugin bağlamı

Bu beceri `medeni-hukuk-baslangic` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
