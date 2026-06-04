---
name: ispat-ve-delil-sunumu
description: "Kullanıcı iddiasını nasıl ispatlayacağını, hangi delilin geçerli olduğunu, tanık mı senet mi gerektiğini veya bilirkişi-keşif-yemin yollarını öğrenmek istediğinde kullanılır."
---

# İspat Yükü ve Delillerin Sunumu

## Görev
İddiaları doğru delil türleriyle eşleştirmek; ispat yükünü doğru dağıtmak; senetle ispat zorunluluğu gibi tuzaklardan kaçınmak.

## Soğuk başlangıç (intake)
- İspatlamanız gereken temel olgular neler?
- Elinizde yazılı belge/sözleşme/dekont var mı?
- Olayı bilen tanıklar var mı, kimler?
- İşlem değeri belli bir tutarın üzerinde miydi?
- Teknik/hesap içeren bir konu mu (bilirkişi gerekebilir)?

## Denetim şeması
1. **İspat yükü (HMK m.190; TMK m.6):** Bir vakıadan kendi lehine hak çıkaran taraf onu ispatla yükümlüdür. Karşı tarafın savunması (örn. ödeme) için ispat yükü ona geçer.
2. **Kesin/takdiri deliller:** Senet, kesin hüküm, ikrar, yemin kesin delildir; tanık, bilirkişi, keşif, uzman görüşü takdiri delildir (hâkim serbestçe değerlendirir).
3. **Senetle ispat zorunluluğu (HMK m.200):** Belli bir parasal sınırı aşan hukuki işlemler kural olarak senetle ispatlanır; bu sınırın üstünde tanık dinlenmez. Sınır yıllık güncellenir — **[doğrulanacak]**. İstisna: yazılı delil başlangıcı (m.202), delil sözleşmesi, karşı tarafın muvafakati.
4. **Delil sunum zamanı:** Deliller dilekçelerde gösterilir; basit yargılamada dilekçeyle birlikte sunulur (m.318). Sonradan delil ancak m.145 koşullarıyla kabul edilir.
5. **Tamamlayıcı yollar:** Bilirkişi (m.266 vd.) teknik/özel bilgi gerektiren konularda; keşif (m.288); yemin (m.225 vd.) son çare delil olarak.
6. **Ara sonuç:** Her vakıa için uygun delil türü + zamanında sunum + senet zorunluluğu kontrolü tamamsa ispat planı hazırdır.

## Çıktı modülleri
- Vakıa → ispat yükü → delil türü eşleme tablosu.
- Senetle ispat zorunluluğu uyarısı (tanık dinlenemeyebilir).
- Eksik delil ve tamamlama (bilirkişi/keşif/yemin) önerileri.

## Plugin bağlamı

Bu beceri `kendini-temsil-asliye` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
