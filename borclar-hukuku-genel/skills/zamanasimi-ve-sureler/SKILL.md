---
name: zamanasimi-ve-sureler
description: "Bir alacağın zamanaşımına uğrayıp uğramadığı, sürenin başlangıcı, kesilmesi-durması ve def'i olarak ileri sürülmesi söz konusu olduğunda kullanılır."
---

# Zamanaşımı ve Süreler

## Görev
Alacağa uygulanacak zamanaşımı süresini, başlangıcını, kesilme/durma hâllerini saptamak ve def'i olarak doğru zamanda ileri sürülmesini sağlamak.

## Soğuk başlangıç (intake)
- Alacağın türü ne (genel sözleşme alacağı, dönemsel edim, özel kanun alacağı)?
- Alacak ne zaman muaccel oldu (sürenin başlangıcı)?
- Arada dava, icra takibi, ikrar veya başka kesen işlem oldu mu?
- Tarafların biri tacir/şirket mi; özel süre öngören kanun var mı?

## Denetim şeması
1. Genel süre: TBK m.146 — kanunda aksi öngörülmedikçe her alacak 10 yıllık zamanaşımına tabidir.
2. Beş yıllık süre: m.147 — kira bedelleri, anapara faizleri, dönemsel edimler; vekâlet/komisyon/eser sözleşmesinden doğan bazı alacaklar; serbest meslek ve esnaf alacakları. Liste dikkatle uygulanmalı.
3. Başlangıç: m.149 — alacağın muaccel olduğu an. Kesin vade yoksa muacceliyet için ihtar gerekebilir.
4. Kesilme: m.154 — borçlunun ikrarı (taksit, faiz ödeme, rehin/kefil verme), dava/def'i, icra takibi, iflas masasına başvuru; kesilmeyle yeni süre işlemeye başlar (m.156).
5. Durma: m.153 — belirli kişisel ilişkiler ve hukuki engeller süresince durur; engel kalkınca kaldığı yerden işler.
6. Sonuç ve usul: m.161 — zamanaşımından önceden feragat edilemez; hâkim resen dikkate alamaz, mutlaka def'i olarak ileri sürülmelidir (HMK çerçevesinde cevap dilekçesi/ilk fırsatta). Zamanaşımına uğramış borç eksik borçtur; ifa edilirse geri istenemez.
7. İspat yükü: Süreyi ve başlangıcı zamanaşımını ileri süren; kesilme/durmayı buna dayanan taraf ispatlar.

## Çıktı modülleri
- Süre hesap tablosu (başlangıç, kesilme, kalan süre).
- Zamanaşımı def'i metni taslağı (usule uygun aşama uyarısıyla).
- Karşı tarafça kesilme iddiasına savunma notu.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
