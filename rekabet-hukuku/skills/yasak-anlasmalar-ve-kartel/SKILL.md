---
name: yasak-anlasmalar-ve-kartel
description: "Fiyat tespiti, bölge/müşteri paylaşımı, ihalede danışıklılık, bilgi paylaşımı veya teşebbüs birliği kararı gibi rekabeti sınırlayıcı koordinasyon iddialarını 4054 m.4 çerçevesinde değerlendirmek istendiğinde kullanılır."
---

# Yasak Anlaşmalar, Uyumlu Eylem ve Kartel (m.4)

## Görev
Teşebbüsler arası bir anlaşma, uyumlu eylem veya teşebbüs birliği kararının 4054 m.4 kapsamında rekabeti sınırlayıp sınırlamadığını; amaç mı yoksa etki bakımından mı ihlal oluşturduğunu ve muafiyet ihtimalini değerlendirmek.

## Soğuk başlangıç (intake)
- Taraflar yatay (rakip) mı, dikey (sağlayıcı-alıcı) mı?
- Koordinasyon konusu: fiyat, miktar, pazar/müşteri paylaşımı, ihale, ortak satınalma, bilgi değişimi?
- Yazılı bir anlaşma mı var, yoksa paralel davranış/temas mı söz konusu?
- Bir dernek/birlik kararı veya tavsiyesi var mı?

## Denetim şeması
1. **Çoklu irade unsuru (m.4)** — anlaşma, uyumlu eylem veya teşebbüs birliği kararı tespit edilir. Uyumlu eylemde doğrudan irade beyanı aranmaz; bilinçli paralellik + rasyonel açıklama yokluğu yeterli olabilir. Uyumlu eylem karinesi piyasa koşullarına dayalı ispatı kolaylaştırır.
2. **Rekabeti sınırlama** — açık/sert ihlaller (kartel: fiyat tespiti, bölge-müşteri paylaşımı, arz kısıtlama, ihalede danışıklı teklif) **amaç bakımından** ihlaldir; ayrıca etki analizi gerekmez. Diğer kısıtlamalarda ilgili pazarda fiili/olası etki gösterilmelidir.
3. **Dikey ilişki süzgeci** — dikey anlaşmalarda Dikey Anlaşmalara İlişkin Grup Muafiyeti Tebliği'ne (2002/2) bakılır; pazar payı eşiği aşılmıyor ve ağır kısıtlama (yeniden satış fiyatının tespiti vb.) yoksa grup muafiyeti uygulanır.
4. **De minimis** — De Minimis Tebliği kapsamında pazar payı eşiklerinin altında ve açık ihlal niteliği taşımayan anlaşmalar soruşturma dışı bırakılabilir; kartel buna dâhil değildir.
5. **Muafiyet (m.5)** — grup muafiyeti dışında kalan anlaşmada dört şart birlikte aranır; ispat yükü teşebbüstedir.
6. **Yaptırım ve pişmanlık** — kartel ihlalinde ciro üzerinden idari para cezası (m.16); Pişmanlık (Kartel) Yönetmeliği ile ilk başvurana ceza muafiyeti/indirimi imkânı; özel hukukta üç kat tazminat (m.57-58).

## Çıktı modülleri
- Anlaşma/eylem nitelendirmesi ve amaç-etki ayrımı notu.
- Grup muafiyeti / de minimis / bireysel muafiyet kontrol listesi.
- Risk ve ceza tahmini; pişmanlık başvurusu uygunluk değerlendirmesi.
- Delil zayıflık/güçlülük haritası ve doğrulanacak Kurul kararı atıfları `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `rekabet-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
