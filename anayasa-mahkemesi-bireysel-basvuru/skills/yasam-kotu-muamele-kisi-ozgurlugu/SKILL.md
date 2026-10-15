---
name: yasam-kotu-muamele-kisi-ozgurlugu
description: "Yaşam hakkı, işkence/kötü muamele yasağı ile kişi hürriyeti ve güvenliği (gözaltı, tutukluluk, uzun tutukluluk) bağlamında negatif ve pozitif yükümlülük ihlalleri iddia edildiğinde kullanılır."
---

# Yaşam, Kötü Muamele ve Kişi Özgürlüğü

## Görev
m.17 (yaşam, maddi-manevi varlık, kötü muamele yasağı) ve m.19 (kişi hürriyeti ve güvenliği) kapsamında Devletin negatif ve pozitif (koruma + etkili soruşturma) yükümlülüklerinin ihlalini değerlendirmek.

## Soğuk başlangıç (intake)
- Olay nedir (ölüm/yaralanma, gözaltı/tutuklama, kötü muamele iddiası)?
- Devlet görevlisi mi sorumlu, yoksa Devletin koruma/önleme/soruşturma ihmali mi var?
- Özgürlükten yoksun bırakma hangi sebebe ve hangi karara dayanıyor?
- Tutukluluk ne kadar sürdü; etkili bir başvuru/itiraz imkânı tanındı mı?

## Denetim şeması
1. Yaşam hakkı (m.17) — negatif yükümlülük: Devletin kasten veya orantısız güç kullanımıyla ölüme yol açmaması. Pozitif yükümlülük: yaşamı koruma ve ölümü/ağır yaralanmayı aydınlatan ETKİLİ, bağımsız, ivedi soruşturma.
2. Kötü muamele yasağı — eşik: muamelenin asgari ağırlık eşiğini aşması. Maddi boyut (muamelenin kendisi) ve usuli boyut (etkili soruşturma) ayrı incelenir; ispat "makul şüphenin ötesinde", gözetim altındaki kişide ispat yükü Devlete kayar.
3. Kişi özgürlüğü (m.19) — yoksun bırakma yalnızca m.19/2-3'teki sınırlı sebeplerle ve kanunda gösterilen usulle mümkündür.
4. Tutuklama denetimi — makul suç şüphesi (somut delil), tutuklama nedenlerinin (kaçma, delil karartma) varlığı, ölçülülük ve adli kontrolün yetersizliği; tutukluluğun makul süreyi aşması (m.19/7) ihlaldir.
5. Usuli güvenceler — yakalanma sebebinin bildirilmesi, hâkim önüne çıkarılma, tutukluluğa etkili itiraz ve tazminat hakkı (m.19/8-9).

İspat yükü: gözaltı/tutukluluk koşullarında ve resmî gözetimde Devlete; aksi halde başvurucuya ağırlıklı olarak düşer.

Ara sonuç: ihlalin maddi mi usuli mi olduğu ve dayanak.

## Çıktı modülleri
- Negatif/pozitif yükümlülük ayrımı.
- Soruşturmanın etkililiği değerlendirmesi.
- Tutukluluk için makul şüphe–neden–süre denetimi.
- İlke kararlarına atıf [doğrulanacak].

## Plugin bağlamı

Bu beceri `anayasa-mahkemesi-bireysel-basvuru` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
