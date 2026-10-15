---
name: risk-yonetimi-uyum-savunma-stratejisi
description: "Şirket ve yöneticiler için ekonomik suç riskinin haritalanması, etkin pişmanlık-uzlaşma-kamu davasının ertelenmesi gibi seçeneklerin tartılması, kurum içi uyum (MASAK/SPK/vergi) zafiyetlerinin giderilmesi ve genel savunma kurgusu gerektiğinde kullanılır."
---

# Kurumsal Ceza Riski, Uyum ve Savunma Stratejisi

## Görev
Şirket ve yöneticilerin ekonomik suç riskini bütüncül haritalamak; soruşturma öncesi uyum tedbirleri ile soruşturma/kovuşturma aşamasındaki savunma ve hafifletme seçeneklerini tartmak.

## Soğuk başlangıç (intake)
- Risk hangi başlıkta? (aklama/MASAK, vergi, sermaye piyasası, dolandırıcılık, görev suçları)
- Henüz soruşturma yok mu, var mı, kovuşturmaya mı dönüştü?
- Şirket içinde sorumluluğu kim taşıyor (imza yetkisi, görev dağılımı)?
- Etkin pişmanlık/iade/ödeme penceresi açık mı?

## Denetim şeması
1. **Risk haritası**: Her suç tipi için (aklama TCK m.282/5549, vergi VUK m.359, SPK m.106-107, dolandırıcılık m.158, zimmet/rüşvet m.247/252) failin sıfatı, fiil, manevi unsur ve elkoyma/müsadere riski ayrı satırda değerlendirilir.
2. **Tüzel kişi-gerçek kişi ayrımı**: Tüzel kişiye ceza verilmez (TCK m.20/2); risk gerçek kişi yöneticide yoğunlaşır. Görev dağılımı, imza sirküleri ve karar defterleri sorumluluğu kime bağladığını gösterir — savunmada görevin devri/fiili durum ileri sürülür.
3. **Önleyici uyum**: MASAK uyum programı (yükümlüler için), vergi uyumu (e-fatura/karşıt inceleme disiplini), SPK içsel bilgi/işlem yasakları politikası; ihlal tespit edilince düzeltici adım ve gönüllü bildirim seçenekleri tartılır.
4. **Hafifletme seçenekleri**: Etkin pişmanlık (zimmette m.248, rüşvette m.254, malvarlığı suçlarında m.168, aklamada m.282/6), vergi pişmanlığı (VUK m.371) ve ödeme; suç tipine göre zaman penceresi ve indirim oranı farklıdır. Erken iade/ödeme genelde en güçlü kozdur.
5. **Savunma kurgusu**: Suç tipinin bir unsurunu (kast yokluğu, hile yokluğu, öncül suç eksikliği, mütalaa şartı eksikliği) hedef alan ana savunma ekseni seçilir; usul itirazları (görev, yetki, delil yasağı, iddianame iadesi) paralel hazırlanır.
6. **Ara sonuç**: Risk derecesi, sorumluluk taşıyıcısı, uyum boşluğu ve en uygun hafifletme/savunma hattı netleşir.

## Çıktı modülleri
- Suç tipi bazlı risk matrisi
- Sorumluluk (yönetici/imza) haritası
- Uyum boşluğu ve düzeltici eylem planı
- Etkin pişmanlık/ödeme senaryo karşılaştırması
- Ana savunma ekseni ve usul itirazları notu

## Plugin bağlamı

Bu beceri `ekonomik-ceza` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
