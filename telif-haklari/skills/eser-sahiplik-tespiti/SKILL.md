---
name: eser-sahiplik-tespiti
description: "Bir fikir veya sanat ürününün FSEK anlamında eser olup olmadığını, türünü ve hak sahibinin kim olduğunu belirlemek gerektiğinde; korumanın eşiğini, hususiyet ölçütünü ve sahiplik karinelerini değerlendirmek için kullanılır."
---

# Eser Niteliği ve Sahipliğin Tespiti

## Görev
Somut ürünün FSEK m.1/B ve m.2-6 anlamında korunan bir eser olup olmadığını, hangi türe girdiğini ve hak sahibinin kim olduğunu tespit etmek; aktif husumetin temelini kurmak.

## Soğuk başlangıç (intake)
- Ürün nedir (yazılım, fotoğraf, müzik, logo, makale, mimari proje, veri tabanı)?
- Kim, ne zaman, hangi koşullarda (hizmet/sipariş/serbest) meydana getirdi?
- Birden çok kişi katkı verdi mi; iş sözleşmesi/eser sözleşmesi var mı?
- Daha önce kamuya açıklanmış/yayımlanmış mı; üzerinde isim/işaret var mı?

## Denetim şeması
1. Tür eşleştirme: Ürün FSEK m.2 (ilim-edebiyat, yazılım dâhil), m.3 (musiki), m.4 (güzel sanat), m.5 (sinema) veya m.6 (işlenme/derleme) sayımına giriyor mu? Numerus clausus geçerlidir; sayıma girmeyen ürün eser olarak korunmaz.
2. Hususiyet (sübjektif unsur): Ürün "sahibinin hususiyetini" taşıyor mu (m.1/B-a)? Salt emek/yatırım yetmez; bağımsız yaratıcı seçim aranır. Fikirler, yöntemler, veriler tek başına korunmaz — koruma ifade biçimine bağlıdır.
3. Şekil verme/algılanabilirlik: Düşünce, dış dünyada algılanabilir biçime kavuşmuş mu? Sırf zihindeki tasarım korunmaz.
4. Sahiplik: Kural olarak eseri meydana getiren gerçek kişi sahiptir (m.8). İştirak hâlinde (ayrılmaz bütün) m.9; müşterek eserde m.10. Sahiplik karinesi: nüsha üzerindeki ad veya umuma arzdaki açıklama (m.11-12). Çalışan/memur eserinde mali hak kullanımı kural olarak işverene aittir (m.18/2), aksi sözleşme saklıdır.
5. Ara sonuç: Eser + tür + sahip belirlenir; eser değilse koruma reddi, sınai hak (6769 SMK) veya haksız rekabet (TTK m.54 vd.) alternatifi değerlendirilir.

İspat yükü: eser ve sahiplik iddiasını ileri sürende (HMK m.190); karine lehine olan tarafın işi kolaylaşır.

## Çıktı modülleri
- Eser/sahiplik analiz notu (tür, hususiyet gerekçesi, sahip ve dayanak madde).
- Sahiplik karinesi ve aktif husumet değerlendirmesi.
- Eser sayılmama hâlinde alternatif koruma yolları listesi.

## Plugin bağlamı

Bu beceri `telif-haklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
