---
name: sigorta-sozlesmesi-denetimi
description: "Poliçenin kurulup kurulmadığı, teminatın ne zaman başladığı, genel/özel şartların bağlayıcılığı ve sözleşmenin geçerliliği tartışıldığında kullanılır; teminat kapsamı ve sigortalanabilir menfaat sorgusu için temel beceridir."
---

# Sigorta Sözleşmesinin Kuruluşu ve Geçerlilik Denetimi

## Görev
Sigorta sözleşmesinin geçerli kurulup kurulmadığını, teminatın başlangıç anını ve genel/özel şartların bağlayıcılığını tespit ederek teminat kapsamını netleştirmek.

## Soğuk başlangıç (intake)
1. Teklifname/başvuru ile poliçe arasında fark var mı; poliçe sigortalıya verildi mi?
2. İlk prim ödendi mi, ne zaman ödendi?
3. Sigortalanan menfaat kime ait, riziko anında mevcut muydu?
4. Genel şartlara ek özel şart/klozlar var mı (çek kloz, abonman, blok poliçe)?

## Denetim şeması
1. **Sözleşmenin kurulması.** TTK m.1401, 1405: icap ve kabul; poliçe verme yükümlülüğü TTK m.1424. Sigortacı, başvurudan itibaren makul sürede red etmezse durumu değerlendir.
2. **Sigortalanabilir menfaat.** Zarar sigortasında menfaat şartı TTK m.1453-1454; menfaat yoksa veya son bulmuşsa sözleşme geçersiz/sona ermiş sayılır. Ara sonuç: korunan menfaat var mı?
3. **Teminatın başlangıcı.** TTK m.1421-1422 ve m.1430: kural olarak ilk prim (peşin/ilk taksit) ödenmeden sigortacının sorumluluğu başlamaz; aksi kararlaştırılabilir. Geçici sigortacılık (cover note) ayrıca değerlendirilir.
4. **Genel/özel şartların bağlayıcılığı.** SEDDK onaylı tip genel şartlar sözleşmenin parçasıdır; sigortalı aleyhine emredici hükme aykırı şartlar geçersizdir (TTK m.1452 — nispi emredicilik). Çelişkide özel şart genel şarta üstün; tüketici sigortalarında haksız şart denetimi (6502 m.5).
5. **Geçersizlik halleri.** TTK m.1408 (rizikonun gerçekleşmiş ya da imkânsız olması), kanuna/ahlaka aykırı menfaat. İspat yükü geçersizliği ileri sürende.

## Çıktı modülleri
- Kuruluş ve teminat başlangıcı zaman çizelgesi.
- Sigortalanabilir menfaat değerlendirmesi.
- Genel/özel şart çatışması ve geçerlilik notu.
- Teminat kapsamı/istisna özeti.

## Plugin bağlamı

Bu beceri `sigorta-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
