---
name: kullanmama-defi-ve-ispati
description: "Karşı taraf markayı uzun süredir kullanmıyorsa veya müvekkile karşı kullanmama itirazı/def'i ileri sürüldüyse; beş yıllık ciddi kullanım koşulu ve ispat yükünü m.9-m.19/2 üzerinden yönetmek için kullanılır."
---

# Kullanmama Def'i ve Kullanımın İspatı

## Görev
Markanın "kullan ya da kaybet" ilkesini işletmek: tescilden sonra beş yıl içinde Türkiye'de ciddi biçimde kullanılmayan markanın itiraz/dava dayanağı olmasını engellemek (m.19/2 def'i; iptal için m.26/1-a, m.9). İspat yükü kural olarak marka sahibindedir.

## Soğuk başlangıç (intake)
- Dayanak marka kaç yıldır tescilli (beş yıl doldu mu)?
- Hangi mal/hizmette kullanım iddia ediliyor?
- Kullanım Türkiye'de, ciddi ve tescil edildiği biçimde mi?
- Kullanmama için haklı sebep var mı (idari engel, ithalat yasağı)?

## Denetim şeması
1. **Beş yıllık süre.** Tescil tarihinden (veya son ciddi kullanımdan) itibaren kesintisiz beş yıl kullanmama aranır (m.9/1).
2. **Def'i hakkı (m.19/2).** Yayına itirazda, itiraz dayanağı marka beş yıldır tescilliyse başvuru sahibi kullanım ispatı isteyebilir; ispatlanamazsa itiraz o markaya dayanılarak reddedilir.
3. **Ciddi kullanım ölçütü.** Pazarda gerçek ticari amaçla, markanın esas işlevine uygun, somut ve süreklilik gösteren kullanım; sırf hakkı korumak için sembolik kullanım yeterli değildir.
4. **Kapsam.** Kullanım, tescilli mal/hizmetin hangileri için ispatlandıysa koruma o kapsamla sınırlanır; kısmî kullanmama kısmî iptal/etkisizlik doğurur.
5. **Ayırt ediciliği değiştirmeyen kullanım.** Markanın ayırt edici karakterini değiştirmeyen farklı unsurlarla kullanım da kullanım sayılır (m.9/2).
6. **Haklı sebep.** Marka sahibinin iradesi dışındaki engeller (ruhsat bekleme, ithalat yasağı) kullanmamayı mazur gösterebilir.

## Çıktı modülleri
- Beş yıllık süre ve kullanım dönemi cetveli.
- Ciddi kullanım delil listesi (fatura, katalog, reklam, ambalaj — tarihli).
- Def'i/iptal talebi taslağı ve ispat yükü notu.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
