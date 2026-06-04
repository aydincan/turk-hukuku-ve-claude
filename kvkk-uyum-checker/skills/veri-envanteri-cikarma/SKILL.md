---
name: veri-envanteri-cikarma
description: "Kuruluşun hangi veriyi hangi amaç ve hukuki sebeple işlediğinin haritalanması, mevcut envanterin doğrulanması veya sıfırdan envanter oluşturulması gerektiğinde kullanılır."
---

# Kişisel Veri İşleme Envanteri Çıkarma

## Görev
Tüm uyum mimarisinin temel taşı olan kişisel veri işleme envanterini çıkarmak veya mevcut envanteri fiili işleme ile karşılaştırarak doğrulamak. Diğer her belge (aydınlatma, VERBİS, saklama matrisi) envanterle tutarlı olmak zorundadır.

## Soğuk başlangıç (intake)
1. Hangi süreçlerde kişisel veri toplanıyor (işe alım, satış, üyelik, ziyaretçi kaydı, kamera)?
2. Her süreçte hangi veri kategorileri işleniyor; özel nitelikli veri (m.6) var mı?
3. Veri kimlerden alınıyor, kime aktarılıyor, nerede saklanıyor (yurt içi/yurt dışı, bulut)?
4. Mevcut bir envanter var mı, ne zaman güncellendi?

## Denetim şeması
1. **Faaliyet bazlı kayıt**: Her işleme faaliyeti için satır açılır — faaliyet adı, veri konusu kişi grubu, veri kategorileri, işleme amacı.
2. **Hukuki sebep haritalama (m.5/m.6)**: Her faaliyet için geçerli işleme şartı yazılır; açık rıza dışı sebepler önce denenir, açık rızaya gereksiz bağımlılık "kırmızı bayrak" olarak işaretlenir.
3. **Aktarım ve saklama sütunları**: Alıcı/alıcı grupları, yurt içi/yurt dışı aktarım, aktarım mekanizması (m.8-9), azami saklama süresi (m.4/2-d dayanağıyla).
4. **Özel nitelikli ve hassas alanlar**: m.6 verisi, çocuk verisi, biyometrik/kamera kayıtları ayrı işaretlenir; bunlar yüksek risk grubudur.
5. **Tutarlılık çapraz kontrolü**: Envanter, VERBİS kaydı ve aydınlatma metinleriyle satır satır karşılaştırılır; uyumsuzluklar bulgu listesine geçer.
6. **Ara sonuç**: Eksik/çelişkili envanter, m.4 ilke ihlallerinin ve VERBİS hatalarının kaynağıdır; envanter "yaşayan" belge olarak güncelleme döngüsüne bağlanır.

İspat yükü: İşlemenin geçerli şarta dayandığını ve envanterin gerçeği yansıttığını veri sorumlusu gösterir.

## Çıktı modülleri
- Faaliyet bazlı işleme envanteri tablosu (Excel'lenebilir).
- Hukuki sebep–faaliyet eşleştirme ve "açık rıza bağımlılığı" uyarı listesi.
- Envanter–VERBİS–aydınlatma tutarlılık çapraz kontrol raporu.

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
