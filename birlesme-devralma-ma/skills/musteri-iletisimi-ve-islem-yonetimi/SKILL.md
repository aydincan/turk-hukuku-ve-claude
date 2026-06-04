---
name: musteri-iletisimi-ve-islem-yonetimi
description: "M&A işleminin yol haritasını müvekkile sade biçimde anlatmak, riskleri ve karar noktalarını özetlemek, term sheet aşamasından kapanışa süreç ve sorumluluk dağılımını yönetmek için kullanılır."
---

# Müvekkil İletişimi ve İşlem Yönetimi

## Görev
İşlemi müvekkilin anlayacağı dille çerçevelemek, kritik karar noktalarını ve riskleri özetlemek, term sheet'ten kapanışa süreci ve görev dağılımını yönetmek.

## Soğuk başlangıç (intake)
- Müvekkilin işlemdeki önceliği ne (hız, fiyat, risk minimizasyonu)?
- Müvekkil M&A deneyimi olan kurumsal bir aktör mü, ilk kez mi?
- Karşı tarafın danışmanları ve müzakere üslubu nasıl?
- İşlem gizliliği ve kamuya açıklama hassasiyeti var mı?

## Denetim şeması
1. **Term sheet / niyet mektubu**: Bağlayıcı (gizlilik, münhasırlık) ve bağlayıcı olmayan hükümlerin ayrımı net yapılır; yanlış anlaşılma TBK m.1 anlamında erken bağlanma riski yaratır.
2. **Gizlilik (NDA)**: Bilgi paylaşımı öncesi gizlilik sözleşmesi ve veri odası kuralları.
3. **Süreç planı**: Signing → CP → closing → post-closing aşamaları, her aşamada müvekkilden beklenen kararlar ve onaylar.
4. **Risk iletişimi**: DD kırmızı bayrakları, indemnity sınırları ve earn-out belirsizlikleri sade dille; karar müvekkile bırakılır, hukuki sonuç açıklanır.
5. **Çıkar çatışması ve gizlilik**: Avukatlık Kanunu (1136) ve meslek kuralları çerçevesinde çatışma taraması ve sır saklama.
6. **İspat/kayıt hijyeni**: Önemli kararlar yazılı teyitle (e-posta/karar notu) belgelenir.
7. **Ara sonuç**: Müvekkile karar matrisi (seçenek, sonuç, öneri) sunulur.

## Çıktı modülleri
- İşlem yol haritası (sade dilli, aşamalı)
- Karar noktaları ve risk özeti (yönetici özeti)
- Term sheet bağlayıcılık ayrım notu
- Görev/sorumluluk dağılım tablosu (responsibility matrix)

## Plugin bağlamı

Bu beceri `birlesme-devralma-ma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
