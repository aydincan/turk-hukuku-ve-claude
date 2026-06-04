---
name: kloz-tasarimi-strateji
description: "Bir sözleşmeye tahkim veya arabuluculuk klozu yerleştirirken forum, dil, yer, kurum ve çok kademeli uyuşmazlık çözüm zinciri kurmak; uyuşmazlık öncesi strateji belirlemek gerektiğinde kullanılır."
---

# Kloz Tasarımı ve Forum Stratejisi

## Görev
Sözleşme müzakeresinde uyuşmazlık çözüm mimarisini kurmak: tahkim mi devlet yargısı mı,
çok kademeli (müzakere-arabuluculuk-tahkim) zincir mi; yer, dil, kurum ve uygulanacak
hukuk seçimini stratejik olarak belirlemek.

## Soğuk başlangıç (intake)
1. Sözleşme yerli mi sınır ötesi mi, taraflar ve ifa yeri nerede?
2. Uyuşmazlık değeri ve niteliği (gizlilik, teknik bilirkişi, hız ihtiyacı) nedir?
3. İcra/tenfiz nerede aranacak (karşı tarafın malvarlığı nerede)?
4. Çok kademeli çözüm (önce arabuluculuk, sonra tahkim) isteniyor mu?

## Denetim şeması
1. **Forum seçimi**: Yabancılık unsuru ve tenfiz ihtiyacı varsa tahkim (**New York
   Sözleşmesi** sayesinde tenfiz kolaylığı) tercih edilir; tamamen yerli ve düşük değerli
   uyuşmazlıkta devlet yargısı daha ekonomik olabilir. Elverişlilik **HMK m.408** süzgeci.
2. **Kloz unsurları**: Tahkim klozunda **tahkim yeri, dil, hakem sayısı, kurum kuralları**
   (ör. ISTAC, ICC, ITOTAM) ve esasa uygulanacak hukuk açıkça belirlenir; yazılılık
   (**HMK m.412**, **MTK m.4**) sağlanır. Eksik/çelişkili kloz patolojiktir.
3. **Çok kademeli (multi-tier) zincir**: Önce zorunlu müzakere/arabuluculuk, sonra tahkim
   öngörülebilir; her kademenin **süresi ve geçiş şartı** somut yazılmalı, aksi halde
   tahkime erişim tartışmaya açılır. Dava şartı arabuluculuk kapsamındaki uyuşmazlıklarda
   yasal zorunluluk ayrıca gözetilir.
4. **Tenfiz odaklı tasarım**: Hakem kararının icra edileceği ülkenin rejimi (kamu düzeni,
   elverişlilik) baştan değerlendirilir; karşı tarafın malvarlığının bulunduğu yer
   belirleyicidir.
5. **Ara sonuç**: Önerilen forum, kloz iskeleti ve strateji gerekçesi.

## Çıktı modülleri
- Forum karşılaştırma tablosu (tahkim/arabuluculuk/devlet yargısı; maliyet-hız-tenfiz).
- Tahkim ve/veya çok kademeli kloz taslağı ([doldurulacak] yer, dil, kurum, hukuk).
- Tenfiz/strateji risk notu.

## Plugin bağlamı

Bu beceri `tahkim-arabuluculuk` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
