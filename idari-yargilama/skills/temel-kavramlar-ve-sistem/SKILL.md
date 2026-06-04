---
name: temel-kavramlar-ve-sistem
description: "İdari yargı kolunun adli yargıdan ayrımı, görevli yargı düzeninin tespiti, iptal/tam yargı/idari sözleşme dava tiplerinin ayrıştırılması gibi sistematik ve nitelendirme sorularında kullanılır; uyuşmazlığın hangi mahkemeye ait olduğu belirsiz olduğunda başvurulur."
---

# Temel Kavramlar ve İdari Yargı Sistematiği

## Görev
Uyuşmazlığı doğru yargı koluna ve doğru dava tipine yerleştirmek; idari yargının görevli olup olmadığını ve hangi dava tipinin (iptal, tam yargı, idari sözleşme) açılması gerektiğini gerekçeli olarak saptamak.

## Soğuk başlangıç (intake)
- Uyuşmazlığın kaynağı bir idari işlem mi, idari eylem mi, yoksa sözleşme mi?
- Karşı taraf bir kamu idaresi/kurumu mu; işlem kamu gücü kullanılarak mı tesis edildi?
- Talep bir işlemin iptali mi, bir zararın tazmini mi, yoksa her ikisi mi?
- İşlemin tebliğ/öğrenme tarihi nedir?

## Denetim şeması
1. **Yargı kolu** (Anayasa m.125; İYUK m.1-2): İşlem/eylem kamu hizmetinin yürütülmesinden ve kamu gücünden doğuyorsa idari yargı görevlidir. Özel hukuk ilişkisi (ör. idarenin tasarruf malı kirası, fiili yol/kamulaştırmasız el atmada bedel) varsa adli yargı söz konusu olabilir; tereddütte 2247 sayılı Kanun çerçevesinde Uyuşmazlık Mahkemesi belirleyicidir.
2. **Kesin ve yürütülebilir işlem** (İYUK m.14/3-d): İcrai olmayan, hazırlık/iç işlem niteliğindeki işlemler dava edilemez. Zincir işlemlerde kesin işlemi tespit et.
3. **Dava tipi**:
   - Yetki-şekil-sebep-konu-maksat yönünden hukuka aykırılık iddiası ve menfaat ihlali varsa → **iptal davası** (m.2/1-a).
   - Kişisel hak ihlali ve zarar tazmini varsa → **tam yargı davası** (m.2/1-b); idari eylemde m.13 ön başvurusu unutulmaz.
   - İdari sözleşme şartlarından doğuyorsa → m.2/1-c.
4. **İstisna/ayrım**: İptal ve tam yargı birlikte (m.12) açılabilir; iptal kararı sonrası tam yargı için süre m.12 hükmüne göre işler.
5. **İspat yükü**: İdari işlemin sebep ve konu unsurlarına ilişkin dayanak belgeler kural olarak idarededir; resen araştırma ilkesi (İYUK m.20) geçerlidir.

## Çıktı modülleri
- Yargı kolu ve dava tipi nitelendirme notu (gerekçeli)
- Görevli/yetkili mahkeme önerisi
- Sıradaki adım: süre ve dava şartı kontrolüne yönlendirme

## Plugin bağlamı

Bu beceri `idari-yargilama` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
