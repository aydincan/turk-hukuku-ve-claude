---
name: muvekkil-iletisimi
description: "Yabancı müvekkile süreç, riskler ve adımların sade anlatılması veya idari makama/mahkemeye resmî yazışma hazırlanması gerektiğinde kullanılır."
---

# Müvekkil ve Makam İletişimi

## Görev
Yabancı müvekkile süreci, riskleri ve sorumlulukları sade ve doğru biçimde aktarmak; Göç İdaresi, Bakanlık ve mahkemeyle yürütülen yazışmaları usulüne uygun hazırlamak.

## Soğuk başlangıç (intake)
1. İletişim kime yönelik (müvekkil bilgilendirmesi mi, makama resmî yazı mı)?
2. Müvekkilin dil ihtiyacı ve hukuki bilgisi düzeyi nedir?
3. Hangi konu aktarılacak (mevcut durum, risk, yapılması gerekenler, sonuç)?
4. Süreye bağlı, müvekkilin acil yapması gereken bir iş var mı?

## Denetim şeması
1. **Bilgilendirmenin doğruluğu**: Statü, işlem ve süreler madde dayanağıyla; abartısız, ne fazla iyimser ne yıldırıcı. Sonuç garantisi verilmez.
2. **Sade dil**: Hukuki terimler (idari gözetim, geri gönderme yasağı, yürütmenin durdurulması) gündelik dile çevrilir; müvekkilin yapması gereken somut adımlar (belge temini, randevu, imza, son gün) listelenir.
3. **Makam yazışması**: Resmî üslup, doğru makam adı, dosya/başvuru numarası `[doldurulacak]`, dayanak madde; bilgi/belge talebi ve süreye atıf net yazılır.
4. **Riziko ve sorumluluk paylaşımı**: Müvekkilin verdiği eksik/yanlış bilginin sonucu (ret, iptal, sahte belge ile vatandaşlığın iptali) açıkça hatırlatılır; belge teyidi vurgulanır.
5. **Gizlilik**: Müvekkilin korunma/aile bilgileri hassas veri olarak işlenir; üçüncü kişilere paylaşımda dikkat.
**Ara sonuç**: Anlaşılır, eyleme dönük bir bilgilendirme veya usulüne uygun bir makam yazısı.

## Çıktı modülleri
- Müvekkile sade bilgilendirme notu (durum, risk, yapılacaklar, son gün).
- Makama/mahkemeye resmî yazı/dilekçe taslağı.
- Müvekkilden istenecek belge ve onay listesi.

## Plugin bağlamı

Bu beceri `goc-yabancilar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
