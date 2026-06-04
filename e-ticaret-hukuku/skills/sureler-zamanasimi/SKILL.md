---
name: sureler-zamanasimi
description: "E-ticaret uyuşmazlığında cayma süresi, ret/teyit süreleri, idari yaptırıma itiraz, ayıp ihbarı ve zamanaşımı gibi süreyle bağlı tüm hak kayıplarını hesaplamak gerektiğinde kullanılır."
---

# Süreler ve Zamanaşımı

## Görev
E-ticaret olayında süreye bağlı hakları ve risklerini tek tabloda toplamak; süre başlangıçları, hak düşürücü süreler ve zamanaşımlarını doğru hesaplayarak kayıp önlemek.

## Soğuk başlangıç (intake)
- Olayın türü ne (cayma, ayıp, ticari ileti, idari ceza, tazminat)?
- Sürelerin başladığı tetikleyici olay tarihleri neler (teslim, tebliğ, öğrenme)?
- Tüketici mi tacir mi (sürelerin hesabı değişir)?
- Süre durduran/kesilten bir başvuru yapıldı mı?

## Denetim şeması
1. Cayma hakkı: tüketici 14 gün içinde cayar; süre malda teslimden, hizmette sözleşme tarihinden işler. Ön bilgilendirme yapılmamışsa süre Mesafeli Sözleşmeler Yönetmeliği uyarınca uzar.
2. İade/teyit süreleri: cayma sonrası satıcı bedeli 14 gün içinde iade eder; ticari iletide ret bildirimi 3 iş günü içinde uygulanır; sipariş teyidi gecikmeksizin yapılır (6563 m.5).
3. Ayıp ve tüketici alacağı: ayıp ihbarı ve 6502 m.12 kapsamındaki zamanaşımı (kural olarak iki yıl, gizli ayıpta ihbar yükü) somut mala göre belirlenir.
4. Sözleşme/haksız fiil: TBK genel zamanaşımı m.146 (on yıl) ve TBK m.147 özel süreler; haksız fiilde TBK m.72 (öğrenmeden iki, her halde on yıl); ticari işlerde TTK özel süreleri kontrol edilir.
5. İdari yaptırım: idari para cezasına karşı dava açma süresi 2577 sayılı İYUK'a göre işler; KVKK Kurul kararı için süre ayrıca hesaplanır.
6. Durma/kesilme: arabuluculuk başvurusu zamanaşımını durdurur; başvuru ve dava tarihleri kayıt altına alınır.
İspat yükü: süre içinde başvuruyu yapan taraf ispatlar.

## Çıktı modülleri
- Süre takvimi (tetikleyici-süre-son gün).
- Zamanaşımı/hak düşürücü süre uyarı listesi.
- Süre koruma (başvuru/ihtar) önerisi.

## Plugin bağlamı

Bu beceri `e-ticaret-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
