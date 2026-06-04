---
name: elkoyma-musadere-malvarligi
description: "Ekonomik suç dosyalarında taşınmaz/hak/alacaklara elkoyma (CMK m.128), eşya ve kazanç müsaderesi (TCK m.54-55), tedbire itiraz ve malvarlığının iadesi/serbest bırakılması söz konusu olduğunda kullanılır."
---

# Elkoyma, Müsadere ve Malvarlığı Tedbirleri

## Görev
Ekonomik suç soruşturma ve kovuşturmasında uygulanan elkoyma/müsadere tedbirlerinin hukuki dayanağını ve sınırlarını denetlemek; tedbire itiraz ve malvarlığının korunması stratejisini kurmak.

## Soğuk başlangıç (intake)
- Hangi malvarlığına, hangi kararla elkonuldu? (taşınmaz, banka hesabı, şirket payı, araç)
- Karar mercii: hâkim/mahkeme kararı mı, gecikmesinde sakınca olan halde savcılık/kolluk mu?
- Tedbir suçla ve elde edilen menfaatle orantılı mı?
- Üçüncü kişinin (iyiniyetli malik) hakkı etkileniyor mu?

## Denetim şeması
1. **Elkoyma dayanağı (CMK)**: Genel elkoyma CMK m.123 vd.; taşınmaz, hak ve alacaklara elkoyma m.128 — bu tedbir ancak kanunda sayılan katalog suçlar (aklama, zimmet, irtikâp, rüşvet, dolandırıcılık nitelikli halleri, vergi kaçakçılığı vb.) bakımından ve suçun işlendiğine dair somut delillere dayanan kuvvetli şüphe varsa uygulanabilir. Hâkim/mahkeme kararı esastır.
2. **Orantılılık ve şüphe yoğunluğu**: m.128 kuvvetli şüphe ve değerin suçtan elde edildiğine dair somut delil arar; tedbir suç konusu değerle orantılı olmalıdır. Bu eşik savunmanın ana itiraz noktasıdır.
3. **Müsadere (TCK m.54-55)**: Eşya müsaderesi (m.54 — suçta kullanılan/üretilen eşya) ile kazanç müsaderesi (m.55 — suçtan elde edilen ve dönüştürülen değerler) ayrılır. İyiniyetli üçüncü kişiye ait eşya müsadere edilemez (m.54/2).
4. **İtiraz yolu**: Elkoyma kararına CMK genel itiraz hükümleri (m.267 vd.) uyarınca itiraz edilir; mercii ve süre kontrol edilir.
5. **İade/serbest bırakma**: Şüphe ortadan kalktığında, tedbir konusu değerin işletmenin faaliyetini durduracak nitelikte olduğunda veya orantısızlıkta, kısmi serbest bırakma/teminatla iade talep edilir.
6. **Ara sonuç**: Tedbirin dayanağı, orantılılığı, üçüncü kişi hakları ve itiraz/iade imkânı netleşir.

## Çıktı modülleri
- Elkoyma dayanağı ve katalog suç kontrolü
- Orantılılık/şüphe eşiği itiraz notu
- Eşya/kazanç müsaderesi ayrımı
- Üçüncü kişi (iyiniyetli malik) hak analizi
- İtiraz veya iade/teminat talebi dilekçe taslağı

## Plugin bağlamı

Bu beceri `ekonomik-ceza` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
