---
name: cezai-sart-ve-tazminat-on-belirleme
description: "Cezai şart, götürü tazminat, gecikme cezası ve dönme cezası maddelerinin türünü, geçerliliğini ve fahişliğini değerlendirmek gerektiğinde kullanılır."
---

# Cezai Şart ve Götürü Tazminat Denetimi

## Görev
Cezai şart/götürü tazminat kayıtlarının türünü (seçimlik, ifaya ekli, dönme cezası), geçerliliğini ve fahiş olup olmadığını belirlemek; müvekkil lehine dengeli lafzı kurmak.

## Soğuk başlangıç (intake)
- Ceza hangi ihlale bağlı (gecikme mi, hiç ifa etmeme mi, dönme mi)?
- Müvekkil cezayı ödeyecek taraf mı, talep edecek taraf mı?
- Taraflar tacir mi (TTK m.22 indirim sınırı)?
- Ceza yanında ayrıca tazminat ve aynen ifa talep ediliyor mu?

## Denetim şeması
1. **Tür tespiti**: TBK m.179 — (f.1) seçimlik cezai şart (ya ifa ya ceza), (f.2) ifaya ekli ceza (hem ifa hem ceza), (f.3) dönme cezası/cayma akçesi. Lafız hangisini kurduğu yoruma açıksa m.179'un karinesi uygulanır.
2. **Asıl borca bağlılık**: TBK m.182/f.1 — asıl borç geçersizse ceza da istenemez; ceza asıl borçtan fazla olsa bile kural olarak istenebilir ama (f.3) fahiş ceza hâkimce indirilir.
3. **Fahişlik indirimi**: TBK m.182/f.3 — hâkim aşırı cezayı indirir; bu yetki **emredicidir**, sözleşmeyle bertaraf edilemez. İstisna: tacir, ticari işinde TTK m.22 uyarınca fahişlik def'inden yararlanamaz (ancak ahlaka aykırı/ekonomik yıkım hâli saklı).
4. **Zarar şartı**: Cezai şart için alacaklının zarara uğraması şart değildir (m.180/f.1). Zarar cezayı aşarsa fark TBK m.180/f.2 uyarınca ispatla istenir.
5. **Denge testi**: Tek taraflı ceza, müvekkil aleyhine ağır ceza, ölçülemez tetikleyici işaretlenir; karşılıklılık ve tavan önerilir.
6. **İspat/usul**: İhlali ve cezanın muacceliyetini alacaklı ispatlar; temerrüt cezasında borçlunun temerrüde düşürülmesi (TBK m.117) aranabilir.

## Çıktı modülleri
- Cezai şart tür/geçerlilik/fahişlik değerlendirme notu.
- Dengeli ceza lafzı (karşılıklı, tavanlı, net tetikleyicili) önerisi.
- Tacir-tüketici ayrımına göre indirim riski uyarısı.

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
