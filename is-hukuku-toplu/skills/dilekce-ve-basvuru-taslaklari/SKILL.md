---
name: dilekce-ve-basvuru-taslaklari
description: "Yetki tespiti/itirazi, toplu gorusme cagri yazisi, uyusmazlik tutanagi, grev karari, YHK basvurusu ve sendikal tazminat davasi gibi toplu is hukuku belgelerinin taslaklarini uretir; bir belge kaleme almak gerektiginde kullanilir."
---

# Dilekçe, Tutanak ve Başvuru Taslakları

## Görev
Toplu iş hukukunun tipik belgelerini doğru madde dayanağı ve usul mimarisiyle taslaklamak. Boş bırakılması gereken her yer `[doldurulacak]` ile işaretlenir; uydurma bilgi konmaz.

## Soğuk başlangıç (intake)
- Hangi belge isteniyor (çağrı, itiraz dilekçesi, grev kararı, dava dilekçesi, YHK başvurusu)?
- Taraflar, işkolu, düzey ve tarihler nedir?
- Mahkeme/Bakanlık/YHK gibi muhatap kim?
- Dayanılacak temel vakıalar ve talep nedir?

## Denetim şeması
1. **Belge türünü ve dayanağını eşle:** Yetki itirazı → 6356 m.43 + HMK genel dilekçe unsurları (HMK m.119). TİS yorum/sendikal tazminat davası → HMK m.119 dava dilekçesi (taraflar, vakıa, hukuki sebep, deliller, talep sonucu). Çağrı/tutanak → 6356 m.46-47.
2. **Görevli/yetkili mercii doğrula:** Dava ve yetki itirazı İş Mahkemesi (7036 m.5); yetki tespiti başvurusu Bakanlık; menfaat uyuşmazlığında arabuluculuk (m.50) ve YHK (m.51).
3. **İskelet kur:** Başlık ve muhatap; taraf/vekil bilgileri `[doldurulacak]`; konu; açıklamalar (vakıa kronolojisi + madde altlaması); hukuki sebepler (6356 ilgili maddeleri, HMK); deliller; talep sonucu; tarih-imza.
4. **Süre uyarısı ekle:** İlgili hak düşürücü süre (örn. 6 işgünü itiraz) belge başında not düşülür.
5. **Doğrulama:** Madde numaraları ve tarihler kontrol edilir; içtihat anılacaksa künye `[doğrulanacak]` ve kaynak (karararama.yargitay.gov.tr) belirtilir.

Ara sonuç: Eksiksiz bir taslak + doldurulacak alan listesi + süre uyarısı.

## Çıktı modülleri
- İstenen belgenin tam taslağı (`[doldurulacak]` yer tutucularıyla).
- Dayanak madde ve görevli mercii notu.
- Doldurulacak alan ve ek/delil kontrol listesi.

## Plugin bağlamı

Bu beceri `is-hukuku-toplu` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
