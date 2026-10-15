---
name: veri-ihlali-siber-olay-mudahale
description: "Yaşanan bir veri ihlali veya siber saldırı sonrası KVKK m.12 bildirim yükümlülüğü, kriz yönetimi ve hukuki müdahale adımlarını planlamak; bildirim sürelerini ve içeriklerini belirlemek gerektiğinde kullanılır."
---

# Veri İhlali ve Siber Olay Müdahalesi

## Görev
Gerçekleşmiş veya şüpheli bir veri ihlali/siber olayda hukuki müdahale akışını kurmak; KVKK bildirim yükümlülüklerini, içeriklerini ve eş zamanlı ceza/sözleşme adımlarını yönetmek.

## Soğuk başlangıç (intake)
1. Ne oldu ve ne zaman fark edildi? (sızıntı, fidye yazılımı, yetkisiz erişim?)
2. Hangi kişisel veriler ve kaç ilgili kişi etkilendi? (özel nitelikli veri var mı?)
3. Veri sorumlusu kim, yurt dışı aktarım/işleyen zinciri var mı?
4. Sistem hâlâ tehdit altında mı, loglar/imaj korundu mu?

## Denetim şeması
1. **Kapsam ve sınıflandırma.** Olayın KVKK m.12/5 anlamında bir "veri ihlali" (kişisel verilerin kanuni olmayan yollarla başkalarınca elde edilmesi) olup olmadığı belirlenir. İhlal yoksa salt güvenlik olayı olarak iç süreç işler.
2. **Bildirim yükümlülüğü (KVKK m.12/5).** Veri sorumlusu ihlali öğrendiği tarihten itibaren en kısa sürede Kurula bildirir; Kurul kararları uyarınca bu süre kural olarak **72 saat** olarak uygulanır. İlgili kişilere de makul en kısa sürede bildirim yapılır. Form ve içerik kvkk.gov.tr'deki ihlal bildirim usulüne göre hazırlanır (ihlalin niteliği, etkilenen veri/kişi sayısı, olası sonuçlar, alınan önlemler).
3. **Delil ve sistem güvenliği.** Adli bilişim için imaj/log korunur (bkz. dijital delil becerisi); müdahale ekibinin hareketleri kayda alınır. İz silmemek esastır.
4. **Ceza ekseni.** Fiil aynı zamanda TCK m.243-244 ve m.135-140 kapsamında suç olabilir; suç duyurusu seçeneği değerlendirilir. İspat yükü: KVKK uyumunda veri sorumlusu, m.12'deki teknik/idari tedbirleri aldığını ispatla yükümlüdür; aksi halde m.18 idari para cezası riski doğar.
5. **Sözleşme ve aktarım ekseni.** Veri işleyen/alt işleyen sözleşmeleri, yurt dışı aktarım şartları ve müşteri/iş ortağı bildirim yükümlülükleri kontrol edilir. **Ara sonuç:** Bildirim takvimi, sorumlu rolleri ve risk önceliklendirmesi netleştirilir.

## Çıktı modülleri
- 72 saatlik aksiyon takvimi ve sorumlu matrisi.
- Kurul ihlal bildirim formu taslağı ve ilgili kişi bilgilendirme metni.
- Ceza/sözleşme eksenli ek aksiyon listesi.

## Plugin bağlamı

Bu beceri `bilisim-hukuku-siber` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
