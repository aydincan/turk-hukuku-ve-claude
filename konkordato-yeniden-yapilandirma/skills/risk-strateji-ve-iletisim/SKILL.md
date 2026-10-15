---
name: risk-strateji-ve-iletisim
description: "Borçlu, alacaklı veya komiser perspektifinden konkordato stratejisini belirlemek, risk haritası çıkarmak ve taraflarla iletişim metinlerini hazırlamak gerektiğinde kullanılır."
---

# Risk, Strateji ve Taraf İletişimi

## Görev
Tarafın konumuna göre strateji kurmak: borçlu için sürecin başarısını ve yöneticilerin sorumluluk riskini yönetmek; alacaklı için tahsil/itiraz stratejisi; komiser/alacaklılar kurulu için denetim stratejisi. Risk haritası ve iletişim metinleri üretmek.

## Soğuk başlangıç (intake)
- Müvekkilin konumu: borçlu, alacaklı, komiser/kurul üyesi mi?
- Hedef: sürecin başarısı, alacağın korunması yoksa süreçten çıkış mı?
- Yöneticilerin kişisel sorumluluk riski (TTK m.553, vergi/SGK) gündemde mi?
- Karşı tarafla müzakere/yazışma ihtiyacı var mı?

## Denetim şeması
1. **Konum analizi.** Borçlu tarafında: konkordatonun reddi halinde iflas riski (m.308/son), yönetici sorumluluğu (TTK m.553), kamu borçlarından (vergi/SGK) şahsi sorumluluk (VUK m.10, 6183 s.K. mük. m.35) değerlendirilir.
2. **Alacaklı stratejisi.** Alacağı kaydettirme, çekişmeli alacak iddiası, çoğunluk hesabındaki ağırlık, rehin/imtiyaz konumunu güçlendirme; tasdike/projeye itiraz (m.304) hakkı denetlenir.
3. **Risk haritası.** Olasılık ve etki ekseninde: tasdik edilmeme, mühletin kaldırılması (m.292), iptal/fesih (m.308/e), kamu borcu yaptırımları, sözleşmesel temerrüt etkileri sıralanır. İspat zafiyetleri işaretlenir.
4. **İletişim metinleri.** Müvekkile sade dilde durum/seçenek notu; karşı tarafa müzakere veya itiraz yazısı; komisere/mahkemeye sunum dili. Gizlilik ve avukatlık sır saklama (Av.K. m.36) gözetilir.
5. **Ara sonuç.** Önerilen strateji (sürdür/itiraz et/çık), gerekçesi ve sonraki somut adımlar belirlenir.

## Çıktı modülleri
- Konuma özgü strateji notu.
- Risk haritası (olasılık-etki matrisi).
- Müvekkil bilgilendirme metni (sade dil).
- Karşı tarafa/komisere yazı taslağı (yer tutuculu).

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
