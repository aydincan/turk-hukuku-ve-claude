---
name: dava-usul-gorev-yetki
description: "İş kazası tazminatı, SGK rücuu, idari ceza itirazı ve ceza yargılaması gibi farklı yolların görevli-yetkili mercilerini, dava şartlarını ve usul yolunu belirlemek için kullanılır."
---

# İSG Uyuşmazlıklarında Dava, Görev ve Yetki

## Görev
İSG kaynaklı her uyuşmazlığı doğru yargı koluna ve mercie yönlendirmek; görev, yetki, dava şartı (özellikle arabuluculuk) ve usul yolunu netleştirmek.

## Soğuk başlangıç (intake)
- Talep türü: işçi/hak sahibi tazminatı mı, SGK rücuu mu, idari ceza itirazı mı, ceza soruşturması mı?
- Taraflar kim; alt işveren-asıl işveren birlikte mi davalı?
- Olayın ve tebligatın tarihleri (süre ve zamanaşımı için)?
- Arabuluculuğa başvuruldu mu (işçilik alacağı/işe iade dava şartı)?

## Denetim şeması
1. **İş kazası tazminatı:** Görevli mahkeme iş mahkemesidir (7036 sayılı Kanun); yetki kural olarak davalının yerleşim yeri ile işin/işyerinin bulunduğu yer mahkemesi. İşçinin işverenden tazminat talebinde **dava şartı arabuluculuk** uygulanır; ancak iş kazasından kaynaklanan maddi-manevi tazminat ve rücu davaları arabuluculuk dava şartının istisnasıdır (doğrudan dava açılır) — bu istisnayı her dosyada güncel mevzuatla doğrula.
2. **SGK rücu davası:** Görevli mahkeme iş mahkemesi; davacı SGK, davalı kusurlu işveren/üçüncü kişi.
3. **İdari para cezası:** Adli yargı — sulh ceza hâkimliğine itiraz (5326 m.27), idari yargı değil. Bu ayrım sık karıştırılır; yanlış mercie başvuru süre kaybına yol açar.
4. **Ceza yargılaması:** Taksirle öldürme/yaralama (TCK m.85-89) için asliye ceza/ağır ceza; şikâyet ve uzlaşma rejimi suç tipine göre değişir.
5. **Dava şartı ve süre denetimi:** Husumet (asıl işveren-alt işveren birlikte), ehliyet, harç ve süreler. **Ara sonuç:** Her talep için merci-yol-süre üçlüsünü tablola; mevzuata dayalı doğrula.

## Çıktı modülleri
- Talep türü → görevli/yetkili merci → usul yolu tablosu.
- Dava şartı (arabuluculuk) ve istisna notu.
- Husumet ve taraf teşkili kontrol listesi.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
