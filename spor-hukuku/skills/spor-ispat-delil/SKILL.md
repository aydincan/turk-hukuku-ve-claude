---
name: spor-ispat-delil
description: "Disiplin, doping, şike veya sözleşmesel uyuşmazlıklarda ispat yükünü, delil türlerini ve delil değerini analiz etmek; delil toplama ve sunma stratejisi kurmak gerektiğinde kullanın."
---

# Spor Uyuşmazlıklarında İspat ve Delil

## Görev
Spor uyuşmazlığında ispat yükünü doğru dağıtmak, mevcut delilleri türü ve değerine göre değerlendirmek, eksik delilleri tespit etmek ve delil toplama/sunma stratejisi kurmaktır.

## Soğuk başlangıç (intake)
1. Uyuşmazlık türü: disiplin, doping, şike, sözleşmesel alacak?
2. İspatlanması gereken vakıa nedir ve kim iddia ediyor?
3. Eldeki deliller neler (rapor, görüntü, mesaj, ödeme kaydı, tanık)?
4. Delillerin elde ediliş usulü hukuka uygun mu?
5. Karşı tarafın dayandığı deliller neler?

## Denetim şeması
1. **İspat yükü**: Kural olarak iddia eden ispatla yükümlüdür (HMK m.190, TMK m.6). Disiplinde sevk eden federasyon, sözleşmesel alacakta alacaklı; dopingde varlık ispatı federasyonda, kusursuzluk/kontaminasyon ispatı sporcudadır.
2. **Delil türleri**: Hakem/gözlemci/güvenlik raporları, müsabaka kamera görüntüleri (VAR dahil), doping numune ve laboratuvar kayıtları, sözleşme ve ödeme belgeleri, elektronik yazışmalar, tanık.
3. **Delil değeri**: Tahkim ve disiplin organları serbest delil değerlendirmesi yapar; resmi raporların aksi ispatlanana kadar üstün değeri ve görüntü kayıtlarının teyit edici gücü değerlendirilir.
4. **Hukuka aykırı delil**: Hukuka aykırı yolla elde edilen delil (izinsiz kayıt, hukuka aykırı erişim) reddi gündeme gelir; usulüne uygunluk denetlenir.
5. **Delil tespiti ve sunma**: Kaybolma riski olan delil için tespit; dilekçeye delil bağlama ve dizin; bilirkişi/uzman görüşü gereken teknik konular (doping analizi, mali hesap) belirlenir.
6. **Ara sonuç**: İspat şansı, eksik deliller ve toplama planı netleşir.

## Çıktı modülleri
- İspat yükü ve vakıa-delil eşleştirme tablosu
- Eksik delil ve toplama planı
- Delil dizini taslağı
- Hukuka uygunluk değerlendirme notu

## Plugin bağlamı

Bu beceri `spor-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
