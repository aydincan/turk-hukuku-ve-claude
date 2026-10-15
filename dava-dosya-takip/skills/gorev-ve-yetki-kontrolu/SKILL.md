---
name: gorev-ve-yetki-kontrolu
description: "Davanın doğru görevli ve yetkili mahkemede açılıp açılmadığını, görevsizlik-yetkisizlik veya gönderme riskini denetlemek gerektiğinde kullan."
---

# Görev ve Yetki Kontrolü

## Görev
Dosyanın görevli mahkeme (dava konusuna göre) ve yetkili mahkeme (yer itibarıyla) bakımından doğru yerde olup olmadığını denetlemek; görevsizlik/yetkisizlik ile zaman kaybı riskini erken yakalamak.

## Soğuk başlangıç (intake)
- Dava konusu ve türü ne (alacak, tazminat, tüketici, iş, ticari, aile)?
- Dava hangi mahkemede ve hangi yerde açılmış?
- Taraflar arasında yetki sözleşmesi veya tahkim şartı var mı?
- Kesin yetki gerektiren bir dava türü söz konusu mu?

## Denetim şeması
1. Görev: HMK m.1 gereği görev kamu düzenindendir ve re'sen incelenir. Genel görevli asliye hukuk (HMK m.2) ile özel görevli mahkemeleri ayırt et: tüketici mahkemesi (6502 TKHK m.73), iş mahkemesi (7036 m.5), ticari dava-asliye ticaret (TTK m.4-5), aile mahkemesi, FSHM. Yanlış görevli mahkeme → görevsizlik kararı ve gönderme.
2. Yetki: genel yetki davalının yerleşim yeri (HMK m.6); özel/kesin yetki halleri (taşınmazda taşınmazın yeri HMK m.12; sözleşmede ifa yeri HMK m.10; haksız fiilde HMK m.16). Kesin yetki re'sen gözetilir.
3. Yetki sözleşmesi/tahkim: tacir-kamu tüzel kişisi arasında yetki sözleşmesi (HMK m.17) geçerli mi; tahkim şartı varsa tahkim ilk itirazı (HMK m.116) riski.
4. İtiraz zamanı: yetki ilk itirazdır, cevap süresinde ileri sürülmezse düşer (HMK m.116, m.117, m.19); görev her aşamada gözetilir.
5. Ara sonuç: görev/yetki uygun mu, değilse hangi mahkemeye gönderme ve süre etkisi. Mevzuat dışı varsayım yapılmaz.

## Çıktı modülleri
- Görev/yetki değerlendirme notu (doğru mahkeme + dayanak madde).
- Görevsizlik/yetkisizlik riski ve gönderme senaryosu.
- İtiraz süresi ve usul uyarısı.

## Plugin bağlamı

Bu beceri `dava-dosya-takip` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
