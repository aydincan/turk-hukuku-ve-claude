---
name: zamanasimi-ve-sure-hesabi
description: "Bir talebin hâlâ ileri sürülebilir olup olmadığını, zamanaşımı veya hak düşürücü süre dolup dolmadığını ve kesilme-durma etkilerini değerlendirmek gerektiğinde kullanılır."
---

# Zamanaşımı ve Hak Düşürücü Süre Hesabı

## Görev
Somut bir talep için zamanaşımı/hak düşürücü süre durumunu hesaplamak; başlangıç anını, süreyi, kesilme ve durma sebeplerini değerlendirip talebin canlı olup olmadığını belirlemek.

## Soğuk başlangıç (intake)
1. Talebin hukuki niteliği nedir (sözleşme alacağı, haksız fiil tazminatı, sebepsiz zenginleşme, işçilik alacağı vb.)?
2. Talebin doğduğu/muaccel olduğu tarih nedir; haksız fiilde fail ve zarar ne zaman öğrenildi?
3. Bu arada dava, takip, ihtarname, borç ikrarı veya kısmi ödeme oldu mu?
4. Tarafların tacir/şirket olup olmadığı ve özel bir kanunun (İş K., TKHK, sigorta) uygulanıp uygulanmadığı?

## Denetim şeması
1. **Süre tipi ayrımı**: Zamanaşımı def'i ileri sürülünce dikkate alınır; hak düşürücü süre re'sen gözetilir ve kesilmez/durmaz. Önce talebin hangi rejime tabi olduğu belirlenir.
2. **Süre uzunluğu**: Genel zamanaşımı TBK m.146 — 10 yıl; periyodik edimler/kira/faiz vb. TBK m.147 — 5 yıl; haksız fiil TBK m.72 — fiil ve failin öğrenilmesinden 2, her halde 10 yıl (ceza zamanaşımı daha uzunsa o); sebepsiz zenginleşme TBK m.82 — 2/10 yıl. İş Kanunu, TKHK, sigorta (TTK), taşıma gibi özel süreler önceliklidir.
3. **Başlangıç**: Kural olarak alacağın muaccel olduğu an (TBK m.149); haksız fiilde öğrenme anı.
4. **Kesilme (TBK m.154)**: Borçlunun ikrarı, kısmi ödeme, dava/takip, ihtilafın mahkemeye/hakeme götürülmesi süreyi keser; kesilmeden sonra yeni süre işler (m.156).
5. **Durma (TBK m.153)**: Belirli ilişkilerde (örn. evlilik, vesayet) süre durur.
6. **Ara sonuç**: Başlangıç + süre − kesilme/durma hesabıyla son tarih bulunur; dolduysa talebin riski, dolmadıysa kalan süre raporlanır.

## Çıktı modülleri
- Zamanaşımı hesap tablosu (nitelik, dayanak, başlangıç, kesilmeler, sonuç tarihi).
- Risk notu (dolmuş/dolmak üzere/canlı) ve önerilen acil aksiyon.

## Plugin bağlamı

Bu beceri `hukuk-burosu-yonetimi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
