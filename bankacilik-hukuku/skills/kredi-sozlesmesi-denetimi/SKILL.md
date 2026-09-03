---
name: kredi-sozlesmesi-denetimi
description: "Genel kredi sözleşmesi, tüketici/konut kredisi veya ticari kredi metnini emredici hükümler, genel işlem koşulu ve haksız şart açısından madde madde denetlemek, geçersiz/yazılmamış sayılan kayıtları tespit etmek gerektiğinde kullanılır."
---

# Kredi Sözleşmesi ve Genel Kredi Sözleşmesi Denetimi

## Görev
Bir kredi sözleşmesini (genel kredi sözleşmesi, tüketici kredisi, konut finansmanı veya ticari kredi) emredici hukuk, genel işlem koşulu denetimi ve haksız şart süzgecinden geçirerek geçerli, sakat ve yazılmamış sayılacak kayıtları ayırmak; risk ve müzakere noktalarını çıkarmak.

## Soğuk başlangıç (intake)
- Kredi türü: nakdi/gayrinakdi, rotatif genel kredi, taksitli tüketici kredisi, konut finansmanı, ticari işletme kredisi?
- Müşteri tüketici mi, tacir mi? Sözleşme matbu/standart mı, müzakere edilmiş mi?
- Faiz tipi: sabit/değişken; akdi ve temerrüt faizi oranları ne, bileşik faiz var mı?
- Talep edilen masraf/komisyon/sigorta kalemleri neler; teminat yapısı (kefalet/ipotek/rehin) nasıl?

## Denetim şeması
1. **Standart koşul tespiti**: Sözleşme tek tarafça hazırlanıp dayatılmışsa genel işlem koşulu denetimine tabidir (TBK m.20-25). Diğer tarafın menfaatine aykırı, beklenmeyen, dürüstlüğe aykırı kayıtlar yazılmamış sayılır (TBK m.21-22); değiştirme yasağı (TBK m.24) ve aleyhe yorum (TBK m.23) uygulanır.
2. **Tüketici ise haksız şart denetimi**: TKHK m.5 ve Haksız Şartlar Yönetmeliği uyarınca dürüstlüğe aykırı, dengesizlik yaratan şartlar kesin hükümsüzdür. TKHK m.22-31 emredici hükümleri (sözleşmenin yazılı şekli, ön bilgilendirme, cayma hakkı 14 gün, erken ödeme indirimi) karşılanmış mı?
3. **Faiz ve eklentiler**: Akdi faiz oranı, temerrüt faizi (TBK m.120 — sözleşmede kararlaştırılmamışsa kanuni temerrüt faizi), bileşik faiz yasağı ve TTK m.8-9 istisnaları kontrol edilir. Tüketici kredisinde değişken faizde tavan/referans şartları (TKHK m.25) aranır. Haksız komisyon/masraf kalemleri iadeye tabidir.
4. **Teminat zinciri**: Kefalet varsa TBK m.583 (yazılı şekil, azami miktar-tarih el yazısı şartı) ve m.584 (eşin rızası) sağlanmış mı; sağlanmamışsa kefalet geçersizdir. İpotek/rehinde tesis usulü ayrıca denetlenir.
5. **Muacceliyet ve fesih kayıtları**: Tek taksit temerrüdüyle tüm borcun muaccel olması koşulu tüketici kredisinde TKHK m.27 sınırlamasına (en az iki taksit, 30 gün önel) tabidir. Ara sonuç olarak her kayıt için geçerli/sakat/yazılmamış nitelendirmesi yap.

## Çıktı modülleri
- Madde madde risk tablosu (geçerli / yazılmamış sayılır / hükümsüz / müzakere).
- Önerilen redline ve alternatif lafızlar.
- İade/itiraz konusu faiz-masraf kalemleri listesi.

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
