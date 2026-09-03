---
name: veri-guvenligi-tedbir-denetimi
description: "KVKK m.12 kapsamında teknik ve idari güvenlik tedbirlerinin Kurul rehberine göre denetlenmesi veya tedbir boşluklarının tespiti gerektiğinde kullanılır."
---

# Veri Güvenliği ve Teknik-İdari Tedbir Denetimi

## Görev
KVKK m.12/1 uyarınca veri sorumlusunun aldığı teknik ve idari tedbirleri Kurul'un Teknik ve İdari Tedbirler Rehberi ölçütünde denetlemek; boşlukları risk seviyesine göre işaretlemek. Bu beceri hukuki uyumu güvenlik kontrolleriyle köprüler.

## Soğuk başlangıç (intake)
1. Verilere kimler erişiyor; yetki ve erişim kontrolü (rol bazlı) tanımlı mı?
2. Veriler şifreleniyor mu (durağan/iletimde); yedekleme ve loglama var mı?
3. Çalışanlarla gizlilik taahhüdü ve KVKK farkındalık eğitimi yapılıyor mu?
4. Veri işleyenlerle (bulut, dış hizmet) m.12 sözleşmesi ve güvenlik denetimi var mı?

## Denetim şeması
1. **İdari tedbirler**: Kişisel veri envanteri, kurumsal politikalar, gizlilik taahhütleri, erişim yetki matrisi, eğitim ve farkındalık programı, veri işleyenlerle m.12 sözleşmeleri ve denetim hakkı. Her biri "var/eksik" işaretlenir.
2. **Teknik tedbirler**: Yetkilendirme ve kimlik doğrulama, ağ güvenliği, şifreleme, log tutma, sızma testi/zafiyet taraması, yedekleme, anti-virüs/güvenlik duvarı, silme/yok etme altyapısı. Özel nitelikli veride (m.6) Kurul ek tedbir bekler (örn. şifreleme ve daha sıkı erişim kontrolü).
3. **Veri işleyen zinciri**: Bulut/SaaS ve dış hizmet sağlayıcılarla yazılı m.12 sözleşmesi, sorumluluk paylaşımı ve denetim yetkisi kontrol edilir; sözleşmesiz işleyen yüksek risk bulgusudur.
4. **Orantılılık**: Tedbirler verinin niteliği ve riskiyle orantılı olmalı; eksik tedbir, ihlal halinde m.18 ve tazminat sorumluluğunu ağırlaştırır.
5. **Ara sonuç**: Güvenlik tedbiri eksikliği yalnızca ihlal anında değil, denetimde de m.12 ihlali olarak skorlanır.

İspat yükü: Uygun tedbirlerin alındığını veri sorumlusu belge ve kayıtla ispatlar; tedbirlerin yokluğu ihlalde kusur karinesini güçlendirir.

## Çıktı modülleri
- Teknik/idari tedbir kontrol listesi (Rehber kalemleriyle eşleşen, Uygun/Eksik).
- Veri işleyen sözleşme ve güvenlik denetim durum tablosu.
- Tedbir boşluğu risk haritası ve öncelikli aksiyon listesi.

## Plugin bağlamı

Bu beceri `kvkk-uyum-checker` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
