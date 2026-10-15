---
name: kat-karsiligi-insaat
description: "Arsa sahibi ile yüklenici arasında daire/bağımsız bölüm karşılığı inşaat anlaşması yapılması, ihlali veya tasfiyesi söz konusu olduğunda; sözleşmenin kuruluşu, gecikme/ayıp, fesih-dönme ve üçüncü kişi haklarının çözümü için kullanılır."
---

# Kat Karşılığı (Arsa Payı Karşılığı) İnşaat Sözleşmesi

## Görev
Karma (atipik) nitelikteki kat karşılığı inşaat ilişkisini kurmak ve uyuşmazlığını çözmek: yüklenicinin inşa ve devir borçları ile arsa sahibinin arsa payı devri borcunu dengelemek; gecikme, ayıp ve eksik iş hâllerinde dönme/fesih ile tazminat yollarını belirlemek; daire alan üçüncü kişilerin durumunu çözmek.

## Soğuk başlangıç (intake)
- Sözleşme noterde resmî şekilde mi yapıldı; arsa payları/bağımsız bölüm paylaşımı net mi?
- İnşaat hangi seviyede (ruhsat, kaba/ince, iskân); süre/teslim tarihi geçti mi?
- Gecikme, eksik iş veya ayıp iddiası var mı; ceza-i şart kararlaştırıldı mı?
- Yüklenici kendi payındaki daireleri üçüncü kişilere sattı/vaad etti mi?

## Denetim şeması
1. **Hukuki nitelik ve şekil**: Sözleşme, eser (TBK m.470 vd.) ile taşınmaz devri (satış vaadi) unsurlarını birleştiren karma sözleşmedir; taşınmaz devri içerdiğinden resmî şekle tabidir (noterde düzenleme; TBK m.29, m.237). Şekle aykırılık kural olarak hükümsüzlük doğurur (TBK m.27); fakat inşaatın önemli ölçüde tamamlanması hâlinde şekil eksikliğini ileri sürmek dürüstlük kuralına aykırı olabilir (TMK m.2).
2. **Yüklenicinin borcu**: Eseri sözleşmeye, ruhsata ve fen kurallarına uygun, kararlaştırılan sürede teslim (TBK m.470, m.473). Gecikmede temerrüt hükümleri ve varsa cezai şart (TBK m.179) işler.
3. **Ayıp ve eksik iş**: Ayıba karşı tekeffül (TBK m.474-478); iş sahibi onarım, bedel indirimi veya ağır ayıpta sözleşmeden dönme ile tazminat isteyebilir; ayıp ihbarı (m.474) ve süreler gözetilir.
4. **Dönme/fesih**: Yüklenicinin temerrüdünde TBK m.123-125 (süre verme/dönme) ile m.473 (işin zamanında bitirilemeyeceğinin anlaşılması) değerlendirilir. Geriye etkili dönme ile ileriye etkili fesih ayrımı, ifa derecesine göre belirlenir; kısmen ifada tasfiye ilişkisi kurulur.
5. **Üçüncü kişilerin durumu**: Yükleniciden bağımsız bölüm alan/vaad alan üçüncü kişiler, yüklenicinin hak kazandığı paylar ölçüsünde korunur; arsa sahibine karşı tescil talebi yüklenicinin edimini ifa etmesine bağlıdır. Sözleşmenin feshi bu kişilerin haklarını etkiler [doğrulanacak — karararama.yargitay.gov.tr].
6. **Ara sonuç**: İfa ediliyorsa pay devri/tescil; ihlalde dönme-fesih + tazminat ve üçüncü kişi haklarının tasfiyesi.

## Çıktı modülleri
- Kat karşılığı inşaat sözleşmesi ana hat taslağı (paylaşım tablosu, süre, ceza-i şart, teslim) [doldurulacak].
- Temerrüt/dönme veya ayıp ihtarı taslağı (süre verme, talepler).
- Üçüncü kişi (daire alan) hak durumu analizi ve tasfiye notu.

## Plugin bağlamı

Bu beceri `gayrimenkul-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
