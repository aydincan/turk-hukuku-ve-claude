---
name: ictihat-arama-ve-degerlendirme
description: "Bir hukuki görüşü yargı kararlarıyla desteklemek ya da güncel içtihat eğilimini saptamak gerektiğinde; karara ulaşma, bağlayıcılık derecesini tartma ve emsal olarak kullanma için kullanılır."
---

# İçtihat Arama ve Değerlendirme

## Görev
Bir hukuki sorunun yargı kararlarıyla nasıl çözüldüğünü doğrulanabilir kaynaklardan tespit etmek, kararın bağlayıcılık/ikna değerini tartmak ve emsal olarak güvenli biçimde kullanmak.

## Soğuk başlangıç (intake)
- Aranan ilke nedir; hangi kanun maddesi etrafında dönüyor?
- Hangi yargı kolu (Yargıtay/Danıştay/AYM/BAM-BİM) ve hangi daire ilgili?
- Lehe mi, aleyhe mi karar arıyoruz; karşı içtihat var mı?
- Karar güncel mi; sonradan değişen mevzuat/içtihat var mı?

## Denetim şeması
1. **Kaynaktan arama** — Resmî bankalar: karararama.yargitay.gov.tr, karararama.danistay.gov.tr, kararlarbilgibankasi.anayasa.gov.tr. Karar metni görülmeden künye yazılmaz; **karar numarası asla model hafızasından uydurulmaz.**
2. **Bağlayıcılık derecesi** — (a) İçtihadı Birleştirme Kararları: benzer konularda mahkemeleri bağlar, en yüksek değerdedir. (b) AYM kararları (norm denetimi ve bireysel başvuru): bağlayıcı (Anayasa m.153). (c) Daire/Genel Kurul kararları: emsal/ikna edici, kural olarak bağlamaz ama yerleşik içtihat ağırlık taşır. (d) BAM/BİM kararları: bölgesel emsal değeri.
3. **Karar okuma** — Olay örgüsünü (vakıa) eldeki olayla karşılaştır; benzemiyorsa karar emsal olmaz. *Ratio decidendi* (bağlayıcı gerekçe) ile *obiter dictum* (geçer söz) ayrılır. Karşı oy ayrıca not edilir.
4. **Güncellik denetimi** — Karardan sonra kanun değişti mi, içtihat birleştirme/değişikliği oldu mu, AYM iptal etti mi? Eski içtihat güncel mevzuata sözcü kılınmaz.
5. **Çelişkili içtihat** — Daireler arası çelişki varsa hiyerarşi (HGK, İBK) ve tarih gözetilir; eğilim tek cümlede dürüstçe özetlenir, lehe karar seçilip aleyhe karar gizlenmez.

## Çıktı modülleri
- Aranan ilke + arama sorgusu (banka adıyla).
- Karar künyesi şablonu: Mahkeme/Daire, E. .../..., K. .../..., T. gg.aa.yyyy `[doğrulanacak]`.
- Bağlayıcılık ve güncellik notu.
- Olay benzerliği ve ratio/obiter ayrımı.

## Plugin bağlamı

Bu beceri `hukuk-metodolojisi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
