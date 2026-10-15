---
name: gecici-kesin-muhlet
description: "Geçici mühletin alınması, kesin mühlete geçiş, mühletin uzatılması veya kaldırılması ile mühletin alacaklılar ve sözleşmeler üzerindeki etkilerini yönetmek gerektiğinde kullanılır."
---

# Geçici ve Kesin Mühlet Yönetimi

## Görev
Mühlet aşamasını uçtan uca yönetmek: geçici mühletin alınması, kesin mühlete geçiş kararının hazırlanması, mühletin uzatılması veya kaldırılması (m.291, m.292) ve mühletin hukuki sonuçlarının takibi.

## Soğuk başlangıç (intake)
- Geçici mühlet kararı tarihli mi, ne kadar süre kaldı?
- Komiserin ara raporu hazırlandı mı?
- Mühlet sırasında borçlunun aleyhine yeni takip/ihtiyati haciz girişimi var mı?
- Borçlunun rehinli/imtiyazlı alacaklıları kim?

## Denetim şeması
1. **Geçici mühletin sonuçları (m.288).** Geçici mühlet, kesin mühletin sonuçlarını doğurur. İlan ve ilgili sicillere bildirim yapılmış mı kontrol edilir.
2. **Kesin mühlete geçiş (m.289).** Komiser raporu, borçlu ve varsa talep eden alacaklı dinlenir; başarı ihtimali değerlendirilir. İspat yükü borçluda.
3. **Mühletin takipler bakımından sonucu (m.294).** Mühlet içinde borçluya karşı icra takibi yapılamaz, başlamış takipler durur; istisnalar: rehnin paraya çevrilmesi yoluyla takip başlatılabilir ancak muhafaza tedbirleri ve satış yapılamaz (m.295). İmtiyazlı alacaklar için ihtiyati haciz/tedbir sınırlamaları denetlenir.
4. **Sözleşmeler bakımından (m.296).** Borçlunun taraf olduğu sözleşmelerin mühlet nedeniyle feshini sınırlayan hükümler uygulanır; sürekli edimli sözleşmelerin akıbeti değerlendirilir.
5. **Tasarruf yetkisinin sınırlanması (m.297).** Borçlu, komiserin onayı olmadan rehin tesisi, kefil olma, taşınmaz/işletme devri gibi işlemleri yapamaz; aksi işlem hükümsüzdür. İhlal halinde mühletin kaldırılması (m.292) gündeme gelir.
6. **Mühletin kaldırılması (m.291-292).** Konkordatonun başarıya ulaşamayacağı anlaşılır veya borçlu kötüye kullanırsa mühlet kaldırılır, iflasa tabi borçlu için iflas açılır. Ara sonuç: mühlet devam mı, kaldırma mı.

## Çıktı modülleri
- Mühlet süre takvimi ve uzatma/kaldırma senaryoları.
- Tasarruf yetkisi kısıtı için onay-gerektiren işlemler listesi.
- Rehinli/imtiyazlı alacaklı haritası.
- Komisere/mahkemeye sunulacak ara rapor taslağı.

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
