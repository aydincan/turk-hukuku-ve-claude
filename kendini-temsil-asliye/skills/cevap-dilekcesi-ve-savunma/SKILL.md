---
name: cevap-dilekcesi-ve-savunma
description: "Kendisine dava açılmış ve cevap dilekçesi vermesi gereken davalı, itirazlarını ve karşı delillerini düzenlemek istediğinde veya zamanaşımı, yetki, takas gibi savunmaları ileri sürmek istediğinde kullanılır."
---

# Cevap Dilekçesi ve Savunma Hazırlama

## Görev
Davalı tarafın süresinde, eksiksiz ve stratejik bir cevap dilekçesi vermesini sağlamak; itiraz ve def'ileri doğru sırayla ileri sürmek.

## Soğuk başlangıç (intake)
- Dava dilekçesi/tebligat size ne zaman tebliğ edildi (süre için kritik)?
- İddiaların hangisini kabul, hangisini inkâr ediyorsunuz?
- Yetki/görev itirazınız var mı?
- Alacak zamanaşımına uğramış olabilir mi?
- Karşı alacağınız (takas) veya karşı dava talebiniz var mı?

## Denetim şeması
1. **Süre:** Cevap dilekçesi, dava dilekçesinin tebliğinden itibaren kural olarak iki hafta içinde verilir (HMK m.127); basit yargılamada da iki hafta (m.317). Süre içinde verilmezse davacının dilekçesindeki vakıaları inkâr etmiş sayılır (m.128); ek süre talep edilebilir.
2. **İlk itirazlar (HMK m.116, 117):** Kesin yetki dışındaki yetki itirazı, tahkim itirazı, iş bölümü gibi itirazlar **cevap dilekçesinde birlikte** ileri sürülür; sonradan ileri sürülemez.
3. **Maddi savunma:** Vakıaların açıkça kabul/inkârı; inkâr edilen her vakıa için karşı delil (m.129). Susulan vakıa ikrar sayılabilir.
4. **Def'iler:** Zamanaşımı def'i talep edilmedikçe hâkim re'sen dikkate almaz — mutlaka açıkça ileri sürülür. Takas, ödemezlik def'i (TBK m.97) gibi savunmalar bu aşamada belirtilir.
5. **Karşı dava:** Şartları varsa (HMK m.132-134) cevap dilekçesiyle birlikte açılır.
6. **Ara sonuç:** Süre + ilk itirazlar + maddi inkâr + def'iler eksiksizse savunma tamamdır; basit yargılamada savunmanın genişletilmesi de sınırlıdır (m.319).

## Çıktı modülleri
- Cevap dilekçesi taslağı (itiraz/def'i/karşı delil bölümleriyle).
- Süre uyarısı ve kalan gün hesabı.
- Zamanaşımı/takas kontrol notu.

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
