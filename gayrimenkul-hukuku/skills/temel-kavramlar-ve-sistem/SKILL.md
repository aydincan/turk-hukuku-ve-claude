---
name: temel-kavramlar-ve-sistem
description: "Taşınmaza ilişkin bir işi ilk kez ele alırken; talebin ayni hakka mı borç ilişkisine mi idari boyuta mı dayandığını, hangi sözleşme/dava tipinin söz konusu olduğunu ayırmak ve doğru hukuki temeli kurmak için kullanılır."
---

# Temel Kavramlar ve Gayrimenkul İşlem Sistematiği

## Görev
Önündeki taşınmaz işini doğru eksene oturtmak: talebin ayni hakka mı (mülkiyet, irtifak, rehin), borç ilişkisine mi (satış vaadi, inşaat, kira), yoksa kamusal/idari boyuta mı (imar, kamulaştırma, kat mülkiyeti) dayandığını belirlemek. Doğru nitelendirme; şekil, süre, görev-yetki ve ispatın tamamını belirler.

## Soğuk başlangıç (intake)
- Taşınmazın türü ne: arsa, tarla, bina, bağımsız bölüm (daire/dükkân), devre mülk?
- Müvekkilin talebi tapuyu/mülkiyeti elde etmek/iptal ettirmek mi, para/tazminat mı, yoksa bir kullanımı durdurmak/sağlamak mı?
- İşin dayanağı bir sözleşme mi (satış vaadi, inşaat, kira), bir tapu kaydı mı, yoksa idari bir işlem mi (imar, kamulaştırma)?
- Tapu kaydı kimin adına; üzerinde ipotek, haciz, şerh, beyan var mı?

## Denetim şeması
1. **Eksen tespiti**: Mülkiyet ve sınırlı ayni haklar mutlaktır, herkese karşı ileri sürülür ve sınırlı sayı (numerus clausus) ilkesine tabidir. Buna karşılık satış vaadi, inşaat ve kira nispi (borç) ilişkileridir; tek başlarına ayni hak doğurmaz.
2. **Kazanım kuralı**: Taşınmaz mülkiyeti kural olarak tapuya tescille kazanılır (TMK m.705/1, m.1021). Miras, mahkeme kararı, cebrî icra, kamulaştırma tescilden önce kazandırır (m.705/2). Bu ayrım, satış vaadi alacaklısının doğrudan malik olamayacağını; tescil davası gerektiğini gösterir.
3. **Şekil süzgeci**: Mülkiyeti devir sözleşmeleri resmî senetle (tapu önünde) yapılır (TMK m.706; TBK m.237). Satış vaadi noterde resmî şekle tabidir (TBK m.29; Noterlik K. m.60/3) ve tapuya şerh edilebilir (TMK m.1009). Şekle aykırılık kural olarak kesin hükümsüzlüktür (TBK m.27).
4. **Takyidat haritası**: Tapu kaydındaki ipotek, haciz, şerh (satış vaadi, kira), beyan ve kat irtifakı/mülkiyeti durumu işin tüm seyrini etkiler; ilk işte mutlaka çıkarılır.
5. **Ara sonuç**: İşin baskın ekseni, uygulanacak sözleşme/dava tipi ve doğru hukuki dayanak belirlenir; ispat yükü hakkı iddia edene aittir (TMK m.6).

## Çıktı modülleri
- Nitelendirme notu (eksen, sözleşme/dava tipi, dayanak madde).
- Tapu/takyidat kontrol listesi (malik, ipotek, haciz, şerh-beyan, irtifak).
- İlgili uzman beceriye yönlendirme (satış vaadi, inşaat, tapu iptali, kat mülkiyeti, kamulaştırma).

## Plugin bağlamı

Bu beceri `gayrimenkul-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
