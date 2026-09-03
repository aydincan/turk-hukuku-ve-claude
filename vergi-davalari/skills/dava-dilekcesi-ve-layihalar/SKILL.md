---
name: dava-dilekcesi-ve-layihalar
description: "İYUK'a uygun vergi dava dilekçesi, cevaba cevap ve istinaf-temyiz dilekçelerinin yapısını kurup talep sonucunu asıl-ceza-faiz ekseninde doğru formüle etmek için kullanılır."
---

# Vergi Dava Dilekçesi ve Layihalar

## Görev
İYUK biçim ve içerik kurallarına uygun dava dilekçesi ve sonraki layihaları (cevaba cevap, istinaf, temyiz) üretmek; vakıa-hukuki sebep-talep sonucu mimarisini vergi uyuşmazlığına özgü olarak kurmak.

## Soğuk başlangıç (intake)
1. Dava konusu işlem ve tarafları kim (mükellef / vergi dairesi başkanlığı veya defterdarlık)?
2. İşlemin türü, tarihi ve tebliğ tarihi; talep edilen iptal kapsamı (asıl / ceza / faiz)?
3. YD talebi olacak mı; teminat gösterilecek mi?
4. Dayanak deliller neler (ihbarname, inceleme raporu, defterler, ödeme belgeleri)?

## Denetim şeması
1. **Biçim unsurları.** İYUK m.3 — dilekçede tarafların ad-unvan ve adresleri, dava konusu işlem ve tebliğ tarihi, olaylar, hukuki sebepler, talep sonucu ve varsa YD talebi yer alır. İYUK m.5 — her işlem için ayrı dava kuralı ve istisnaları (bağlantı) gözetilir.
2. **Husumet.** Dava, işlemi tesis eden idareye (ilgili Vergi Dairesi Başkanlığı / Defterdarlık) yöneltilir; doğru hasım belirlenir.
3. **Talep sonucu.** Vergi aslı, vergi ziyaı cezası, usulsüzlük cezası ve gecikme faizi/zammı ayrı kalemler halinde, tutar belirtilerek iptal talep edilir; kısmi iptal hedefleniyorsa miktar netleştirilir.
4. **Hukuki sebepler.** Her iptal sebebi ilgili madde ile altlanır (örn. re'sen tarh sebebinin yokluğu — VUK m.30; cezada kat hatası — VUK m.344; zamanaşımı — VUK m.114). İçtihat ilkesel atıfla anılır, künye `[doğrulanacak]` bırakılır.
5. **Süre ve harç.** İYUK m.7/m.58 süresine uygunluk dilekçe başında teyit edilir; harç ve posta gideri ile dilekçe ekleri (tebliğ alındısı, işlem örneği) listelenir. Yer tutucular `[doldurulacak]` biçiminde işaretlenir. Ara sonuç: dilekçenin reddini doğuracak şekil eksiği (İYUK m.15 ret sebepleri) kalmadığı kontrol edilir.
6. **Layiha zinciri.** Cevap dilekçesine karşı ikinci dilekçe (cevaba cevap) ve idarenin ikinci cevabı; istinaf (m.45) ve temyiz (m.46) dilekçelerinde bozma/kaldırma sebepleri ayrı başlıklanır.

## Çıktı modülleri
- Vergi dava dilekçesi tam iskeleti (başlık → vakıa → hukuki sebep → talep sonucu → YD → ekler).
- Talep sonucu kalem tablosu (asıl/ceza/faiz, tutar).
- İstinaf/temyiz dilekçesi şablonu.

## Plugin bağlamı

Bu beceri `vergi-davalari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
