---
name: usul-gorev-yetki-tahkim
description: "Sigorta uyuşmazlığının nereye götürüleceği (Sigorta Tahkim Komisyonu mu mahkeme mi), görevli-yetkili mahkeme, başvuru şartı ve kanun yolları belirlenirken kullanılır; doğru forum ve usul seçimi için başvurulacak beceri."
---

# Usul, Görev-Yetki ve Sigorta Tahkim Komisyonu

## Görev
Uyuşmazlığı en doğru forumda başlatmak: Sigorta Tahkim Komisyonu mu, ticaret/tüketici mahkemesi mi; görevli-yetkili yer neresi; başvuru şartı, parasal sınır ve kanun yolu nedir.

## Soğuk başlangıç (intake)
1. Sigortacı, Sigorta Tahkim Komisyonu sistemine üye mi (zorunlu sigortalarda üyelik zorunludur)?
2. Talep tutarı ve uyuşmazlığın niteliği (zarar/can/sorumluluk) ne?
3. Sigortalı tüketici mi, tacir mi?
4. Sigortacıya/Güvence Hesabına önce başvuru yapıldı mı?

## Denetim şeması
1. **Tahkim mi mahkeme mi.** 5684 sayılı Kanun m.30: Sigorta Tahkim Komisyonu, üye sigortacılarla zarar görenler arasındaki uyuşmazlıklara bakar. Başvuru şartı: önce sigortacıya yazılı başvuru ve uyuşmazlığın doğması (kısmen/tamamen red ya da 15 gün sessizlik). Ara sonuç: tahkim yolu açık mı?
2. **Parasal sınır ve kanun yolu.** m.30/12: tutara göre hakem kararı kesin olabilir, belirli tutar üstü kararlara Komisyon nezdinde itiraz ve daha üst tutarda temyiz yolu açıktır (güncel parasal sınırları teyit et). Tahkime başvuran bu yola bağlı kalır.
3. **Görevli mahkeme.** Mahkeme yolu seçilirse: ticari nitelikteki sigorta uyuşmazlığında Asliye Ticaret Mahkemesi (TTK m.4-5); sigortalı tüketici ise Tüketici Mahkemesi (6502 m.73). Görev kamu düzenindendir, re'sen incelenir.
4. **Yetki.** HMK genel yetki (davalı yerleşim yeri, HMK m.6) yanında sözleşmenin ifa yeri, sigorta ettirenin/zarar görenin yerleşim yeri gibi özel yetki kuralları; zorunlu sigortalarda zarar görene elverişli yetki.
5. **Süre.** Zamanaşımı TTK m.1420 ya da KTK m.109; tahkim başvurusu zamanaşımını keser. İspat: usul şartlarının yerine geldiğini başvuran gösterir.

## Çıktı modülleri
- Forum seçimi kararı (tahkim/ticaret/tüketici) ve gerekçe.
- Başvuru şartı ve ön başvuru kontrol listesi.
- Görevli-yetkili yer tespiti.
- Kanun yolu ve parasal sınır notu, süre uyarısı.

## Plugin bağlamı

Bu beceri `sigorta-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
