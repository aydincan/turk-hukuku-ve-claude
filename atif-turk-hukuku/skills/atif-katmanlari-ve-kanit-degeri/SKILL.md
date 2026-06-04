---
name: atif-katmanlari-ve-kanit-degeri
description: "Bir metindeki her önermenin mevzuat mı içtihat mı doktrin mi yoksa kişisel çıkarım mı olduğunu ayırmak ve her katmanın bağlayıcılık/kanıt değerini doğru sunmak gerektiğinde kullanılır."
---

# Atıf Katmanları ve Kanıt Değeri

## Görev
Bir hukuki metinde geçen her önermeyi doğru kaynak katmanına (mevzuat / içtihat / doktrin / çıkarım) yerleştirmek ve her katmanın bağlayıcılık derecesini abartmadan ve eksiltmeden göstermek.

## Soğuk başlangıç (intake)
- Metin ne tür: layiha, mütalaa, sözleşme şerhi, iç değerlendirme mi?
- Hangi önerme bağlayıcı kurala, hangisi tartışmalı görüşe dayanıyor?
- İddialar arasında "kanun böyle diyor" ile "doktrin/içtihat böyle diyor" karışmış mı?
- Okuyucu kararı kim verecek (hâkim, müvekkil, karşı vekil)?

## Denetim şeması
1. **Katman ayrımı** — Her cümle dört kutudan birine konur: (a) yürürlükteki mevzuat (bağlayıcı kural, Anayasa m.138/1), (b) içtihat (emsal; İBK bağlayıcı, diğeri ikna edici), (c) doktrin (bağlamayan görüş, TMK m.1/3), (d) yazarın çıkarımı/yorumu.
2. **Bağlayıcılık sıralaması** — Anayasa/AYM kararı (m.153/son: herkesi bağlar) > kanun/CB kararnamesi > İBK (Yargıtay K. m.45: bağlar) > yerleşik daire/genel kurul içtihadı (ikna edici) > tek karar > doktrin > kişisel çıkarım.
3. **Sunum disiplini** — Bağlayıcı kural "…m.X uyarınca" diye kesin; içtihat "Yargıtay'ın yerleşik uygulamasına göre"; doktrin "öğretide … savunulmaktadır" diye kiplenir. Çıkarım açıkça "kanaatimce/değerlendirildiğinde" ile ayrılır.
4. **Abartma denetimi** — Tek bir daire kararı "yerleşik içtihat" diye sunulmaz; bir yazarın görüşü "kural" gibi yazılmaz; tartışmalı konuda tek yön gösterilmez.
5. **İspat-hukuk ayrımı** — Vakıa iddiası (ispatı gerekir, HMK m.190) ile hukuk önermesi (iura novit curia) ayrı işaretlenir; atıf yalnızca hukuk katmanına yapılır, vakıa için delil gösterilir.

## Çıktı modülleri
- Önerme → katman eşleme tablosu.
- Bağlayıcılık derecesi notu (her önerme için).
- Kiplenme düzeltme önerileri (kesin/ikna edici/görüş).
- Abartılmış/temelsiz atıf uyarı listesi.

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
