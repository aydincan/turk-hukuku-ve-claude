---
name: kurumsal-siber-guvenlik-yukumlulukleri
description: "Bir kurumun siber güvenlik ve veri güvenliği yükümlülüklerini (KVKK m.12 teknik-idari tedbirler, sektörel düzenlemeler, politika ve sözleşme mimarisi) değerlendirmek ve uyum boşluğunu çıkarmak gerektiğinde kullanılır."
---

# Kurumsal Siber Güvenlik Yükümlülükleri ve Uyum

## Görev
Kurumun siber/veri güvenliği hukuki yükümlülüklerini saptamak; politika, teknik-idari tedbir ve sözleşme mimarisindeki boşlukları çıkarıp uyum yol haritası kurmak.

## Soğuk başlangıç (intake)
1. Kurumun faaliyeti ve sektörü ne? (banka/ödeme, sağlık, telekom, e-ticaret, genel?)
2. Hangi ve ne kadar kişisel veri işleniyor, işleyen/bulut kullanılıyor mu?
3. Mevcut politika, olay müdahale planı, log yönetimi var mı?
4. Tetikleyici ne? (denetim, ihlal sonrası, yatırım/due diligence, proaktif uyum?)

## Denetim şeması
1. **Genel veri güvenliği (KVKK m.12).** Veri sorumlusu, kişisel verilerin hukuka aykırı işlenmesini ve erişilmesini önlemek ile muhafazasını sağlamak üzere uygun **teknik ve idari tedbirleri** almakla yükümlüdür; işleyen ile müştereken sorumludur. Tedbirlerin alındığını ispat yükü kurumdadır. Eksiklik m.18 idari para cezası ve ihlal halinde ağırlaştırılmış sorumluluk doğurur.
2. **Sektörel katman.** Bankacılık/ödeme (BDDK, 6493 ve bilgi sistemleri düzenlemeleri), elektronik haberleşme (BTK/5809 ve ağ güvenliği), kritik altyapı düzenlemeleri ve varsa kurumun tabi olduğu özel rejim eklenir. TS ISO/IEC 27001 ve ilgili standartlar uyum ölçütü olarak referans alınır (sözleşme/idari beklenti düzeyinde).
3. **Belge ve süreç denetimi.** Veri envanteri, saklama-imha politikası, erişim yönetimi, log kayıtları, olay müdahale ve iş sürekliliği planı, sızma testi/zafiyet yönetimi, farkındalık eğitimleri kontrol edilir.
4. **Sözleşme mimarisi.** Veri işleyen sözleşmeleri, gizlilik ve güvenlik taahhütleri, SLA/güvenlik ekleri, sorumluluk sınırlamaları (TBK çerçevesinde geçerlilik), yurt dışı aktarım şartları denetlenir.
5. **Ara sonuç.** Yükümlülük-mevcut durum karşılaştırmasıyla **uyum boşluğu** ve öncelik/risk sıralaması çıkarılır.

## Çıktı modülleri
- Yükümlülük envanteri (genel KVKK + sektörel + standart).
- Uyum boşluğu raporu (boşluk, risk, öncelik, aksiyon).
- Politika/sözleşme eki şablon önerileri.

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
