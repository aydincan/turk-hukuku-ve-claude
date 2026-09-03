---
name: ifa-ve-ifa-engelleri
description: "Borcun gereği gibi ifa edilip edilmediği, alacaklının ifayı kabulden kaçındığı veya edimin sonradan imkânsızlaştığı durumlarda kullanılır."
---

# İfa, Alacaklı Temerrüdü ve İfa İmkânsızlığı

## Görev
Borcun ifa yeri, zamanı ve biçimi yönünden gereği gibi ifa edilip edilmediğini; alacaklı temerrüdü ve sonraki imkânsızlığın sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
- Borç muaccel mi; ifa zamanı ve yeri ne?
- Borçlu ifayı sundu mu; alacaklı kabul etti mi?
- Edim sonradan imkânsızlaştı mı; kimden kaynaklanan sebeple?
- Kısmi ifa, üçüncü kişi ifası veya ifa yerine edim söz konusu mu?

## Denetim şeması
1. İfa esasları: TBK m.83 vd. — bizzat ifa zorunluluğu istisnaları (m.83), kısmi ifanın reddi (m.84), ifa yeri (m.89: para borçları alacaklının yerleşim yerinde — götürülecek borç), ifa zamanı ve süreden önce ifa (m.96).
2. Mahsup/sıra: Birden çok borçta ifanın hangi borca sayılacağı (m.100-101); faiz ve masrafların önce mahsubu.
3. İspat ve makbuz: Borçlu ifayı ve makbuz/senet iadesini isteyebilir (m.103-105); senedin borçluda olması ödeme karinesi.
4. Alacaklı temerrüdü: m.106-108 — alacaklı haklı sebep olmaksızın ifayı veya hazırlık fiillerini yapmaktan kaçınırsa temerrüde düşer; borçlu tevdi (m.107), satış (m.108) veya sözleşmeden dönme yoluna gidebilir, hasar alacaklıya geçer.
5. Sonraki imkânsızlık: m.136 — borçluya yüklenemeyen sebeple imkânsızlaşma borcu sona erdirir; karşılıklı sözleşmede alınanın iadesi, alınmamışsa istemekten vazgeçme. Kısmi imkânsızlık m.137. Borçluya yüklenebilen imkânsızlık ise m.112 üzerinden tazminata dönüşür.
6. Aşırı ifa güçlüğü/uyarlama: m.138 — öngörülemeyen olağanüstü değişiklik dürüstlüğe aykırı hâle getirirse uyarlama, mümkün değilse dönme/fesih.
7. İspat yükü: İfayı borçlu, imkânsızlığın kusursuzluğunu yine borçlu ispatlar (m.136 ile m.112 birlikte).

## Çıktı modülleri
- İfa uygunluk ve muacceliyet analizi.
- Tevdi/ifa yerine edim veya uyarlama yol haritası.
- İmkânsızlık türü ve borç-tazminat geçişi şeması.

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
