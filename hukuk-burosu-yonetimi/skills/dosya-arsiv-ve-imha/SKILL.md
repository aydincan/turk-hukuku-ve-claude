---
name: dosya-arsiv-ve-imha
description: "İş tamamlandıktan sonra dosyanın kapatılması, ne kadar saklanacağı, arşivlenmesi, müvekkile iadesi ve süre sonunda KVKK uyumlu imhası kararlaştırılırken kullanılır."
---

# Dosya Saklama, Arşiv ve İmha

## Görev
Sona eren işlerde dosyayı düzenli kapatmak; evrakın iadesi/saklanması ve saklama süresini belirlemek; süre sonunda kişisel verileri KVKK'ya uygun imha etmek; olası sorumluluk ve denetim ihtiyacını dengelemek.

## Soğuk başlangıç (intake)
1. İş nasıl sona erdi (karar kesinleşti, sulh, azil/istifa, danışmanlık bitti)?
2. Müvekkile ait asıl evrak/belge büroda mı; iadesi gerekiyor mu?
3. Dosyada hangi kişisel/özel nitelikli veriler var?
4. İleride sorumluluk, kanun yolu veya icra ihtiyacı doğabilir mi?

## Denetim şeması
1. **Kapanış kontrolü**: Tüm süreler kapanmış, kesinleşme/sulh tutanağı dosyada, vekâlet ücreti tahsil/hesap durumu net mi?
2. **Asıl evrakın iadesi (TBK m.508 hesap verme; 1136 ilişkisi)**: Müvekkile ait asıl belgeler iade edilir; hapis hakkı (1136 m.166) saklı kalır. İade tutanakla yapılır.
3. **Saklama süresi**: Olası sorumluluk zamanaşımı (vekâlet ilişkisinde TBK genel süreleri), mevzuat gerekleri ve kanun yolu ihtimali gözetilerek saklama süresi belirlenir; süre KVKK saklama-imha politikasıyla uyumlandırılır.
4. **Arşiv güvenliği (KVKK m.12)**: Fiziki/dijital arşivde erişim sınırlaması, gizlilik (1136 m.36) ve veri güvenliği sürdürülür.
5. **İmha/anonimleştirme**: Saklama süresi dolan kişisel veriler KVKK saklama-imha rejimine göre silinir/yok edilir/anonim hale getirilir; imha kayıt altına alınır.
6. **Ara sonuç**: İade + saklama süresi + güvenli arşiv + süre sonu imha planı tanımlanınca dosya usulüne uygun kapatılmıştır.

## Çıktı modülleri
- Dosya kapanış kontrol listesi.
- Evrak iade tutanağı taslağı.
- Saklama süresi ve imha planı tablosu (veri kategorisi, süre, imha yöntemi).

## Plugin bağlamı

Bu beceri `hukuk-burosu-yonetimi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
