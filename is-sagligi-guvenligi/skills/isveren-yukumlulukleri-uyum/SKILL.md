---
name: isveren-yukumlulukleri-uyum
description: "Bir işyerinin 6331 sayılı Kanun kapsamındaki önleme, organizasyon, eğitim ve dokümantasyon yükümlülüklerine uyumunu denetlemek ve uyum boşluklarını çıkarmak için kullanılır."
---

# İşveren Yükümlülükleri ve Uyum Denetimi

## Görev
İşverenin 6331 m.4 vd. yükümlülüklerine uyumunu sistematik olarak denetlemek; eksikleri, idari ceza riskini ve düzeltici eylemleri raporlamak. Hem proaktif uyum hem de kaza sonrası savunma için temel oluşturur.

## Soğuk başlangıç (intake)
- Tehlike sınıfı ve çalışan sayısı; işyeri tek mi, çok lokasyonlu mu?
- İş güvenliği uzmanı/işyeri hekimi hizmeti var mı (kendi bünyesi mi, OSGB mi)?
- Risk değerlendirmesi, acil durum planı, eğitim ve muayene kayıtları mevcut ve güncel mi?
- Alt işveren/geçici iş ilişkisi var mı?

## Denetim şeması
1. **Genel yükümlülük (m.4):** İşveren mesleki risklerin önlenmesi, eğitim ve bilgilendirme, organizasyon ve gerekli araç-gereci sağlamakla yükümlü; risklerden kaçınma, kaynağında önleme, ikame ve toplu korumaya öncelik ilkeleri (m.5) altlanır.
2. **İSG organizasyonu (m.6-8):** Tehlike sınıfı ve çalışan sayısına göre iş güvenliği uzmanı ve işyeri hekimi görevlendirme zorunluluğu; bunların görev, yetki ve süreleri.
3. **Risk değerlendirmesi (m.10):** Yapılmış mı, güncel mi, kaza/değişiklik sonrası yenilenmiş mi? Yokluğu ağır ihlaldir.
4. **Acil durumlar (m.11-12):** Acil durum planı, yangın/tahliye, ilkyardım, destek elemanı atamaları.
5. **Bilgilendirme/eğitim/gözetim (m.16-17, m.15):** İşe giriş ve periyodik muayeneler, belgelendirilmiş İSG eğitimleri, çalışana risk bilgisi.
6. **Katılım yapıları (m.18, m.20, m.22):** Çalışan görüşü, çalışan temsilcisi, 50+ çalışanlı işyerinde İSG kurulu.
7. **İspat yükü:** Uyumun ve önlemlerin ispatı işverende; her yükümlülük için tarih/imza içeren belge aranır. **Ara sonuç:** Her madde için uyumlu / eksik / belgesiz işaretle.

## Çıktı modülleri
- Madde bazlı uyum kontrol listesi (durum + dayanak belge + eksik).
- İdari para cezası risk tablosu (m.26 atfıyla).
- Önceliklendirilmiş düzeltici eylem planı.

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
