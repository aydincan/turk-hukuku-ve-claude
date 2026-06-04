---
name: gizlilik-veri-medya
description: "Haber veya yayında özel hayatın gizliliği, görüntü-ses kaydının izinsiz yayını, kişisel verilerin işlenmesi ve KVKK ile basın özgürlüğü çatışması söz konusu olduğunda kullanılır."
---

# Özel Hayat, Kişisel Veri ve Medya

## Görev
Yayında özel hayatın gizliliği (Anayasa m.20), görüntü ve ses üzerindeki hak ile kişisel verilerin korunmasını (6698 sayılı KVKK) basın özgürlüğüyle dengelemek.

## Soğuk başlangıç (intake)
1. Yayımlanan içerik kişinin özel/aile hayatına mı ait?
2. Görüntü/ses rıza ile mi alındı, gizli mi kaydedildi?
3. İçerik kamusal tartışmaya katkı sunuyor mu?
4. Kişisel veri işleme gazetecilik istisnası kapsamında mı?

## Denetim şeması
1. **Özel hayat alanı**: Anayasa m.20 ve TMK m.24 koruması; kişinin gizli alanı, özel alanı ve kamuya açık alanı ayrımı yapılır. Kamuya mal olmuş kişilerde kamusal faaliyete ilişkin kısım daha düşük korumadan yararlanır.
2. **Görüntü ve ses**: İzinsiz kayıt ve yayım, rıza yoksa ve kamu yararı yoksa hukuka aykırıdır; TCK m.134 ve TMK m.24 birlikte değerlendirilir.
3. **KVKK çatışması**: Kişisel verilerin işlenmesi kural olarak rıza veya kanuni şarta bağlıdır (KVKK m.5). Ancak gazetecilik amacıyla işleme, ifade özgürlüğü kapsamında istisnaya tabidir; bu istisna kişilik hakkı ve özel hayat ölçüsünde sınırlıdır (KVKK m.28 değerlendirmesi).
4. **Tartım**: Kamuya katkı, kişinin tanınırlığı, elde etme yöntemi ve içeriğin biçimi ölçütleriyle menfaat dengesi kurulur.
5. **Ara sonuç**: Rıza/kamu yararı yoksa ihlal sabittir; gazetecilik istisnası ölçülü kalmamışsa KVKK koruması devreye girer.

## Çıktı modülleri
- Özel hayat alan sınıflandırması
- KVKK gazetecilik istisnası tartım notu
- İçerik kaldırma/tazminat yol önerisi

## Plugin bağlamı

Bu beceri `basin-medya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
