---
name: temel-kavramlar-ve-sistem
description: "Marka hukukuna ilk girişte; markanın hukuki niteliği, hak sahipliği, koruma kapsamı ve SMK'nın tescil-koruma-tasarruf ekseninin haritalanması gerektiğinde uyuşmazlığı doğru kanala yerleştirmek için kullanılır."
---

# Temel Kavramlar ve SMK Sistematiği

## Görev
Somut sorunu 6769 sayılı SMK'nın doğru ekseninde (tescil/idari süreç, hükümsüzlük-iptal, tecavüz, sözleşme) konumlandırmak; markanın tanımı (m.4), hakkın doğumu (tescil ilkesi) ve kapsamının (m.7) çerçevesini kurmak. Yanlış kanal seçimi süre ve görev hatasına yol açar; bu yüzden ilk filtre budur.

## Soğuk başlangıç (intake)
- İşaret tescilli mi, başvuru aşamasında mı, tescilsiz kullanım mı?
- Hangi mal/hizmetler (Nice sınıfları) söz konusu?
- Talep ne: tescil/itiraz, hükümsüzlük/iptal, tecavüzün önlenmesi, tazminat, lisans/devir?
- Karşı tarafın hakkı/önceliği var mı, tarih sırası nedir?

## Denetim şeması
1. **Marka olabilirlik (m.4).** İşaret ayırt edici mi ve sicilde açık-kesin gösterilebiliyor mu (kelime, şekil, renk, ses, üç boyutlu). Olamıyorsa hiç tescil edilmemeli.
2. **Hakkın doğumu.** Türk sisteminde marka hakkı kural olarak tescille doğar (m.7/1). Tescilsiz işaret için m.6/3 (eskiye dayalı kullanım) ve haksız rekabet (TTK m.54-55) yolu ayrıca değerlendirilir.
3. **Koruma kapsamı (m.7).** Aynı işaret-aynı mal; benzer işaret-benzer mal + karıştırılma; tanınmış markada farklı sınıf koruması. Yasaklama yetkisinin kapsamı buradan çıkar.
4. **Sınırlar.** Dürüst kullanım (m.7/5), hakkın tüketilmesi (m.152), kullanmama def'i (m.19/2), sessiz kalma (m.25/6) hakkın kullanımını sınırlar.
5. **Ara sonuç.** Uyuşmazlığın türü (idari/adli), görevli merci (TÜRKPATENT/FSHHM) ve uygulanacak ana norm bloğu (m.5-6 / m.25-26 / m.29-150) belirlenir; süre riski işaretlenir.

## Çıktı modülleri
- Uyuşmazlık türü ve doğru kanal haritası.
- İşaret-mal/hizmet (Nice sınıfı) tablosu.
- Uygulanacak ana norm bloğu ve süre uyarı listesi.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
