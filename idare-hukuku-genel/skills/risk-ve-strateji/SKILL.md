---
name: risk-ve-strateji
description: "İdari uyuşmazlıkta kazanma ihtimalini, süre/yargı yolu risklerini, idari ve adli yol seçeneklerini ve müzakere/uzlaşma imkânlarını tartmak için kullanılır; dava açma kararı verilmeden önce bütünsel değerlendirme istendiğinde başvurulur."
---

# Risk Değerlendirmesi ve Dava Stratejisi

## Görev
Dosyayı bütünsel değerlendirip dava açma/açmama, hangi yolu izleme ve idare ile müzakere kararını risk temelli vermek; müvekkile gerçekçi bir tablo sunmak.

## Soğuk başlangıç (intake)
1. Müvekkilin asıl hedefi nedir (işlemin iptali mi, tazminat mı, süre kazanmak mı)?
2. En kritik risk hangisi (süre, ehliyet, yargı yolu, esasın zayıflığı)?
3. İdareyle uzlaşma/işlemin geri alınması imkânı var mı?
4. Zaman ve maliyet baskısı ne düzeyde?

## Denetim şeması
1. **Eşik (kabul edilebilirlik) riskleri.** Önce süre, ehliyet-menfaat, görev-yetki ve zorunlu ön başvuru (m.11/m.13) eşiklerini denetle; biri kapalıysa esas tartışması anlamsızdır.
2. **Esasın gücü.** Beş unsur denetiminden çıkan aykırılıkları "güçlü / tartışmalı / zayıf" olarak derecelendir; idarenin re'sen araştırmada savunmasını öngör.
3. **Yürütmenin durdurulması ihtimali.** m.27 çifte koşulu karşılanıyor mu; YD alınamazsa işlem icra edilir ve zarar büyür mü?
4. **Alternatif yollar.** İYUK m.11 ile işlemin idarece geri alınması/düzeltilmesi, üst makama başvuru, bilgi edinme (4982) ile belge toplama, uzlaşma (vergi alanında) gibi dava dışı seçenekler.
5. **Maliyet-fayda.** Yargılama süresi, harç/masraf, vekâlet ücreti riski, icranın geri dönülebilirliği ve müvekkilin hedefi birlikte tartılır.
6. **İçtihat eğilimi.** Benzer uyuşmazlıkta Danıştay/İDDK eğilimini araştır ve künyeyi `[doğrulanacak]` işaretle (karararama.danistay.gov.tr).
7. **Ara sonuç.** Tavsiye edilen yol (dava/başvuru/uzlaşma) + gerekçe + en büyük üç risk ve azaltma önerisi.

## Çıktı modülleri
- Eşik riskleri kontrol listesi (süre/ehliyet/görev/ön başvuru).
- Esas gücü derecelendirme tablosu.
- Yol seçenekleri karşılaştırması (dava/başvuru/uzlaşma).
- Müvekkile sunulacak risk özeti ve tavsiye.

## Plugin bağlamı

Bu beceri `idare-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
