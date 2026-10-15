---
name: yorum-yontemleri-ve-bosluk
description: "Bir normun anlamı tartışmalıyken ya da hiç norm yokken (kanun boşluğu); lafzî-sistematik-tarihsel-amaçsal yorum, kıyas, a contrario ve TMK m.1 çerçevesinde hâkimin hukuk yaratması yöntemini uygulamak gerektiğinde kullanın."
---

# Yorum Yöntemleri ve Boşluk Doldurma

## Görev
Normun anlamını yöntemli biçimde belirlemek (yorum) veya norm yokluğunda boşluğu TMK m.1
disipliniyle doldurmak; yorum argümanlarını hiyerarşik ve gerekçeli biçimde sıralamak.

## Soğuk başlangıç (intake)
- Norm var mı? Varsa anlamı mı tartışmalı (yorum), yoksa hiç mi yok (boşluk)?
- Boşluk gerçek (kural hiç yok) mü, örtülü/açık mı, yoksa "kasıtlı sessizlik" (a contrario) mi?
- Tartışmada karşı tarafın dayandığı yorum argümanı ne?
- Emredici/yasaklayıcı bir alanda mıyız (kıyas yasağı/dar yorum gerektiren alan var mı, ör. ceza)?

## Denetim şeması
1. **Lafzî yorumla başla.** Metnin olağan dil anlamını sapta (TMK m.1: önce kanunun "sözü").
   Açık ve tek anlamlı lafız varsa amaçsal yoruma zıt sonuç çıkarmaktan çekin.
2. **Sistematik + tarihsel + amaçsal yorumu ekle.** Normun kanun içindeki yerini, gerekçesini
   (tarihsel) ve koruduğu amacı (gai/teleolojik) değerlendir. TMK m.1: kanunun "özü/ruhu".
   Objektif-güncel ve sübjektif-tarihsel yorum gerilimini, hangisinin makul sonucu verdiğini
   tartışarak çöz.
3. **Mantıksal argümanları sırala.** Kıyas (benzer olaya benzer kural), evleviyet (a fortiori),
   aksi ile kanıt (a contrario) ve amaca aykırı genişlemeyi daraltan teleolojik redüksiyonu
   uygula. Ceza hukukunda kıyas yasağı (TCK m.2; Anayasa m.38 kanunilik) sınırını mutlaka gözet.
4. **Boşluk tespiti ve doldurma.** Norm yoksa: (a) örtülü boşluk-kasıtlı susma ayrımını yap;
   (b) kasıtlı susma ise a contrario; (c) gerçek boşluk ise önce örf-âdet hukuku (TMK m.1/II),
   sonra hâkimin hukuk yaratması (TMK m.1/II son cümle: "kendisi kanun koyucu olsaydı")
   devreye girer; (d) bu yaratma "bilimsel görüşlere ve yargı kararlarına" dayandırılır
   (TMK m.1/III). Ara sonuç: kanun → örf-âdet → hâkim hukuku sırası.
5. **İspat/gerekçe yükü.** Tercih edilen yorumun neden diğerlerine üstün olduğu gerekçelendirilir;
   dayanak doktrin/yerleşik içtihat ile desteklenir, künye doğrulanmadıkça [doğrulanacak].

## Çıktı modülleri
- Yorum argümanları tablosu (lafzî/sistematik/tarihsel/amaçsal + sonuç).
- Boşluk tipi etiketi ve doldurma yolu (TMK m.1 sırasıyla).
- Karşı argümana cevap notu.
- Önerilen yorumun gerekçeli özeti.

## Plugin bağlamı

Bu beceri `hukuk-felsefesi-genel-teori` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
