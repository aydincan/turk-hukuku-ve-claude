---
name: temel-kavramlar-ve-sistem
description: "Yapay zekâ içeren bir dosyayı katman (veri-KVKK, sözleşme, sorumluluk, fikri mülkiyet, sektörel), sistemin rolü (karar destek, tam otomatik karar, üretken model, profilleme) ve tarafların sıfatı eksenlerinde konumlandırıp doğru normu ve görevli mercii belirlemek gerektiğinde kullanılır."
---

# Yapay Zekâ Hukuku Temel Kavramlar ve Sistematik

## Görev
Yapay zekâ unsuru içeren dosyayı doğru hukuki katmana oturtmak; Türkiye'de yatay bir YZ kanunu bulunmadığını dikkate alarak uygulanacak norm setini (KVKK 6698, TBK 6098, FSEK/SMK, sektörel) ve görevli mercii hızlıca tespit ederek sonraki uzman becerilere giriş kapısını açmak.

## Soğuk başlangıç (intake)
1. Sistem ne yapıyor: karar destek mi, tam otomatik karar mı, üretken model (metin/görüntü) mü, profilleme/skorlama mı?
2. Müvekkilin sıfatı: model geliştiren/sağlayan, sistemi kullanan (deployer), veri sorumlusu/işleyen, zarar gören/ilgili kişi mi?
3. Coğrafi erişim: sistem AB'deki kişilere ürün/hizmet sunuyor mu (AB Tüzüğü/GDPR riski)?
4. Uyuşmazlık türü: veri/KVKK uyumu mu, sözleşmesel mi, tazminat mı, fikri mülkiyet mi, kamu işlemi mi?

## Denetim şeması
1. **Katman tespiti**: Kişisel veri işleniyorsa KVKK (m.4 ilkeler, m.5-6 şartlar) devrede; otomatik kararla aleyhe sonuç varsa m.11/1-g; sözleşmesel ilişki varsa TBK 6098; zarar varsa haksız fiil (TBK m.49 vd.) veya kusursuz sorumluluk (m.66, m.71); içerik/eser üretimi varsa FSEK/SMK. Ara sonuç: hangi norm seti baskın.
2. **Sistemin rolü**: Tam otomatik karar mı (insan denetimi yok), insan onaylı karar destek mi? Bu ayrım KVKK m.11 itiraz hakkını ve sorumluluk dağılımını belirler.
3. **Yer/uygulama**: AB pazarına dokunuyorsa AB Yapay Zekâ Tüzüğü 2024/1689 ve GDPR m.22 doğrudan; yalnız Türkiye ise bu metinler karşılaştırmalı kaynaktır, bağlayıcı değildir. Müvekkile bunu açıkça belirt.
4. **Görevli merci**: KVKK ihlalinde Kurul (m.14) ve sulh/asliye hukuk; tüketici işleminde tüketici mahkemesi/hakem heyeti; kamu otomatik işleminde idari yargı (İYUK); fikri hakta FSHM.
5. **Tarih kilidi**: KVKK m.9 aktarım rejimi ve ceza tutarları değişti; olay tarihini sabitle.

## Çıktı modülleri
- Dosya konumlandırma notu (katman + sistemin rolü + norm seti).
- Uygulanır/karşılaştırmalı norm ayrımı (KVKK/TBK vs. AB Tüzüğü).
- Görevli merci ve hangi uzman beceriye geçileceğine dair yönlendirme.

## Plugin bağlamı

Bu beceri `yapay-zeka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
