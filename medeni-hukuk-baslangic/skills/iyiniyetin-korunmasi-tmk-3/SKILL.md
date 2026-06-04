---
name: iyiniyetin-korunmasi-tmk-3
description: "Bir hakkın kazanılması veya bir hukuki sonucun doğumu kişinin bir durumu bilmemesine bağlandığında; iyiniyet karinesi, gösterilmesi gereken özen ve iyiniyetin sağladığı koruma tartışıldığında TMK m.3 şemasını uygulamak için kullanılır."
---

# İyiniyetin Korunması (TMK m.3)

## Görev
Kanunun bir hakkın doğumunu iyiniyete bağladığı hâllerde (taşınır iktisabı, tapuya güven, ehliyetsizlik vb.) iyiniyetin varlığını, özen ölçütünü ve sağladığı korumanın kapsamını denetlemek.

## Soğuk başlangıç (intake)
- Hangi hakkın kazanımı/sonucu iyiniyete bağlı (ör. taşınır mülkiyeti TMK m.988 vd., tapuya güven m.1023, evlenme hükümleri)?
- Kişi hangi durumu bilmiyordu ve bunu bilmemesi durumun gereğine uygun mu?
- Karşı taraf, kişinin gerekli özeni göstermediğini mi ileri sürüyor?
- İyiniyetin hangi anda (kazanım anı) bulunması gerekiyor?

## Denetim şeması
1. **İyiniyet karinesi** — TMK m.3/1: kanunun iyiniyete hukuki sonuç bağladığı hâllerde asıl olan iyiniyettin varlığıdır; iyiniyetin yokluğunu (kötüniyeti) iddia eden ispatlar (m.6 ile bağ).
2. **İyiniyetin konusu** — İyiniyet, bir hakkın kazanılmasına engel olan hukuki sakatlığı (ör. devredenin yetkisizliği, sicildeki yolsuzluğu) *bilmemek*tir; bilmesi hâlinde korunmaz.
3. **Özen sınırı — m.3/2** — Durumun gerektirdiği özeni göstermeyen kişi iyiniyet iddiasında bulunamaz. Özen ölçütü objektiftir; basit bir araştırmayla anlaşılabilecek sakatlığı görmeyen iyiniyetli sayılmaz. Tacir için özen ağırlaşır.
4. **Zaman** — İyiniyet, hakkın kazanıldığı anda bulunmalıdır; sonradan öğrenme kazanımı geri almaz, önceden bilme korumayı düşürür.
5. **Koruma kapsamı** — Şartlar sağlanırsa kişi, gerçek hak durumuna rağmen hakkı kazanır (ör. emin sıfatıyla zilyetten iyiniyetle iktisap, tapu kaydına güven). Koruma istisnaidir; ilgili özel normun kendi sınırlarına tabidir.
6. **m.2 ile ayrım** — m.3 bilgisizliğin korunması (sübjektif bilgi durumu), m.2 davranışın dürüstlüğüdür.

## Çıktı modülleri
- İyiniyete bağlı kazanım normunun tespiti.
- Karine + ispat yükü dağılımı (kötüniyet iddiası).
- Özen denetimi (m.3/2) ve zaman tespiti.
- Koruma sonucu + ilkesel içtihat `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `medeni-hukuk-baslangic` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
