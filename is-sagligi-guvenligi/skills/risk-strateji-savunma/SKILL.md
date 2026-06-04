---
name: risk-strateji-savunma
description: "İşveren veya çalışan tarafı için iş kazası ve uyum riskini değerlendirmek, savunma stratejisi ve sulh-uzlaşma seçeneklerini tartmak için kullanılır."
---

# Risk Stratejisi ve Savunma Planlaması

## Görev
Tarafın konumuna göre (işveren savunması ya da çalışan/hak sahibi talebi) bütüncül risk değerlendirmesi yapmak; idari, tazminat, rücu ve ceza eksenlerini birlikte tartıp strateji ve sulh seçeneklerini önermek.

## Soğuk başlangıç (intake)
- Müvekkil sıfatı ve hedefi (riski sınırlamak / azami tazminat / cezadan kaçınmak)?
- Dört eksenden hangileri açık (idari ceza, tazminat, SGK rücuu, ceza)?
- Kusur oranı/bilirkişi tahmini ve karşı tarafın delil gücü ne?
- Sulh/uzlaşma için tarafların eğilimi ve ödeme kapasitesi var mı?

## Denetim şeması
1. **Çok eksenli risk haritası:** Aynı kaza dört ayrı sonuç doğurur — idari ceza (6331 m.26), işçi/hak sahibi tazminatı (TBK m.417), SGK rücuu (5510 m.21), ceza (TCK m.85-89). Bir eksendeki kusur tespiti diğerlerini güçlü biçimde etkiler; tek strateji tüm eksenleri gözetmeli.
2. **İşveren tarafı:** Önlem ve uyum belgeleriyle kusuru azaltma (önleme hiyerarşisi, eğitim, yazılı uyarı zinciri), müterafik/üçüncü kişi kusuru argümanı, idari cezada usul itirazı, ceza eksende bilinçli taksir-basit taksir ayrımı.
3. **Çalışan/hak sahibi tarafı:** Risk değerlendirmesi/eğitim eksikliği ve önleme hiyerarşisi ihlaliyle kusuru yükseltme, belirsiz alacakla tam talep, manevi tazminat ve destek kalemleri.
4. **Sulh-uzlaşma ekonomisi:** Ceza ekseninde uzlaşma kapsamı, tazminatta makbuz/ibraname riskleri (gerçek iradeyi yansıtmayan ibra geçersiz olabilir), maluliyetin kesinleşmemesi nedeniyle erken sulhün riski.
5. **Senaryo karşılaştırması:** En iyi/orta/en kötü senaryoda mali ve cezai sonuç. **Ara sonuç:** Önerilen strateji + gerekçe + sonraki adımları sırala.

## Çıktı modülleri
- Dört eksenli risk haritası ve etkileşim notu.
- Taraf bazlı argüman ve savunma listesi.
- Sulh/uzlaşma senaryo karşılaştırma tablosu.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
