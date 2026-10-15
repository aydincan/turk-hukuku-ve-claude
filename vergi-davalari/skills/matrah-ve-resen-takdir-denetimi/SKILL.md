---
name: matrah-ve-resen-takdir-denetimi
description: "Re'sen ve ikmalen tarhta matrahın nasıl belirlendiğini, takdir komisyonu kararının ve inceleme raporunun dayanaklarını denetleyerek matrah uyuşmazlığını çözmek için kullanılır."
---

# Matrah ve Re'sen Takdir Denetimi

## Görev
Re'sen veya ikmalen yapılan tarhiyatta matrahın belirlenme yöntemini ve dayanağını denetlemek; takdir komisyonu kararının ve vergi inceleme raporunun maddi-hukuki tutarlılığını sınamak, matrahın gerçek duruma uygunluğunu tartışmak.

## Soğuk başlangıç (intake)
1. Matrah neye dayalı tespit edildi: takdir komisyonu kararı mı, vergi inceleme raporu mu, karşıt inceleme mi?
2. Re'sen tarh sebebi ne (defter-belge ibraz edilmemesi, kayıt dışı hasılat, sahte belge)?
3. Matrah tespitinde hangi karine/oran/emsal kullanıldı?
4. Defter ve belgeler tam olarak ibraz edildi mi, edilebilir mi?

## Denetim şeması
1. **Re'sen tarh sebebi.** VUK m.30 — sebeplerin (defter tutulmaması, ibraz edilmemesi, kayıtların sıhhatsizliği vb.) gerçekten var olup olmadığı denetlenir. Sebep yoksa re'sen tarhın hukuki temeli düşer.
2. **Yöntem denetimi.** Takdir komisyonu kararı (VUK m.72-76) somut verilere mi dayanıyor, yoksa soyut/varsayımsal mı? İnceleme raporundaki hasılat-gider tespiti maddi delile (banka, POS, stok, randıman) bağlanmalı.
3. **Gerçek mahiyet.** VUK m.3/B — matrah, vergiyi doğuran olayın gerçek mahiyetine göre belirlenir. Mükellefin defterleri, ekonomik gerçeklik ve emsal verilerle çelişen takdirler eleştirilir.
4. **İspat dağılımı.** İdarenin matrah farkını somut tespitle ortaya koyma yükü ile mükellefin karşı delil (fatura, ödeme, stok hareketi) sunma yükü karşılaştırılır. İktisadi icaplara aykırılık iddiası eden taraf ispatla yükümlü.
5. **Bilirkişi ve hesap.** Karmaşık hasılat/maliyet hesaplarında bilirkişi incelemesi (HMK ilkeleri, İYUK m.31 atfı) talep edilir; randıman ve oran hesaplarındaki maddi hatalar tek tek gösterilir. Ara sonuç: matrahın tamamen mi yoksa kısmen mi hatalı olduğu, hedeflenen indirim miktarı belirlenir.

## Çıktı modülleri
- Matrah tespit yöntemi eleştiri tablosu (dayanak / itiraz).
- Karşı delil ve hesaplama notu.
- Bilirkişi talebi gerekçesi taslağı.

## Plugin bağlamı

Bu beceri `vergi-davalari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
