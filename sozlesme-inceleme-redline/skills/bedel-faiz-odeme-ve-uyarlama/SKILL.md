---
name: bedel-faiz-odeme-ve-uyarlama
description: "Bedel belirleme, faiz, ödeme koşulları, mücbir sebep ve aşırı ifa güçlüğü uyarlama maddelerinin denetimi gerektiğinde kullanılır."
---

# Bedel, Faiz, Ödeme ve Uyarlama Şartları

## Görev
Bedel, faiz, ödeme takvimi, fiyat artış mekanizması, mücbir sebep ve uyarlama (hardship) maddelerini denetlemek; belirsizlikleri ve dengesizlikleri gidermek.

## Soğuk başlangıç (intake)
- Bedel sabit mi, endeksli mi, dövizli mi (kambiyo/yasak riski)?
- Temerrüt faizi oranı ve türü kararlaştırılmış mı?
- Mücbir sebep tanımı var mı; uyarlama/yeniden müzakere kaydı bulunuyor mu?
- Ödeme tetikleyicileri (milestone, teslim, kabul) net mi?

## Denetim şeması
1. **Bedel belirliliği**: Edim ve karşı edim belirli/belirlenebilir olmalı; "ayrıca anlaşılacaktır" gibi açık uçlu bedel uyuşmazlık doğurur. Endeks/artış formülü ölçülebilir yazılmalı.
2. **Faiz**: Temerrüt faizi kararlaştırılmamışsa kanuni faiz (TBK m.120, 3095 s.K.); ticari işlerde avans faizi/TTK rejimi. Sözleşmeyle kararlaştırılan faiz fahişse TBK m.120/f.2-3 ve dürüstlük denetimi; bileşik faiz yasağı (yalnız cari hesap/ticari ödünçte istisna).
3. **Para birimi**: Döviz/dövize endeksli bedellerde yürürlükteki kambiyo mevzuatı ve TBK m.99 (yabancı para borcu) kontrol edilir; yasak kapsamı `[doğrulanacak]` güncel mevzuattan teyit edilir.
4. **Mücbir sebep**: Tanım, sayılan haller (kapsayıcı/sınırlı), bildirim süresi, ispat ve sonuç (askı/fesih). Mücbir sebep ifa imkânsızlığına (TBK m.136) köprülenir.
5. **Uyarlama (hardship)**: TBK m.138 — sözleşme yapılırken öngörülemeyen olağanüstü durum ifayı aşırı güçleştirirse hâkimden uyarlama, mümkün değilse dönme/fesih istenebilir; bu hak emredici çekirdek taşır, sözleşmesel hardship klozu bunu somutlaştırır.
6. **İspat/usul**: Ödemeyi borçlu (TBK m.6/genel), temerrüdü ve faizi alacaklı ispatlar; makbuz/dekont düzeni önerilir.

## Çıktı modülleri
- Bedel-faiz-ödeme denetim notu ve belirsizlik listesi.
- Dengeli mücbir sebep + uyarlama (m.138) lafzı önerisi.
- Para birimi/kambiyo ve fahiş faiz riski uyarısı.

## Plugin bağlamı

Bu beceri `sozlesme-inceleme-redline` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
