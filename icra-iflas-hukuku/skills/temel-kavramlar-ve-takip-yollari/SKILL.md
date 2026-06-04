---
name: temel-kavramlar-ve-takip-yollari
description: "İcra-iflas hukukunun sistematiğini, cüzî/külli icra ayrımını ve hangi alacak için hangi takip yolunun seçileceğini belirlemek gerektiğinde; takip yolu seçimi, görev-yetki ve genel yön bulma için kullanılır."
---

# Temel Kavramlar ve Takip Yolları Haritası

## Görev
Eldeki alacağı/edimi nitelendirip doğru takip yolunu (ilamsız, ilamlı, kambiyo, rehnin paraya çevrilmesi, tahliye, iflas) seçmek; icra dairesi-icra mahkemesi-genel mahkeme görev dağılımını ve yetkiyi netleştirmek.

## Soğuk başlangıç (intake)
- Alacağın kaynağı ne: ilam/ilam niteliğinde belge mi, kambiyo senedi (çek/bono/poliçe) mi, sözleşme/fatura/adi belge mi, rehinle teminatlı mı?
- Borçlu gerçek kişi/tacir/şirket mi; iflasa tabi mi?
- Talep para alacağı mı, teminat mı, taşınır/taşınmaz teslimi mi, tahliye mi?
- Borçlunun yerleşim yeri/işyeri ve malvarlığının bulunduğu yer neresi?

## Denetim şeması
1. **Nitelendirme**: İlam veya ilam niteliğinde belge (İİK m.38) varsa ilamlı icra (m.24 vd.) — itiraz takibi durdurmaz, ancak icranın geri bırakılması (m.33, m.36) mümkündür. Çek/bono/poliçe varsa kambiyo senetlerine özgü takip (m.167 vd.) tercih edilebilir.
2. **İlamsız takip**: Para ve teminat alacaklarında genel haciz yolu (m.42 vd.); dayanak belge şart değildir ama itiraz takibi durdurur (m.66). Adi kiranın temerrütle tahliyesi için m.269.
3. **Rehinli alacak**: Kural olarak önce rehnin paraya çevrilmesi yoluna gidilir (m.45, m.145 vd.); ipotek/menkul rehni ayrımı yapılır. İstisnalar (m.45/son, kambiyo) gözetilir.
4. **İflas yolu**: Borçlu İİK m.43 anlamında iflasa tabi ise (tacirler vb.) takipli (m.155 vd.) veya doğrudan (m.177) iflas seçilebilir; basit alacak için orantısızlık değerlendirilir.
5. **Görev/yetki**: Takip işlemleri icra dairesi; takip hukukuna ilişkin uyuşmazlıklar icra mahkemesi (m.4); maddi hukuk uyuşmazlıkları (itirazın iptali, menfi tespit, tasarrufun iptali) genel mahkeme. Yetki HMK kuralları + İİK m.50.
6. **Ara sonuç**: Seçilen yol, beklenen itiraz/şikâyet riski, süre ve maliyet tablosu çıkarılır.

## Çıktı modülleri
- Takip yolu karar matrisi (alacak türü × yol × avantaj/risk).
- Görev-yetki tespiti ve dayanak madde listesi.
- İlk adım kontrol listesi (takip talebi unsurları, harç/gider avansı).

## Plugin bağlamı

Bu beceri `icra-iflas-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
