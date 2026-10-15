---
name: musvedde-disiplini-yer-tutucu
description: "Taslak layihada eksik bilgileri uydurmadan yer tutucularla işaretlemek, kontrol listesi ve eksik raporu üretmek, avukat denetimine hazır müsvedde teslim etmek gerektiğinde kullanılır."
---

# Müsvedde Disiplini ve Yer Tutucu Yönetimi

## Görev
Üretilen her layiha müsveddesini avukat denetimine hazır, eksiksiz işaretlenmiş ve doğrulanabilir biçimde teslim etmek. Eksik bilgi asla uydurulmaz; yer tutucularla işaretlenir ve listelenir. Bu beceri atölyenin kalite kapısıdır.

## Soğuk başlangıç (intake)
- Müsveddede hangi bilgiler eksik (tarih, bedel, taraf, delil)?
- Hangi madde atıfları teyit edilmeli (yürürlük/tutar)?
- Hangi içtihat künyesi doğrulanmamış durumda?
- Son kontrol listesi (süre, harç, görev) tamam mı?

## Denetim şeması
1. Yer tutucu standardı: Eksik bilgileri `[doldurulacak]`, `[tarih]`, `[bedel]`, `[TC/vergi no]`, `[delil eki]` gibi tutarlı işaretlerle gösterin; metne tahmini değer yazmayın.
2. Madde teyidi: Süre, tutar ve harç gibi güncellenen normları (parasal sınırlar, faiz oranı) `[yürürlük teyit edilecek]` ile işaretleyin; yürürlük tarihini kontrol önerisi ekleyin.
3. İçtihat hijyeni: İlkesel atıf yapın; karar künyesini doğrulamadan yazmayın. Doğrulanmamış her künyeyi `[doğrulanacak]` ile işaretleyip karararama.yargitay.gov.tr / karararama.danistay.gov.tr / kararlarbilgibankasi.anayasa.gov.tr kaynağını anın.
4. Son kontrol listesi: Görev-yetki, dava şartı/arabuluculuk, süre, harç, talep sonucu netliği, delil-vakıa bağı, imza/vekâletname. Her kalemi tamam/eksik olarak işaretleyin.
5. Teslim notu: Müsveddenin avukat onayı gerektirdiğini, kritik risklerin (süre, teksif) makinece kapatılamadığını belirtin. Ara sonuç: eksik listesi ve kontrol listesi olmadan müsvedde teslim edilmez.

## Çıktı modülleri
- İşaretlenmiş layiha müsveddesi
- Eksik bilgi/yer tutucu raporu
- Doğrulanacak madde ve içtihat listesi
- Teslim öncesi son kontrol listesi

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
