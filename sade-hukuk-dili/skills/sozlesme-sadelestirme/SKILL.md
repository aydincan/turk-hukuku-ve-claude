---
name: sozlesme-sadelestirme
description: "Bir sözleşmeyi veya belirli maddelerini imzalamadan önce müvekkilin anlayacağı dile çevirmek; hangi yükümlülük, hangi risk, hangi çıkış var sorularını yalın anlatmak gerektiğinde kullanılır."
---

# Sözleşme ve Madde Sadeleştirme

## Görev
Bir sözleşmeyi veya seçili maddeleri, tarafın "neyi taahhüt ediyorum, ne risk alıyorum, nasıl
çıkarım" sorularına cevap verecek sade bir özete çevirmek; yükümlülükleri, riskleri ve çıkış
mekanizmalarını anlam kaybı olmadan aktarmak.

## Soğuk başlangıç (intake)
1. Sözleşme türü nedir (satış, kira, hizmet, eser, gizlilik, pay devri)?
2. Müvekkil hangi taraf ve imza öncesi mi sonrası mı?
3. En çok endişe edilen konu (para, süre, sorumluluk, fesih)?
4. Karşı tarafın hazırladığı tip sözleşme / genel işlem koşulu mu?

## Denetim şeması
1. ROL VE EDİMLER: Tarafların asli edimleri ayrıştırılır (kim ne verecek, ne ödeyecek, ne zaman).
   Sözleşmenin yorumunda gerçek irade esastır (TBK m.19); sade metin bu iradeyi yansıtır.
2. PARA VE SÜRE: Bedel, ödeme planı, vade, ifa süreleri takvim/somut tutarla yazılır; muacceliyet
   ("borcun istenebilir hale gelmesi") açıklanır.
3. RİSK MADDELERİ: Sorumluluğun sınırlanması (TBK m.115 — ağır kusurda sorumsuzluk anlaşması
   geçersiz), cezai şart (TBK m.179-182), temerrüt faizi, müteselsil sorumluluk yalın dille
   ama anlamı korunarak aktarılır; "müteselsil" = her biri borcun tamamından sorumlu.
4. GENEL İŞLEM KOŞULU SÜZGECİ (ispat/geçerlilik): Tip sözleşmelerde diğer tarafın aleyhine olup
   beklenmeyen şartlar yazılmamış sayılabilir (TBK m.21); belirsizlik düzenleyen aleyhine
   yorumlanır (TBK m.23); tüketici ise haksız şart denetimi (TKHK m.5). Bu noktalar okuyucuya
   risk olarak işaretlenir.
5. ÇIKIŞ: Fesih, dönme ve cayma hakları ayrı ayrı açıklanır (anlamları farklıdır); bildirim
   süreleri ve şekil şartları belirtilir.
6. ARA SONUÇ: Sade özet, her asli yükümlülüğü, parasal sonucu ve çıkış yolunu kapsıyor mu; hiçbir
   aleyhe şart gizlenmemiş mi denetlenir.

## Çıktı modülleri
- "Bu sözleşmeyle ne taahhüt ediyorsunuz" özeti.
- Yükümlülük / karşılık / süre tablosu.
- Risk işaretleri (yüksek-orta-düşük) ve madde atfı.
- Çıkış yolları ve bildirim süreleri; "[doldurulacak]" boşluklar.

## Plugin bağlamı

Bu beceri `sade-hukuk-dili` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
