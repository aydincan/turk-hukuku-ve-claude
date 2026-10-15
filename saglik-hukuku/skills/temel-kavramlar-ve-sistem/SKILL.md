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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
