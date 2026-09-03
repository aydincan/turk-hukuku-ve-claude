---
name: bankacilik-temel-kavramlar
description: "Bankacılık uyuşmazlığının kamusal düzenleme katmanı mı yoksa banka-müşteri özel hukuk ilişkisi mi olduğunu ayırmak, uygulanacak kanunu (5411, TBK, TKHK, TTK) ve mahkeme/merci yolunu doğru seçmek gerektiğinde kullanılır."
---

# Bankacılık Hukuku Temel Kavramlar ve Sistematik

## Görev
Önündeki bankacılık sorununun hangi hukuki katmana ve ilişki tipine ait olduğunu belirlemek, uygulanacak normu ve doğru merci/yargı yolunu sabitlemek. Bu, sonraki tüm denetimin altyapısıdır.

## Soğuk başlangıç (intake)
- Müvekkil hangi sıfatta: banka, kredi müşterisi, kefil, mevduat sahibi, kart hamili, tüketici mi?
- İlişki tipi nedir: kredi, mevduat/katılım fonu, teminat (kefalet/ipotek/rehin), havale/EFT, kiralık kasa, banka/kredi kartı?
- Müşteri tüketici mi (gerçek kişi, ticari/mesleki amaç dışı) yoksa ticari işletme mi? Bu, TKHK ile TTK rejimi arasında seçimi belirler.
- Sorun bir BDDK işlemi/yaptırımı mı (idari yargı), yoksa sözleşmesel/icrai uyuşmazlık mı (adli yargı)?

## Denetim şeması
1. **Katman ayrımı**: Düzenleyici-denetleyici sorun mu? Bankanın kuruluşu, faaliyet izni, sermaye yeterliliği, kredi sınırları (5411 m.48-54), banka sırrı yükümlülüğü (5411 m.73), TMSF/mevduat sigortası (5411 m.63) ve BDDK idari yaptırımları (5411 m.146 vd.) düzenleyici katmandır; bunlara karşı yol İYUK (2577) gereği idari yargıdır. Banka-müşteri sözleşmesi ise özel hukuk katmanıdır.
2. **İlişki tipini normla eşle**: Mevduat → TBK karz/usulsüz tevdi hükümleri ve 5411 m.60 fon kabul tekeli; kredi → genel kredi sözleşmesi (TBK genel hükümler) veya tüketici kredisi (TKHK m.22 vd.); teminat → kefalet (TBK m.581 vd.), ipotek/rehin (TMK/İİK); kart → 5464; çek → 5941 ve TTK.
3. **Tüketici/ticari süzgeci**: Karşı taraf tüketici ise TKHK m.5 haksız şart denetimi ve m.22 vd. emredici hükümleri devreye girer; uyuşmazlık tüketici hakem heyeti/tüketici mahkemesine gider. Ticari ise asliye ticaret mahkemesi görevli olup 7155 (TTK m.5/A) uyarınca dava şartı arabuluculuk uygulanır.
4. **Ara sonuç**: Uygulanacak kanun, görevli mahkeme/merci, zorunlu ön şart (arabuluculuk/hakem heyeti) ve ispat yükünün kimde olduğunu yaz. İspat yükü kural olarak iddia edene (TMK m.6, HMK m.190) aittir; banka kayıtlarının ibrazı bankadan istenir.
5. **İstisna kontrolü**: Karma sözleşmeler (örn. tüketici kefaleti) ve hem idari hem adli boyutu olan dosyalarda her iki yolu ayrı değerlendir.

## Çıktı modülleri
- İlişki-tipi ve uygulanacak-norm haritası (tablo).
- Görev-yetki ve zorunlu ön şart tespiti.
- Sonraki adım için doğru uzman beceriye yönlendirme notu.

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
