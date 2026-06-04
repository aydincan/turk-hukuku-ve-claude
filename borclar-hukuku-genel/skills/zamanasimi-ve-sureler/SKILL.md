---
name: zamanasimi-ve-sureler
description: "Bir alacağın zamanaşımına uğrayıp uğramadığı, sürenin başlangıcı, kesilmesi-durması ve def'i olarak ileri sürülmesi söz konusu olduğunda kullanılır."
---

# Zamanaşımı ve Süreler

## Görev
Alacağa uygulanacak zamanaşımı süresini, başlangıcını, kesilme/durma hâllerini saptamak ve def'i olarak doğru zamanda ileri sürülmesini sağlamak.

## Soğuk başlangıç (intake)
- Alacağın türü ne (genel sözleşme alacağı, dönemsel edim, özel kanun alacağı)?
- Alacak ne zaman muaccel oldu (sürenin başlangıcı)?
- Arada dava, icra takibi, ikrar veya başka kesen işlem oldu mu?
- Tarafların biri tacir/şirket mi; özel süre öngören kanun var mı?

## Denetim şeması
1. Genel süre: TBK m.146 — kanunda aksi öngörülmedikçe her alacak 10 yıllık zamanaşımına tabidir.
2. Beş yıllık süre: m.147 — kira bedelleri, anapara faizleri, dönemsel edimler; vekâlet/komisyon/eser sözleşmesinden doğan bazı alacaklar; serbest meslek ve esnaf alacakları. Liste dikkatle uygulanmalı.
3. Başlangıç: m.149 — alacağın muaccel olduğu an. Kesin vade yoksa muacceliyet için ihtar gerekebilir.
4. Kesilme: m.154 — borçlunun ikrarı (taksit, faiz ödeme, rehin/kefil verme), dava/def'i, icra takibi, iflas masasına başvuru; kesilmeyle yeni süre işlemeye başlar (m.156).
5. Durma: m.153 — belirli kişisel ilişkiler ve hukuki engeller süresince durur; engel kalkınca kaldığı yerden işler.
6. Sonuç ve usul: m.161 — zamanaşımından önceden feragat edilemez; hâkim resen dikkate alamaz, mutlaka def'i olarak ileri sürülmelidir (HMK çerçevesinde cevap dilekçesi/ilk fırsatta). Zamanaşımına uğramış borç eksik borçtur; ifa edilirse geri istenemez.
7. İspat yükü: Süreyi ve başlangıcı zamanaşımını ileri süren; kesilme/durmayı buna dayanan taraf ispatlar.

## Çıktı modülleri
- Süre hesap tablosu (başlangıç, kesilme, kalan süre).
- Zamanaşımı def'i metni taslağı (usule uygun aşama uyarısıyla).
- Karşı tarafça kesilme iddiasına savunma notu.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
