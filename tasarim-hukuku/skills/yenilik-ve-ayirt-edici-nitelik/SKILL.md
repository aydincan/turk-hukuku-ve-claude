---
name: yenilik-ve-ayirt-edici-nitelik
description: "Bir tasarımın SMK m.56-58 uyarınca yeni ve ayırt edici olup olmadığının bilgilenmiş kullanıcı ve seçenek özgürlüğü ölçütleriyle değerlendirilmesi; tescil başvurusu öncesi veya hükümsüzlük tartışmasında koruma şartı analizi gerektiğinde kullanılır."
---

# Yenilik ve Ayırt Edici Nitelik Denetimi

## Görev
Tasarımın korumaya değer olup olmadığını belirleyen iki maddi şartı denetlemek: yenilik (SMK m.56/4) ve ayırt edici nitelik (SMK m.56/5, m.57). Bu, hem başvuru stratejisinin hem de hükümsüzlük/tecavüz savunmasının çekirdeğidir.

## Soğuk başlangıç (intake)
1. İncelenen tasarımın tüm görselleri ve hangi ürüne uygulandığı elimizde mi?
2. Karşılaştırılacak önceki tasarım(lar) — kamuya sunma tarihi ve kaynağı nedir?
3. İlgili sektörde tasarımcının seçenek özgürlüğü ne kadar geniş (teknik kısıt yoğunluğu)?
4. Tasarım sahibinin kendi açıklaması var mı (12 aylık grace period uygulanır mı)?

## Denetim şeması
1. Başvuru/rüçhan tarihini sabitle (SMK m.56/6): Karşılaştırma anı budur. Rüçhan varsa rüçhan tarihi esas alınır.
2. Yenilik (SMK m.56/4): Aynı tasarım, başvuru/rüçhan tarihinden önce dünyanın herhangi bir yerinde kamuya sunulmamış olmalı. "Yalnızca küçük ayrıntılarda farklılık" aynılık sayılır. İspat yükü yeniliğin yokluğunu iddia edende (hükümsüzlük davacısı).
3. Kamuya sunmanın istisnası (SMK m.58/3): Başvurudan önceki 12 ay içinde tasarımcının/halefinin/kötüye kullananın açıklaması yeniliği bozmaz (grace period). Bu süreyi titizlikle hesaplayın.
4. Ayırt edici nitelik (SMK m.56/5, m.57/1): Bilgilenmiş kullanıcıda bıraktığı genel izlenim, önceki tasarımların bıraktığından farklı olmalı. Değerlendirme bütünsel genel izlenime göre yapılır; ayrıntı farkları tek başına yetmez.
5. Seçenek özgürlüğü (SMK m.57/2): Tasarımcının seçenek özgürlüğü dar olan sektörlerde küçük farklar ayırt ediciliği sağlayabilir; geniş olduğunda daha belirgin fark aranır. Teknik/standart kısıtları belgeleyin.
6. Koruma dışı: Teknik zorunluluğun dayattığı görünüm ve zorunlu ara bağlantı (SMK m.58/4) yenilik/ayırt edicilikten önce eler.
7. Ara sonuç: Her iki şart için ayrı ayrı "karşılanıyor/karşılanmıyor" ve gerekçe; bilgilenmiş kullanıcının kim olduğu mutlaka tanımlanır.

## Çıktı modülleri
- Yenilik ve ayırt edicilik kontrol cetveli (önceki tasarım vs. dava konusu, fark analizi).
- Bilgilenmiş kullanıcı profili ve seçenek özgürlüğü değerlendirmesi.
- Grace period takvimi ve sonuç notu.

## Plugin bağlamı

Bu beceri `tasarim-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
