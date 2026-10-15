---
name: istinaf-kanun-yolu
description: "İlk derece mahkemesi kararına karşı bölge adliye mahkemesine istinaf başvurusu yapılması, sebeplerin belirlenmesi ve süre denetimi gerektiğinde kullanılır."
---

# İstinaf Kanun Yolu

## Görev
İlk derece hükmüne karşı istinaf yolunun açık olup olmadığını, süresini ve sebeplerini belirlemek; bölge adliye mahkemesi (BAM) önündeki incelemeyi yönlendirmek.

## Soğuk başlangıç (intake)
- Hüküm ne zaman tefhim/tebliğ edildi (süre başlangıcı)?
- Verilen ceza istinaf sınırının üzerinde mi (kesin hüküm mü)?
- Başvuru sebepleri neler: maddi vakıa, hukuka aykırılık, ceza tayini?
- Sanık duruşmada hazır mıydı (süre tefhimden mi tebliğden mi)?
- Yeni delil/tanık talebi var mı?

## Denetim şeması
1. **Süre ve başvuru.** İstinaf, hükmün tefhiminden, yokluğunda verilmişse tebliğinden itibaren 7 gün içinde mahkemeye dilekçeyle veya zabıt kâtibine beyanla yapılır (CMK m.273).
2. **Kesinlik sınırı.** 3.000 TL'ye kadar (yürürlükteki tutar güncellenmiştir, m.272/3 — `[doğrulanacak: güncel parasal sınır]`) adli para cezaları ve bazı kararlar kesindir; bu hallerde istinaf yolu kapalıdır. Beraat kararına karşı da sınırlar gözetilir (m.272).
3. **Sebepler.** İstinaf dilekçesinde hukuka aykırılık nedenleri ve dayanılan vakıalar gösterilir (m.273/4). BAM hem maddi olayı hem hukuku denetler (m.280).
4. **İnceleme ve karar.** BAM ceza dairesi başvuruyu esastan reddedebilir, düzelterek/yeniden hüküm kurabilir veya duruşma açar (m.280, m.289-294 bağlamı). Kovuşturma genişletilebilir.
5. **Aleyhe bozma yasağı.** Yalnız sanık lehine başvuruda ceza ağırlaştırılamaz (m.283).
6. **Ara sonuç.** Süre içinde ve sebepli başvuru hazırlanır; kesinlik sınırı altındaysa istinaf yerine itiraz/yargılamanın yenilenmesi değerlendirilir.

## Çıktı modülleri
- Süre ve kesinlik denetim notu (başlangıç tarihi hesabı).
- İstinaf dilekçesi iskeleti (sebepler + dayanak vakıalar).
- Yeni delil/duruşma talebi gerekçesi.
- Aleyhe bozma yasağı ve risk değerlendirmesi.

## Plugin bağlamı

Bu beceri `ceza-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
