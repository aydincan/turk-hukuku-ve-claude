---
name: infaz-hakimligi-basvuru
description: "Ceza infaz kurumu işlem ve kararlarına karşı infaz hâkimliğine şikâyet, süre, görev-yetki ve itiraz mercii yolunu kurgulamak gerektiğinde kullanılır."
---

# İnfaz Hâkimliğine Başvuru ve İtiraz

## Görev
İnfaz kurumu idaresinin işlem ve kararlarına ya da infaz savcılığı uygulamalarına karşı 4675 sayılı İnfaz Hâkimliği Kanunu yolunu doğru biçimde işletmek.

## Soğuk başlangıç (intake)
- Hangi işlem/karar şikâyet konusu (disiplin, nakil, infaz hesabı, hak kısıtlaması)?
- İşlem hükümlüye ne zaman tebliğ/uygulanıp öğrenildi (süre için)?
- Hükümlü hangi infaz kurumunda, hangi savcılığın yetki alanında (yetki için)?
- Daha önce idareye başvuru yapıldı mı?

## Denetim şeması
1. Görev: 4675 sayılı Kanun m.4 uyarınca infaz kurumu idaresinin işlem ve eylemlerine ilişkin şikâyetleri infaz hâkimliği inceler; ceza yargılamasıyla ilgili olmayan, infaza özgü uyuşmazlıklar bu yola tabidir. Ara sonuç: konu infaz hâkimliği görevinde mi?
2. Süre: şikâyet, işlemin öğrenildiği tarihten itibaren kanunda öngörülen süre içinde (4675 m.5) yapılmalıdır; sürenin kaçırılması başvuruyu usulden reddettirir. İspat yükü: süreye uygunluğu başvurucu, aksini idare ortaya koyar.
3. Yetki: hükümlünün bulunduğu infaz kurumunun yargı çevresindeki infaz hâkimliği yetkilidir.
4. İnceleme ve karar: infaz hâkimi dosya üzerinden inceler, gerekirse bilgi/belge ister; kabul, ret veya işlemin iptaline karar verir (4675 m.6).
5. İtiraz: infaz hâkimliği kararına karşı ağır ceza mahkemesine (CMK itiraz hükümleri çerçevesinde) itiraz yolu açıktır (4675 m.6). Ara sonuç: itiraz mercii ve süresi.
6. İlkesel içtihat: görev sınırı ve süre başlangıcı için karararama.yargitay.gov.tr; tutulma koşulları ihlalinde AYM bireysel başvuru (kararlarbilgibankasi.anayasa.gov.tr). Künye `[doğrulanacak]`.
7. Ara sonuç: görev/yetki/süre üçlüsü + başvuru stratejisi.

## Çıktı modülleri
- Görev-yetki-süre kontrol çizelgesi.
- Şikâyet dayanak listesi.
- İnfaz hâkimliği şikâyet ve itiraz dilekçesi tetiği.

## Plugin bağlamı

Bu beceri `infaz-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
