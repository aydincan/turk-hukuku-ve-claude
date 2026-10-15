---
name: risk-strateji-danismanlik
description: "Kambiyo senedi alacak/borç ilişkisinde tahsil kabiliyetini, ceza riskini ve süreç seçeneklerini tartmak; müvekkile yön verecek strateji ve müvekkil/karşı taraf iletişimi gerektiğinde kullanılır."
---

# Risk Değerlendirmesi ve Strateji

## Görev
Bir kambiyo senedi uyuşmazlığında müvekkilin (alacaklı veya borçlu) konumunu bütünsel tartmak; tahsil/ödeme, ceza riski, süre durumu ve uzlaşma seçeneklerini değerlendirip eyleme dönük strateji üretmek ve müvekkile sade dille aktarmak.

## Soğuk başlangıç (intake)
- Müvekkil alacaklı (hamil) mı, borçlu (keşideci/ciranta/avalist) mı?
- Senedin türü, bedeli, vade/ibraz durumu ve borçluların mali durumu nedir?
- Süreler ve def'iler bakımından zayıf/güçlü yönler neler?
- Müvekkilin önceliği hızlı tahsil mi, ceza baskısı mı, masrafı sınırlamak mı, uzlaşma mı?

## Denetim şeması
1. Hak envanteri: senet kambiyo vasfı, yetkili hamil, devir zinciri, def'i ve süre durumu — her biri için güçlü/zayıf değerlendirmesi yap (ilgili becerilere yolla).
2. Borçlu çevresi ve tahsil kabiliyeti: müteselsil borçlular (TTK m.724) içinde mali gücü olanı belirle; hacze elverişli malvarlığı araştırması (UYAP/tapu/araç) planla.
3. Çek özelinde ceza kaldıracı: karşılıksız çekte 5941 s. K. m.5 adli para cezası ve çek yasağı, ödeme/uzlaşma için baskı aracıdır; şikâyet süresi ve usulünü gözet.
4. Yol seçimi: kambiyo takibi (İİK m.167) hızlı ama itirazla karşılaşabilir; menfi tespit (İİK m.72) borçlu için tedbir gerektirir; sulh/protokolle yapılandırma masrafı düşürür.
5. Süre riski: zamanaşımı (TTK m.808/m.749) ve hak düşümü tarihlerini öne çıkar; gerekirse sebep alacağı planını hazır tut.
6. Ara sonuç: olasılık-maliyet-süre matrisiyle önerilen strateji ve alternatif planı belirle; karşı tarafa yapılacak bildirim/teklifin tonunu ayarla.

## Çıktı modülleri
- SWOT/risk matrisi (güçlü-zayıf yön, olasılık, tahsil kabiliyeti).
- Strateji ve aksiyon planı (öncelik sıralı, süre uyarılı).
- Müvekkile sade dilde bilgilendirme notu ve karşı tarafa ihtar/teklif taslağı.

## Plugin bağlamı

Bu beceri `kiymetli-evrak` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
