---
name: hukum-ve-erteleme-hagb
description: "Beraat, mahkûmiyet, düşme gibi hüküm türlerini ayırt etmek; cezanın ertelenmesi, hükmün açıklanmasının geri bırakılması ve adli para cezasına çevirmeyi değerlendirmek gerektiğinde kullanılır."
---

# Hüküm Türleri, Erteleme ve HAGB

## Görev
Mahkemenin verebileceği hüküm türlerini ve cezaya bağlı bireyselleştirme kurumlarını (erteleme, HAGB, seçenek yaptırım) değerlendirmek; sanık lehine talepleri kurmak.

## Soğuk başlangıç (intake)
- Yargılama sonunda hangi hüküm bekleniyor/verildi?
- Verilecek hapis cezası 2 yıl ve altında mı (HAGB/erteleme eşiği)?
- Sanığın sabıkası var mı; daha önce HAGB/erteleme uygulandı mı?
- Mağdurun zararı giderildi mi, sanık kabul ediyor mu?
- Hüküm tefhim edildiyse kanun yolu süresi işliyor mu?

## Denetim şeması
1. **Hüküm türleri.** Mahkeme beraat, ceza verilmesine yer olmadığı, mahkûmiyet, güvenlik tedbirine hükmedilmesi, davanın reddi veya düşmesine karar verir (CMK m.223). Hangi koşulda hangi hükmün verileceği m.223/2-9'da ayrılır.
2. **HAGB.** 2 yıl veya altı hapis/adli para cezasında, sanık daha önce kasıtlı suçtan mahkûm olmamışsa, zarar giderilmişse ve mahkemece yeniden suç işlemeyeceği kanaati oluşursa hükmün açıklanması geri bırakılabilir (CMK m.231/5-6). 5 yıl denetim süresi uygulanır; sanığın kabulü gerekir. Karara itiraz yolu açıktır (m.231/12).
3. **Cezanın ertelenmesi.** 2 yıl veya altı hapis cezası, koşulları varsa ertelenebilir (TCK m.51); 1-3 yıl denetim süresi belirlenir.
4. **Seçenek yaptırımlar.** Kısa süreli hapis (1 yıl ve altı), adli para cezasına veya TCK m.50'deki tedbirlere çevrilebilir.
5. **Sıra ilkesi.** Uygulamada önce ceza belirlenir, sonra seçenek yaptırım/erteleme/HAGB sırasıyla değerlendirilir; her birinin reddi gerekçelendirilmelidir.
6. **Ara sonuç.** Eşik ve koşullar sağlanıyorsa ilgili kurumun uygulanması talep edilir; reddedilirse gerekçesizlik kanun yolu sebebi olur.

## Çıktı modülleri
- Hüküm türü ve bireyselleştirme uygunluk tablosu.
- HAGB/erteleme/seçenek yaptırım talebi gerekçesi.
- Zarar giderimi ve kabul beyanı notu.
- Karara itiraz/kanun yolu yönlendirmesi.

## Plugin bağlamı

Bu beceri `ceza-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
