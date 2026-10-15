---
name: idari-islem-unsur-denetimi
description: "Bir idari işlemin hukuka uygunluğunu yetki-şekil-sebep-konu-maksat unsurları üzerinden denetlemek ve sakatlık (yokluk/iptal) hallerini tespit etmek için kullanılır; iptal davası gerekçesi kurarken başvurulur."
---

# İdari İşlemin Unsurları ve Sakatlık Denetimi

## Görev
İdari işlemi beş unsur üzerinden adım adım denetleyerek hukuka aykırılıkları tespit etmek ve iptal sebeplerini somut dayanaklarla kurmak. Bu beceri iptal davasının maddi çekirdeğini üretir.

## Soğuk başlangıç (intake)
1. İşlemin tam metni, dayanağı (kanun/yönetmelik maddesi) ve gerekçesi elinde mi?
2. İşlemi tesis eden makam ve imza yetkisi/devri belli mi?
3. İşlemden önce alınması gereken görüş, savunma, kurul kararı var mıydı?
4. İşlemin maddi ve hukuki sebepleri dosyada gösterilmiş mi?

## Denetim şeması
1. **Yetki.** Kişi (doğru makam mı, yetki devri/imza devri usulüne uygun mu), yer, zaman ve konu bakımından yetki. Yetkisizlik ağırsa **yokluk**; aksi halde iptal sebebidir. Fonksiyon gaspı/yetki gaspı yokluk doğurur.
2. **Şekil.** Yazılılık, gerekçe gösterme, başvuru yollarının bildirilmesi, kurul ise toplantı/karar nisabı. Savunma alınması gereken hallerde (özellikle yaptırım işlemleri) savunma alınmamışsa esaslı şekil sakatlığı. Anayasa m.40 başvuru yollarının gösterilmesi.
3. **Sebep.** İşlemin dayandığı maddi olay ve hukuki neden gerçek, doğru ve ilgili kuralın aradığı nitelikte mi? Sebebin hiç bulunmaması veya yanlış nitelendirme iptal sebebidir; maddi olayın gerçekliği re'sen araştırılır (İYUK m.20).
4. **Konu.** İşlemin doğurduğu hukuki sonuç, kanunun öngördüğü sonuç mu? İmkânsız/kanuna aykırı konu sakatlık doğurur.
5. **Maksat (amaç).** İşlem kamu yararı amacıyla mı tesis edilmiş? Yetki saptırması (başka amaç, kişisel/siyasi saik) iptal sebebidir.
6. **Takdir yetkisi denetimi.** Bağlı yetki yoksa idarenin takdiri; ancak takdir eşitlik, ölçülülük (Anayasa m.13) ve kamu yararı ile sınırlıdır; sınır aşımı denetlenir.
7. **Ara sonuç ve ispat.** Her unsur için "uygun/sakat" ve dayanak. İspat yükü kural olarak işlemin hukuka uygunluğunu belgeleyecek idarededir; davacı somut aykırılık iddiasını ortaya koyar.

## Çıktı modülleri
- Beş unsur denetim tablosu (uygun/sakat + dayanak + delil).
- Yokluk/iptal nitelendirmesi.
- İptal dilekçesi için hukuki sebepler listesi.
- Eksik belge ve ek bilgi talebi notu.

## Plugin bağlamı

Bu beceri `idare-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
