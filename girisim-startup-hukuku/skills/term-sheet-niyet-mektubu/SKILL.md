---
name: term-sheet-niyet-mektubu
description: "Bir yatırım turunun ön anlaşma belgesi (term sheet / niyet mektubu) müzakere edilir veya hazırlanırken; hangi maddelerin bağlayıcı olduğunu, münhasırlık ve gizlilik hükümlerini, değerleme ve temel koruma şartlarını netleştirmek için kullanılır."
---

# Term Sheet ve Niyet Mektubu

## Görev
Yatırım turunun çatısını kuran term sheet'i hazırlamak/müzakere etmek; bağlayıcı ve bağlayıcı olmayan hükümleri ayırmak; değerleme, tur büyüklüğü ve temel koruma şartlarını çerçevelemek.

## Soğuk başlangıç (intake)
1. Tur büyüklüğü, ön/son para değerlemesi (pre/post-money) ve yatırımcı tipi nedir?
2. Enstrüman ne: doğrudan equity, SAFE, dönüştürülebilir borç?
3. İstenen koruma kalemleri: tasfiye tercihi, anti-dilution, veto, yönetim koltuğu?
4. Münhasırlık (exclusivity) ve gizlilik isteniyor mu; ne süreyle?
5. Due diligence ve kapanış için öngörülen takvim ne?

## Denetim şeması
1. Bağlayıcılık ayrımı: Term sheet kural olarak bağlayıcı değildir (niyet beyanı); ancak münhasırlık, gizlilik, masraf paylaşımı ve uygulanacak hukuk maddeleri açıkça bağlayıcı kılınmalıdır. TBK m.1 vd. — irade beyanı yorumu; tarafların belgeyi bağlayıcı sayma iradesi metinde net olmalı.
2. Müzakerede dürüstlük: Münhasırlık süresince haklı sebep olmadan müzakereyi koparma culpa in contrahendo (TBK m.35 atıf alanı, dürüstlük TMK m.2) sorumluluğu doğurabilir — bunu bilinçli kurgula.
3. Değerleme ve havuz: Post-money mı pre-money mı; opsiyon havuzunun turdan önce mi sonra mı açılacağı (kimi sulandıracağı) açıkça yazılmalı.
4. Koruma kalemleri başlığı: Tasfiye tercihi, anti-dilution (tam/ağırlıklı ortalama), veto/onay konuları, bilgi alma, yönetim temsili — bunlar burada ilkesel, kesin sözleşmede (SHA) ayrıntılı kurgulanır.
5. Kapanış ön şartları: DD tamamlanması, kurumsal onaylar (GK/YK), gerekiyorsa rekabet izni (4054 m.7) ve üçüncü kişi onayları.
6. İspat/şekil: Yazılı; bağlayıcı maddeler için imza. Sayısal değerleri [doldurulacak] bırak.

## Çıktı modülleri
- Term sheet taslağı (bağlayıcı/bağlayıcı olmayan ayrımı işaretli).
- Münhasırlık ve gizlilik madde önerileri.
- Değerleme/havuz/sulandırma açıklama notu.

## Plugin bağlamı

Bu beceri `girisim-startup-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
