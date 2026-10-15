---
name: ucret-eklenti-esit-davranma
description: "Ödenmeyen ücret, prim, ikramiye, AGİ ve eşit davranma (ayrımcılık) tazminatı tartışıldığında; ücretin tespiti, gecikme faizi, ücret kesintisi sınırları ve eşitlik ilkesi ihlalini değerlendirmek için kullan."
---

# Ücret, Ücret Ekleri ve Eşit Davranma

## Görev
Ücret ve eklerinin ödenip ödenmediğini, miktarını ve eşit davranma ilkesine aykırılığı denetlemek; doğan alacak ve tazminatları belirlemek.

## Soğuk başlangıç (intake)
1. Kararlaştırılan ve fiilen ödenen ücret nedir; bordro ile banka kaydı uyuşuyor mu?
2. Prim, ikramiye, sosyal yardım gibi ekler düzenli mi?
3. Ücret kesintisi/avans mahsubu yapıldı mı?
4. Aynı işi yapan emsallere kıyasla farklı muamele iddiası var mı?

## Denetim şeması
1. **Ücretin korunması (m.32):** Ücret en geç ayda bir, kural olarak banka aracılığıyla ödenir. Ücret nitelikli alacaklarda zamanaşımı **5 yıl**. Ödenmeyen ücret işçiye haklı fesih hakkı verir (m.24/II-e) ve gününde ödenmezse iş görmekten kaçınma hakkı doğabilir (m.34).
2. **Ücretin ispatı:** Bordro imzalı ve ihtirazi kayıtsızsa aksini işçi yazılı delille çürütmelidir. Miktar çekişmeliyse meslek odası/sendika emsal ücret araştırması yapılır.
3. **Ücret kesintisi sınırları (m.38):** İşveren disiplin cezası dışında ücretten kesinti yapamaz; toplu sözleşme/sözleşme dayanağı ve ayda iki günlük ücreti aşmama sınırı vardır.
4. **Asgari ücret ve AGİ:** Ücret asgari ücretin altında olamaz; AGİ ayrı kalemdir (güncel mevzuat ve uygulama değişiklikleri [doğrulanacak]).
5. **Eşit davranma (m.5):** İşveren biyolojik/cinsiyet, dil, ırk, din vb. sebeplerle ayrım yapamaz; esaslı sebep olmadıkça tam-kısmi süreli ve belirli-belirsiz süreliyi farklı işleme tabi tutamaz. İhlalde işçi, dört aya kadar ücreti tutarında **ayrımcılık tazminatı** ve yoksun bırakıldığı haklar talep edebilir. İhlali işçi ortaya koyar, ayrım olmadığını işveren ispatlar.

## Çıktı modülleri
- Ücret/ek tespit tablosu ve eksik ödeme kalemleri.
- Faiz ve zamanaşımı değerlendirmesi.
- Eşit davranma ihlali değerlendirmesi ve tazminat öngörüsü.
- İspat stratejisi notu.

## Plugin bağlamı

Bu beceri `is-hukuku-bireysel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
