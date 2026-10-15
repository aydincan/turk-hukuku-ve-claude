---
name: meslektas-mahkeme-iliskileri
description: "Avukatın meslektaşlarına, karşı taraf vekiline, mahkemeye ve adli mercilere karşı davranış kuralları, mektuplaşma gizliliği ve dürüstlük yükümü söz konusu olduğunda kullanılır."
---

# Meslektaşlar Arası İlişkiler ve Mahkemeyle İletişim

## Görev
Avukatın meslektaşları, karşı taraf ve yargı mercileriyle ilişkilerinde uyması gereken
nezaket, dürüstlük ve gizlilik kurallarını somut olaya uygulamak.

## Soğuk başlangıç (intake)
1. Uyuşmazlık meslektaşla mı (karşı vekil, devir alınan dosya) yoksa mahkemeyle mi?
2. Karşı vekille yapılan sulh görüşmesi/yazışması gizli kaydıyla mı yürütüldü?
3. Mahkemeye/karşı tarafa yönelik bir beyan dürüstlük/saygı sınırında mı?
4. Devralınan dosyada önceki meslektaşın ücreti çözüldü mü?

## Denetim şeması
1. **Meslektaşa saygı ve dürüstlük.** Avukatlar birbirine ve mesleğe karşı dürüst ve saygılı
   davranmakla yükümlüdür (Av. K. m.34; TBB Meslek Kuralları m.5, m.11 vd.). Meslektaşı
   küçük düşüren beyan disiplin suçudur. Ara sonuç: beyan eleştiri mi, kişisel saldırı mı?
2. **Sulh görüşmesi gizliliği.** "Gizli/sulh amaçlı" kaydıyla yapılan yazışma ve görüşmeler,
   karşı tarafın muvafakati olmadan mahkemeye delil olarak sunulamaz (TBB Meslek Kuralları
   m.27). Bu kural müzakere serbestisini korur.
3. **Dosya devri ve önceki vekilin hakkı.** Bir işi başka avukattan devralan avukat, önceki
   meslektaşın ücret hakkı ve durumu konusunda meslek kurallarını gözetir (TBB Meslek
   Kuralları m.38); devir öncesi bilgilendirme beklenir.
4. **Mahkemeye karşı yükümlülük.** Avukat mahkemeye saygı gösterir, yanıltıcı beyandan
   kaçınır; usule uygun, doğru ve özenli savunma yapar (Av. K. m.34; HMK m.29 dürüstlük ve
   doğruyu söyleme yükümü). Duruşma düzenine ve hâkime saygı esastır.
5. **Yaptırım.** İhlaller disiplin sorumluluğu (m.135) doğurur; mahkemeye karşı taşkınlık
   ayrıca duruşma düzeni ve ilgili usul yaptırımlarını gündeme getirir.

## Çıktı modülleri
- Davranışın kural uygunluğu değerlendirmesi (meslektaş/mahkeme ekseninde).
- "Gizli/sulh amaçlı" yazışma şerhi şablonu.
- Dosya devir bilgilendirme yazısı taslağı.

## Plugin bağlamı

Bu beceri `avukatlik-meslek-kurallari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
