---
name: cevresel-tazminat-sorumluluk
description: "Kirlilikten kaynaklanan maddi/manevi zararın tazmini, kirletenin kusursuz ve müteselsil sorumluluğu, illiyet bağı ve zararın hesabı ile el atmanın önlenmesi taleplerinde; tahsis edilemeyen kirleticiler ve çoklu sorumlu durumlarında kullan."
---

# Çevresel Zarar Tazminatı ve Sorumluluk

## Görev
Kirlilikten doğan maddi ve manevi zararın kirletenden tazminini sağlamak; kusursuz ve müteselsil sorumluluk ile illiyet bağını kurmak, zararı hesaplamak ve el atmanın önlenmesini talep etmek.

## Soğuk başlangıç (intake)
1. Zarar türü: mal varlığı (ürün/hayvan/taşınmaz), sağlık, ekonomik kayıp, manevi zarar?
2. Kirletici kim; tek mi çoklu mu, kaynak tespit edilebiliyor mu?
3. Kirlilik ile zarar arasında teknik illiyet ortaya konabiliyor mu?
4. Talep tazminat mı, el atmanın/kirliliğin durdurulması mı, ikisi birlikte mi?

## Denetim şeması
1. **Sorumluluk esası**: 2872 m.28 — çevreyi kirletenler ve bozanlar, oluşan zarardan kusuruna bakılmaksızın sorumludur; birden fazla kirleten varsa sorumluluk müteselsildir. Bu, TBK m.49'un kusur şartını çevresel zararda hafifleten özel bir kusursuz sorumluluk normudur.
2. **Unsurlar**: Kirletme/bozma fiili, zarar ve illiyet bağı ispatlanır; kusur aranmaz. İlliyet, teknik bilirkişi raporuyla kurulur.
3. **Zararın hesabı**: Maddi zarar (eski hale getirme/temizleme masrafı, değer kaybı, kazanç kaybı) ve manevi zarar (TBK m.56/58) ayrı kalemlenir; eski hale getirme talebi öncelikli olabilir.
4. **El atmanın önlenmesi**: Mülkiyet ve komşuluk hukuku temelinde (TMK m.683, m.730, m.737) devam eden kirliliğin durdurulması istenir; ihtiyati tedbir (HMK m.389) erken talep edilir.
5. **Usul, ispat ve ara sonuç**: Görevli mahkeme asliye hukuktur; zamanaşımı için bu becerinin yanında "süreler ve zamanaşımı" becerisine bak. Delil tespiti (HMK m.400) ve keşif belirleyicidir; çoklu kirleticide rücu ilişkisi ayrıca kurulur.

## Çıktı modülleri
- Sorumluluk ve illiyet analizi
- Zarar kalemleri tablosu (maddi/manevi)
- Tazminat + el atmanın önlenmesi dava iskeleti
- İhtiyati tedbir ve delil tespiti talebi taslağı

## Plugin bağlamı

Bu beceri `cevre-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
