---
name: denklestirme-ve-iade
description: "Mirasbırakanın sağlığında yasal mirasçılara yaptığı karşılıksız kazandırmaların paylaşmada hesaba katılması ya da terekeye iadesi gerektiğinde; çeyiz, kuruluş sermayesi, eğitim gideri ve malvarlığı devri tartışmalarında kullanılır."
---

# Denkleştirme (İade) Davası

## Görev
Yasal mirasçıların mirasbırakandan sağlararası aldıkları karşılıksız kazandırmaların paylaşmada denkleştirilmesini (iade veya hesaba katma) TMK m.669-675 uyarınca sağlamak.

## Soğuk başlangıç (intake)
- Kazandırmayı alan yasal mirasçı mı? (denkleştirme yalnızca yasal mirasçılar arası)
- Kazandırma türü: çeyiz, kuruluş sermayesi, borç ödeme, malvarlığı devri, eğitim gideri?
- Mirasbırakan iadeden açıkça bağışık tuttu mu (m.669/1)?
- Kazandırma tarihi ve ölüm tarihindeki değeri?
- Alan kişi mirası reddetti mi? (m.674 — reddedende iade yükü farklı)

## Denetim şeması
1. **İade yükümlülüğünü belirle (m.669):** Yasal mirasçılar, miras payına mahsuben yapılan kazandırmaları iadeyle yükümlüdür. Mirasbırakanın aksi iradesi (bağışıklık) açık olmalı; altsoya çeyiz/kuruluş sermayesi/malvarlığı devri için iade karinesi vardır (m.669/2).
2. **Kapsam dışını ayır (m.670):** Olağan eğitim-öğretim giderleri, mutat hediyeler kural olarak iadeye tabi değildir; aşırı olanlar tabidir.
3. **İade biçimini seç (m.671):** Mirasçı, aldığını aynen geri verebilir veya değerini miras payına mahsup edebilir; kazandırma miras payını aşsa bile aşan kısım — mirasbırakanın iradesi ve tenkis kuralları saklı — iade edilmeyebilir (m.672).
4. **Değerleme (m.673):** İade, kazandırmanın denkleştirme anındaki (paylaşma anı) değerine göre; elden çıkarılmışsa sürüm değeri esas alınır.
5. **Çocukların çocukları (m.675):** Önceden ölen mirasçının yerine geçenler, onun almadığı kazandırmaları iade etmez ama kendi aldıklarını iade eder. Ara sonuç: iadeye tabi tutar + biçim (aynen/mahsup) + paylaşmaya etkisi.

## Çıktı modülleri
- Denkleştirme hesap tablosu (kazandırma, değer, mahsup)
- Tenkis ile denkleştirme ayrımı notu (hangisi uygulanır)
- Paylaşma/ortaklığın giderilmesi davasına entegre talep
- İspat için kazandırma belgeleri dizini

## Plugin bağlamı

Bu beceri `miras-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
