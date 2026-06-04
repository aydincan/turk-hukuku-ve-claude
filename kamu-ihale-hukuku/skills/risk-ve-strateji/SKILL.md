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

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
