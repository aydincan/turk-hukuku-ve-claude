---
name: gorev-yetki-yargi-yolu
description: "Fikri-sınai bir davada hangi mahkemenin (FSHM, asliye hukuk, Ankara FSHM) görevli, hangi yerin yetkili olduğunu, hukuk-ceza-idari yol ayrımını ve TÜRKPATENT aleyhine dava merkezini belirlemek gerektiğinde kullanılır."
---

# Görev, Yetki ve Yargı Yolu

## Görev
Davayı doğru mahkemede, doğru yerde ve doğru yargı kolunda açmak; görevsizlik/yetkisizlik riskini ve TÜRKPATENT kararlarına karşı dava merkezini netleştirmek.

## Soğuk başlangıç (intake)
- Talep tecavüz/tazminat mı, hükümsüzlük mü, yoksa TÜRKPATENT (YİDK) kararının iptali mi?
- Karşı taraf gerçek/tüzel kişi mi, TÜRKPATENT mi?
- Tecavüz fiili nerede gerçekleşti veya etkisi nerede görüldü; davalının yerleşim yeri neresi?
- Davanın açılabileceği yerde ihtisas FSHM var mı?

## Denetim şeması
1. Görev: Fikri-sınai hukuk uyuşmazlıkları Fikrî ve Sınaî Haklar Hukuk Mahkemesi'nde görülür (SMK m.156/1; FSEK m.76). İhtisas mahkemesi bulunmayan yerde HSK'nın görevlendirdiği asliye hukuk mahkemesi FSHM sıfatıyla bakar; bu husus dilekçede belirtilir.
2. TÜRKPATENT kararları: Kurum kararlarının (YİDK) iptali ve Kurum aleyhine hükümsüzlük/sicil davaları münhasıran Ankara FSHM'de açılır (SMK m.156/2). İdari karara karşı süre kaçırılmamalı (SMK m.20-21 itiraz süreçleri tüketilmeli).
3. Yetki (tecavüz/tazminat): Hak sahibi davacı, kendi yerleşim yeri yahut hukuka aykırı fiilin gerçekleştiği veya etkilerinin görüldüğü yer mahkemesinde dava açabilir (SMK m.156/3). Tecavüz edenin açacağı davada genel yetki (HMK m.6) uygulanır.
4. Yargı kolu ayrımı: Tecavüz/tazminat/hükümsüzlük adli yargıdadır; ancak gümrük el koyma idari işlemine itiraz ve YİDK öncesi idari aşama farklı kanallardır. Ceza boyutu (SMK m.30 marka suçları, FSEK m.71-72) FSHM Ceza/asliye ceza yolundadır.
5. Ara sonuç: İspat yükü görevsizlik itirazında davalıya geçmez; görev kamu düzenindendir, re'sen gözetilir (HMK m.114/1-c). Yanlış mahkemede açılan davada görevsizlik/yetkisizlik üzerine HMK m.20 süresi izlenir.

## Çıktı modülleri
- Görev-yetki tespit notu (madde gerekçeli).
- TÜRKPATENT dava merkezi ve süre uyarısı.
- Yetki itirazı veya yetki sözleşmesi değerlendirmesi.

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
