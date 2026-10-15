---
name: sozlesme-taslagi-ve-redline
description: "Satış, kira, eser, vekâlet veya kefalet sözleşmesi taslağı hazırlamak ya da mevcut bir taslağı emredici hükümler ve risk dengesi açısından gözden geçirmek gerektiğinde kullanılır."
---

# Sözleşme Taslağı ve Redline (İsimli Sözleşmeler)

## Görev
İsimli bir sözleşmenin taslağını üretmek veya mevcut metni TBK Özel Hükümler ve emredici tabanlar süzgecinden geçirip risk-dengeli redline önermek; geçersiz/asimetrik şartları tespit edip alternatif lafız sunmak.

## Soğuk başlangıç (intake)
- Sözleşme tipi ve taraflar (hangi tarafı temsil ediyoruz)?
- Edimler, bedel, vade ve teminat yapısı?
- Tüketici/konut kirası gibi emredici taban var mı?
- Müzakere gücü ve kabul edilebilir risk seviyesi?

## Denetim şeması
1. **Zorunlu/şekil unsurları.** Taşınmaz satışı/satış vaadi resmî şekil (TBK m.237, m.29 satış vaadi noter); kefalette el yazısı azami miktar + tarih + eş rızası (m.583-584); aksi halde hükümsüzlük.
2. **Emredici taban taraması.** Konut/çatılı işyeri kirasında kiracı aleyhine kayıt yasağı (m.346); muacceliyet/cezai şart geçersiz. Tüketici sözleşmelerinde haksız şart denetimi (6502 m.5). Genel işlem koşullarında yazılmamış sayılma (TBK m.20-25).
3. **Risk maddeleri.** Sorumluluk sınırlaması: ağır kusur/kasıt için sorumsuzluk anlaşması kesin geçersiz (TBK m.115); ayıptan sorumluluğu kaldıran kayıt satıcı ayıbı gizlemişse geçersiz (m.221). Cezai şart (m.179-182) ve aşırı cezanın indirilmesi (m.182/3).
4. **Denge kontrolü.** Fesih hakları simetrik mi; temerrüt faizi ve oranı (TBK m.120, ticari işte 3095 s.K.); teslim/kabul ve ayıp ihbar süreleri; mücbir sebep ve uyarlama (m.138) kaydı.
5. **Uyuşmazlık çözümü.** Yetkili mahkeme/tahkim şartı geçerlilik (HMK m.17 yetki sözleşmesi tacir şartı); arabuluculuk ön şartına atıf.
6. **Ara sonuç.** Madde madde risk skoru, geçersiz şart listesi, müzakere notu. İspat boyutu: ihtar/bildirim için yazılılık ve tebligat klozları eklenir.

## Çıktı modülleri
- Sözleşme taslağı veya redline (gerekçeli değişiklik notlarıyla).
- Geçersiz/riskli şart tablosu + alternatif lafız.
- Müzakere pozisyon notu (müvekkil lehine/karşı taraf beklentisi).

## Plugin bağlamı

Bu beceri `borclar-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
