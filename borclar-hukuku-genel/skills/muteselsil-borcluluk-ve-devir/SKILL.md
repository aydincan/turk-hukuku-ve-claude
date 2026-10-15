---
name: muteselsil-borcluluk-ve-devir
description: "Birden çok borçlunun aynı borçtan birlikte sorumlu olduğu, alacağın temlik edildiği veya borcun başkasına geçtiği durumlarda taraflar arası ilişkiyi çözmek için kullanılır."
---

# Müteselsil Borçluluk, Alacağın Devri ve Borcun Üstlenilmesi

## Görev
Birden çok borçlu/alacaklı arasındaki teselsül ilişkisini, iç-dış ilişki ve rücuyu çözmek; alacağın devri ve borcun üstlenilmesinin geçerlilik ve sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
- Borçlular birden çok mu; teselsül kararlaştırıldı mı yoksa kanundan mı doğuyor?
- Alacaklı kime, ne kadar başvurdu; ödeyen borçlunun rücu hakkı ne?
- Alacak bir başkasına devredildi mi; yazılı temlik var mı?
- Borç bir üçüncü kişiye mi geçti; alacaklının rızası alındı mı?

## Denetim şeması
1. Müteselsil borçluluğun kaynağı: TBK m.162 — teselsül ya borçluların beyanıyla ya kanunla doğar (örn. ortak haksız fiil m.61, adi şirket). Aksi belirtilmedikçe bölünebilir borçlarda teselsül karinesi yoktur.
2. Dış ilişki: m.163 — alacaklı borcun tamamını dilediği borçludan isteyebilir; biri ifa edince hepsi borçtan kurtulur. Borçluların def'ileri: ortak def'iler herkese, kişisel def'iler yalnız ilgiliye ait (m.164-165).
3. İç ilişki ve rücu: m.167 — aksi kararlaştırılmadıkça borçlular eşit pay taşır; fazlasını ödeyen, payları oranında diğerlerine rücu eder; ödeyemeyenin payı paylaştırılır. Halefiyet (m.168) ile alacaklının teminatlarına girer.
4. Alacağın devri (temlik): m.183-194 — kural olarak borçlunun rızası gerekmez; geçerlilik için yazılı şekil (m.184). Devirden önce borçluya yöneltilen def'iler yeni alacaklıya karşı da ileri sürülebilir (m.188); iyiniyetli borçlunun eski alacaklıya ifası (m.186).
5. Borcun üstlenilmesi: m.195-201 — iç üstlenme + dış üstlenme; borçlunun değişmesi alacaklının kabulüne bağlıdır (m.196). Kabule kadar iç ilişki, ret hâlinde sonuçlar; teminatların akıbeti (m.198-199).
6. İspat yükü: Teselsülü/temliki ileri süren yazılı dayanağı; rücu ve payları ödeyen borçlu ispatlar.

## Çıktı modülleri
- Teselsül haritası (dış ilişki/iç ilişki/rücu).
- Temlik veya borç üstlenme sözleşmesi taslağı iskeleti.
- Def'i ve teminat akıbeti kontrol listesi.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
