---
name: yz-yonetisim-uyum-programi
description: "Bir kurumda yapay zekâ sistemlerinin geliştirilmesi veya kullanılması için iç politika, etki değerlendirmesi, envanter, insan gözetimi ve sorumluluk yapısı kurulması istendiğinde proaktif uyum programı tasarlandığında kullanılır."
---

# Kurumsal Yapay Zekâ Yönetişimi ve Uyum Programı

## Görev
Bir kurumun yapay zekâ kullanımını hukuki riske karşı yöneten iç yönetişim programını tasarlamak: envanter, politika, etki değerlendirmesi, insan gözetimi ve sorumluluk dağılımı.

## Soğuk başlangıç (intake)
1. Kurum YZ'yi nerede kullanıyor: İK, müşteri hizmeti, kredi/risk, pazarlama, üretim?
2. Sistemler iç geliştirme mi, üçüncü taraf (kapalı API) mi?
3. Kişisel veri ve özel nitelikli veri işleniyor mu; VERBİS kaydı var mı?
4. Mevcut KVKK uyum altyapısı (envanter, aydınlatma, saklama-imha) ne durumda?

## Denetim şeması
1. **Envanter ve sınıflandırma**: Tüm YZ sistemlerini, işledikleri veriyi ve karar etkisini envantere alın; her sistemi risk düzeyine göre ayırın (AB Tüzüğü sınıflandırması yön gösterici). Ara sonuç: yüksek etkili sistemler önceliklendirilir.
2. **KVKK uyumu**: m.4 ilkeler, m.5-6 işleme şartı, m.10 aydınlatma (otomatik karar açıklaması), m.11 hak süreçleri, m.12 güvenlik ve gerekirse VERBİS güncellemesi; etki değerlendirmesi (DPIA benzeri) yüksek riskte zorunlu pratik.
3. **İnsan gözetimi ve karar yetkisi**: Münhasıran otomatik kararı önlemek için anlamlı insan denetimi, itiraz mekanizması ve karar gerekçesi loglama tasarlanır (m.11/1-g riski yönetimi).
4. **Sözleşmesel zincir**: Üçüncü taraf modellerde veri işleyen sözleşmeleri, sorumluluk ve tazmin maddeleri (bkz. YZ sözleşmeleri becerisi).
5. **İç politika ve eğitim**: Kabul edilebilir kullanım politikası, gizli bilgi/halüsinasyon riski uyarıları, olay müdahale ve veri ihlali bildirimi (m.12) akışı.

Kurul rehberlerini kvkk.gov.tr'den güncel takip et; doğrulanmamış kaynağı [doğrulanacak] işaretle.

## Çıktı modülleri
- YZ envanteri ve risk sınıflandırma tablosu.
- Uyum boşluğu raporu ve aksiyon planı.
- İç politika ve insan gözetimi prosedürü taslağı.

## Plugin bağlamı

Bu beceri `yapay-zeka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
