---
name: risk-ve-uyum-stratejisi
description: "İhraççı, yönetici veya yatırım kuruluşu için sermaye piyasası mevzuatına uyum, yaptırım/cezai risk haritası, içsel bilgi yönetimi ve önleyici politika tasarımı gerektiğinde kullanılır."
---

# Risk Değerlendirmesi ve Uyum Stratejisi

## Görev
İhraççı/yönetici/yatırım kuruluşu için sermaye piyasası risklerini haritalamak; idari ve cezai sorumluluk olasılıklarını tartmak; önleyici uyum politikaları önermek.

## Soğuk başlangıç (intake)
- Müvekkil kim: ihraççı, yönetim kurulu üyesi, yatırım kuruluşu, ortak mı?
- Risk konusu: kamuyu aydınlatma, içsel bilgi yönetimi, çağrı, ilişkili taraf işlemleri mi?
- Geçmişte Kurul incelemesi/yaptırımı veya devam eden işlem var mı?
- Amaç önleyici uyum mu, devam eden bir riske müdahale mi?

## Denetim şeması
1. **Risk envanteri:** Faaliyet türüne göre yükümlülükler listelenir: özel durum açıklamaları (SPK m.15), finansal raporlama (m.14), içsel bilgi erişen listesi, ilişkili taraf/örtülü kazanç aktarımı (m.21), geri alım (m.22), çağrı (m.25-26).
2. **Olasılık-etki tartımı:** Her risk için ihlal olasılığı ve sonucu (idari para cezası m.103, menfaat iadesi m.104, tedbir m.96-99, cezai sorumluluk m.106-107) değerlendirilir; ölçülülük ve tekerrür etkisi gözetilir. Ara sonuç: öncelikli riskler sıralanır.
3. **İçsel bilgi yönetimi:** Bilgi bariyerleri, içsel bilgiye erişen listesi, açıklama/erteleme prosedürü ve işlem yasağı pencereleri tasarlanır; yöneticilerin kişisel işlemleri için kurallar konur.
4. **Sözleşmesel dağıtım:** Aracılık, danışmanlık ve M&A işlemlerinde sorumluluk ve tazminat klozları (TBK çerçevesinde) ile bilgi/beyan yükümlülükleri dengelenir.
5. **Belgeleme:** Tüm karar ve gerekçelerin yazılı/iz bırakacak şekilde tutulması; ispat ve savunma için bu kayıtların kritikliği vurgulanır.

## Çıktı modülleri
- Risk haritası (olasılık-etki matrisi)
- İçsel bilgi yönetim politikası iskeleti
- Uyum kontrol listesi ve sorumluluk dağıtım önerisi
- Öncelikli eylem planı

## Plugin bağlamı

Bu beceri `sermaye-piyasasi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
