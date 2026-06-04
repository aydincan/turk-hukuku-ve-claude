---
name: zaman-yer-bakimindan-uygulama
description: "Kanunların zaman bakımından uygulanması (lehe kanun) ile yer bakımından uygulanması (Türkiye'de/yurt dışında işlenen suçlar) sorunlarını çözmek gerektiğinde kullanılır."
---

# Zaman ve Yer Bakımından Uygulama

## Görev
Hangi ceza normunun zaman (lehe kanun) ve yer (mülkilik/şahsilik) bakımından uygulanacağını belirlemek; özellikle suç tarihi ile karar tarihi arasında değişen mevzuatta lehe hükmü saptamak.

## Soğuk başlangıç (intake)
- Suç tarihi ile karar/inceleme tarihi arasında ilgili norm değişti mi?
- Suç Türkiye'de mi, yurt dışında mı işlendi; fail ve mağdurun vatandaşlığı?
- İnfaz rejimini etkileyen bir değişiklik var mı?
- Suç birden çok ülkede mi gerçekleşti (hareket/netice farklı yerlerde mi)?

## Denetim şeması
1. **Kanunilik (m.2):** İşlendiği zaman kanunda suç sayılmayan fiil cezalandırılamaz; aleyhe kıyas ve geriye yürüme yasaktır.
2. **Lehe kanun (m.7/1-2):** Suçun işlendiği ve sonraki zaman dilimlerindeki normlar arasında failin lehine olan uygulanır; kesinleşmiş hükümlerde dahi infazı ve sonuçlarını etkileyen lehe değişiklik gözetilir. Ara sonuç: hangi metin failin lehine?
3. **Karşılaştırma yöntemi:** Lehe tespit soyut değil, somut olaya uygulanan sonuç üzerinden yapılır; karma uygulama yapılmaz, bir bütün olarak lehe olan metin seçilir.
4. **Mülkilik (m.8):** Türkiye'de işlenen suçlarda Türk kanunu uygulanır; hareket veya netice Türkiye'de gerçekleşmişse suç Türkiye'de işlenmiş sayılır.
5. **Yurt dışında işlenen suçlar (m.9-13):** Vatandaş (m.11) ve yabancı (m.12) tarafından işlenen suçlar, koruma ve evrensellik ilkeleri (m.13); yabancı ülkede mahkûmiyetin etkisi ve non bis in idem (m.9).
6. **Cezadan mahsup (m.16):** Yurt dışında gözaltı/tutukluluk/hükümlülük sürelerinin mahsubu.

## Çıktı modülleri
- Lehe kanun karşılaştırma tablosu (eski/yeni metin, somut sonuç).
- Yer bakımından uygulama yetki analizi.
- Mahsup ve non bis in idem notu.
- Eksik bilgi ve `[doğrulanacak]` içtihat ihtiyacı.

## Plugin bağlamı

Bu beceri `ceza-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
