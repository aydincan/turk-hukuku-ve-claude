---
name: risk-strateji-ve-muvekkil-iletisimi
description: "İmar dosyasında dava açmadan önce kazanım şansı, idari çözüm, maliyet ve geri dönülemez risklerin tartılması; müvekkile sade dilde durum, seçenek ve beklenti yönetimi sunulması gerektiğinde kullanılır."
---

# Risk Haritası, Strateji ve Müvekkil İletişimi

## Görev
İmar uyuşmazlığında hukuki yolların kazanım olasılığını, maliyetini ve riskini tartmak; müvekkile anlaşılır bir strateji ve beklenti çerçevesi sunmak.

## Soğuk başlangıç (intake)
- Müvekkilin asıl amacı ne (yapıyı korumak, tazminat, inşaata devam, süre kazanmak)?
- Geri dönülemez bir adım var mı (yıkım yakın mı, inşaat ilerliyor mu)?
- İdari çözüm/uzlaşma (ruhsata bağlama, aykırılığı giderme, YKB) mümkün mü?
- Maliyet, süre ve itibar açısından kısıtlar neler?

## Denetim şeması
1. **Hedef ve seçenek ayrımı**: Müvekkilin gerçek menfaati ile hukuki araç eşleştirilir: iptal davası, tam yargı (tazminat), idari başvuru/uzlaşma, aykırılığı giderme, Yapı Kayıt Belgesi değerlendirmesi. Her seçeneğin sonucu ayrı yazılır.
2. **Kazanım olasılığı**: İşlemin unsur sakatlığı (yetki-şekil-sebep-konu-maksat), üst plana/yönetmeliğe aykırılık ve içtihat eğilimi tartılarak güçlü/zayıf/belirsiz olarak derecelendirilir; belirsizlik açıkça belirtilir, garanti verilmez.
3. **Geri dönülemez risk**: Yıkım, satış, inşaatın ilerlemesi gibi telafisi imkânsız sonuçlar varsa, **yürütmenin durdurulması (İYUK m.27)** ve ivedi başvuru önceliklendirilir; zamanlama riski en kritik kalemdir.
4. **Maliyet-fayda**: Harç, bilirkişi-keşif gideri, vekâlet ücreti, süre (idari yargıda istinaf/temyiz dahil yıllar) ile beklenen kazanım karşılaştırılır; uzlaşma/idari çözüm maliyet avantajıyla sunulur.
5. **Müvekkil iletişimi (sade dil)**: Teknik kavramlar (emsal, DOP, mühürleme, YD) yalın anlatılır; "kesin kazanırız" yerine olasılık, süre ve maliyet dürüstçe aktarılır; kararı müvekkilin vermesi sağlanır.
6. **Ara sonuç**: Önerilen yol, gerekçesi, alternatifleri, ilk 30 günde atılacak adımlar ve süre uyarıları tek sayfalık karar notuna bağlanır.

## Çıktı modülleri
- Risk haritası (seçenek × olasılık × maliyet × süre).
- Geri dönülemez risk ve ivedilik uyarısı.
- Müvekkile sade dilde durum/strateji notu.
- İlk adımlar ve süre takvimi (eylem planı).

## Plugin bağlamı

Bu beceri `imar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
