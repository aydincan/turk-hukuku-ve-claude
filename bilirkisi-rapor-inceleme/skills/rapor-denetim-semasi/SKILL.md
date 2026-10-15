---
name: rapor-denetim-semasi
description: "Eldeki bilirkişi raporunu uçtan uca eleştirel biçimde denetlemek ve hangi usulî hamlenin (ek rapor, yeni heyet, esasa itiraz) seçileceğine karar vermek istendiğinde kullanılır."
---

# Rapor Denetim Şeması ve İtiraz Stratejisi

## Görev
Raporu dört eksende (usul, metodoloji, hesap, çelişki) sistematik denetleyip her bulguyu görevlendirme sorusuna ve dosya deliline çıpalamak; ardından bulguların ağırlığına göre doğru usulî yolu (HMK m.281) seçmek.

## Soğuk başlangıç (intake)
- Görevlendirme kararındaki sorular ile raporun yanıtladığı sorular örtüşüyor mu?
- Hangi husus(lar) müvekkilin aleyhine ve neden hatalı görülüyor?
- Dosyada raporla çelişen başka delil/rapor var mı?
- Hedef raporu tümden çürütmek mi, yoksa belirli kalemleri düzeltmek mi?

## Denetim şeması
1. **Usul ekseni:** Bilirkişinin yetkisi, yemini, uzmanlık alanı sınırı (6754 s.K. m.3), görevlendirme kapsamına uygunluk (HMK m.273). Kapsam aşımı veya eksik yanıt belirlenir.
2. **Metodoloji ekseni:** Kullanılan yöntem açıkça belirtilmiş mi; kabuller ve varsayımlar dosya verisiyle örtüşüyor mu; veri kaynağı gösterilmiş mi (HMK m.279 gerekçe zorunluluğu)? Gerekçesiz sonuç denetlenebilir değildir.
3. **Hesap ekseni:** Aritmetik doğruluk, birim/tarih tutarlılığı, faiz başlangıcı ve türü, zamanaşımı/ıslah kesişimi. (Detaylı kontrol için hesap denetimi becerisi.)
4. **Çelişki ekseni:** Rapor içi çelişki, dosyadaki diğer delillerle çelişki, sorulara verilmeyen yanıtlar.
5. **Strateji seçimi (HMK m.281):** Tamamlanabilir eksik → **ek rapor**; yöntem hatası veya tarafsızlık kusuru → **yeni bilirkişi/heyet**; hukuki nitelendirme aşımı veya caizsizlik → **doğrudan esasa itiraz** (rapor hâkimi bağlamaz, HMK m.282). **Ara sonuç:** her bulgu için "hangi yol, hangi gerekçe, hangi dayanak" üçlüsü doldurulur.

## Çıktı modülleri
- Eksen-bulgu-dayanak (görevlendirme sorusu + dosya sayfası) matrisi.
- Bulgu başına önerilen usulî yol ve gerekçesi.
- İki hafta içinde sunulacak itiraz dilekçesinin omurgası.
- Talep sonucu önerisi (ek rapor / yeni heyet / rapora itibar edilmemesi).

## Plugin bağlamı

Bu beceri `bilirkisi-rapor-inceleme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
