---
name: risk-strateji-ve-planlama
description: "Bir işlemin veya yapının vergi riskini değerlendirmek, meşru vergi planlaması ile peçeleme/muvazaa sınırını çizmek ve dava-uzlaşma stratejisini önermek için kullanılır."
---

# Vergi Riski, Strateji ve Planlama

## Görev
Mevcut ya da planlanan bir işlemin vergisel riskini ölçmek, meşru planlama ile kanuna karşı hile (peçeleme/muvazaa) sınırını belirlemek ve uyuşmazlık halinde en uygun strateji yolunu önermek.

## Soğuk başlangıç (intake)
1. Değerlendirme geçmiş bir işleme mi (savunma) yoksa planlanan yapıya mı (önleyici) ilişkin?
2. İşlemin ekonomik amacı ve ticari gerekçesi nedir?
3. İlişkili kişiler/grup içi işlem veya yurt dışı unsur var mı?
4. Benzer işlemlerde idare görüşü/özelge veya yerleşik içtihat var mı?
5. Mükellefin risk iştahı ve nakit/teminat kapasitesi nedir?

## Denetim şeması
1. **Meşru planlama-peçeleme sınırı:** VUK m.3/B (gerçek mahiyet) ve ekonomik yaklaşım; vergiden kaçınma (kanunun tanıdığı seçenekleri kullanma) meşru, kanuna karşı hile/peçeleme (görünürdeki işlemle gerçeği gizleme) ise vergi ziyaı ve m.359 riski doğurur. Bu sınırı somut olaya göre çiz.
2. **İlişkili kişi riski:** KVK m.13 (transfer fiyatlandırması — emsallere uygunluk) ve KVK m.12 (örtülü sermaye); grup içi işlemde emsal ve belgelendirme yeterli mi?
3. **Belge ve şeklî uyum:** VUK m.227-242 belge düzeni; eksik belge hem KKEG hem özel usulsüzlük riskidir. İşlemin kâğıt zemini sağlam mı?
4. **Özelge ile koruma:** VUK m.369 ve m.413 — mükellefe verilmiş özelgeye uygun işlemde ceza kesilmez ve gecikme faizi hesaplanmaz; ancak özelge yalnızca muhatabını bağlar ve idareyi her zaman bağlamaz. Korumanın kapsamını gerçekçi değerlendir.
5. **Senaryo ve beklenen değer:** İhtilaf çıkma olasılığı × (vergi + ceza + faiz) ile uzlaşma/dava maliyetini karşılaştır; uzlaşma indirimi, dava kazanma olasılığı ve yürütmenin durması rejimini (İYUK m.27/4) hesaba kat. Ara sonuç: önerilen strateji (planı revize et / özelge iste / uzlaş / dava aç).
6. **Ceza yargısı eşiği:** Sahte belge ve hile unsuru varsa idari değil cezai (VUK m.359) risk öne çıkar; strateji bu eşiği gözeterek kurulur.

## Çıktı modülleri
- Risk haritası (kalem / olasılık / tutar etkisi / hukuki dayanak).
- Meşru planlama-peçeleme sınır notu.
- Strateji karşılaştırması (planı değiştir / özelge / uzlaşma / dava — beklenen değer).
- Önleyici aksiyon ve belgelendirme listesi.

## Plugin bağlamı

Bu beceri `vergi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
