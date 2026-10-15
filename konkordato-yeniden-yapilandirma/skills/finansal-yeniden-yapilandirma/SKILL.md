---
name: finansal-yeniden-yapilandirma
description: "Mahkeme dışı, sözleşmesel finansal yeniden yapılandırma (FYY çerçeve anlaşmaları, banka/alacaklı müzakereleri) ile konkordato arasında seçim ve yapılandırma sözleşmesi kurgusu gerektiğinde kullanılır."
---

# Finansal Yeniden Yapılandırma (Mahkeme Dışı)

## Görev
Mahkeme dışı yeniden yapılandırmayı kurgulamak: 5411 sayılı Bankacılık Kanunu Geçici m.32 ve Finansal Yeniden Yapılandırma (FYY) çerçeve anlaşmaları kapsamında banka/finans alacaklılarıyla yapılan yapılandırmayı veya genel sözleşmesel yapılandırmayı (TBK çerçevesinde) tasarlamak.

## Soğuk başlangıç (intake)
- Alacaklılar ağırlıklı olarak banka/finansal kuruluş mu, ticari alacaklı mı?
- Borçlu FYY çerçeve anlaşması kapsamına giren bir teşebbüs mü?
- Mevcut teminat yapısı ve toplam borç büyüklüğü nedir?
- Mahkeme süreci (konkordato) yerine sözleşmesel çözüm tercih ediliyor mu?

## Denetim şeması
1. **Kapsam tespiti.** Finansal kuruluşlara olan borçlar baskınsa FYY çerçeve anlaşması (5411 s.K. Geçici m.32, ilgili BDDK Yönetmeliği) uygulanabilir mi denetlenir. Genel ticari alacaklarda TBK genel hükümleriyle yapılandırma (tecil, ibra, yenileme — TBK m.133) kullanılır.
2. **Konkordato ile karşılaştırma.** FYY mahkeme dışıdır, gizlilik ve hız avantajı sunar; ancak tüm alacaklıları bağlamaz, çoğunluk düzenlemesi sözleşme/çerçeve anlaşma ile sınırlıdır. Konkordato ise mahkeme tasdikiyle tüm alacaklıları bağlar.
3. **Yapılandırma araçları.** Vade uzatımı, faiz indirimi, anapara silme/ibra, teminat güçlendirme, borcun sermayeye dönüştürülmesi (debt-to-equity), yeni finansman. Her aracın TTK/TBK ve vergi sonuçları (örn. ibranın vergisel etkisi) değerlendirilir.
4. **Sözleşme tekniği.** Yapılandırma sözleşmesinde temerrüt halleri, çapraz temerrüt, teminat paketi, taahhüt ve beyanlar, fesih ve hızlandırma (acceleration) maddeleri kurgulanır. İspat: borçlunun mali tablolarıyla yapılandırmanın sürdürülebilirliği gösterilir.
5. **Başarısızlık senaryosu.** Sözleşmesel yapılandırma çökerse konkordatoya geçiş köprüsü hazırlanır. Ara sonuç: mahkeme dışı mı, konkordato mı; hibrit yol mümkün mü.

## Çıktı modülleri
- Konkordato vs. FYY karar matrisi.
- Yeniden yapılandırma sözleşmesi/protokol taslağı (yer tutuculu).
- Teminat ve taahhüt listesi.
- Başarısızlık halinde konkordato geçiş planı.

## Plugin bağlamı

Bu beceri `konkordato-yeniden-yapilandirma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
