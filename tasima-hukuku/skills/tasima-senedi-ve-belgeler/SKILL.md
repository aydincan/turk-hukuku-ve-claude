---
name: tasima-senedi-ve-belgeler
description: "Taşıma senedi, CMR belgesi, irsaliye, teslim makbuzu gibi belgelerin düzenlenmesi, içeriği, ispat değeri ve gönderenin beyan sorumluluğunun değerlendirilmesi gerektiğinde kullanılır."
---

# Taşıma Senedi ve Taşıma Belgeleri

## Görev
Taşıma belgelerinin içerik, geçerlilik ve ispat değerini denetlemek; belgelerden doğan karine ve sorumlulukları (özellikle gönderenin beyanlarından doğan sorumluluk) tespit etmek.

## Soğuk başlangıç (intake)
1. Hangi belgeler düzenlendi: taşıma senedi, CMR belgesi, sevk irsaliyesi, teslim makbuzu?
2. Belgede zorunlu kayıtlar (taraflar, eşya cinsi/miktarı, ağırlık, varma yeri) tam mı?
3. Eşyanın durumu/ağırlığı hakkında taşıyıcı şerh (rezerv) koydu mu?
4. Gönderen tehlikeli madde/özel değer beyanında bulundu mu (TTK m.880, m.884)?

## Denetim şeması
1. **Senedin niteliği:** TTK m.856 — taşıma senedi düzenlenmesi tarafların isteğine bağlıdır; geçerlilik şartı değil ispat aracıdır. İçeriği m.856'da sayılır.
2. **İspat değeri/karineler:** TTK m.858 — kurallara uygun düzenlenen senet, sözleşmenin yapıldığına ve içeriğine karine teşkil eder; eşyanın senette yazılı durumda teslim alındığı varsayılır. Taşıyıcının şerhi bu karineyi kırar.
3. **Gönderenin sorumluluğu:** TTK m.864 — senetteki ve verilen bilgilerin doğruluğundan gönderen sorumludur; yanlış/eksik beyandan doğan zararı tazmin eder. CMR m.7.
4. **Tehlikeli eşya:** TTK m.868 — gönderen tehlikeli eşyanın niteliğini ve önlemleri bildirmekle yükümlüdür; bildirmezse doğan zarardan sorumlu olur.
5. **Değer/menfaat beyanı:** TTK m.880-881 — eşyanın değerinin veya teslim menfaatinin senede yazılması, sorumluluk sınırının (m.882) aşılmasını sağlar.
6. **Emre/nama yazılı belgeler:** Taşıma senedi emre yazılı düzenlenebilir; tasarruf hakkı ve devir bu çerçevede değerlendirilir.
7. **Ara sonuç:** Belgelerin doğurduğu karineler, ispat dağılımı ve gönderen-taşıyıcı sorumluluk paylaşımı.

## Çıktı modülleri
- Belge envanteri ve zorunlu kayıt eksiklik tablosu.
- Karine/şerh analizi (lehte-aleyhte ispat etkisi).
- Beyan sorumluluğu ve değer beyanının sınır üzerindeki etkisine ilişkin not.

## Plugin bağlamı

Bu beceri `tasima-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
