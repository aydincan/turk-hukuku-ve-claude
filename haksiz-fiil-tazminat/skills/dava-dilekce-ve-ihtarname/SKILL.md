---
name: dava-dilekce-ve-ihtarname
description: "Tazminat talebi için ihtarname, dava dilekçesi veya talep sonucu taslağı hazırlanması istendiğinde; vakıa-hukuki sebep-talep mimarisini kurmak için kullanılır."
---

# Dava Dilekçesi ve İhtarname Taslağı

## Görev
Haksız fiil tazminatı için HMK m.119'a uygun dava dilekçesi, dava öncesi ihtarname ve talep sonucu taslağı üretmek; vakıa-hukuki sebep-talep mimarisini kurmak ve delilleri vakıalara bağlamak. Eksik/belirsiz veriler `[doldurulacak]` yer tutucularıyla işaretlenir.

## Soğuk başlangıç (intake)
- Taraf bilgileri, olayın özeti ve talep edilen kalemler (maddi/manevi, tutar) nedir?
- Hangi sorumluluk normu dayanak (m.49 / objektif sorumluluk)?
- Faiz türü ve başlangıç tarihi ne istenecek?
- Eldeki deliller ve henüz toplanmamış olanlar neler?

## Denetim şeması
1. **İhtarname (dava öncesi).** Olay-zarar-talep özetlenir, belirli süre verilir, temerrüt ve faiz başlangıcı için ihtarın tarihi/içeriği netleştirilir; noterden keşide önerilir. Zamanaşımını kesmez ama temerrüt için önemlidir.
2. **Dilekçe zorunlu unsurları (HMK m.119).** Mahkeme, taraflar ve adresler, dava konusu/değeri, açık vakıalar, dayanılan hukuki sebepler, her vakıanın hangi delille ispatlanacağı, açık talep sonucu, imza.
3. **Vakıa-altlama.** Maddi olay kronolojik ve sade anlatılır; her vakıa haksız fiil unsuruyla (fiil, hukuka aykırılık, kusur, zarar, illiyet) eşleştirilir; gereksiz hukuki tartışma vakıa bölümüne taşınmaz.
4. **Hukuki sebepler.** TBK m.49 (ve varsa m.66-71 objektif sorumluluk), zarar kalemleri için m.51-56, gerekiyorsa TMK m.24-25; usul için HMK ve yetki m.16.
5. **Talep sonucu.** Kalem bazlı (maddi/manevi) tutar; belirsiz alacaksa HMK m.107 ifadesi; faiz türü-başlangıcı; yargılama gideri ve vekâlet ücreti.
6. **Ara sonuç.** Delil listesi vakıalara bağlanır; eksik veriler `[doldurulacak]` ile, doğrulama bekleyen içtihat `[doğrulanacak]` ile işaretlenir; uydurma karar numarası yazılmaz.

## Çıktı modülleri
- İhtarname taslağı (süre + temerrüt unsurları).
- HMK m.119 yapılı dava dilekçesi iskeleti.
- Talep sonucu ve delil listesi taslağı.

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
