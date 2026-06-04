---
name: kentsel-donusum-riskli-yapi
description: "6306 sayılı Kanun kapsamında riskli yapı/alan tespiti, tahliye ve yıktırma, malik kararı çoğunluğu ve dönüşüm uyuşmazlıkları gündeme geldiğinde; riskli yapı tespitine itiraz ve 2/3 çoğunluk süreci sorulduğunda kullanılır."
---

# Kentsel Dönüşüm ve Riskli Yapı (6306)

## Görev
6306 sayılı Kanun kapsamındaki riskli yapı/alan sürecini denetlemek; tespite itiraz, malik kararı ve tahliye-yıktırma adımlarında hukuki yolu kurmak.

## Soğuk başlangıç (intake)
- Riskli yapı tespiti mı, riskli/rezerv alan ilanı mı var?
- Tespit raporu hangi lisanslı kuruluşça düzenlendi, tebliğ tarihi ne?
- Maliklerin dönüşüm/anlaşma çoğunluğu sağlandı mı?
- Tahliye ya da yıktırma kararı çıktı mı, kira/taşınma yardımı talebi var mı?

## Denetim şeması
1. **Riskli yapı tespiti (6306 m.3)**: Tespit, Bakanlıkça lisanslandırılmış kuruluşlarca yapılır ve tapuya şerh edilir. Maliklere tebliğ edilir; teknik dayanağın ve usulün denetimi ilk adımdır.
2. **Tespite itiraz**: Riskli yapı tespitine, tebliğden itibaren kanunda öngörülen sürede (15 gün) idareye itiraz edilebilir; itiraz teknik heyetçe incelenir. İdari sürecin tüketilmesi sonraki dava için önemlidir.
3. **Tahliye ve yıktırma (m.5)**: Riskli yapı maliklerce tahliye/yıktırılmazsa idarece yıktırılır; süreler ve idari yaptırım kademeli işler. Tahliye işlemine karşı idari yargı yolu açıktır.
4. **Malik kararı çoğunluğu (m.6)**: Yıkılan yapının arsası üzerinde yapılacak uygulamada **maliklerin hisseleri çoğunluğu (en az 2/3) ile karar** alınır; karara katılmayan maliklerin hisseleri Bakanlık marifetiyle satışa konu olabilir. Çoğunluk hesabı ve azınlık malik hakları denetlenir.
5. **Yargı kolu ve uyuşmazlık**: Riskli yapı tespiti ve idari işlemler → idari yargı (iptal); malikler arası dönüşüm sözleşmesi, müteahhit ilişkisi → adli yargı. 6306 işlemlerinde yürütmenin durdurulmasına ilişkin özel sınırlamalar gözetilir.
6. **İspat ve ara sonuç**: Tespit raporu, statik veriler, malik kararı tutanakları, sözleşmeler delildir. Teknik dayanak/usul sakatsa tespitin iptali; çoğunluk veya azınlık hakkı ihlali varsa ilgili dava. Mülkiyet hakkı (Anayasa m.35) AYM denetimi açısından değerlendirilir; künyeler `[doğrulanacak]`.

## Çıktı modülleri
- Riskli yapı süreç kronolojisi.
- Tespit raporu/usul denetim notu.
- Malik çoğunluğu (2/3) ve azınlık hakkı analizi.
- Tespit/tahliye iptali veya dönüşüm sözleşmesi değerlendirme taslağı.

## Plugin bağlamı

Bu beceri `imar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
