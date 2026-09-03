---
name: durustluk-davasi-usul-gorev-yetki
description: "TMK m.2/m.3 gibi başlangıç hükümlerinin bir davada nasıl ileri sürüleceği, hangi mahkemenin görevli/yetkili olduğu ve def'i mi itiraz mı olduğu tartışıldığında usul yol haritasını çıkarmak için kullanılır."
---

# Başlangıç Hükümlerine Dayalı Uyuşmazlıklarda Usul, Görev ve Yetki

## Görev
Başlangıç hükümlerinin (özellikle TMK m.2/2 kötüye kullanma, m.3 iyiniyet, m.6 ispat) bir yargılamada doğru usulle ileri sürülmesini, görevli-yetkili mahkemenin belirlenmesini ve hâkimce re'sen gözetilip gözetilmeyeceğini netleştirmek.

## Soğuk başlangıç (intake)
- Başlangıç hükmü bağımsız bir talep olarak mı, yoksa asıl talebe karşı savunma/def'i olarak mı ileri sürülüyor?
- Asıl uyuşmazlık hangi mahkemenin görev alanında (sulh hukuk / asliye hukuk / tüketici / aile / ticaret)?
- Hangi yargılama usulü uygulanıyor (yazılı / basit — HMK m.118 vd., m.316 vd.)?
- İddia hangi aşamada ileri sürülmek isteniyor (dilekçeler, ön inceleme, tahkikat)?

## Denetim şeması
1. **Başlangıç hükmü ≠ bağımsız dava** — TMK m.2, m.3 kural olarak bağımsız dava sebebi değildir; asıl hak/borç ilişkisine bağlı olarak ileri sürülür. Görev ve yetki, asıl uyuşmazlığa göre belirlenir.
2. **Görev** — Genel görev kuralı HMK m.2 (malvarlığı/şahıs varlığı davalarında asliye hukuk); sulh hukukun görevi HMK m.4'te sayılıdır. Özel mahkemeler: aile, tüketici (6502), ticaret (TTK m.4-5), iş. Görev kamu düzenindendir, re'sen gözetilir (HMK m.1, m.114/1-c).
3. **Yetki** — Genel yetki davalının yerleşim yeri (HMK m.6); taşınmazda kesin yetki (HMK m.12); sözleşmeden doğan davalarda m.10. Yetki itirazı ilk itiraz olarak cevap dilekçesinde ileri sürülür (HMK m.116, m.117).
4. **Def'i mi, itiraz mı?** — Hakkın kötüye kullanılması ve iyiniyet bir *itiraz* niteliğindedir ve hâkimce re'sen göz önünde tutulur; bu yüzden taraf açıkça ileri sürmese de açık kötüye kullanmayı hâkim dikkate alabilir (kamu düzeni boyutu). Zamanaşımı gibi *def'iler* ise ileri sürülmedikçe gözetilmez.
5. **Aşama ve teksif** — İddia ve savunmanın genişletilmesi yasağı (HMK m.141) kapsamında başlangıç hükmüne dayalı vakıalar zamanında ileri sürülmelidir; ancak hâkimin re'sen gözettiği itirazlar bu yasağın dışındadır.
6. **İspat usulü** — TMK m.6 / HMK m.190; senetle ispat sınırı (HMK m.200-201) ve resmî belge ispat gücü (TMK m.7 / HMK m.204) usul boyutuyla birlikte uygulanır.

## Çıktı modülleri
- Talep mi / savunma mı ayrımı.
- Görev-yetki tespiti (asıl uyuşmazlığa göre) + dayanak madde.
- Def'i/itiraz nitelendirmesi ve re'sen gözetme notu.
- İleri sürme aşaması + ispat usulü + ilkesel içtihat `[doğrulanacak]`.

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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
