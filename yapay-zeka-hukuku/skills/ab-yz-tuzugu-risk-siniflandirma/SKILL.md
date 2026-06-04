---
name: ab-yz-tuzugu-risk-siniflandirma
description: "Müvekkilin yapay zekâ sistemi AB pazarına ürün veya hizmet sunduğunda ya da karşılaştırmalı uyum hedeflendiğinde AB Yapay Zekâ Tüzüğü kapsamında yasak/yüksek riskli/sınırlı risk sınıflandırması ve yükümlülükler değerlendirildiğinde kullanılır."
---

# AB Yapay Zekâ Tüzüğü ve Risk Sınıflandırması

## Görev
Bir yapay zekâ sisteminin AB Yapay Zekâ Tüzüğü (Regulation (EU) 2024/1689) kapsamında risk sınıfını belirlemek ve buna bağlı yükümlülükleri tespit etmek; Türkiye için bunun bağlayıcı değil karşılaştırmalı/sözleşmesel bir referans olduğunu netleştirmek.

## Soğuk başlangıç (intake)
1. Sistem AB'deki kullanıcılara/pazara sunuluyor mu, çıktısı AB'de kullanılıyor mu?
2. Müvekkilin rolü: sağlayıcı (provider), uygulayıcı (deployer), ithalatçı, dağıtıcı?
3. Sistem ne yapıyor: biyometrik tanıma, kredi/işe alım skorlama, kritik altyapı, genel amaçlı model (GPAI)?
4. Mevcut uyum belgeleri (teknik dokümantasyon, uygunluk değerlendirmesi) var mı?

## Denetim şeması
1. **Uygulanabilirlik**: Tüzük Türkiye'de doğrudan yürürlükte değildir. AB'ye ürün/hizmet sunuluyorsa ülke-dışı etki nedeniyle uygulanabilir; yalnız Türkiye içiyse yön gösterici/sözleşmesel referanstır. Ara sonuç: bağlayıcı mı, referans mı.
2. **Risk sınıfı**: (a) Yasak uygulamalar (ör. sosyal puanlama, manipülatif sistemler); (b) Yüksek riskli sistemler (biyometri, eğitim, istihdam, kredi, kamu hizmeti, kritik altyapı) — uygunluk değerlendirmesi, risk yönetimi, veri yönetişimi, insan gözetimi, kayıt tutma yükümlülükleri; (c) Sınırlı risk — şeffaflık (örn. sohbet botu/derin sahte etiketleme); (d) Asgari risk.
3. **GPAI/temel model**: Genel amaçlı modeller için teknik dokümantasyon, telif uyum politikası ve sistemik risk eşiği yükümlülükleri.
4. **Rol bazlı yükümlülük**: Sağlayıcı ve uygulayıcı için farklı görevler; sözleşmeyle rollerin ve sorumlulukların netleştirilmesi gerekir.
5. **Türkiye'ye yansıma**: Tüzük yükümlülükleri Türk müvekkiline ancak sözleşme veya AB'ye erişim üzerinden gelir; Türkiye'de paralel uyum çoğu zaman KVKK + sektörel mevzuatla sağlanır.

Tüzük metni ve yürürlük takvimi sık güncellenir; her atıfta resmî AB kaynağından versiyon kontrol et, künyeyi [doğrulanacak] işaretle.

## Çıktı modülleri
- Risk sınıflandırma sonucu ve gerekçesi.
- Rol bazlı yükümlülük tablosu.
- Türkiye-AB uyum köprüsü ve sözleşmesel aktarım önerisi.

## Plugin bağlamı

Bu beceri `yapay-zeka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
