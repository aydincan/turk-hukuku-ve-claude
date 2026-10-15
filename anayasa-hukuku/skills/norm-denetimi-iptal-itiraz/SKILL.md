---
name: norm-denetimi-iptal-itiraz
description: "Bir kanun veya Cumhurbaşkanlığı kararnamesinin Anayasaya aykırılığının AYM önünde nasıl denetleneceğini belirlemek; soyut norm denetimi (iptal davası) ve somut norm denetimi (itiraz yolu) ile başvurma şartlarının gerektiği hallerde kullanılır."
---

# Norm Denetimi (İptal ve İtiraz Yolu)

## Görev
Bir kanun, CB kararnamesi veya TBMM İçtüzüğü hükmünün Anayasaya aykırılığının Anayasa Mahkemesi önünde denetlenmesi yolunu belirlemek: soyut norm denetimi (iptal davası) ve somut norm denetimi (itiraz/def'i) şartlarını uygulamak.

## Soğuk başlangıç (intake)
1. Denetlenecek norm türü ne — kanun, CB kararnamesi, İçtüzük?
2. Soyut denetim mi (iptal davası) yoksa görülmekte olan bir davada itiraz mı söz konusu?
3. İptal davası için başvurucu, m.150'deki yetkili makamlar arasında mı?
4. Süre işliyor mu; iptal davasında RG'de yayımdan itibaren 60 günlük süreye dikkat edildi mi?

## Denetim şeması
1. **Denetim konusu (m.148).** AYM, kanunların, CB kararnamelerinin ve TBMM İçtüzüğünün Anayasaya şekil ve esas bakımından uygunluğunu denetler. Bazı işlemler (ör. usulüne göre yürürlüğe konmuş milletlerarası andlaşmalar) denetim dışıdır.
2. **Soyut denetim — iptal davası (m.150).** Başvuru yetkisi sınırlıdır: Cumhurbaşkanı, iktidar/ana muhalefet partisi meclis grupları ve TBMM üye tamsayısının en az beşte biri. Süre: kanunun RG'de yayımından itibaren 60 gün (m.151).
3. **Somut denetim — itiraz yolu (m.152).** Bir davaya bakan mahkeme, uygulayacağı norm hükmünü Anayasaya aykırı görür veya tarafın ciddi iddiasını benimser ise AYM'ye başvurur. AYM 5 ay içinde karar vermezse mahkeme mevcut hükümlere göre karar verir; on yıl içinde aynı norma yeniden itiraz yasağına dikkat (m.152/4).
4. **Şekil/esas denetimi.** Şekil bakımından kanunlarda son oylama, kararnamelerde yetki/usul; esas bakımından m.13 ve ilgili maddeler süzgeci. Ara sonuç: şekil denetimi süreye tabidir (m.148/2).
5. **Karar sonuçları (m.153).** İptal kararları RG'de yayımıyla yürürlüğe girer, geriye yürümez; AYM yürürlük tarihini erteleyebilir. Kararlar herkesi bağlar.
İlke düzeyinde AYM kararlarına atıf yapın; esas/karar no ve RG künyesini `[doğrulanacak]` işaretleyin (kararlarbilgibankasi.anayasa.gov.tr).

## Çıktı modülleri
- Uygun denetim yolu ve başvuru ehliyeti/süre kontrol listesi.
- İptal/itiraz gerekçesinin madde bazlı iskeleti.
- Olası karar sonuçlarının (iptal, erteleme, geriye yürümezlik) müvekkile etki notu.

## Plugin bağlamı

Bu beceri `anayasa-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
