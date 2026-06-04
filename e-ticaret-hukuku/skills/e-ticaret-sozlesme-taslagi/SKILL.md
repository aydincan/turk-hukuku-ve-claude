---
name: e-ticaret-sozlesme-taslagi
description: "Mesafeli satış sözleşmesi, ön bilgilendirme formu, üyelik/kullanım koşulları, aracılık sözleşmesi veya açık rıza/onay metni gibi e-ticaret belgelerinin hazırlanması ya da revize edilmesi gerektiğinde kullanılır."
---

# E-Ticaret Sözleşme ve Metin Taslakları

## Görev
E-ticaret faaliyetinin ihtiyaç duyduğu belgeleri (mesafeli satış sözleşmesi, ön bilgilendirme formu, kullanım koşulları, aracılık sözleşmesi, ileti onayı, aydınlatma metni) mevzuata uygun ve [doldurulacak] yer tutucularıyla üretmek.

## Soğuk başlangıç (intake)
- Hangi belge isteniyor; taraflar B2C mi B2B mi?
- Müvekkil hizmet sağlayıcı mı, aracı platform mu?
- Konu mal mı hizmet mi dijital içerik mi (cayma istisnaları)?
- Ödeme, teslim, iade ve uyuşmazlık çözüm tercihi nedir?

## Denetim şeması
1. Zorunlu içerik eşlemesi: mesafeli satış sözleşmesi ve ön bilgilendirme formu için 6502 m.48 ve Mesafeli Sözleşmeler Yönetmeliği'nin asgari içerik listesi (taraflar, mal/hizmet nitelikleri, toplam fiyat, ödeme/teslim, cayma hakkı ve istisnaları, şikâyet mercii) madde madde doldurulur.
2. 6563 uyumu: kullanım koşullarına bilgi verme (m.3), sözleşme öncesi teknik adımlar ve hata düzeltme (m.4), sipariş teyidi (m.5) hükümleri işlenir.
3. Emredici sınır denetimi: tüketici aleyhine, cayma hakkını kaldıran veya hakem heyeti/mahkeme yolunu engelleyen haksız şartlar (6502 m.5) elenir; aracılık sözleşmesinde ETAHS yükümlülükleriyle çelişen kayıtlar düzeltilir.
4. KVKK/ileti metinleri: açık rıza ve aydınlatma ayrı belgelenir; ticari ileti onayı İYS uyumlu kurgulanır.
5. Uyuşmazlık ve yürürlük: yetki/tahkim, uygulanacak hukuk, yürürlük ve değişiklik bildirimi maddeleri eklenir; tüketici sözleşmelerinde zorunlu yargı yolu saklı tutulur.
İspat ve saklama: sözleşme/onayın kalıcı veri saklayıcısında tutulması ve erişilebilirliği sağlanır.

## Çıktı modülleri
- Belge taslağı ([doldurulacak] alanlarla).
- Zorunlu içerik kontrol listesi.
- Haksız/eksik şart revizyon notu.

## Plugin bağlamı

Bu beceri `e-ticaret-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
