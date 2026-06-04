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
