---
name: risk-ve-strateji
description: "İstekli ya da idare adına bir ihale uyuşmazlığında başvuru/dava yoluna gitmenin başarı şansını, maliyetini ve alternatif çözümlerini tartmak; strateji ve öncelik belirlemek için kullanılır."
---

# Risk Değerlendirmesi ve Strateji

## Görev
İhale uyuşmazlığında müvekkilin (istekli veya idare) konumunu, başvuru/dava yolunun başarı olasılığını, maliyet ve sürelerini değerlendirip uygulanabilir bir strateji önerisi sunmak.

## Soğuk başlangıç (intake)
1. Müvekkil kim: istekli mi, idare mi, alt yüklenici mi?
2. Hedef ne: ihaleyi kazanmak, kararı iptal ettirmek, zarar tazmini, yasaklamadan kurtulmak?
3. Süre durumu: başvuru/dava süresi açık mı, sıkışık mı?
4. İhale ekonomik olarak hâlâ değerli mi; sözleşme imzalandı mı?

## Denetim şeması
1. **Pozisyon tespiti:** İddianın hukuki gücü, yerleşik KİK/Danıştay içtihadıyla uyumu ve karşı argümanlar değerlendirilir. Süre uygunluğu ilk filtredir; süre kaçmışsa esasa girilmez.
2. **Yol seçimi:** Şikâyet-itirazen şikâyet zorunlu yoldur; bu yol tüketilmeden iptal davası açılamaz. Düzeltici işlem mi, iptal mi, tam yargı mı hedefleniyor netleştirilir.
3. **Maliyet-fayda:** İtirazen şikâyet başvuru bedeli, dava harç/masrafları, vekâlet ücreti riski ile beklenen kazanç (ihale bedeli, kâr) karşılaştırılır. Düşük katma değerli ihalede agresif strateji önerilmez.
4. **Zaman riski:** Sözleşme imzalanmışsa düzeltici işlem fiilen sonuçsuz kalabilir; bu durumda tam yargı (zarar) yoluna ağırlık verilir.
5. **Alternatifler:** Bir sonraki ihaleye odaklanma, idareyle uyumlu çözüm, yasaklamada savunma stratejisi gibi seçenekler tartılır.
6. **Ara sonuç:** Önerilen yol, gerekçesi, başarı tahmini (yüksek/orta/düşük) ve eylem sırası verilir.

İspat yükü: Strateji, mevcut delil gücüne göre kalibre edilir.

## Çıktı modülleri
- SWOT benzeri pozisyon tablosu (güçlü/zayıf iddialar).
- Yol seçeneği karşılaştırma matrisi (süre/maliyet/şans).
- Önerilen strateji ve aksiyon sırası.

## Plugin bağlamı

Bu beceri `kamu-ihale-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
