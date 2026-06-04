---
name: mutalaa-dili-ve-uslubu
description: "Hukuki görüşün tarafsız, gerekçeli ve ikna edici biçimde yazılmasını, olasılık dilinin ve atıf düzeninin doğru kullanılmasını sağlamak gerektiğinde kullanılır; mütalaayı dava dilekçesi üslubundan ayırır."
---

# Mütalaa Dili ve Üslubu

## Görev
Mütalaa metnini analitik, dengeli ve ikna edici bir hukukçu diliyle kaleme almak; abartılı taraf-savunucu üsluptan ve sahte kesinlikten kaçınmak. Mütalaanın inandırıcılığı gerekçenin şeffaflığından gelir.

## Soğuk başlangıç (intake)
- Metin dava dosyasına mı girecek (HMK m.293 uzman görüşü), yoksa iç danışmanlık mı?
- Okuyucu hâkim/hukukçu mu, yoksa hukukçu olmayan müvekkil mi?
- İstenen uzunluk/derinlik seviyesi ne?
- Hassas/gizli bilgi içeriyor mu?

## Denetim şeması
1. Üslup seçimi: Dava içi uzman görüşünde tarafsız-bilimsel ton zorunludur; danışmanlık mütalaasında aleyhe senaryo açıkça tartılır. Her iki halde de "kazanırsınız" gibi kategorik vaatlerden kaçınılır.
2. Olasılık dili: Sonuçlar derecelendirilir — "kuvvetle muhtemel / tartışmalı / zayıf ihtimal / hâkimin takdirine bağlı". Belirsizlik gizlenmez, dürüstçe ifade edilir.
3. Gerekçe görünürlüğü: Her sonuç önermesi norm + altlama + (varsa) içtihada bağlanır; "kanaatimce" denip geçilmez, gerekçe yazılır.
4. Atıf düzeni: Mevzuat madde/fıkra/bent ile (ör. "TBK m.49/1", "HMK m.119/1-ğ"); içtihat künyesi doğrulanmadıysa `[doğrulanacak]`; doktrin yazar-eser-sayfa. Model hafızasından karar numarası yazılmaz.
5. Yapı disiplini: Başlıklandırma, numaralı alt sorular, ara sonuçların belirginleştirilmesi; uzun paragraflar yerine izlenebilir akış.
6. Yer tutucu disiplini: Eksik bilgi `[doldurulacak: ...]`, doğrulanacak künye `[doğrulanacak]` ile işaretlenir; uydurma veriyle boşluk kapatılmaz.

## Çıktı modülleri
- Üsluba uygun yazılmış değerlendirme metni
- Olasılık dili kontrol listesi
- Atıf formatı denetimi (mevzuat/içtihat/doktrin)
- Yer tutucu ve `[doğrulanacak]` envanteri

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
