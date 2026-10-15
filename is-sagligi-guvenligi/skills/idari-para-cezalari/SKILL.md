---
name: idari-para-cezalari
description: "6331 sayılı Kanun kapsamında uygulanan idari para cezalarının hukukiliğini denetlemek ve sulh ceza hâkimliğine itiraz yolunu kurmak için kullanılır."
---

# İdari Para Cezaları ve İtiraz

## Görev
İş müfettişi denetimi sonucu uygulanan idari para cezalarının dayanağını, usulünü ve miktarını denetlemek; 5326 sayılı Kabahatler Kanunu çerçevesinde itiraz yolunu kurmak.

## Soğuk başlangıç (intake)
- Ceza hangi yükümlülük ihlaline dayanıyor (6331 m.26 hangi bent); ceza tutanağı ve denetim raporu elde mi?
- Tebliğ tarihi ne; itiraz süresi kaçtı mı (tebliğden itibaren on beş gün)?
- İşyerinin tehlike sınıfı ve çalışan sayısı (bazı cezalar bunlara göre/her çalışan başına katlanır)?
- Aynı fiil için tekerrür veya birden çok ceza var mı?

## Denetim şeması
1. **Dayanak (6331 m.26):** Her ceza, ihlal edilen yükümlülük maddesine (m.4, 6, 8, 10, 11, 14, 15, 16, 17, 18, 22 vb.) bağlanır; m.26 bentleri hangi maddeye hangi tutarı öngördüğünü gösterir. Cezanın doğru maddeye dayandığını ve eylemin gerçekten o yükümlülüğü ihlal ettiğini denetle.
2. **Çalışan başına/aylık tekrar:** Bazı cezalar her çalışan için ayrı ve aykırılığın devam ettiği her ay için tekrar uygulanır; bu çarpanların doğru hesaplandığını kontrol et.
3. **Usul denetimi:** Yetkili merci, tutanağın usulü, savunma hakkı, tebligatın usulüne uygunluğu (7201). Usul sakatlığı iptal sebebidir.
4. **İtiraz yolu (5326 m.27-28):** İdari para cezasına karşı tebliğden itibaren on beş gün içinde sulh ceza hâkimliğine başvurulur; sulh ceza kararına karşı itiraz mercii bir sonraki numaralı sulh ceza hâkimliğidir. Süreyi kaçırmamak esastır.
5. **İspat ve karine:** İdarenin tespitleri aksi ispatlanana kadar esas alınır; işveren uyumunu belgeyle çürütür. **Ara sonuç:** İptal/indirim argümanlarını madde ve usul ekseninde sırala.

## Çıktı modülleri
- Ceza-madde-tutar eşleştirme tablosu.
- Usul ve esas itiraz gerekçeleri listesi.
- Sulh ceza hâkimliği başvuru dilekçesi taslağı.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
