---
name: dava-usul-gorev-yetki-tahkim
description: "Deniz ticareti uyuşmazlığında dava açmadan veya savunma kurmadan önce görevli ve yetkili mahkemeyi, tahkim/yabancı hukuk şartının geçerliliğini, dava şartlarını ve kanun yollarını belirlemek için kullan."
---

# Dava, Görev-Yetki ve Tahkim

## Görev
Deniz ticareti uyuşmazlığını doğru forumda (mahkeme veya tahkim) konumlandırmak; görevli/yetkili mahkemeyi, tahkim ve yabancı hukuk kayıtlarının geçerliliğini, dava şartlarını ve istinaf/temyiz yolunu belirlemek.

## Soğuk başlangıç (intake)
- Uyuşmazlık konusu nedir ve taraflar tacir mi (ticari dava niteliği)?
- Sözleşmede tahkim şartı, yetki kaydı veya yabancı hukuk seçimi var mı?
- Yabancılık unsuru var mı (yabancı bayrak, yabancı taraf, yurt dışı ifa)?
- Talep edilen geçici koruma var mı (ihtiyati haciz/tedbir)?

## Denetim şeması
1. **Görevli mahkeme**: Deniz ticaretine ilişkin uyuşmazlıklar mutlak ticari dava olup **asliye ticaret mahkemesi**nde görülür (TTK m.4, m.5); ticaret mahkemesi bulunmayan yerde asliye hukuk mahkemesi ticaret mahkemesi sıfatıyla bakar.
2. **Yetki**: HMK'nın genel yetki kurallarıyla birlikte deniz hukukuna özgü kuralları (örn. ihtiyati hacizde geminin bulunduğu yer; taşıma sözleşmesinde teslim/varış yeri) uygula; tacirler arası geçerli yetki sözleşmesini (HMK m.17) gözet.
3. **Tahkim ve yabancı hukuk şartı**: Çarter partilerdeki tahkim ve yabancı hukuk kayıtlarının geçerliliğini ve konişmentoya incorporation (atıf) yoluyla sirayetini değerlendir; milletlerarası tahkimde MTK (4686) ve yabancı hakem kararlarının tenfizini (New York Sözleşmesi) gözet.
4. **Dava şartları ve geçici koruma**: Hukuki yarar, husumet ve gerekirse dava şartı arabuluculuk (ticari alacaklarda 6325 sayılı HUAK) kontrolünü yap; ihtiyati haciz/tedbir talebini ayrı değerlendir.
5. **İspat ve kanun yolu**: İddiayı ileri süren ispatlar; belge ve sörvey raporları esastır. İlk derece sonrası **istinaf** (BAM) ve kesinlik sınırını aşan kararlarda **temyiz** (Yargıtay) yolunu ve sürelerini hesapla. Çıktıda forum ve süre haritasını netleştir.

## Çıktı modülleri
- Görev-yetki-forum karar tablosu
- Tahkim/yabancı hukuk kaydı geçerlilik notu
- Dava şartı ve kanun yolu süre takvimi

## Plugin bağlamı

Bu beceri `deniz-ticareti-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
