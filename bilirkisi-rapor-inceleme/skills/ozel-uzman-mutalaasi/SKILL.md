---
name: ozel-uzman-mutalaasi
description: "Bilirkişi raporunu mahkemenin atadığı bilirkişi dışında bir özel uzmandan alınacak mütalaayla teknik olarak çürütmek; bu mütalaanın delil değerini ve itirazla nasıl bağlanacağını planlamak istendiğinde kullanılır."
---

# Karşı Uzman Mütalaası ile Çürütme

## Görev
Resmî bilirkişi raporunun teknik yanını, tarafın kendi seçtiği bir uzmandan aldığı mütalaayla karşılamak; bu mütalaayı usulî olarak doğru konumlandırıp itiraza güç katacak biçimde dosyaya kazandırmak.

## Soğuk başlangıç (intake)
- Raporun çürütülmek istenen teknik noktası tam olarak nedir?
- Bu alanda mütalaa verebilecek bağımsız bir uzman erişiminiz var mı?
- Mütalaa, rapordaki yöntem hatasını mı yoksa hesap/veri hatasını mı hedefliyor?
- Mütalaayı itiraz süresine yetiştirebilecek misiniz?

## Denetim şeması
1. **Delil niteliği:** Tarafın aldığı uzman mütalaası, mahkemece atanan bilirkişi raporu gibi bağlayıcı bir delil olmayıp tarafın iddiasını destekleyen, hâkimin serbest takdirine (HMK m.282) sunulan bir görüştür. Bu sınır mütalaada açıkça belirtilmelidir.
2. **Hedef seçimi:** Mütalaa, raporun en zayıf ve teknik olarak çürütülebilir noktasına odaklanır (yöntem, kabul, veri veya hesap). Hukuki nitelendirmeye girmez; aksi hâlde bilirkişi raporuyla aynı görev sınırı sorununa düşer (HMK m.266).
3. **Çıpalama:** Mütalaadaki her itiraz, resmî rapordaki sayfa/paragrafa ve dosya verisine bağlanır; böylece mahkeme iki teknik görüşü karşılaştırabilir.
4. **Usule bağlama:** Mütalaa, HMK m.281 itiraz dilekçesine ek olarak ve süresinde sunulur; gerekirse mütalaa doğrultusunda yeni/üçüncü heyet veya ek rapor talep edilir.
5. **Ara sonuç:** Mütalaa, soyut itirazı bilimsel temele oturtarak yeni heyet talebinin gerekçesini güçlendirir.

## Çıktı modülleri
- Çürütülecek teknik noktanın ve karşı tezin tek cümlelik özeti.
- Uzmandan istenecek soruların listesi (rapordaki paragraflara çıpalı).
- Mütalaanın itiraz dilekçesine bağlanma planı.
- Mütalaanın delil değerine ilişkin sınırlayıcı not (bağlayıcı değil, takdiri).

## Plugin bağlamı

Bu beceri `bilirkisi-rapor-inceleme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
