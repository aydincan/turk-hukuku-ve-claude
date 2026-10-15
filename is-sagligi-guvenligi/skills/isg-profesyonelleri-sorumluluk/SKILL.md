---
name: isg-profesyonelleri-sorumluluk
description: "İş güvenliği uzmanı, işyeri hekimi ve OSGB'lerin görev, yetki ve hukuki-cezai sorumluluğunu, işverenle sorumluluk paylaşımını değerlendirmek için kullanılır."
---

# İSG Profesyonelleri ve OSGB Sorumluluğu

## Görev
İş güvenliği uzmanı, işyeri hekimi, diğer sağlık personeli ve ortak sağlık güvenlik birimlerinin (OSGB) görev-yetki sınırlarını ve hukuki/cezai sorumluluğunu; işverenle aralarındaki sorumluluk paylaşımını değerlendirmek.

## Soğuk başlangıç (intake)
- Hizmet işyerinin kendi profesyoneli mi, OSGB üzerinden mi sağlanıyor; sözleşme süresi ve atanan görevlendirme süresi ne?
- Uzmanın belge sınıfı (A/B/C) işyerinin tehlike sınıfına uygun mu?
- Kaza/ihlal öncesi uzman/hekim hangi yazılı uyarı, öneri ve tespitleri yaptı; onay defteri (İSG kaydı) işlendi mi?
- Müvekkil işveren mi, profesyonel mi, OSGB mi?

## Denetim şeması
1. **Görevlendirme zorunluluğu (6331 m.6-8):** Tehlike sınıfı ve çalışan sayısına göre uzman/hekim çalıştırma yükümlülüğü; belge sınıfı uyumu (çok tehlikelide (A), tehlikelide en az (B) vb.).
2. **Görev sınırı ve uyarı yükümlülüğü:** Uzman/hekim önleyici öneri ve tespitlerini yazılı bildirmekle yükümlüdür; işveren bu önerilere uymazsa, profesyonel durumu yetkili makama/işverene yazılı bildirerek sorumluluğunu sınırlayabilir. Yazılı uyarının varlığı sorumluluk paylaşımının ekseni.
3. **İşverenin asli sorumluluğu:** İSG hizmeti alınması veya profesyonel görevlendirilmesi, işverenin 6331 m.4 sorumluluğunu kaldırmaz; profesyonelin kusuru işverenin sorumluluğunu sona erdirmez (zincirleme/paylaşımlı sorumluluk).
4. **Cezai sorumluluk:** Kazada profesyonelin görevini gereği gibi yapmaması taksirle ölüm/yaralama (TCK m.85-89) bakımından bağımsız değerlendirilir; kusur dağılımı bilirkişiyle belirlenir.
5. **Sözleşmesel rücu:** İşveren ile OSGB/uzman arasında hizmet sözleşmesine dayalı iç rücu ilişkisi. **Ara sonuç:** Yazılı uyarı zinciri ve kusur dağılımına göre paylaşımı sabitle.

## Çıktı modülleri
- Görev-belge sınıfı uyum tablosu.
- Yazılı uyarı/öneri kronolojisi.
- Sorumluluk paylaşımı ve iç rücu değerlendirme notu.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
