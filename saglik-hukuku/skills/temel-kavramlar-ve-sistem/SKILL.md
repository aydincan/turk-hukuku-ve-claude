---
name: temel-kavramlar-ve-sistem
description: "Sağlık hukukunda ilk vasıflandırma için kullanılır; hekim-hasta ilişkisinin sözleşmesel mi idari mi olduğunu, hangi sorumluluk rejiminin ve yargı kolunun devreye gireceğini belirler."
---

# Temel Kavramlar ve Sistematik

## Görev
Olayın hangi sorumluluk eksenine ve yargı koluna düştüğünü baştan doğru saptamak. Yanlış vasıflandırma görev-yetki, zamanaşımı ve ispat yükünü baştan bozar.

## Soğuk başlangıç (intake)
1. Müdahale nerede yapıldı: kamu hastanesi mi, özel hastane mi, muayenehane mi?
2. Talep eden hasta/yakını mı, hekim/hastane mi, sigorta mı?
3. Olay teşhis/tedavi/ameliyat/ilaç/onam hangi aşamada?
4. Zarar ne (ölüm, yaralanma, kalıcı sakatlık, sadece manevi)?
5. Olay tarihi ve dava/şikâyet açılmış mı?

## Denetim şeması
1. **İlişkinin niteliği**: Özel hastane/muayenehane ise ilişki kural olarak TBK m.502 vd. vekâlet sözleşmesidir; estetik/protez gibi sonucun vaat edildiği işlerde eser sözleşmesi (TBK m.470 vd.) tartışılır. Kamu hastanesinde ilişki idaridir; sorumluluk hizmet kusuruna dayanır.
2. **Yargı kolu**: Özel sağlık kuruluşu → adli yargı (tüketici/asliye hukuk). Kamu hastanesi → idari yargı, tam yargı davası (İYUK m.12-13). Hekime karşı kişisel dava 3359 Ek m.18 nedeniyle kural olarak idareye yöneltilir; rücu ayrı işler.
3. **Sorumluluk ekseni**: Hukuki (sözleşme TBK m.112 / haksız fiil TBK m.49), cezai (TCK m.85-89 taksir), idari/disiplin (1219, 663 KHK). Eksenler birikebilir.
4. **Özen ölçütü**: Hekim sonucu değil tıbbın gereği özeni borçlanır (TBK m.506/f.3 — benzer uzmandan beklenen özen). Ara sonuç: kusur var mı sorusuna geçilir.
5. **İspat yükü**: Kusuru kural olarak davacı ispatlar; aydınlatma ve onamın varlığını ise hekim/hastane ispatlar (TMK m.6 istisnası).

## Çıktı modülleri
- İlişki ve yargı kolu tespiti tablosu
- Uygulanacak sorumluluk eksenleri listesi
- Bir sonraki adım önerisi (hangi alt-beceriye geçilecek)
- Belirsizlik/eksik bilgi notu

## Plugin bağlamı

Bu beceri `saglik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
