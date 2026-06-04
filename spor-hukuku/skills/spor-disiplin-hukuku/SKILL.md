---
name: spor-disiplin-hukuku
description: "Sporcu, kulüp, yönetici veya görevliye verilen disiplin cezasını değerlendirmek, savunma hazırlamak veya cezaya itiraz etmek; tipiklik, kusur ve orantılılık denetimi yapmak gerektiğinde kullanın."
---

# Spor Disiplin Hukuku ve Disiplin Cezaları

## Görev
Bir disiplin fiilini ilgili federasyon disiplin talimatı çerçevesinde değerlendirmek; isnadın tipikliğini, kusuru ve cezanın orantılılığını denetlemek; savunma veya itiraz dilekçesi üretmektir.

## Soğuk başlangıç (intake)
1. İsnat edilen fiil nedir ve hangi müsabakada/olayda geçti?
2. Hangi federasyon ve hangi disiplin talimatı maddesi uygulanıyor?
3. Fail kim: sporcu, kulüp, yönetici, teknik adam, taraftar?
4. Sevk yazısı/rapor (hakem, gözlemci, güvenlik) elde var mı?
5. Savunma süresi ne zaman doluyor?

## Denetim şeması
1. **Yetkili merci ve talimat**: Federasyonun disiplin talimatı tespit edilir (futbolda TFF Disiplin Talimatı). Yürürlük tarihi ve fiil tarihindeki metin kontrol edilir (lehe hüküm değerlendirmesi).
2. **Tipiklik**: İsnat edilen fiilin talimatta tanımlı bir disiplin ihlaline birebir uyup uymadığı denetlenir; kıyasla ceza genişletilemez.
3. **Sorumluluk türü**: Kişisel kusur sorumluluğu mu, yoksa kulübün objektif/sıkı sorumluluğu (taraftar olayları, sahaya yabancı madde atılması gibi) mı? Objektif sorumlulukta kusur tartışılmaz, ancak ağırlatıcı/hafifletici sebepler değerlendirilir.
4. **Kusur ve nitelikli haller**: Kast/taksir ayrımı, tahrik, tekerrür, ağırlatıcı ve hafifletici sebepler; cezanın alt-üst sınırı içinde takdir denetimi.
5. **Orantılılık**: Verilen ceza (müsabakadan men, para cezası, puan silme, hak mahrumiyeti) fiilin ağırlığıyla orantılı mı; emsal uygulamayla tutarlı mı?
6. **Usul güvenceleri**: Savunma hakkı, sevk ve bildirim usulü, gerekçe; usule aykırılık iptal/bozma sebebidir.
7. **Ara sonuç**: Cezanın hukuka uygunluğu, itiraz şansı ve dayanılacak temel argüman belirlenir.

## Çıktı modülleri
- İsnat-tipiklik eşleştirme tablosu
- Savunma veya itiraz dilekçesi taslağı (madde atıflı)
- Hafifletici sebep ve emsal argüman listesi
- Süre uyarısı

## Plugin bağlamı

Bu beceri `spor-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
