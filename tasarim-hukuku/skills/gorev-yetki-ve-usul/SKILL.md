---
name: gorev-yetki-ve-usul
description: "Tasarım uyuşmazlıklarında görevli ve yetkili mahkemenin, idari/adli yol ayrımının ve dava şartlarının SMK m.156 ile HMK çerçevesinde belirlenmesi; doğru mahkemede doğru davanın açılması ve dava şartı arabuluculuk gibi ön koşulların kontrolü gerektiğinde kullanılır."
---

# Görev, Yetki ve Usul Haritası

## Görev
Tasarım uyuşmazlığını doğru mecraya yerleştirmek: görevli mahkeme, yetkili yer, idari yol (TÜRKPATENT/YİDD) ile adli yol ayrımı, dava şartları ve arabuluculuk ön koşulunu netleştirmek.

## Soğuk başlangıç (intake)
1. Uyuşmazlık türü nedir (tescil/itiraz idari süreci, hükümsüzlük, tecavüz, tazminat, devir)?
2. Tarafların yerleşim yeri ve tecavüzün/işlemin yapıldığı yer neresi?
3. Talep parasal mı (tazminat → ticari dava → arabuluculuk şartı olabilir)?
4. İlgili ilde FSHHM var mı, yoksa görevlendirilen asliye mi?

## Denetim şeması
1. Görevli mahkeme (SMK m.156/1): SMK'den doğan hukuk davalarında Fikrî ve Sınai Haklar Hukuk Mahkemesi görevlidir; bulunmayan yerlerde HSK'nin belirlediği asliye hukuk mahkemesi bu sıfatla bakar. Ceza boyutu için Fikrî ve Sınai Haklar Ceza Mahkemesi.
2. İdari/adli ayrımı: Tescil, yayın, itiraz ve YİDD kararları idari süreçtir; YİDD'nin nihai kararına karşı 2 ay içinde Ankara FSHHM'de iptal davası açılır (SMK m.67). Hükümsüzlük ve tecavüz ise doğrudan adli davadır.
3. Yetki (SMK m.156/3-5): Hak sahibinin açacağı davalarda davacının yerleşim yeri veya tecavüzün/fiilin işlendiği yahut etkilerinin görüldüğü yer mahkemesi yetkilidir; üçüncü kişilerin hak sahibine açacağı davalarda davalının (sicildeki) yerleşim yeri. TÜRKPATENT aleyhine davada Ankara mahkemeleri.
4. Dava şartı arabuluculuk: Konusu para olan ticari davalarda (TTK m.5/A, HMK çerçevesi) tazminat talepleri için dava şartı arabuluculuk işletilir; tecavüzün tespiti/men gibi taleplerle birlikte yapı kurulur. Hükümsüzlük gibi münhasıran mahkeme yetkisindeki talepler arabuluculuğa elverişli değildir.
5. Dava şartları ve süre: Görev resen incelenir (HMK m.114/1-c); zamanaşımı (tazminatta TBK m.72), tedbirde 2 haftalık esas dava süresi (HMK m.397) kontrol edilir.
6. Ara sonuç: Görevli/yetkili mahkeme, idari mi adli mi, arabuluculuk gerekip gerekmediği net yazılır.

## Çıktı modülleri
- Yol haritası tablosu (idari/adli, görevli mahkeme, yetkili yer).
- Dava şartı kontrol listesi (görev, yetki, arabuluculuk, süre).
- Talep türüne göre arabuluculuk elverişlilik notu.

## Plugin bağlamı

Bu beceri `tasarim-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
