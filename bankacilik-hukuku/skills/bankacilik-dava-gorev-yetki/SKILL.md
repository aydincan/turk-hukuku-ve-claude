---
name: bankacilik-dava-gorev-yetki
description: "Bankacılık uyuşmazlığında doğru mahkemeyi (asliye ticaret, tüketici, idare), zorunlu ön şartı (dava şartı arabuluculuk, tüketici hakem heyeti) ve yetkili yeri belirlemek, yanlış yol nedeniyle hak kaybını önlemek gerektiğinde kullanılır."
---

# Bankacılık Uyuşmazlıklarında Görev, Yetki ve Yargı Yolu

## Görev
Bankacılık uyuşmazlığında görevli mahkemeyi, yetkili yeri, zorunlu ön şartları ve kanun yollarını doğru belirleyerek usul hatasından kaynaklanan hak kayıplarını önlemek.

## Soğuk başlangıç (intake)
- Taraflar: banka-tüketici, banka-tacir, banka-BDDK hangisi?
- Uyuşmazlık konusu ve tutarı nedir; tüketici hakem heyeti sınırı içinde mi?
- Sözleşmede yetki/tahkim şartı var mı; tüketici aleyhine yetki şartı geçerli mi?
- Dava mı, icra takibi mi, idari başvuru mu söz konusu?

## Denetim şeması
1. **Yargı kolu**: BDDK işlemleri ve düzenleyici uyuşmazlıklar idari yargıda (İYUK 2577); banka-müşteri sözleşmesel uyuşmazlıkları adli yargıda görülür.
2. **Görevli mahkeme**: Taraflar arasında ticari iş niteliğindeki uyuşmazlık asliye ticaret mahkemesinde (TTK m.4-5); tüketici işlemlerinde tüketici mahkemesinde, parasal sınır altında tüketici hakem heyetinde (TKHK m.66-70) görülür. Banka işlemleri tacir bakımından mutlak ticari iş sayılır (TTK m.3-4).
3. **Zorunlu ön şartlar**: Ticari davalarda konusu para alacağı/tazminat olan uyuşmazlıklarda TTK m.5/A dava şartı arabuluculuk; tüketici uyuşmazlıklarında 6325 sayılı HUAK m.18/B dava şartı arabuluculuk (parasal sınır üstü) ve tüketici hakem heyeti yolu kontrol edilir. Ön şart yerine getirilmeden açılan dava usulden reddedilir.
4. **Yetki**: Genel yetki davalının yerleşim yeri (HMK m.6); sözleşmeden doğan davada ifa yeri (HMK m.10). Tüketici aleyhine yetki sözleşmesi geçersizdir; tüketici kendi yerleşim yeri mahkemesinde de dava açabilir.
5. **Kanun yolları**: İstinaf ve temyiz sınırları (HMK m.341, m.362) ile tüketici/ticari dava özellikleri kontrol edilir. Ara sonuç olarak görevli mahkeme, yetkili yer, ön şart ve süreleri net yaz.

## Çıktı modülleri
- Görev-yetki-ön şart karar tablosu.
- Yanlış yol riskine karşı uyarı notu.
- Süre ve kanun yolu takvimi.

## Plugin bağlamı

Bu beceri `bankacilik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
