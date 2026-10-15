---
name: sureler-ve-zamanasimi
description: "Hangi talep için hangi zamanaşımı veya hak düşürücü sürenin işlediğini, başlangıcını ve kesilme-durma hallerini belirlemek gerektiğinde; her sözleşme tipinin özel sürelerini genel kuraldan ayırmak için kullanılır."
---

# İsimli Sözleşmelerde Süreler ve Zamanaşımı

## Görev
Talep bazında doğru süreyi (genel/özel zamanaşımı veya hak düşürücü ihbar süresi), başlangıç anını ve kesilme/durma hallerini belirlemek; sürenin niteliğini (zamanaşımı mı, hak düşürücü mü) ayırmak çünkü sonuçları farklıdır.

## Soğuk başlangıç (intake)
- Talebin türü ve hukuki dayanağı (ayıp, ücret, tazminat, iade)?
- Olayların tarihleri (teslim, kabul, ifa, fark etme)?
- Adi mi ticari mi tüketici işlemi mi?
- Kesen işlem var mı (dava, takip, ikrar)?

## Denetim şeması
1. **Genel zamanaşımı (m.146-147).** Kural 10 yıl; m.147 istisnaları 5 yıl: kira bedeli, vekâlet/komisyon/simsarlık ücreti, eser sözleşmesinden doğan alacaklar (bazı haller), serbest meslek/zanaatkâr alacakları. Önce talebin bu listeye girip girmediğine bakılır.
2. **Satışta ayıp (m.231).** 2 yıl; taşınmaz yapıda 5 yıl; satıcı ağır kusurlu/hileli ise süreyle korunmaz.
3. **Eserde ayıp (m.478).** 2 yıl; taşınmaz yapı 5 yıl; yüklenici ağır kusurlu ise 20 yıl.
4. **İhbar/hak düşürücü süreler.** Satışta gözden geçirme-ihbar (m.223), eserde m.477, ticari satışta TTK m.23/c (2/8 gün) hak düşürücüdür; geçirilirse kabul sayılır ve hâkim resen dikkate alır. Bunlar zamanaşımından ayrıdır.
5. **Başlangıç anı.** Zamanaşımı alacağın muaccel olduğu anda işler (m.149); ayıpta teslim/kabul; tazminatta zarar ve failin öğrenilmesi ilgili tipe göre belirlenir.
6. **Kesilme/durma (m.153-156).** Dava, takip, ikrar, hakeme başvuru keser; kesilince yeni süre işler. Durma halleri (m.153) sınırlı. İspat: zamanaşımı def'ini ileri süren taraf; kesilme/durmayı buna dayanan taraf ispatlar. Ara sonuç: her talep için tek bir nihai süre/tarih.

## Çıktı modülleri
- Talep-süre-başlangıç-kesilme tablosu.
- Zamanaşımı def'i / def'e cevap notu.
- Risk uyarısı (yakın dolan süreler için aksiyon listesi).

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
