---
name: ictihat-baglayiciligi-ibk-ve-aym
description: "Bir karara dayanılırken onun mahkemeleri ne ölçüde bağladığı tartışıldığında; içtihadı birleştirme kararı, genel kurul, daire ve AYM kararlarının bağlayıcılık hiyerarşisini belirlemek için kullanılır."
---

# İçtihat Bağlayıcılığı (İBK, HGK, AYM)

## Görev
Bir yargı kararının somut uyuşmazlıkta ne kadar ağırlık taşıdığını — bağlayıcı mı yoksa yalnızca ikna edici mi olduğunu — doğru sınıflandırmak ve buna göre güç atfetmek.

## Soğuk başlangıç (intake)
- Karar hangi merciden: İBK, HGK/İDDK/VDDK, daire, BAM/BİM mi?
- Konu AYM norm denetimi veya bireysel başvuru kararına mı dayanıyor?
- Karşı tarafın dayandığı içtihat ile çatışan başka karar var mı?
- Karardan sonra mevzuat veya içtihat değişmiş mi?

## Denetim şeması
1. **AYM kararları** — Anayasa m.153/son: bağlayıcı (herkesi bağlar). Norm denetimi kararı iptal ettiği hükmü ortadan kaldırır; bireysel başvuruda ihlal kararı yeniden yargılama yolu açabilir. En üst değer.
2. **İçtihadı Birleştirme Kararı (İBK)** — Yargıtay Kanunu m.45: benzer hukuki konularda Yargıtay genel kurullarını, dairelerini ve mahkemeleri bağlar. Daireler arası çelişkiyi giderir; daire kararından üstündür.
3. **Genel Kurul (HGK / Ceza GK / İDDK / VDDK)** — Bağlayıcı değil ama daire kararından ağır basan, yön gösterici emsal; direnme kararlarında belirleyici.
4. **Daire kararı** — İkna edici emsal (Anayasa m.138/1: hâkim yalnız hukuka bağlı). "Yerleşik içtihat" demek için birden çok, istikrarlı, güncel karar gerekir.
5. **BAM/BİM (istinaf)** — Bölgesel emsal değeri; ülke çapında bağlayıcılığı yoktur, daireler arasında farklılaşabilir.
6. **Çatışma ve güncellik** — Çelişen kararlarda hiyerarşi (İBK > GK > daire) ve tarih gözetilir; eski karar, sonraki kanun değişikliği veya İBK ile aşılmış olabilir.

## Çıktı modülleri
- Karar → bağlayıcılık sınıfı eşlemesi.
- "Yerleşik içtihat" iddiası için yeterlilik kontrolü.
- Çatışan içtihat varsa öncelik/tarih analizi.
- Güç atfı önerisi (bağlar / güçlü emsal / tek görüş) + `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `atif-turk-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
