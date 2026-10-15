---
name: ozel-hayat-aile-esitlik
description: "Özel hayatın ve aile yaşamının korunması, haberleşme ve konut gizliliği, kişisel veri, çevre etkisi ile ayrımcılık yasağı/eşitlik bağlamında müdahaleler iddia edildiğinde kullanılır."
---

# Özel Hayat, Aile ve Eşitlik

## Görev
m.20 (özel hayatın ve haberleşmenin gizliliği), m.21 (konut), aile yaşamı ve m.10 (eşitlik) ile m.17 manevi bütünlük kesişimindeki müdahaleleri değerlendirmek.

## Soğuk başlangıç (intake)
- Müdahale neye dokundu (özel yaşam, itibar, kişisel veri, aile birliği, haberleşme, konut)?
- Müdahale bir kamu işlemi mi, yoksa Devletin koruma yükümlülüğünü yerine getirmemesi mi?
- Ayrımcılık iddiası varsa hangi statüye dayalı ve karşılaştırma grubu kim?
- Müdahalenin kanuni dayanağı ve güttüğü amaç nedir?

## Denetim şeması
1. Uygulanabilirlik — m.20: özel hayat geniş yorumlanır; kişisel veriler, itibar, mesleki-sosyal kimlik, beden bütünlüğü dahildir. Aile yaşamı fiilî yakın bağları kapsar.
2. Negatif/pozitif yükümlülük — Devlet hem müdahaleden kaçınmalı hem de üçüncü kişilere karşı koruma sağlamalıdır (örn. işyerinde izleme, sağlık verisi, çevresel zarar).
3. Müdahale denetimi — m.13: kanunilik, meşru amaç, demokratik toplumda gereklilik ve ölçülülük. Usuli güvenceler (kişinin görüşünü sunması, etkili itiraz) ölçülülüğün parçasıdır.
4. Haberleşme ve konut — iletişimin dinlenmesi, arama-el koyma, konuta müdahale hâkim kararı ve sınırlı istisna şartlarına bağlıdır; usulsüz tedbir ihlal doğurur.
5. Eşitlik/ayrımcılık (m.10) — benzer durumdakilere farklı muamele, objektif ve makul gerekçeye dayanmıyorsa ve ölçüsüzse ayrımcılık oluşur; ayrımcılık genellikle başka bir hakla BAĞLANTILI incelenir. Cinsiyet, doğum, din, dil gibi şüpheli kategorilerde denetim sıkılaşır.

İspat yükü: müdahaleyi/farklı muameleyi başvurucu; haklılığı kamu makamı gösterir. Ayrımcılıkta ilk görünüş ispatından sonra yük yer değiştirebilir.

Ara sonuç: ihlal edilen hak ve varsa eşitlik bağlantısı.

## Çıktı modülleri
- Hak nitelendirmesi (özel hayat/aile/haberleşme/konut/eşitlik).
- Negatif/pozitif yükümlülük ve ölçülülük altlaması.
- Ayrımcılık karşılaştırma analizi.
- İlke kararlarına atıf [doğrulanacak].

## Plugin bağlamı

Bu beceri `anayasa-mahkemesi-bireysel-basvuru` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
