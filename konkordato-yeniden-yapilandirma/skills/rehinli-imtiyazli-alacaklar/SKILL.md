---
name: rehinli-imtiyazli-alacaklar
description: "Rehinle temin edilmiş ve imtiyazlı alacakların mühlet, çoğunluk ve tasdik aşamalarındaki özel rejimini çözümlemek gerektiğinde kullanılır."
---

# Rehinli ve İmtiyazlı Alacaklıların Konumu

## Görev
Konkordatoda en hassas alacaklı gruplarının özel rejimini çözmek: rehinli alacaklıların takip/satış kısıtı, müzakere ve faiz konumu (İİK m.295, m.308/h) ile imtiyazlı alacakların (m.206) çoğunluk dışılığı ve tam ödeme güvencesi.

## Soğuk başlangıç (intake)
- Rehinli alacaklı kim, rehnin kapsadığı malın değeri alacağı karşılıyor mu?
- İmtiyazlı alacaklar (işçi alacakları, nafaka vb. — m.206) var mı?
- Rehinli alacaklılarla ayrı bir anlaşma öngörülüyor mu?
- Mühlet içinde rehnin paraya çevrilmesi talebi var mı?

## Denetim şeması
1. **Rehinli alacaklar — mühlet etkisi (m.295).** Rehnin paraya çevrilmesi yoluyla takip mühletten etkilenmez şekilde başlatılabilir/sürdürülebilir; ancak muhafaza tedbiri alınamaz ve rehinli malın satışı gerçekleştirilemez. Bu sınır titizlikle uygulanır.
2. **Rehinli alacakla anlaşma (m.308/h).** Tasdik kararında, rehinle temin edilmiş alacaklar için yapılandırma (vade, faiz, taksit) ayrıca düzenlenebilir; rehinli alacaklı projenin adi alacaklara ilişkin kısmına oy veremez ölçüde teminat altındaki bölümüyle çoğunluk dışıdır.
3. **İmtiyazlı alacaklar (m.206).** Birinci sıra imtiyazlı alacaklar (örn. işçilik alacakları, nafaka) çoğunluk hesabına katılmaz (m.302/4) ve tasdik için tam ödenmelerinin güvenceye bağlanması şarttır (m.305/1-b), alacaklı feragat etmedikçe.
4. **Karşılıksız kalan rehin bölümü.** Rehin değeri alacağı karşılamıyorsa açık kalan kısım adi alacak gibi işlem görür ve çoğunluk ile yapılandırmaya tabi olur; rehin değerinin tespiti (bilirkişi) önem taşır. İspat: rehin değeri ve alacak tutarı belgeyle ortaya konur.
5. **Ara sonuç.** Her alacaklı grubunun çoğunluk hesabındaki ve tasdikteki konumu netleştirilir; güvence mekanizması (teminat, depo) belirlenir.

## Çıktı modülleri
- Alacaklı sınıf haritası (rehinli/imtiyazlı/adi) ve oy ağırlıkları.
- Rehin değer tespiti ihtiyaç notu.
- İmtiyazlı alacak güvence planı.
- Rehinli alacaklıyla yapılandırma şartı taslağı.

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
