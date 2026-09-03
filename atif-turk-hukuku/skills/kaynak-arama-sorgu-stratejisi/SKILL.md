---
name: kaynak-arama-sorgu-stratejisi
description: "Belirli bir hukuki ilkeyi veya güncel içtihat eğilimini bulmak gerektiğinde; resmî karar bankalarında ve mevzuat sisteminde etkili arama sorgusu kurmak ve sonuçları değerlendirmek için kullanılır."
---

# Kaynak Arama ve Sorgu Stratejisi

## Görev
Aranan hukuki ilkeyi veya içtihat eğilimini resmî kaynaklarda verimli biçimde bulmak için arama sorgusu kurmak ve dönen sonuçları güvenilirlik/güncellik bakımından elemek.

## Soğuk başlangıç (intake)
- Aranan ilke nedir; hangi kanun maddesi etrafında dönüyor?
- Hangi yargı kolu/banka uygun (Yargıtay, Danıştay, AYM, AİHM)?
- Lehe karar mı, eğilim tespiti mi, karşı içtihat taraması mı amaç?
- Konunun teknik terimi/anahtar kelimesi ne?

## Denetim şeması
1. **Banka seçimi** — Adli/özel hukuk ve ceza: karararama.yargitay.gov.tr. İdari/vergi: karararama.danistay.gov.tr. Anayasal/temel hak: kararlarbilgibankasi.anayasa.gov.tr. AİHS: hudoc.echr.coe.int. Mevzuat: mevzuat.gov.tr.
2. **Sorgu kurma** — Hukuki terim + ilgili madde (örn. "ayıplı ifa" + "TBK 219") kombinlenir; çok genel terim çok sonuç, çok dar terim sıfır sonuç verir, kademeli daraltılır. Eş anlamlı/eski terim de denenir (örn. "müdahalenin meni" / "el atmanın önlenmesi").
3. **Tarih ve daire filtresi** — Güncellik için tarih aralığı; konu dairesini bilen ilgili daireyle filtreler (örn. ticari için 11. HD, iş için 9./22. HD eğilimi). Filtre, eğilimi daraltmak için araçtır, gerçeği saptırmak için değil.
4. **Sonuç eleme** — Dönen kararın vakıası eldeki olaya benziyor mu; ratio aranan ilkeyi gerçekten kuruyor mu? Benzemeyen karar emsal listesine alınmaz.
5. **Eğilim okuma** — Birden çok karar varsa istikrar ve tarih izlenir; daireler arası çelişki/İBK varlığı kontrol edilir; eğilim dürüstçe (lehe-aleyhe) özetlenir.
6. **Künye çıkarımı** — Bulunan kararın künyesi metinden aynen alınır; **arama yapılmadan/karar görülmeden künye yazılmaz.**

## Çıktı modülleri
- Banka + sorgu önerileri (kademeli).
- Filtre stratejisi (tarih/daire/terim).
- Bulunan kararların eleme tablosu (vakıa benzerliği).
- Eğilim özeti + doğrulanmış künyeler / `[doğrulanacak]`.

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
