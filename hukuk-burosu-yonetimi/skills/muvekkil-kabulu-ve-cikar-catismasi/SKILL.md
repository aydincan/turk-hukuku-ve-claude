---
name: muvekkil-kabulu-ve-cikar-catismasi
description: "Yeni bir iş veya müvekkil teklifi geldiğinde dosya açmadan önce çıkar çatışması taraması, kabul-ret kararı ve kabul koşullarının belirlenmesi gerektiğinde kullanılır."
---

# Müvekkil Kabulü ve Çıkar Çatışması Taraması

## Görev
Yeni bir müvekkil/iş teklifi geldiğinde, işin kabul edilip edilemeyeceğini meslek hukuku açısından denetlemek; çıkar çatışmasını taramak; kabul edilebilirse kabul koşullarını (kapsam, ücret, masraf) çerçevelemek.

## Soğuk başlangıç (intake)
1. Karşı taraf(lar) ve gerçek lehtar kim? Tam kimlik/unvan nedir?
2. Büro daha önce bu işte, karşı tarafta veya bağlantılı bir uyuşmazlıkta yer aldı mı?
3. İşin türü, değeri ve aciliyeti (yaklaşan bir süre var mı) nedir?
4. Müvekkil başka bir avukattan bu iş için vekâlet aldı/azletti mi?

## Denetim şeması
1. **Çıkar çatışması (1136 m.38; TBB Meslek Kuralları m.35-37)**: Aynı işte karşı tarafa hukuki yardım, ya da menfaati çatışan başka bir müvekkilin temsili yasaktır. Büro müvekkil/karşı taraf veri tabanı taranır. Çatışma varsa iş REDDEDİLİR; geçmiş müvekkile ait sır söz konusuysa m.36 sır saklama yükümlülüğü devam eder.
2. **Sır ve bilgi engeli**: Çatışma "olası" düzeydeyse, bilgi bariyeri yeterli değildir; Türk hukukunda kural ret yönündedir.
3. **Yetki/uzmanlık ve kapasite**: İşin gerektirdiği süre/uzmanlık karşılanamıyorsa kabul edilmez (özen borcu, TBK m.506).
4. **Süre kontrolü**: Yaklaşan zamanaşımı/hak düşürücü süre/dava süresi varsa, kabul ancak süreye yetişilebiliyorsa anlamlıdır; aksi halde müvekkil derhal uyarılır.
5. **Ücret ve sözleşme (1136 m.163-164)**: Avukatlık ücreti sözleşme ile belirlenir; yazılılık esastır. Asgari Ücret Tarifesi altına inilemez. Karşı taraf vekâlet ücreti avukata aittir (m.164/son).
6. **Ara sonuç**: Çatışma yok + kapasite var + süreye yetişilir ise KABUL; aksi halde gerekçeli RET ve gerekirse yönlendirme.

## Çıktı modülleri
- Çatışma tarama sonucu (taranan isimler, sonuç).
- Kabul/ret kararı ve gerekçesi.
- Kabul halinde: avukatlık sözleşmesi taslağı, vekâletname kalemi listesi, kritik süre uyarısı.
- Reddedilen işte sır saklama hatırlatması.

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
