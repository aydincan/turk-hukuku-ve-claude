---
name: idari-para-cezasi-denetim-semasi
description: "Bir idari para cezası kararının yetki, şekil, unsur ve miktar yönünden hukuka uygunluğunu adım adım denetlemek; cezanın iptali veya kaldırılması için elverişli gerekçeleri çıkarmak gerektiğinde kullanılır."
---

# İdari Para Cezası Denetim Şeması

## Görev
Önündeki idari para cezası kararını yetki-şekil-unsur-miktar başlıklarıyla denetleyip iptal/kaldırma gerekçelerini ve başvuru stratejisini ortaya koymak.

## Soğuk başlangıç (intake)
- Cezayı veren idare, dayanak madde ve fiil tarihi nedir?
- Ceza maktu mu nispi mi; tutar nasıl hesaplanmış?
- Tutanak/karar tebliğ edildi mi, tarih nedir?
- Tutanakta tanık, tespit yöntemi (cihaz, kayıt) ve ölçütler gösterilmiş mi?

## Denetim şeması
1. **Yetki:** Kararı veren organ 5326 m.22 ve özel kanun uyarınca yetkili mi? Yetkisiz makamın verdiği ceza sakattır.
2. **Şekil ve tebligat:** Karar gerekçeli mi, başvuru yolu/süre gösterilmiş mi (5326 m.25); tebligat 7201 sayılı Kanuna uygun mu? Usulsüz tebligat süreyi başlatmaz.
3. **Maddi unsur — kabahatin gerçekleşmesi:** Fiilin özel kanundaki kabahat tanımına birebir uyup uymadığını altla. Tipiklik yoksa ceza verilemez (5326 m.4).
4. **Manevi unsur:** Kabahatler kural olarak kast veya taksirle işlenebilir (5326 m.9). Failin kusuru aranır; mücbir sebep/zorunluluk değerlendirilir.
5. **Miktar ve takdir (5326 m.17):** Nispi cezada matrah/oran doğru mu; maktu cezada alt-üst sınır içinde takdir ölçütleri (m.17/2 — haksızlığın ağırlığı, kusur, ekonomik durum) gösterilmiş mi? Ölçütsüz/gerekçesiz takdir denetime açıktır.
6. **Zamanaşımı:** Soruşturma zamanaşımı (5326 m.20) ve yerine getirme zamanaşımı (m.21) dolmuş mu? Resen dikkate alınır; ceza düşer.
7. **Peşin ödeme indirimi (5326 m.17/6):** Tebliğden itibaren süresinde ödemede 1/4 indirim hakkı; başvuru hakkını saklı tutarak ödeme stratejisi tartılır.

İspat yükü kural olarak idarededir; tutanak aksi ispatlanana kadar geçerli sayılan bir delildir ancak çürütülebilir.

## Çıktı modülleri
- Denetim kontrol listesi (yetki/şekil/unsur/miktar/zamanaşımı).
- İptal-kaldırma gerekçe taslağı.
- Peşin ödeme vs. başvuru karar matrisi.

## Plugin bağlamı

Bu beceri `kabahatler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
