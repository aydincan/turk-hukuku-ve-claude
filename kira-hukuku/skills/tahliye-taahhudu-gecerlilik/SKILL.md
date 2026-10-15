---
name: tahliye-taahhudu-gecerlilik
description: "Bir tahliye taahhütnamesinin geçerliliği, düzenleme tarihi-tahliye tarihi ilişkisi, baskı/boş tarihle alınma iddiası veya taahhüde dayalı icra takibi söz konusu olduğunda bu beceriyi kullan."
---

# Yazılı Tahliye Taahhüdü — Geçerlilik ve İcra

## Görev
Tahliye taahhüdünün TBK m.352/1 şartlarını taşıyıp taşımadığını denetlemek; geçerlilik itirazlarını (sözleşme ile aynı tarihte/öncesinde verilme, irade sakatlığı, boş tarih) değerlendirmek; taahhüde dayalı icra/dava yolunu kurmak.

## Soğuk başlangıç (intake)
- Taahhüt yazılı mı, kim imzalamış (kiracı mı)?
- Taahhüdün düzenleme tarihi ve boşaltma tarihi ne?
- Kira sözleşmesi ile aynı tarihte mi alınmış?
- Tahliye tarihi geçti mi; üzerinden ne kadar süre geçti?

## Denetim şeması
1. **Şekil ve taraf (TBK m.352/1)**: Taahhüt **yazılı** olmalı ve **kiracı (veya yetkili temsilcisi)** tarafından verilmelidir. Kiraya verenin değil kiracının iradesi esastır.
2. **Tarih ilişkisi**: Yerleşik uygulamaya göre taahhüt, kiralananın tesliminden/sözleşmenin kurulmasından **sonra** verilmiş olmalıdır; teslimle eş zamanlı veya öncesinde alınan taahhüt, kiracının korunması gereği geçersiz sayılır. Bu ilkesel kabul için güncel Yargıtay içtihadını karararama.yargitay.gov.tr üzerinden doğrula `[doğrulanacak]`.
3. **İrade sakatlığı / boş tarih iddiası**: Kiracı, taahhüdün baskı altında veya boş/ileri tarihli alındığını ileri sürerse ispat yükü kendisindedir; senede karşı senetle/kesin delille ispat kuralı (HMK m.200-201) işler.
4. **Süre (TBK m.352/1)**: Taahhüt edilen boşaltma tarihinden başlayarak **bir ay** içinde icra takibi (İİK m.272) veya dava açılır.
5. **İcra yolu (İİK m.272 vd.)**: Yazılı tahliye taahhüdüne dayanarak ilamsız tahliye takibi yapılabilir; itiraz halinde icra mahkemesinde itirazın kaldırılması.
6. **Ara sonuç**: Taahhüdün geçerli olup olmadığı ve süresinde harekete geçilip geçilmediği.

## Çıktı modülleri
- Geçerlilik kontrol listesi (şekil-taraf-tarih-süre).
- Taahhüde dayalı icra takip talebi taslağı.
- Olası kiracı itirazlarına karşı argüman notu.

## Plugin bağlamı

Bu beceri `kira-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
