---
name: risk-strateji-kriz-yonetimi
description: "Bir siber olay veya bilişim hukuku ihtilafında ceza-idari-tazminat risklerini bütünsel tartmak, kurum/müvekkil için en iyi-en kötü senaryoyu ve eylem stratejisini belirlemek gerektiğinde kullanılır."
---

# Risk, Strateji ve Kriz Yönetimi

## Görev
Çok katmanlı bir bilişim/siber olayda riskleri tartmak, senaryoları çıkarmak ve müvekkil/kurum için tutarlı bir hukuki strateji ile kriz yönetim planı kurmak.

## Soğuk başlangıç (intake)
1. Kurumun/müvekkilin pozisyonu ne? (mağdur, sorumlu, hem mağdur hem sorumlu?)
2. En kritik risk ne? (ceza, idari para cezası, tazminat, itibar, operasyon kesintisi?)
3. Karşı taraf/düzenleyici aktif mi? (savcılık, KVKK, müşteri talepleri?)
4. Zaman baskısı ve kaynak kısıtı ne düzeyde?

## Denetim şeması
1. **Risk envanteri.** Üç eksende risk çıkarılır: ceza (TCK m.243-245, m.135-140 maruziyeti), idari (KVKK m.18 para cezası, sektörel yaptırım), özel hukuk (TBK m.49/m.112 tazminat, toplu talep riski). Her risk olasılık ve etki ile derecelendirilir.
2. **Pozisyon analizi.** Kurum aynı anda mağdur (saldırıya uğrayan) ve potansiyel sorumlu (tedbirsizlik) olabilir; bu ikili konum stratejiyi belirler. Suç duyurusu seçeneği ile sorumluluk savunması çelişmemelidir.
3. **Senaryo çıkarma.** En iyi/orta/en kötü senaryolar; her birinde olasılık, mali etki, süre ve karşı hamle. Delil durumu ve ispat yükü dağılımı (KVKK'da tedbir ispatı kurumda; cezada iddia makamında) senaryoları belirler.
4. **Strateji tercihi.** Erken bildirim ve iş birliği (yaptırım hafifletici), uzlaşma/sulh, savunma hattı, eş zamanlı yargı yolları koordinasyonu; itibar/iletişim ile hukuki adımların uyumu. Ölçülülük: aşırı reaksiyon yeni risk doğurmamalı.
5. **Ara sonuç.** Önceliklendirilmiş aksiyon listesi, sorumlu kişiler ve karar noktaları net bir kriz planına bağlanır.

## Çıktı modülleri
- Risk matrisi (eksen, olasılık, etki, öncelik).
- Senaryo tablosu (en iyi/orta/en kötü + aksiyon).
- Kriz yönetim planı ve karar/iletişim notu.

## Plugin bağlamı

Bu beceri `bilisim-hukuku-siber` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
