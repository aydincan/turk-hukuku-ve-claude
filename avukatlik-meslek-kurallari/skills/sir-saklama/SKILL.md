---
name: sir-saklama
description: "Avukatın sır saklama yükümü, kapsamı, istisnaları, tanıklıktan çekinme ve büroda arama-elkoyma rejimi söz konusu olduğunda; sır ihlali riskinin değerlendirilmesinde kullanılır."
---

# Mesleki Sır ve Sır Saklama Yükümlülüğü

## Görev
Avukatın sır saklama yükümlülüğünün kapsamını, istisnalarını ve usul güvencelerini somut
olaya uygulamak; sır ihlali riskini değerlendirmek.

## Soğuk başlangıç (intake)
1. Sır, müvekkilden mi öğrenildi, yoksa görev dolayısıyla başkasından mı?
2. İfşa kime, hangi amaçla yapılacak (mahkeme, baro, üçüncü kişi, medya)?
3. Müvekkilin açık muvafakati var mı?
4. Büroda/dosyada arama veya elkoyma tehdidi mi söz konusu?

## Denetim şeması
1. **Yükümlülüğün kaynağı ve kapsamı.** Avukat, kendisine tevdi edilen veya mesleğin
   icrası dolayısıyla öğrendiği hususları açığa vuramaz (Av. K. m.36/1, TBB Meslek Kuralları
   m.37). Yükümlülük müvekkilin ölümü/azilden sonra da sürer ve büro çalışanlarını da kapsar.
2. **Tanıklıktan çekinme.** Avukat bu konularda tanıklıktan çekinebilir; rızası olsa dahi
   sır sahibi izin vermedikçe tanıklık edemez (Av. K. m.36/2; CMK m.46; HMK m.249-250
   çerçevesinde). Ara sonuç: çekinme hak mı, yükümlülük mü? Sır sahibinin izni belirleyicidir.
3. **İstisnalar.** Müvekkilin açık izni; avukatın kendisine yöneltilen suçlama veya ücret
   alacağı davasında savunma için zorunlu açıklama; kanunen bildirim yükümlülüğü (örn. 5549
   sayılı Kanun kapsamı, ancak avukatın salt savunma faaliyeti için sınırları gözetilir).
   İstisna dar yorumlanır; ifşa, amaçla orantılı ve asgari olmalıdır.
4. **Arama-elkoyma rejimi.** Avukat bürosunda arama, ancak mahkeme kararıyla ve kararda
   belirtilen olayla sınırlı; arama sırasında baro başkanı/temsilcisi hazır bulunur; el
   konulmak istenen şeyin sır kapsamında olduğu ileri sürülürse o şey mühürlenip hâkime
   gönderilir (CMK m.130). İspat yükü: sır kapsamı iddiasını ileri süren değerlendirme için
   somutlaştırmalıdır; nihai karar sulh ceza hâkimliğindedir.
5. **İhlalin sonucu.** Sır ihlali disiplin suçudur ve TCK m.239 (ticari sır/müşteri sırrı)
   ile ceza sorumluluğu doğurabilir; ayrıca müvekkile karşı tazminat sorumluluğu (TBK m.49,
   m.502 vd.).

## Çıktı modülleri
- İfşanın hukuka uygun olup olmadığına dair gerekçeli değerlendirme.
- Arama/elkoyma anında uygulanacak adım listesi (baro temsilcisi, mühürleme, hâkim).
- Müvekkil bilgilendirme/muvafakat metni taslağı ([doldurulacak] yer tutucularla).

## Plugin bağlamı

Bu beceri `avukatlik-meslek-kurallari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
