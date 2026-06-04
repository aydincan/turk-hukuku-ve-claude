---
name: anayasaya-uygun-yorum-ve-temel-haklar
description: "Bir kanun hükmü temel hak ve özgürlükleri etkilediğinde ya da birden çok okumaya açık olduğunda; hükmü Anayasa ve AİHS ile uyumlu biçimde yorumlamak ve gerekirse itiraz/başvuru yolunu değerlendirmek için kullanılır."
---

# Anayasaya ve AİHS'e Uygun Yorum

## Görev
Temel hak alanına dokunan bir kanun hükmünü Anayasa ve AİHS ile uyumlu biçimde yorumlamak, sınırlama rejimini ölçülülükle denetlemek ve gerektiğinde AYM yolunu işaretlemek.

## Soğuk başlangıç (intake)
- Hangi temel hak etkileniyor (ifade, mülkiyet, adil yargılanma, özel hayat...)?
- Hükmün birden çok okuması var mı; biri Anayasa'ya uygun mu?
- Sınırlama kanunla mı yapılmış; öngörülebilir mi?
- Konu AİHS kapsamında mı (m.90/5 devreye girer mi)?

## Denetim şeması
1. **Anayasaya uygun yorum ilkesi** — Bir kanun hem Anayasa'ya aykırı hem uygun okunabiliyorsa, hükmü iptal etmeden önce Anayasa'ya uygun yorum tercih edilir (norm korunur, sonuç anayasal sınıra çekilir). Anayasa m.11: Anayasa bağlayıcı ve üstündür.
2. **AİHS üstünlüğü** — Anayasa m.90/5: temel hak ve özgürlüklere ilişkin usulüne göre yürürlüğe konmuş sözleşme ile kanun çatışırsa sözleşme esas alınır; AİHM içtihadı yorum ölçüsü olur.
3. **Sınırlama rejimi — Anayasa m.13** — Temel hak ancak (i) kanunla, (ii) hakkın özüne dokunmadan, (iii) Anayasa'da öngörülen sebeplerle, (iv) demokratik toplum düzeninin gereklerine ve (v) ölçülülük ilkesine uygun olarak sınırlanabilir.
4. **Ölçülülük testi** — Elverişlilik (araç amaca uygun mu), gereklilik (daha az sınırlayıcı yol var mı), orantılılık (yük ile amaç dengeli mi). Üç alt ölçütten biri sağlanmazsa sınırlama Anayasa'ya aykırıdır.
5. **Yol seçimi** — Davada uygulanacak kanunun Anayasa'ya aykırılığı ciddi ise itiraz yolu (Anayasa m.152) ile AYM'ye başvuru; kesinleşmiş ihlalde bireysel başvuru (m.148, ayrı eklenti). AYM kararları bağlayıcıdır (m.153).

## Çıktı modülleri
- Etkilenen hak + hükmün rakip okumaları.
- Anayasaya uygun yorum sonucu.
- m.13 sınırlama ve ölçülülük denetimi tablosu.
- Yol önerisi (yorum / itiraz / başvuru) + `[doğrulanacak]` AYM/AİHM künyesi.

## Plugin bağlamı

Bu beceri `hukuk-metodolojisi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
