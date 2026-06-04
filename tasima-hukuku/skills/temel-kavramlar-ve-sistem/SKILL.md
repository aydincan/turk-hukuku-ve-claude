---
name: temel-kavramlar-ve-sistem
description: "Taşıma sözleşmesinin niteliği, taşıyıcı-komisyoncu-gönderen-gönderilen sıfatları ve uygulanacak rejimin (TTK, CMR, deniz/hava) belirlenmesi gerektiğinde; dosyanın hangi hukuki çerçeveye oturduğunu netleştirmek için kullanılır."
---

# Temel Kavramlar ve Taşıma Sistematiği

## Görev
Somut olayda hangi taşıma rejiminin (TTK Dördüncü Kitap, CMR, deniz/hava/demiryolu) uygulanacağını, tarafların sıfatlarını ve sözleşme tipini doğru saptamak. Bu beceri, sonraki tüm sorumluluk ve usul analizinin temelini kurar.

## Soğuk başlangıç (intake)
1. Taşıma karayolu, denizyolu, havayolu, demiryolu mu yoksa birden çok tür mü (karma/multimodal)?
2. Taşıma tamamen yurt içi mi, yoksa çıkış/varış noktalarından biri yurt dışında mı?
3. Müvekkilin sıfatı nedir: taşıyıcı, gönderen, gönderilen, alt taşıyıcı, taşıma işleri komisyoncusu mu?
4. Elinizde taşıma senedi (CMR belgesi/irsaliye/konişmento) var mı; düzenleyeni ve içeriği nedir?

## Denetim şeması
1. **Taşıma türü:** Karayolu eşya taşıması ise TTK m.850 vd.; deniz navlunu TTK Beşinci Kitap; havayolu Montreal/Varşova; demiryolu COTIF-CIM.
2. **Sınır aşan unsur:** Çıkış veya varış ülkesi CMR tarafı ise, taşıma karayoluyla ve ücret karşılığı yapılmışsa CMR emredici uygulanır (CMR m.1). CMR m.41 uyarınca aksine anlaşmalar batıldır; TTK m.852 CMR'nin önceliğini saklı tutar. İç taşımada TTK uygulanır.
3. **Taşıyıcı sıfatı:** TTK m.850/2-3 — eşyayı taşımayı üstlenen veya işletmesi gereği taşıma yapan taşıyıcıdır; fiilî taşıyan-akdî taşıyan ayrımına dikkat (alt taşıma TTK m.879).
4. **Komisyoncudan ayırma:** Kişi yalnızca taşımayı organize edip kendi adına taşıyıcılarla mı sözleşiyor (komisyoncu, TTK m.917) yoksa taşımayı bizzat mı üstleniyor? Sabit ücret/toplu yük halinde komisyoncu taşıyıcı gibi sorumlu olur (TTK m.926-927).
5. **Sözleşmenin kuruluşu:** Rızai sözleşmedir; taşıma senedi ispat aracıdır, geçerlilik şartı değildir (TTK m.856).
6. **Ara sonuç:** Uygulanacak norm seti, taraf sıfatları ve sorumluluk rejiminin çatısı belirlenir.

## Çıktı modülleri
- Rejim belirleme tablosu (tür / iç-dış / uygulanacak metin).
- Taraf-sıfat haritası (akdî/fiilî taşıyıcı, komisyoncu, gönderen, gönderilen).
- Uygulanacak başat maddeler listesi ve dosyaya özel ilk hukuki çerçeve notu.

## Plugin bağlamı

Bu beceri `tasima-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
