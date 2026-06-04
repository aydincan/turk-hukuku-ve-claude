---
name: ispat-delil-ve-tutanak
description: "İdari yaptırıma dayanak tutanak, cihaz/kayıt ve tespitlerin ispat değerini değerlendirmek, ispat yükünü dağıtmak ve çürütücü delil stratejisi kurmak gerektiğinde kullanılır."
---

# İspat, Delil ve Tutanak Denetimi

## Görev
Kabahatin sübutunu sağlayan delilleri (tutanak, ölçüm cihazı, kamera/ses kaydı, tanık) ispat değeri açısından denetlemek ve çürütücü delil stratejisi kurmak.

## Soğuk başlangıç (intake)
- Kabahat hangi delille tespit edilmiş (tutanak, mobese, hız/emisyon cihazı, numune)?
- Tutanağı kim, hangi yetkiyle, nasıl düzenlemiş; imza/tanık var mı?
- Ölçüm cihazının kalibrasyon/muayene belgesi mevcut mu?
- İlgili kişiye tespit anında bildirim/savunma imkânı tanınmış mı?

## Denetim şeması
1. **İspat yükü:** Kabahatin gerçekleştiğini ispat kural olarak **idareye** düşer. İdare somut, doğrulanabilir delil sunmalıdır; soyut tespit yetersizdir.
2. **Tutanağın değeri:** Usulüne uygun düzenlenmiş tutanak güçlü bir delildir ancak kesin (mutlak) delil değildir; aksi her türlü delille ispatlanabilir. Tutanağın yer-zaman-fiil-tespit yöntemi yönünden çelişki ve eksikliklerini tara.
3. **Teknik tespitler:** Hız/emisyon/gürültü ölçümü, kantar vb. cihazların yetkili kurumca kalibre/muayene edilmiş olması; ölçüm koşullarının kurallara uygunluğu denetlenir. Kalibrasyonsuz/usulsüz ölçüm ispat değerini düşürür.
4. **Hukuka aykırı delil:** Hukuka aykırı yolla elde edilen delilin değerlendirme dışı bırakılması ilkesi (genel ispat hukuku ve Anayasa m.38/6) kabahatler bakımından da gözetilir.
5. **Çürütücü delil:** Tanık, karşı belge, bilirkişi/teknik rapor ve keşif talepleriyle idarenin delilini sars. Başvuruda delillerini açıkça göster.
6. **Ara sonuç:** İspat yükü dengesini değerlendir — idare sübutu sağlayamıyorsa kabahat sabit sayılmaz ve ceza kaldırılır.

## Çıktı modülleri
- Delil-tespit eleştiri tablosu (her delil için zayıf nokta).
- Çürütücü delil listesi ve talep dilekçesi taslağı.
- İspat yükü değerlendirme notu.

## Plugin bağlamı

Bu beceri `kabahatler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
