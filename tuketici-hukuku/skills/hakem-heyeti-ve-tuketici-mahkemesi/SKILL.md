---
name: hakem-heyeti-ve-tuketici-mahkemesi
description: "Bir tüketici uyuşmazlığında parasal sınıra göre zorunlu hakem heyeti mi yoksa tüketici mahkemesi mi gerektiğini belirlemek, görev-yetki ve başvuru usulünü kurmak gerektiğinde kullanılır."
---

# Tüketici Hakem Heyeti ve Tüketici Mahkemesi Yolu

## Görev
Uyuşmazlığın değerine göre doğru başvuru merciini (tüketici hakem heyeti ya da tüketici mahkemesi) belirlemek, görev ve yetkiyi saptamak, başvuru/dava usulünü ve karara karşı itiraz yolunu kurmak.

## Soğuk başlangıç (intake)
- Uyuşmazlığın parasal değeri ne (faizsiz asıl alacak)?
- Tarafların yerleşim yeri/işlemin yapıldığı yer neresi (yetki için)?
- Daha önce hakem heyetine başvuruldu mu, karar çıktı mı?
- Talep yalnızca para mı, yoksa tespit/men/eda gibi karma talep mi?

## Denetim şeması
1. **Görev — parasal sınır (TKHK m.68):** Değeri her yıl Tebliğ ile belirlenen alt parasal sınırın altında kalan uyuşmazlıklarda tüketici hakem heyetine başvuru zorunludur ve heyet kararları taraflar için bağlayıcıdır. Sınırın üzerindeki uyuşmazlıklarda doğrudan tüketici mahkemesi görevlidir. Güncel rakam Tebliğ'den doğrulanmalıdır [doğrulanacak].
2. **Hakem heyeti çeşidi ve yetki (m.66, m.68):** İl/ilçe tüketici hakem heyetleri; tüketicinin yerleşim yeri ya da işlemin yapıldığı yer hakem heyeti yetkilidir. Başvuru ücretsizdir, elektronik (e-Devlet/TÜBİS) veya yazılı yapılabilir.
3. **Karar ve itiraz (m.70):** Heyet kararı tebliğden itibaren on beş gün içinde tüketici mahkemesine itirazla kaldırılabilir; itiraz üzerine mahkeme kararı kesindir. İtiraz, kararın icrasını kendiliğinden durdurmaz ancak tedbir istenebilir.
4. **Tüketici mahkemesi (m.73):** Tüketici işlemlerinden doğan davalarda görevli mahkeme tüketici mahkemesidir; bulunmayan yerde asliye hukuk mahkemesi tüketici mahkemesi sıfatıyla bakar. Davalar basit yargılama usulüne tabidir.
5. **Harç ve gider muafiyeti (m.73/2):** Tüketici davalarında tüketici, dava açarken harçtan ve bilirkişi dahil yargılama giderlerinden muaftır; bu maddi avantaj strateji kurarken not edilir.
6. **Dava şartı arabuluculuk:** Ticari nitelikteki tüketici davalarında değil ama bazı tüketici uyuşmazlıklarında dava açmadan önce arabuluculuk dava şartı olabilir; somut talebe göre kontrol edilir (TKHK m.73/A) [doğrulanacak].
7. **Ara sonuç:** Hangi mercii görevli, hangi yer yetkili, hangi usul ve hangi itiraz yolu?

## Çıktı modülleri
- Görev-yetki belirleme notu.
- Hakem heyeti başvuru dilekçesi taslağı.
- Tüketici mahkemesi dava/itiraz dilekçesi iskeleti.
- Harç/gider ve süre bilgilendirmesi.

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
