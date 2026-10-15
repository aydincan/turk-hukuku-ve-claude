---
name: ilamsiz-takip-ve-itiraz
description: "Genel haciz yoluyla ilamsız takip başlatmak, ödeme emrine itiraz etmek ya da gelen itiraza karşı strateji kurmak gerektiğinde; takip talebi, ödeme emri, itiraz türleri ve takibin durması-kesinleşmesi için kullanılır."
---

# İlamsız Takip ve Ödeme Emrine İtiraz

## Görev
Para/teminat alacağı için genel haciz yoluyla ilamsız takip kurmak; ödeme emrine itirazı (borca, imzaya, kısmî) doğru şekilde yapmak veya karşılamak; takibin durma/kesinleşme mantığını yönetmek.

## Soğuk başlangıç (intake)
- Alacak likit mi, vade gelmiş mi, dayanak belge var mı?
- Ödeme emri tebliğ edildi mi, tarih nedir (7 günlük itiraz süresi)?
- İtiraz edilecekse borca mı, imzaya mı, faize/yetkiye mi itiraz var?
- Borçlu mal beyanında bulundu mu (m.74)?

## Denetim şeması
1. **Takip talebi (m.58)**: Tarafların kimliği, alacak miktarı, faiz başlangıcı, dayanağı ve takip yolu eksiksiz yazılır.
2. **Ödeme emri (m.60)**: Borçluya 7 gün içinde ödeme veya itiraz, aksi halde haciz ihtarı tebliğ edilir. Mal beyanı yükümlülüğü hatırlatılır.
3. **İtiraz (m.62)**: Borçlu 7 gün içinde icra dairesine itiraz eder; itiraz takibi **kendiliğinden durdurur** (m.66). İmzaya itiraz ayrıca ve açıkça belirtilmelidir (m.62/V); aksi halde imza kabul edilmiş sayılır. Yetkiye itiraz esasa itirazla birlikte yapılmalıdır.
4. **İtirazın sonucu**: İtiraz varsa alacaklı ya itirazın iptali davası (m.67, genel mahkeme, 1 yıl) ya itirazın kaldırılması (m.68 vd., icra mahkemesi, 6 ay) yolunu seçer. İtiraz yoksa takip kesinleşir, haciz istenebilir.
5. **İspat yükü**: Alacağın varlığını alacaklı ispatlar; borçlu ödeme/def'ileri belgeyle ileri sürer. İmzaya itirazda imzanın borçluya ait olduğunu alacaklı ispatlar.
6. **Ara sonuç**: Kesinleşme tarihi, haciz isteme süresi (m.78, talepten itibaren 1 yıl) ve sonraki adım belirlenir.

## Çıktı modülleri
- Takip talebi ve ödeme emri taslağı (yer tutucularla).
- İtiraz dilekçesi / itiraza karşı strateji notu.
- Süre ve kesinleşme takvimi.

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
