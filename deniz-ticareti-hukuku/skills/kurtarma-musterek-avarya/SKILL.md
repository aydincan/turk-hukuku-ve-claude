---
name: kurtarma-musterek-avarya
description: "Tehlikedeki gemi veya yükün kurtarılması (kurtarma ücreti) ya da ortak selamet için bilerek yapılan fedakârlık/masrafların paylaşımı (müşterek avarya) gündeme geldiğinde; ücret/garame paylarını ve York-Anvers Kurallarının uygulamasını çözmek için kullan."
---

# Kurtarma ve Müşterek Avarya

## Görev
Kurtarma faaliyetinde kurtarma ücretinin doğup doğmadığını ve miktarını belirlemek; ortak selamet için yapılan fedakârlık ve olağanüstü masrafları müşterek avarya olarak nitelendirip garame paylarını dağıtmak.

## Soğuk başlangıç (intake)
- Olay bir kurtarma mı (üçüncü kişinin yardımı) yoksa müşterek avarya mı (deniz serveti içinde fedakârlık)?
- Tehlike gerçek ve ciddi miydi; kurtarma faydalı sonuç (no cure no pay) doğurdu mu?
- Sözleşme/standart form (örn. LOF) var mı; York-Anvers Kurallarına atıf yapılmış mı?
- Gemi, yük ve navlun değerleri ile fedakârlık/masraf kalemleri nelerdir?

## Denetim şeması
1. **Kurtarma şartları**: Deniz tehlikesi, faydalı sonuç ve gönüllülük unsurlarını (TTK m.1298 vd., 1989 Kurtarma Sözleşmesi esaslı) denetle; "no cure no pay" ilkesini ve çevre zararı önlemeye yönelik özel tazminatı (special compensation) ayrıştır.
2. **Kurtarma ücretinin belirlenmesi**: Kurtarılan değer, tehlikenin derecesi, kullanılan emek/araç ve başarı gibi ölçütlerle ücreti takdir et; ücret kurtarılan değeri aşamaz. Kurtaranlar arasında paylaşımı belirle.
3. **Müşterek avarya nitelendirmesi**: Ortak tehlikeden ortak selameti sağlamak için **bilerek ve makul** yapılan olağanüstü fedakârlık/masrafları müşterek avarya say (TTK m.1272 vd.); kuru/münferit (hususi) avaryadan ayır.
4. **Garame paylaşımı**: York-Anvers Kuralları uyarınca avarya garame payını gemi, yük ve navlunun kurtulan değerleri oranında dağıt; dispeç (avarya raporu) hazırlanmasını ve dispeççinin rolünü belirt.
5. **İspat ve ara sonuç**: Fedakârlığın iradî ve makul olduğunu, ortak tehlikenin varlığını talep eden ispatlar. Çıktıda kurtarma ücreti veya garame payı dağıtımını sayısal taslakla sonuçlandır; ilgili zamanaşımı sürelerini işaretle.

## Çıktı modülleri
- Kurtarma ücreti / müşterek avarya nitelendirme notu
- Değer ve garame payı dağıtım taslağı (dispeç iskeleti)
- Teminat (avarya garantisi/depozito) ve tahsil stratejisi

## Plugin bağlamı

Bu beceri `deniz-ticareti-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
