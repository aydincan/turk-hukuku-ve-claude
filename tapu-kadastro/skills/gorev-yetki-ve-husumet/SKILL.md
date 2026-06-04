---
name: gorev-yetki-ve-husumet
description: "Tapu-kadastro uyuşmazlığında hangi mahkemenin görevli, hangi yerin yetkili olduğu ve davanın kime karşı açılacağı belirlenirken; adli/idari yargı ayrımı, kadastro mahkemesi-genel mahkeme geçişi ve Hazine/idare husumeti netleştirilmek istendiğinde kullanılır."
---

# Görev, Yetki ve Husumet Haritası

## Görev
Tapu-kadastro davasında doğru mahkeme (görev), doğru yer (yetki) ve doğru davalıyı (husumet) tek bir denetimle belirleyip usulden kayıpları önlemek.

## Soğuk başlangıç (intake)
- Talep türü: tapu iptali-tescil, kadastro itirazı, tescil (m.713), düzeltim, men/ecrimisil, ortaklığın giderilmesi, tazminat (m.1007)?
- Taşınmaz hangi adliye çevresinde; kadastro çalışması/tutanağı kesinleşmiş mi?
- Karşı taraf gerçek kişi mi, Hazine mi, belediye/idare mi, mirasçılar mı?
- Uyuşmazlık özel hukuk işlemine mi, idari işleme (kamulaştırma/imar) mı dayanıyor?

## Denetim şeması
1. **Adli/idari yargı ayrımını yap.** Mülkiyet/ayni hak ve sicil uyuşmazlıkları adli yargıda (asliye/sulh hukuk). İdari işlemden (kamulaştırma kararı, imar planı, idari tasarruf) doğan iptal talepleri idari yargıda (2577 sayılı İYUK). Kamulaştırmasız el atmada el atmanın türüne göre adli/idari ayrım gözetilir.
2. **Görevli mahkemeyi seç.** Tapu iptali-tescil, men, düzeltim, tazminat → asliye hukuk (HMK m.2). Ortaklığın giderilmesi → sulh hukuk (HMK m.4). Kesinleşmemiş kadastro işine ilişkin uyuşmazlık → kadastro mahkemesi (3402 m.25-26), kesinleştikten sonra genel mahkeme.
3. **Yetkiyi belirle.** Taşınmazın aynına ilişkin davalarda taşınmazın bulunduğu yer mahkemesi kesin yetkilidir (HMK m.12); birden çok taşınmazda da bunlardan birinin yeri (HMK m.12/2).
4. **Husumeti kur.** Tapu iptalinde kayıt maliki ve ara malikler; tescil/zilyetlik davasında Hazine ve/veya ilgili idare; TMK m.1007 tazminatında Hazine; ortaklığın giderilmesinde tüm paydaşlar (zorunlu dava arkadaşlığı). Husumet eksikliği davanın reddine yol açar.
5. **Dava şartlarını gözden geçir.** Görev ve kesin yetki re'sen incelenir (HMK m.114-115); kadastroda 10 yıllık hak düşürücü süre (3402 m.12/3) re'sen dikkate alınır.
6. **Ara sonuç.** Mahkeme + yer + davalı çevresi tek tabloya bağlanır; yanlışsa gönderme/ret riski not edilir.

## Çıktı modülleri
- Talep türüne göre görev–yetki–husumet tablosu.
- Adli/idari yargı yolu ayrım notu (kamulaştırma/imar bağlantısı).
- Dava şartı ve süre kontrol listesi.

## Plugin bağlamı

Bu beceri `tapu-kadastro` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
