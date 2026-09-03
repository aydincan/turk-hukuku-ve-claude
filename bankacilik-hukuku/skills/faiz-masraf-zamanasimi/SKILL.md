---
name: faiz-masraf-zamanasimi
description: "Banka alacağında veya müşteri iade talebinde akdi/temerrüt/bileşik faiz, komisyon-masraf kalemleri ile uygulanacak zamanaşımı sürelerini ayrıştırıp hesap denetimi yapmak gerektiğinde kullanılır."
---

# Faiz, Komisyon Hesabı ve Zamanaşımı Analizi

## Görev
Bir bankacılık alacağında veya iade talebinde faiz ve eklenti kalemlerini ayrıştırmak, hesabı denetlemek ve doğru zamanaşımı süresini belirlemek; aşan/dayanaksız kalemleri ve zamanaşımına uğramış talepleri işaretlemek.

## Soğuk başlangıç (intake)
- Talep yönü: banka tahsilatı mı, müşteri iade/itiraz talebi mi?
- Faiz tipi: akdi faiz, temerrüt faizi, bileşik faiz; oran ve dönem nedir?
- Hesap kalemleri: dosya masrafı, komisyon, hesap işletim, sigorta, ekspertiz?
- İlişki ticari mi tüketici mi; alacağın doğum ve son işlem tarihleri neler?

## Denetim şeması
1. **Faiz türü ayrımı**: Akdi faiz sözleşmeyle, temerrüt faizi TBK m.120 ile (kararlaştırılmamışsa kanuni oran) belirlenir. Adi işlerde bileşik faiz yasaktır; ticari işlerde TTK m.8 sınırlı istisna ve cari hesapta TTK m.89-101 özel rejim uygulanır. Tüketici işleminde aşırı/dengesiz faiz haksız şart denetimine tabidir.
2. **Eklenti kalemleri**: Dosya masrafı/komisyon gibi kalemler ancak gerçek maliyet ve açık onaya dayanıyorsa geçerlidir; aksi halde tüketici lehine iadeye konu olur (TKHK m.4, m.5). Her kalem ayrı dayanak ister.
3. **Hesap denetimi**: Tahakkuk dönemleri, faiz başlangıç tarihi, kapital-faiz ayrımı ve mükerrer/çifte tahakkuk kontrol edilir; bilirkişi hesabıyla karşılaştırılır.
4. **Zamanaşımı**: Genel sözleşmesel alacakta TBK m.146 (10 yıl); faiz ve dönemsel edimlerde TBK m.147 (5 yıl); kambiyo senetlerinde TTK'nın özel kısa süreleri; haksız fiil unsurunda TBK m.72. İade talebinde sebepsiz zenginleşme süreleri (TBK m.82 — 2 ve 10 yıl) ayrıca değerlendirilir. Zamanaşımının kesilmesi/durması (TBK m.153-154) kontrol edilir.
5. **Ara sonuç**: Geçerli kalemler, iadeye/itiraza konu kalemler ve zamanaşımına uğramış talepler ayrı listelenir; net talep tutarı yazılır.

## Çıktı modülleri
- Kalem kalem faiz/masraf denetim tablosu.
- Zamanaşımı haritası (her talep için süre ve başlangıç).
- Düzeltilmiş alacak/iade hesap özeti ve itiraz noktaları.

## Plugin bağlamı

Bu beceri `bankacilik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
