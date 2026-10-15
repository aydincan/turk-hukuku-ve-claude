---
name: ticari-dava-gorev-arabuluculuk
description: "Bir uyusmazligin ticari dava olup olmadigini, asliye ticaret mahkemesinin gorevli olup olmadigini, dava sarti arabuluculugun zorunlu olup olmadigini ve yetkili mahkemeyi belirlemek gerektiginde kullanilir."
---

# Ticari Davada Görev, Yetki ve Dava Şartı Arabuluculuk

## Görev
Uyuşmazlığın ticari dava niteliğini, görevli ve yetkili mahkemeyi ve dava şartı arabuluculuğun zorunlu olup olmadığını belirlemek. Görev kamu düzenindendir; yanlış mahkeme veya arabuluculuk atlanması davayı baştan tıkar.

## Soğuk başlangıç (intake)
1. Uyuşmazlığın kaynağı ne (TTK'da düzenlenen iş mi, her iki tarafın ticari işletmesiyle ilgili mi)?
2. Taraflar tacir mi; her ikisi için de ticari iş mi?
3. Talep konusu para alacağı/tazminat mı (arabuluculuk eşiği)?
4. Sözleşmede yetki/tahkim şartı var mı?

## Denetim şeması
1. **Ticari dava türleri:** TTK m.4 — (i) mutlak ticari davalar (tarafların sıfatına bakılmaksızın TTK'da ve bazı kanunlarda sayılan davalar; örn. TTK, TMK rehin/kıymetli evrak, bankacılık, fikri mülkiyet bazı davaları), (ii) her iki tarafın ticari işletmesiyle ilgili nispi ticari davalar. Bu davalar değer/miktara bakılmaksızın asliye ticaret mahkemesinde görülür (TTK m.5/1).
2. **Görev:** TTK m.5 — asliye ticaret mahkemesi ile asliye hukuk arasındaki ilişki görev ilişkisidir (kamu düzeni; re'sen incelenir). Heyet/tek hâkim ayrımı için TTK m.5/3-4 (belirli değer/konu eşikleri).
3. **Dava şartı arabuluculuk:** TTK m.5/A — konusu bir miktar paranın ödenmesi olan alacak ve tazminat talepleri (itirazın iptali, menfi tespit, istirdat dahil) bakımından dava açılmadan önce arabulucuya başvurulmuş olması dava şartıdır. Anlaşmama tutanağı dava dilekçesine eklenmezse dava usulden reddedilir. İstisnalar (örn. ihtiyati tedbir/haciz) ve diğer zorunlu arabuluculuk alanlarıyla (tüketici, iş) ilişki gözetilir.
4. **Yetki:** Genel yetki davalının yerleşim yeri (HMK m.6); sözleşmeden doğanlarda ifa yeri (HMK m.10); tacirler/kamu tüzel kişileri arasında yazılı yetki sözleşmesi geçerli (HMK m.17). Tahkim şartı varsa mahkemenin görevsizliği itiraz üzerine incelenir.
5. **İspat/usul:** Görev ve dava şartları re'sen; yetki itirazı ilk itiraz olarak süresinde ileri sürülür. Ara sonuç: ticari dava + para talebi → arabuluculuk şartı + asliye ticaret mahkemesi.

## Çıktı modülleri
- Görev-yetki-arabuluculuk karar tablosu (dayanak: TTK m.4, m.5, m.5/A).
- Arabuluculuk başvuru ve son tutanak kontrol listesi.
- Yetki/tahkim itirazı veya yetkili mahkeme tespiti notu.

## Plugin bağlamı

Bu beceri `ticari-isletme-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
