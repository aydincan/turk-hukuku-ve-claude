---
name: durustluk-risk-strateji
description: "Bir talebin veya savunmanın yalnızca TMK m.2/m.3 gibi esnek başlangıç hükümlerine dayandığı hâllerde; bu argümanın gücünü, başarı olasılığını ve alternatif dayanakları tartmak için kullanılır."
---

# Başlangıç Hükümleri Temelli Risk ve Strateji Değerlendirmesi

## Görev
Dürüstlük kuralı, hakkın kötüye kullanılması veya iyiniyet gibi esnek/takdire açık başlangıç hükümlerine dayanan bir argümanın gerçekçi başarı şansını değerlendirmek; daha sağlam alternatif dayanakları ve ispat risklerini ortaya koymak.

## Soğuk başlangıç (intake)
- Argüman *yalnızca* başlangıç hükmüne mi dayanıyor, yoksa daha güçlü bir özel norm da var mı?
- Başlangıç hükmünün şartları (özellikle m.2/2 "açıklık" eşiği) somut olayda gerçekten karşılanıyor mu?
- İspat yükü (m.6) bizde mi; ispat araçları yeterli mi?
- Hâkimin takdiri (m.4) ne yöne meyledebilir; emsal eğilim nedir?

## Denetim şeması
1. **Önce sağlam dayanak ara** — Esnek başlangıç hükmü, mümkünse asıl dayanak değil destek olmalıdır. Somut bir özel norm (sözleşme ihlali, ayıp, geçersizlik, mülkiyet) varsa o öne çıkarılır; m.2/m.3 ikincil savunma katmanı tutulur.
2. **"Açıklık" riski** — TMK m.2/2 yalnızca *açık* kötüye kullanmada korur; eşik yüksektir. Sıradan menfaat çatışmasını kötüye kullanma diye sunmak zayıf argümandır ve güven kaybı yaratır.
3. **Takdir belirsizliği — m.4** — Hakkaniyet/takdir alanı sonucu öngörülemez kılar; bu belirsizlik dürüstçe müvekkile aktarılır. Sonuç "tartışmalı / hâkimin takdirine bağlı" diye nitelenir, abartılı kesinlik verilmez.
4. **İspat zafiyeti — m.6** — Çelişkili davranış, güven, kötüniyet gibi vakıaların ispatı güçtür; yazılı delil, yazışma, tanık ve karine durumu envanterlenir. İspatlanamayan vakıa "gerçekleşmemiş" sayılır.
5. **Senaryo ve alternatif** — En iyi/orta/en kötü senaryo; başlangıç hükmü tutmazsa devreye girecek yedek dayanak; sulh/uzlaşma penceresi. İçtihat eğilimi tek cümlede dürüstçe (lehe karar seçip aleyhe gizlemeden) özetlenir.
6. **Etik sınır** — Zayıf bir m.2 argümanını "kesin" diye sunmak meslek kurallarına ve dürüst danışmanlığa aykırıdır; risk açıkça paylaşılır.

## Çıktı modülleri
- Dayanak haritası (asıl norm + başlangıç hükmü katmanı).
- Şart/eşik ve ispat riski değerlendirmesi.
- Senaryo tablosu (iyi/orta/kötü) + olasılık nitelemesi.
- Yedek strateji + sulh penceresi + ilkesel içtihat eğilimi `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `medeni-hukuk-baslangic` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
