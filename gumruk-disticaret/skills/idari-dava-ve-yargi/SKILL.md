---
name: idari-dava-ve-yargi
description: "İdari itiraz tüketildikten sonra gümrük uyuşmazlığını vergi/idare mahkemesine taşımak gerektiğinde; görev-yetki, dava türü, süreler ve yürütmenin durdurulmasını planlamak için kullanılır."
---

# İdari Dava ve Yargı Yolu

## Görev
Gümrük ek tahakkuk ve ceza kararlarına karşı idari itiraz tüketildikten sonra açılacak iptal/tam yargı davasını planlamak; görevli mahkeme, dava türü, süreler ve yürütmenin durdurulması ile kanun yollarını doğru kurgulamak.

## Soğuk başlangıç (intake)
- İdari itiraz reddedildi mi; ret kararı/zımni ret tarihi nedir?
- Uyuşmazlık esas olarak vergisel (ek tahakkuk, vergi cezası) mi yoksa salt idari işlem mi?
- Dava açma süresi içinde miyiz; tahsilat işlemi (ödeme emri) başladı mı?
- Tahsilatı durdurmak için yürütmenin durdurulması ve teminat gerekli mi?

## Denetim şeması
1. Görev: Gümrük vergileri ve bunlara bağlı cezalardan doğan uyuşmazlıklar vergi mahkemesinin görev alanındadır; vergiyle ilgisi olmayan salt idari işlemler idare mahkemesinde görülür. Doğru görevli mahkeme dava şartıdır.
2. Yetki: Kural olarak işlemi/tahakkuku yapan gümrük idaresinin bulunduğu yer mahkemesi yetkilidir (İYUK m.37 vd. çerçevesinde).
3. Dava türü: Ek tahakkuk/cezanın iptali için iptal davası; ödenmiş tutarın iadesi veya zarar için tam yargı davası açılır (İYUK m.2).
4. Süre: İdari itirazın reddinin (veya zımni reddin) tebliğinden itibaren İYUK m.7 süresi içinde (vergi mahkemesinde 30 gün) dava açılır. Sürenin doğru başlangıç anı (ret tebliği/zımni ret) titizlikle saptanır.
5. Yürütmenin durdurulması: Tahsilatı durdurmak için İYUK m.27 uyarınca YD talep edilir; teminat ve telafisi güç zarar koşulları değerlendirilir.
6. İspat ve deliller: Beyanname, fatura, menşe/kıymet belgeleri, idari işlem dosyası ve gerekirse bilirkişi/ekspertiz; ispat yükü dağılımı esasa göre kurulur.
7. Kanun yolları: İlk derece kararına karşı istinaf (BİM), istinaf üzerine temyiz (Danıştay) yolları ve süreleri gözetilir.
8. Ara sonuç: Görevli/yetkili mahkeme, dava türü, süre ve YD stratejisi netleşir; dava dilekçesi iskeleti hazırlanır.

## Çıktı modülleri
- Görev-yetki-süre-YD karar tablosu
- İptal/tam yargı dava dilekçesi taslağı [doldurulacak alanlarla]
- Delil dizini ve ispat yükü planı

## Plugin bağlamı

Bu beceri `gumruk-disticaret` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
