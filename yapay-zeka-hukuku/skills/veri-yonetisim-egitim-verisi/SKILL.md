---
name: veri-yonetisim-egitim-verisi
description: "Bir yapay zekâ modelinin eğitiminde veya çalıştırılmasında kullanılan veri kümelerinin hukuka uygunluğu, kişisel veri içerip içermediği, kaynağı ve amaç sınırı değerlendirildiğinde ve web kazıma (scraping) ile veri toplama riski incelendiğinde kullanılır."
---

# Veri Yönetişimi ve Eğitim Verisi Uyumu

## Görev
Model eğitiminde ve çalıştırılmasında kullanılan veri kümelerinin kaynağını, hukuki dayanağını ve amaç sınırını denetleyerek veri yönetişimi uyum haritası ve risk azaltma önlemleri çıkarmak.

## Soğuk başlangıç (intake)
1. Eğitim verisi nereden: kullanıcı verisi, kamuya açık web (scraping), satın alınan/lisanslı set, sentetik veri?
2. Veride kişisel veri var mı; anonimleştirme/takma adlandırma yapıldı mı?
3. Verinin ilk toplanma amacı ile model eğitimi amacı uyumlu mu?
4. Üçüncü kişi/işleyen kullanılıyor mu; veri işleme sözleşmesi var mı?

## Denetim şeması
1. **Kişisel veri tespiti**: Veri kümesinde gerçek kişi belirli/belirlenebilir mi (KVKK m.3). Anonim veri KVKK dışı; ancak "yeniden kişiselleştirilebilir" takma adlı veri hâlâ kişisel veridir. Ara sonuç: KVKK uygulanır mı.
2. **İşleme şartı ve amaç**: m.5 dayanağı (çoğu eğitimde meşru menfaat tartışılır; özel nitelikli veride m.6 çok dar) ve m.4 amaçla bağlılık — başka amaçla toplanan verinin model eğitiminde kullanımı "ikincil işleme" sorununu doğurur, bağdaşırlık değerlendirilir.
3. **Web kazıma**: Kamuya açık olması KVKK muafiyeti değildir; m.28/1-d istisnası dar yorumlanır. Ayrıca kaynağın kullanım şartları (sözleşmesel) ve FSEK ihlali ayrıca denetlenir.
4. **Güvenlik ve işleyen**: m.12 teknik/idari tedbirler; üçüncü kişi işliyorsa veri işleyen sözleşmesi ve sorumluluk paylaşımı. Yurt dışı eğitim altyapısı varsa m.9 aktarım rejimi.
5. **Belgeleme**: Veri kaynağı envanteri, dayanak ve DPIA benzeri etki değerlendirmesi ispat yükünü veri sorumlusunda karşılayacak biçimde tutulmalı.

İçtihat ve Kurul yaklaşımı için kvkk.gov.tr ve karararama.danistay.gov.tr; künyeyi [doğrulanacak] işaretle.

## Çıktı modülleri
- Eğitim verisi kaynak ve dayanak envanteri.
- Risk haritası (scraping/ikincil işleme/özel nitelikli veri).
- Uyum aksiyon listesi ve veri işleyen sözleşmesi maddeleri.

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
