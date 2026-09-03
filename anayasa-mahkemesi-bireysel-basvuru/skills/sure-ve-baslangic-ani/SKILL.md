---
name: sure-ve-baslangic-ani
description: "Otuz günlük başvuru süresinin ne zaman başladığı, tebliğ/öğrenme anı, mücbir sebep ve mazeretle eski hale getirme, sürenin kaçırılması halinde yapılabilecekler sorulduğunda kullanılır."
---

# Süreler ve Sürenin Başlangıcı

## Görev
Otuz günlük başvuru süresinin doğru başlangıç anını saptamak, hesabı yapmak ve süre aşımı/mazeret durumlarını değerlendirmek.

## Soğuk başlangıç (intake)
- Nihai (kesin) karar nedir ve başvurucuya ne zaman tebliğ edildi?
- Tebligat yapılmadıysa kararı fiilen ne zaman öğrendiniz, bunu neyle ispatlarsınız?
- Süreyi kaçırmaya yol açan bir mücbir sebep / ağır engel var mı?
- Bugün itibarıyla kaç gün geçti?

## Denetim şeması
1. Süre — 6216 m.47/5 ve İçtüzük m.64: bireysel başvurunun, başvuru yollarının tüketildiği tarihten; başvuru yolu öngörülmemişse ihlalin öğrenildiği tarihten itibaren OTUZ GÜN içinde yapılması gerekir.
2. Başlangıç anı — kural olarak nihai kararın başvurucuya TEBLİĞİ esastır. Tebligat yoksa fiilî öğrenme tarihi esas alınır; bu tarihin ispatı başvurucudadır.
3. Hesap — süre gün olarak hesaplanır; başlangıç günü hesaba katılmaz, son gün tatile rastlarsa ilk iş gününe uzar (genel usul ilkesi). Hak düşürücü niteliktedir.
4. Mazeret / eski hale getirme — m.47/5 son cümle ve İçtüzük: mücbir sebep veya ağır hastalık gibi haklı engel nedeniyle süre kaçırılmışsa, engelin kalkmasından itibaren onbeş gün içinde, mazereti belgeleyen delillerle başvuru yapılabilir; AYM mazeretin kabulüne karar verir.
5. Tedbir ihtiyacı — İçtüzük m.73: ciddi ve telafisi imkânsız zarar tehlikesi varsa, süreyle ayrıca tedbir talep edilir.

İspat yükü: öğrenme tarihi ve mazerete ilişkin belgeleri başvurucu sunar.

Ara sonuç: "süresinde / süre aşımı / mazeret yolu açık" tespiti, son başvuru tarihi.

## Çıktı modülleri
- Süre hesabı tablosu (nihai karar, tebliğ/öğrenme, son gün).
- Mazeret/eski hale getirme uygunluk notu.
- Süre aşımı halinde seçenekler ve riskler.
- Tedbir talebi gerekiyorsa hatırlatma.

## Plugin bağlamı

Bu beceri `anayasa-mahkemesi-bireysel-basvuru` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
