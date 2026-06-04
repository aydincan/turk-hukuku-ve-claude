---
name: savunma-strateji-risk
description: "Bir ceza isnadında savunma hattını kurmak, beraat-indirim-düşme seçeneklerini tartmak ve müvekkile gerçekçi risk haritası sunmak gerektiğinde kullanılır."
---

# Savunma Stratejisi ve Risk Değerlendirmesi

## Görev
Şüpheli/sanık vekilinin gözünden savunma hattını kurmak; suç teorisi katmanlarındaki zayıf noktaları savunma argümanına çevirmek ve müvekkile gerçekçi risk-seçenek haritası sunmak.

## Soğuk başlangıç (intake)
- İsnat ve sevk maddesi nedir; dosyadaki temel deliller hangileri?
- Müvekkilin hedefi nedir (beraat, en az ceza, hızlı kapanış)?
- Şikâyet, uzlaştırma, önödeme gibi düşme yolları açık mı?
- Sanığın geçmişi ve duruşmadaki tutumu nasıl olacak?

## Denetim şeması
1. **Tipiklik saldırısı:** Maddi unsur eksikliği (netice/nedensellik kopukluğu), manevi unsur eksikliği (kast yokluğu, taksir lehine niteleme) argümanları üretilir. Ara sonuç: tipiklik tartışılabilir mi?
2. **Hukuka aykırılık savunması:** Meşru savunma, rıza, hak kullanma (m.24-27) sebeplerinin şartları somut delille kurgulanır.
3. **Kusurluluk savunması:** Haksız tahrik (m.29), hata (m.30), cebir-zorunluluk (m.28, m.25/2), yaş/akıl (m.31-32) ve buna bağlı rapor talepleri.
4. **Niteleme ve içtima lehine argüman:** Daha hafif suça niteleme, teşebbüs/gönüllü vazgeçme (m.35-36), zincirleme yerine tek suç ya da tersi yönünde lehe değerlendirme.
5. **Düşme/sönme yolları:** Zamanaşımı (m.66), şikâyet süresi (m.73), uzlaştırma (CMK m.253), önödeme (m.75), şikâyetten vazgeçme; ardından yaptırım aşamasında m.62, m.50, m.51, HAGB (CMK m.231) lehine talepler.
6. **Risk tartımı:** Her seçeneğin olasılık ve ceza sonucu, in dubio pro reo ve ispat yükü dikkate alınarak tartılır.

## Çıktı modülleri
- Katman bazlı savunma argümanı matrisi (güç/zayıflık).
- Düşme/indirim yolları kontrol listesi ve süre takvimi.
- Müvekkile sade dilli risk-seçenek haritası.
- Delil talebi ve `[doğrulanacak]` içtihat ihtiyacı.

## Plugin bağlamı

Bu beceri `ceza-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
