---
name: altlama-subsumption-teknigi
description: "Maddi vakıayı hukuk kuralının soyut şartlarına tek tek yerleştirerek gerekçeli ara sonuç üretmek gerektiğinde kullanılır; mütalaanın hukuki değerlendirme bölümünün çekirdek yöntemidir."
---

# Altlama (Subsumption) Tekniği

## Görev
Hukuk kuralının her bir şartını (unsurunu) tek tek alıp somut vakıaya uygulamak ve "bu şart gerçekleşti / gerçekleşmedi" ara sonuçlarını gerekçeyle vermek. Altlama, mütalaayı keyfi kanaatten ayıran asıl yöntemdir: büyük önerme (kural) + küçük önerme (olay) → sonuç.

## Soğuk başlangıç (intake)
- Uygulanacak temel norm hangi madde? (Tam metni ve unsurları çıkarıldı mı?)
- Bu normun unsurları (şartları) nelerdir, kaç tane?
- Her unsur için elde hangi vakıa/delil var?
- Tanımlanması gereken belirsiz kavram var mı? (Ör. ağır kusur, basiretli tacir, dürüstlük)

## Denetim şeması
1. Kuralı unsurlarına ayır: Madde metni cümle cümle çözülür ve kümülatif/seçimlik şartlar listelenir. Örnek — haksız fiil (TBK m.49): (a) hukuka aykırı fiil, (b) kusur, (c) zarar, (d) illiyet bağı. Dördü birlikte aranır.
2. Her unsuru olaya uygula: Unsur → ilgili vakıa → gerçekleşip gerçekleşmediği. Belirsiz kavram varsa önce tanımlanır (içtihat/doktrin ölçütüyle), sonra olaya uygulanır.
3. İspat yükü kontrolü: Her unsuru kim ispatlamalı (TMK m.6, HMK m.190)? Karine veya ispat yükü tersine çevrilen haller (ör. TBK m.66 adam çalıştıranın sorumluluğunda kurtuluş beyyinesi, TBK m.112 ifa etmeme karinesi) ayrıca not edilir.
4. İstisna ve def'iler: Kuralın istisnaları, hukuka uygunluk sebepleri, zamanaşımı def'i gibi karşı argümanlar aynı titizlikle altlanır.
5. Ara sonuç birleştirme: Tüm unsurlar gerçekleşiyorsa hukuki sonuç doğar; bir unsur eksikse talep dayanaktan yoksundur. Çekişmeli unsurda koşullu sonuç ("X ispatlanırsa...") kurulur.
6. Karşıt görüş testi: Aynı vakıaya alternatif nitelendirme mümkün mü? (Ör. fiil hem haksız fiil hem sözleşmeye aykırılık — yarışma) tartışılır.

## Çıktı modülleri
- Unsur tablosu (unsur | olaydaki karşılığı | ispat yükü | ara sonuç)
- Belirsiz kavram tanımı ve uygulanışı
- Def'i/istisna değerlendirmesi
- Birleştirilmiş hukuki sonuç (koşullu varyantlarıyla)

## Plugin bağlamı

Bu beceri `hukuki-mutalaa` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
