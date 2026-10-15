---
name: ictima-suclarin-birlesmesi
description: "Bir kişinin birden çok suç işlediği veya tek fiille birden çok norm ihlal ettiği durumlarda zincirleme suç, fikri içtima ve bileşik suç kurallarını uygulamak gerektiğinde kullanılır."
---

# İçtima — Suçların Birleşmesi

## Görev
Birden fazla fiil veya tek fiille birden fazla norm ihlalinde, kaç suçtan ve hangi ceza ilkesiyle sorumluluk doğacağını (gerçek içtima, zincirleme suç, fikri içtima, bileşik suç) belirlemek.

## Soğuk başlangıç (intake)
- Kaç ayrı fiil var; bunlar aynı mağdura mı, farklı mağdurlara mı yöneldi?
- Fiiller aynı suç işleme kararının icrası mı, bağımsız kararlar mı?
- Tek bir fiil mi var, ama birden çok suç tanımına mı uyuyor?
- Bir suç, başka bir suçun unsuru ya da ağırlaştırıcı hâli mi?

## Denetim şeması
1. **Kural — gerçek içtima:** Birden çok fiille birden çok suç işleyen, her suçtan ayrı cezalandırılır; bu temel ilkedir, istisnalar aşağıdadır.
2. **Bileşik suç (m.42):** Biri diğerinin unsuru/ağırlaştırıcı nedeni olan suçlarda tek ceza; ayrıca içtima uygulanmaz (örn. yağmada cebir + alma).
3. **Zincirleme suç (m.43/1):** Aynı suç işleme kararıyla, aynı kişiye karşı değişik zamanlarda aynı suçun birden çok işlenmesinde tek ceza verilir ve artırılır. Aynı anda tek fiille birden çok kişiye karşı işlenmesi de değerlendirilir. Ara sonuç: tek karar bütünlüğü var mı?
4. **Zincirleme suç sınırı (m.43/3):** Yağma, kasten öldürme, kasten yaralama gibi sayılan suçlarda zincirleme hükmü uygulanmaz.
5. **Fikri içtima (m.44):** Tek fiille birden çok farklı suç oluşuyorsa, en ağır cezayı gerektiren suçtan cezalandırılır. Ara sonuç: fiil tek mi?
6. **Mağdur ve hukuki konu denetimi:** Korunan hukuki yararın çokluğu ve mağdur sayısı, içtima sonucunu doğrudan etkiler.

## Çıktı modülleri
- İçtima türü belirleme akış şeması.
- Suç sayısı ve ceza artırım/seçim notu.
- Zincirleme suç istisnaları kontrol listesi.
- Eksik vakıa ve `[doğrulanacak]` içtihat ihtiyacı.

## Plugin bağlamı

Bu beceri `ceza-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
