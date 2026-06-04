---
name: surecler-ve-zamanasimi
description: "Tüketici uyuşmazlığında ayıp zamanaşımı, cayma süreleri, başvuru ve dava açma sürelerini hesaplamak ve süre riskini önlemek gerektiğinde; her dosyada erken çalıştırılması gereken takvim becerisidir."
---

# Süreler, Zamanaşımı ve Hak Düşürücü Süreler

## Görev
Tüketici dosyasındaki tüm süreleri (ayıp zamanaşımı, cayma, başvuru, itiraz, dava açma) somut tarihlerle hesaplamak, hak kaybı riskini erkenden işaretlemek ve takvim çıkarmak.

## Soğuk başlangıç (intake)
- Olayın kritik tarihleri neler (sözleşme, teslim/ifa, ayıbın fark edilmesi, ödeme, bildirim)?
- Hangi talep söz konusu (ayıp, cayma, iade, hakem heyeti/dava)?
- Daha önce başvuru/ihtar yapıldı mı; varsa tarihleri?
- Karşı tarafın hile/ağır kusuru iddiası var mı (süreyi etkiler)?

## Denetim şeması
1. **Ayıp zamanaşımı (TKHK m.12, m.16):** Maldaki ayıpta kural iki yıl, konut/tatil amaçlı taşınmazda beş yıl; hizmet ayıbında iki yıl. Ağır kusur veya hile ile gizlenen ayıpta süre işlemez (m.12/3). Süre teslim/ifa tarihinden başlar.
2. **Cayma süreleri:** Mesafeli ve kapıdan satışta 14 gün; eksik ön bilgilendirmede süre uzar. Tüketici kredisinde cayma 14 gün (m.24). Sürelerin başlangıç günü (teslim/sözleşme) doğru saptanmalı; son gün resmî tatile gelirse takip eden iş gününe uzar.
3. **Hakem heyeti ve dava:** Hakem heyetine başvuru için TKHK'da özel hak düşürücü süre öngörülmemiştir; ancak talebin esasına ilişkin zamanaşımı (ör. ayıpta iki yıl, genel alacaklarda TBK m.146/147 süreleri) işlemeye devam eder. Hakem heyeti kararına karşı itiraz/tüketici mahkemesine başvuru süresi tebliğden itibaren on beş gündür (m.70).
4. **Genel zamanaşımı yedeklemesi:** TKHK'da süre yoksa TBK genel zamanaşımı (kural on yıl, TBK m.146; bazı periyodik edimlerde beş yıl, m.147) uygulanır.
5. **Zamanaşımının kesilmesi/durması:** İhtar, dava, icra takibi, borç ikrarı gibi sebeplerle kesilme (TBK m.154) değerlendirilir.
6. **Ara sonuç:** Hangi süre hangi tarihte doluyor, en yakın kritik tarih ne, hangi adım hemen atılmalı?

## Çıktı modülleri
- Süre/zamanaşımı takvim tablosu (tarih bazlı).
- Hak kaybı erken uyarı listesi.
- Süre kesme/durdurma stratejisi notu.

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
