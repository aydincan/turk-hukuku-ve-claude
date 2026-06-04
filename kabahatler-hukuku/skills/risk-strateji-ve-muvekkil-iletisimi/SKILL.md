---
name: risk-strateji-ve-muvekkil-iletisimi
description: "Birden çok seçeneğin (başvuru, ödeme, itiraz, bekleme) sonuçlarını tartıp bir risk haritası çıkarmak ve müvekkile sade dille tavsiye iletmek gerektiğinde kullanılır."
---

# Risk-Strateji ve Müvekkil İletişimi

## Görev
Dosyadaki tüm seçenekleri olasılık-maliyet-sonuç ekseninde tartmak, bir risk haritası ve eylem planı çıkarmak, müvekkile anlaşılır bir tavsiye sunmak.

## Soğuk başlangıç (intake)
- Müvekkilin önceliği ne: maliyeti düşürmek mi, sicili/itibarı korumak mı, ilkesel itiraz mı?
- Cezanın tutarı ve müvekkilin ekonomik durumu nedir?
- Sübut ve sakatlık iddialarının gücü ne düzeyde?
- Süreler ne durumda (başvuru/itiraz/peşin ödeme)?

## Denetim şeması
1. **Seçeneklerin haritası:** (a) Süresinde peşin ödeme (1/4 indirim — 5326 m.17/6); (b) sulh ceza hâkimliğine başvuru (m.27); (c) başvuru + itiraz (m.29); (d) zamanaşımını bekleyip infaz edilemezlik (m.21). Her seçeneğin olasılık ve maliyetini yaz.
2. **Sübut/sakatlık değerlendirmesi:** Yetki-şekil sakatlığı ve zamanaşımı varsa başvuru şansı yüksektir; sübut güçlü ve sakatlık yoksa indirimli ödeme rasyoneldir.
3. **Maliyet analizi:** Başvuruda harç/masraf ve red riski; ödemede indirim kazancı; gecikmede tahsil/haciz ve yerine getirme zamanaşımı dengesi.
4. **İtibar/ikincil etkiler:** Ruhsat, faaliyet, tekrar/sicil etkileri varsa idari yargı boyutunu (m.27/8) gözet.
5. **Tavsiye ve onay:** Tek bir önerilen yolu, gerekçesini ve alternatifini sun; müvekkilin bilgilendirilmiş onayını al, süre uyarısını yaz.
6. **Ara sonuç:** Karar verilen yolu takvime bağla ve sorumluyu belirle.

İspat ve süre belirsizliklerini açıkça paylaş; kesin sonuç vaadinden kaçın.

## Çıktı modülleri
- Risk haritası tablosu (seçenek × olasılık × maliyet × sonuç).
- Müvekkile sade dilde bilgilendirme/tavsiye notu.
- Eylem planı ve süre takvimi.

## Plugin bağlamı

Bu beceri `kabahatler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
