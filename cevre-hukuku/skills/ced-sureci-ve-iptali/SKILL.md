---
name: ced-sureci-ve-iptali
description: "Çevresel etki değerlendirmesi zorunluluğu, ÇED Olumlu veya ÇED Gerekli Değildir kararlarının hukuka uygunluğu ve iptali, EK-1/EK-2 listelerine tabilik ve katılım hakkı sorunlarında kullan; ÇED dava ve danışmanlığının ana becerisidir."
---

# ÇED Süreci ve ÇED Kararının İptali

## Görev
Bir projenin ÇED'e tabi olup olmadığını, ÇED sürecinin usulüne uygunluğunu ve ÇED kararının iptal edilebilirliğini denetlemek; yatırımcı veya itiraz eden taraf için strateji kurmak.

## Soğuk başlangıç (intake)
1. Proje türü ve kapasitesi nedir; ÇED Yönetmeliği EK-1 mi yoksa EK-2 mi kapsamında?
2. Hangi karar verilmiş: "ÇED Olumlu", "ÇED Gerekli", "ÇED Gerekli Değildir"? Tarihi ve ilanı?
3. Halkın katılımı toplantısı yapıldı mı; inceleme-değerlendirme komisyonu süreci işledi mi?
4. İtiraz eden tarafın menfaat bağı (komşuluk, yöre halkı, dernek) nedir?

## Denetim şeması
1. **Tabilik**: 2872 m.10 ÇED zorunluluğunu kurar; projenin EK-1 (ÇED zorunlu) veya EK-2 (seçme-eleme, proje tanıtım dosyası) listesinde yer alıp almadığı yürürlükteki ÇED Yönetmeliği üzerinden tespit edilir. Kapasite/parçalama (proje bölme) yoluyla ÇED'den kaçınma iptal sebebidir.
2. **Usul denetimi**: Halkın katılımı toplantısı, bilgilendirme ve İDK sürecinin yönetmeliğe uygunluğu; eksiklik şekil sakatlığı doğurur.
3. **Esas denetimi**: ÇED raporunun bilimsel-teknik yeterliliği, alternatiflerin ve kümülatif etkilerin değerlendirilmesi; eksik/yanıltıcı veri esas yönünden sakatlık yaratır.
4. **Yargı yolu ve süre**: İptal davası idari yargıda açılır (2577 sayılı İYUK m.7 — kural olarak 60 gün; ilan/öğrenme tarihi önem taşır). Yürütmenin durdurulması (m.27) telafisi güç zarar nedeniyle erken talep edilir.
5. **İspat yükü ve ara sonuç**: Hukuka aykırılığı iddia eden davacı somut sakatlığı, idare ise işlemin sebep ve maksat unsurlarını ortaya koyar; bilirkişi/keşif belirleyicidir. ÇED dosyasındaki tek bir esaslı eksik dahi iptale yetebilir.

## Çıktı modülleri
- Tabilik analizi (EK-1/EK-2 eşleştirmesi)
- Usul ve esas sakatlık kontrol listesi
- İptal dilekçesi iskeleti + yürütmenin durdurulması talebi
- Bilirkişi/keşif delil planı

## Plugin bağlamı

Bu beceri `cevre-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
