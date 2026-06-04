---
name: cezai-sart-ve-teminat
description: "Sözleşmede kararlaştırılan ceza koşulu, pey akçesi veya cayma parasının türü, geçerliliği, indirilmesi ve asıl borçla ilişkisi değerlendirilirken kullanılır."
---

# Cezai Şart, Bağlanma Parası ve Cayma Parası

## Görev
Sözleşmedeki ceza koşulunu (cezai şart) türüne göre nitelendirmek, geçerliliğini ve fahiş cezanın indirilmesini değerlendirmek; bağlanma/cayma parasından ayırmak.

## Soğuk başlangıç (intake)
- Sözleşmede ceza/tazminat kaydı nasıl düzenlenmiş?
- Alacaklı hem asıl edimi hem cezayı mı istiyor, yoksa seçimlik mi?
- Ceza miktarı edime göre aşırı/fahiş mi?
- Borçlu tacir mi (indirim talebi sınırı için)?

## Denetim şeması
1. Cezai şart türleri: TBK m.179 — (a) seçimlik cezai şart: alacaklı ya ifayı ya cezayı ister; (b) ifaya eklenen cezai şart: gecikme veya belirli yerde ifa için, hem ifa hem ceza istenebilir; (c) dönme cezası (m.179/f.3): borçlu cezayı ödeyerek sözleşmeden dönebilir.
2. Asıl borca bağlılık: m.182 — geçersiz asıl borçta ceza da istenemez; ceza asıl borcun fer'idir. Asıl alacak zamanaşımına uğrarsa ceza da etkilenir.
3. Aşan zarar: Alacaklı cezayı aşan zararını ancak borçlunun kusurunu ispatla isteyebilir (m.180/f.2).
4. Fahiş cezanın indirilmesi: m.182/f.3 — hâkim aşırı bulduğu cezayı resen indirir. Ancak tacirler bakımından TTK m.22 — tacir, cezanın fahiş olduğu gerekçesiyle indirim isteyemez (sınırlı istisnalar).
5. Bağlanma parası (pey akçesi) ve cayma parası: m.177-178 — bağlanma parası sözleşmenin yapıldığının kanıtıdır, kural olarak ifada mahsup edilir; cayma parası ise dönme hakkının karşılığıdır. Nitelendirme sonuçları değiştirir.
6. İspat yükü: Cezanın kararlaştırıldığını alacaklı; fahişliği ve indirim sebebini borçlu ileri sürer.

## Çıktı modülleri
- Ceza koşulu nitelendirme tablosu (tür ve sonuç).
- Fahiş ceza/indirim analizi (tacir ayrımıyla).
- Sözleşmeye uygun ceza maddesi taslağı önerisi.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
