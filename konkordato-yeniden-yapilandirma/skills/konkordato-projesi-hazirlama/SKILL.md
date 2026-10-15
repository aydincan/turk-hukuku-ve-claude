---
name: konkordato-projesi-hazirlama
description: "Konkordato ön projesini ve projesini ekonomik olarak gerçekçi, tasdik şartlarını karşılayacak biçimde hazırlamak veya mevcut projeyi denetlemek gerektiğinde kullanılır."
---

# Konkordato Projesi ve Ön Proje Hazırlama

## Görev
İİK m.286'ya uygun konkordato ön projesini ve nihai projeyi hazırlamak veya denetlemek; tenzilat/vade/karma yapısını, kaynak planını ve alacaklı sınıflandırmasını tasdik şartlarına (m.305) uyacak şekilde kurmak.

## Soğuk başlangıç (intake)
- Önerilen yapı: alacaktan indirim mi, vade mi, karma mı? Oran ve süreler?
- Ödeme kaynağı: işletme faaliyeti, sermaye artırımı, varlık satışı, yeni finansman?
- Alacaklı sınıfları: rehinli, imtiyazlı (m.206), adi alacaklılar nasıl dağılıyor?
- Makul güvence veren denetim raporu mevcut mu?

## Denetim şeması
1. **Ön proje içeriği (m.286/a).** Alacaklıların hangi oranda alacağından vazgeçeceği veya vadenin nasıl tanınacağı, ödeme planı; ödemelerin nasıl finanse edileceği açıkça gösterilmeli.
2. **Belge seti (m.286/b-e).** Mal varlığı durumunu gösteren belgeler, finansal tablolar, ara bilanço, alacaklı/alacak listesi, makul güvence veren bağımsız denetim raporu (KGK denetim standartları). İspat: projenin sayısal varsayımları belgeyle desteklenmeli.
3. **Kaynak gerçekçiliği.** Nakit akış projeksiyonu ile ödeme planı tutarlı mı? İmtiyazlı alacakların (m.206) tam ödeneceği güvenceye bağlanmış mı (m.305 şartı)?
4. **Alacaklı eşitliği.** Aynı sınıftaki alacaklılara eşit muamele; farklı sınıflar arasında haklı ayrım gerekçesi. Rehinli alacaklılarla yapılan ayrı düzenleme (m.308/h) ayrıca ele alınır.
5. **Tasdik süzgeci.** Teklifin borçlunun kaynaklarıyla orantılılığı (m.305/1-a), çoğunluk (m.302) ve depo şartları önceden test edilir. Ara sonuç: proje tasdik edilebilir nitelikte mi.

## Çıktı modülleri
- Konkordato ön projesi taslağı (yer tutuculu).
- Ödeme planı ve nakit akış tablosu iskeleti.
- Alacaklı sınıflandırma ve oran tablosu.
- Tasdik şartı uyum kontrol listesi.

## Plugin bağlamı

Bu beceri `konkordato-yeniden-yapilandirma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
