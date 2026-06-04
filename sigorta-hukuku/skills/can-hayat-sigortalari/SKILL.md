---
name: can-hayat-sigortalari
description: "Hayat, ferdi kaza veya sağlık/hastalık sigortalarında lehtar tayini, sigorta bedelinin ödenmesi, intihar/suikast gibi özel haller ve tazminat ilkesinin uygulanmayacağı durumlar tartışıldığında kullanılır."
---

# Can Sigortaları (Hayat, Kaza, Sağlık)

## Görev
Can sigortalarında sigorta bedelinin kime, hangi şartlarla ve ne miktarda ödeneceğini; lehtar tayini, beyan ve özel istisnaları (intihar, suikast) değerlendirmek.

## Soğuk başlangıç (intake)
1. Hayat, ferdi kaza yoksa sağlık/hastalık sigortası mı?
2. Lehtar belirlenmiş mi, değiştirilebilir mi; sigortalı ile sigorta ettiren aynı kişi mi?
3. Riziko (vefat/maluliyet/hastalık) ne zaman, nasıl gerçekleşti?
4. Bekleme süresi, yaş/sağlık beyanı, teminat dışı haller poliçede nasıl?

## Denetim şeması
1. **Tazminat ilkesi uygulanmaz.** Can sigortalarında kural olarak gerçek zarar değil, kararlaştırılan sigorta bedeli ödenir (TTK m.1487 vd.); zarar sigortasındaki zenginleşme yasağı geçerli değildir. Ferdi kazada bedel esastır.
2. **Lehtar.** TTK m.1493: sigorta ettiren, lehtarı serbestçe tayin ve değiştirebilir; lehtar tayini yazılı bildirimle hüküm doğurur. Lehtar yoksa sigorta bedeli sigorta ettirenin/sigortalının mirasçılarına/terekesine geçer.
3. **Beyan ve yaş.** Hayat sigortasında yanlış yaş beyanı sözleşmeyi kural olarak iptal ettirmez; sigorta bedeli/prim oranlanır (TTK m.1500 mantığı). Sağlık beyanı için genel beyan yükümlülüğü (TTK m.1435 vd.) uygulanır.
4. **Özel istisnalar.** TTK m.1503: sözleşmeden itibaren belirli süre (genel şartlarda üç yıl) sonra intihar halinde dahi sigorta bedeli ödenir; lehtarın sigortalıyı öldürmesi (suikast) halinde o lehtar bedele hak kazanamaz, diğer hak sahipleri korunur. Ara sonuç: istisna devrede mi?
5. **Sağlık/hastalık.** Bekleme süreleri, mevcut hastalık istisnası ve teminat dışı haller poliçeden denetlenir; tüketici sigortalarında haksız şart kontrolü.

## Çıktı modülleri
- Lehtar/hak sahibi belirleme tablosu.
- Sigorta bedeli ödeme değerlendirmesi (tazminat ilkesi yok notu).
- İntihar/suikast ve beyan istisnaları analizi.
- Ödenecek bedel ve dayanak maddeleri.

## Plugin bağlamı

Bu beceri `sigorta-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
