---
name: ictihat-doktrin-degerlendirmesi
description: "Mütalaadaki hukuki görüşü Yargıtay/Danıştay/AYM içtihadı ve doktrinle desteklemek, içtihat eğilimini ve istikrar durumunu değerlendirmek gerektiğinde kullanılır; katı atıf hijyeniyle çalışır."
---

# İçtihat ve Doktrin Değerlendirmesi

## Görev
Mütalaadaki hukuki kanaati yerleşik içtihat ve doktrinle desteklemek; içtihat eğilimini, varsa görüş ayrılıklarını ve içtihadı birleştirme kararlarını tespit etmek. İçtihat hâkimi bağlamasa da uygulamadaki gerçek eğilimi gösterir; mütalaanın gerçekçiliğini bu sağlar.

## Soğuk başlangıç (intake)
- Hangi alt soru için içtihat aranıyor?
- Konu hangi mahkeme/dairenin görev alanında? (Yargıtay HD/CD, Danıştay dava dairesi, AYM, BAM)
- İçtihadı birleştirme kararı veya AYM/AİHM kararı konuyu doğrudan etkiliyor mu?
- Doktrinde tartışmalı/çoğunluk-azınlık görüşü var mı?

## Denetim şeması
1. Doğru kaynak seçimi: Konuya göre karararama.yargitay.gov.tr, karararama.danistay.gov.tr veya kararlarbilgibankasi.anayasa.gov.tr; mülga/yürürlükteki mevzuat dönemine dikkat.
2. ATIF HİJYENİ (mutlak kural): Hiçbir esas/karar numarası hatırlanarak yazılmaz. Karara dayanılacaksa mahkeme + daire + esas/karar no + tarih kaynaktan doğrulanır. Doğrulanmamış her künye `[doğrulanacak]` ile işaretlenir; sahte numara asla üretilmez. Doğrulanamıyorsa ilkesel atıf yapılır ("yerleşik Yargıtay içtihadına göre... [karararama.yargitay.gov.tr üzerinden doğrulanmalı]").
3. İçtihat eğilimi tespiti: Tek karar değil eğilim aranır; istikrarlı mı, daireler arası çelişki var mı, içtihadı birleştirme kararı (İBK) konuyu bağlayıcı şekilde çözmüş mü?
4. Hiyerarşi: AYM bireysel başvuru ve norm denetimi kararları ile AİHM kararları temel hak boyutunda üstün ağırlıklıdır; İBK Yargıtay daireleri için bağlayıcıdır.
5. Doktrin kullanımı: Yazar-eser-sayfa ile; çoğunluk ve azınlık görüşü ayrılır; mütalaa hangi görüşü neden benimsediğini gerekçelendirir.
6. Ara sonuç: Destekleyici içtihat/doktrin + karşı yöndeki görüş + bunların mütalaadaki sonuca etkisi.

## Çıktı modülleri
- İlkesel içtihat değerlendirmesi (eğilim + istikrar notu)
- Doğrulanacak künye listesi (`[doğrulanacak]` işaretli)
- Doktrin görüş tablosu (çoğunluk/azınlık)
- Arama kaynağı ve sorgu önerisi

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
