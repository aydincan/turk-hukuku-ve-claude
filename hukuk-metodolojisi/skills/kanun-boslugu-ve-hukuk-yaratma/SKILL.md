---
name: kanun-boslugu-ve-hukuk-yaratma
description: "Olaya uygulanacak açık bir kural bulunamadığında ya da var olan kural amacına aykırı biçimde eksik kaldığında; boşluğun türünü belirleyip TMK m.1/2-3 uyarınca kural kurmak için kullanılır."
---

# Kanun Boşluğu ve Hâkimin Hukuk Yaratması

## Görev
Boşluğun varlığını ve türünü doğru teşhis etmek, doldurma aracını seçmek ve gerekirse TMK m.1 uyarınca hâkimin koyacağı kuralı genelleştirilebilir biçimde formüle etmek.

## Soğuk başlangıç (intake)
- Olaya doğrudan uyan bir hüküm var mı; yoksa benzer bir ilişkiye dair hüküm var mı?
- Susan kanun gerçekten mi susuyor, yoksa "aksiyle kanıt" ile bilinçli bir tercih mi (suskunluk = kural)?
- Konu emredici/kanunilik alanı mı (ceza, vergi: kıyas yasağı)?
- Örf-âdet hukuku veya yerleşik içtihat var mı?

## Denetim şeması
1. **Boşluk var mı?** Önce yorumla (lafzî+amaçsal) çözümü dene. Susmanın bilinçli olduğu hâllerde *argumentum a contrario* uygulanır; bu durumda boşluk yoktur.
2. **Boşluğun türü** — (a) Gerçek (açık) boşluk: hiç kural yok. (b) Örtülü/kanun içi boşluk: kural var ama amacı, kapsamı dışına taşmasını gerektiriyor; burada amaca uygun daraltma (teleolojik redüksiyon) veya genişletme yapılır.
3. **Kaynak sırası — TMK m.1**: Önce kanun (yorum/kıyas), sonra örf ve âdet hukuku (sürekli uygulama + genel inanç + yaptırım gücü), sonra hâkimin kuralı.
4. **Doldurma araçları** — Kıyas (benzer olaya konan kuralın taşınması), evleviyet (*a maiore ad minus / a minore ad maius*), TMK m.5 ile genel hükümlerin yayılması, hukukun genel ilkeleri (dürüstlük, ahde vefa, sebepsiz zenginleşme yasağı).
5. **Hukuk yaratma — TMK m.1/2-3 ve m.4**: Hâkim kanun koyucu gibi, hak ve nısfetle, bilimsel görüş ve içtihattan yararlanarak kural kurar. Kural; somut olayı aşan, her benzer olayda aynı sonucu verecek genellikte olmalıdır.
6. **Sınır** — Anayasa m.138 (hâkimin hukuka bağlılığı) ve kanunilik ilkesi; ceza/vergide aleyhe kıyas ve hukuk yaratma yasaktır.

## Çıktı modülleri
- Boşluk teşhisi: var/yok, türü, gerekçe.
- Seçilen araç (kıyas/evleviyet/genel ilke) ve uygulanışı.
- Önerilen kural lafzı + genelleştirilebilirlik testi.
- Karşı görüş ve `[doğrulanacak]` içtihat yeri.

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
