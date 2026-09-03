---
name: reklam-yasagi
description: "Avukatın web sitesi, sosyal medya, tabela, ilan, iş takipçiliği ve tanıtım faaliyetlerinin meslek kurallarına uygunluğu değerlendirildiğinde kullanılır."
---

# Reklam Yasağı ve Mesleki Tanıtım Sınırları

## Görev
Bir tanıtım/iletişim faaliyetinin reklam yasağı ve meslek kurallarına uygun olup olmadığını
saptamak; uyumlu hale getirmek.

## Soğuk başlangıç (intake)
1. Mecra ne (tabela, web sitesi, sosyal medya, gazete/ilan, rehber, arama motoru reklamı)?
2. İçerik hangi bilgileri veriyor ( unvan, uzmanlık iddiası, başarı/oran, fiyat, müvekkil adı)?
3. İş sağlama/aracı kullanma veya iş takipçiliği unsuru var mı?
4. Karşılaştırmalı/abartılı ifade veya müvekkil referansı içeriyor mu?

## Denetim şeması
1. **Yasağın temeli.** Avukat iş elde etmek için reklam sayılabilecek her türlü teşebbüs ve
   harekette bulunamaz (Av. K. m.55; TBB Avukatlık Meslek Kuralları m.7-8; TBB Reklam Yasağı
   Yönetmeliği). Amaç, mesleğin onuru ve haksız rekabetin önlenmesidir.
2. **İzin verilen bilgilendirme.** Ad-soyad, unvan, iletişim, çalışma alanları (uzmanlık
   "iddiası" değil bilgilendirme düzeyinde), büro bilgileri ölçülü biçimde verilebilir.
   Ara sonuç: içerik "bilgilendirme" sınırında mı, yoksa "iş celbi/reklam" düzeyine mi geçti?
3. **Yasak içerik kalıpları.** Başarı oranı/kazanılmış dava reklamı, müvekkil adı/işi ifşası
   (sır yükümü m.36 ile çakışır), karşılaştırmalı üstünlük, fiyat reklamı, arama motorunda
   meslektaş adına/kayırıcı anahtar kelime, panel/aracı yoluyla iş sağlama yasaktır.
4. **Sosyal medya ve web.** Mecraya özgü değil içeriğe özgü değerlendirilir; takipçi
   kazanmaya yönelik abartılı/teşvik edici paylaşım yasak kapsamına girer.
5. **Yaptırım.** İhlal disiplin suçudur (m.34, m.135); ayrıca haksız rekabet boyutu
   (TTK m.55 vd.) gündeme gelebilir.

## Çıktı modülleri
- İçerik bazında "uyumlu / düzeltilmeli / yasak" işaretlemesi.
- Uyumlu tabela/web/sosyal medya metni önerisi.
- Düzeltme ve risk notu.

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
