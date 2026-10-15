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
