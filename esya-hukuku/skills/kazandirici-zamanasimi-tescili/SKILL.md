---
name: kazandirici-zamanasimi-tescili
description: "Tapulu taşınmazda kaydın yanlış/eksik olduğu ya da tapusuz taşınmazda uzun süreli malik gibi zilyetlik bulunduğu hâllerde; olağan ve olağanüstü kazandırıcı zamanaşımı şartları ile tescil davasını kurmak için kullanılır."
---

# Kazandırıcı Zamanaşımı ile Mülkiyet Kazanımı

## Görev
Uzun süreli zilyetliğe dayanarak taşınmaz mülkiyetinin kazanılması talebini değerlendirmek: olağan (m.712) ve olağanüstü (m.713) zamanaşımı şartlarını denetlemek ve tescil davasını kurmak.

## Soğuk başlangıç (intake)
- Taşınmaz tapuda kayıtlı mı; kayıtlıysa kimin adına, değilse hiç mi kaydı yok?
- Müvekkil taşınmazı kaç yıldır, ne sıfatla (malik gibi) kullanıyor; aralıksız ve nizasız mı?
- Zilyetlik nasıl başladı; bir tapu/satış belgesine mi dayanıyordu (olağan), yoksa belgesiz mi (olağanüstü)?
- Taşınmaz tarım arazisi, orman, kıyı, mera gibi kazanılması yasak bir nitelikte mi?

## Denetim şeması
1. **Olağan zamanaşımı (TMK m.712)**: Geçerli olmayan bir hukuki sebebe dayanarak tapuya malik olarak yazılan kişi, taşınmaza davasız ve aralıksız 10 yıl iyiniyetle (m.3) malik gibi zilyet olursa mülkiyeti kazanır. Burada zaten adına tescil vardır; dava bu tescili sağlamlaştırır.
2. **Olağanüstü zamanaşımı (TMK m.713)**: Tapuda kayıtlı olmayan veya maliki kim olduğu belirlenemeyen ya da malikinin 20 yıl önce ölmüş/gaip olduğu taşınmazı, davasız ve aralıksız 20 yıl süreyle malik sıfatıyla zilyet bulunan kişi tescil isteyebilir.
3. **Ortak unsurlar**: Zilyetliğin (a) malik sıfatıyla, (b) davasız (nizasız), (c) aralıksız ve (d) süre boyunca sürmesi gerekir. Önceki zilyedin süresi devralanın süresine eklenir (m.996, zilyetlikte halefiyet).
4. **Kazanılamayan mallar**: Orman, kıyı, mera/yaylak/kışlak, devletin hüküm ve tasarrufundaki yerler kazandırıcı zamanaşımına konu olamaz; bu husus re'sen araştırılır.
5. **Usul**: m.713 davası Hazine ve ilgili kamu tüzel kişilerine husumetle açılır; ilan yapılır, keşif ve tanık delili belirleyicidir. Kadastro sırasında ise 3402 sayılı Kanun hükümleri devreye girer.
6. **Ara sonuç**: Şartlar tamsa mahkeme kararıyla tescil; mülkiyet karar kesinleşince (m.705/2 çerçevesinde) kazanılır.

## Çıktı modülleri
- Tescil davası dilekçesi iskeleti (zilyetlik süresi, sıfat, husumet).
- Delil planı (tanık, keşif, kadastro/vergi kaydı, hava fotoğrafı).
- Kazanma yasağı kontrol listesi (orman/kıyı/mera/Hazine).

## Plugin bağlamı

Bu beceri `esya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
