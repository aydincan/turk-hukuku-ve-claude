---
name: yetkilendirme-isletmeci-uyum
description: "Elektronik haberleşme hizmeti sunmak için bildirim veya kullanım hakkı türü yetkilendirme, işletmeci yükümlülükleri, kaynak tahsisi ve yetkilendirme iptali/iadesi değerlendirildiğinde ve BTK yetkilendirme rejimi uyumu kontrol edileceğinde kullanılır."
---

# Yetkilendirme ve İşletmeci Uyum Şeması

## Görev
Bir elektronik haberleşme faaliyetinin doğru yetkilendirme türüne tabi olup olmadığını, işletmeci yükümlülüklerinin yerine getirilip getirilmediğini ve iptal/iade riskini denetleyerek BTK uyum yol haritası çıkarmak.

## Soğuk başlangıç (intake)
1. Sunulan hizmet türü nedir (sabit/mobil, internet servis sağlayıcılığı, altyapı, sanal mobil, katma değerli)?
2. Yetkilendirme türü: bildirime mi yoksa kullanım hakkına mı (frekans/numara/uydu pozisyonu kaynak tahsisi gerektiren) tabi?
3. Yetkilendirme alındı mı, hangi tarihli; kaynak tahsisi (frekans/numara) var mı?
4. BTK'ya bildirim, ücret ve raporlama yükümlülükleri güncel mi?

## Denetim şeması
1. **Yetkilendirme gerekliliği ve türü**: 5809 m.8-9 — kaynak tahsisi gerektirmeyen hizmetler bildirim, frekans/numara/uydu pozisyonu gibi sınırlı kaynak gerektirenler kullanım hakkı kapsamındadır. Yetkilendirme Yönetmeliği eşik ve usulü belirler. Ara sonuç: bildirim mi kullanım hakkı mı.
2. **Başvuru ve şartlar**: Bildirimde BTK'ya beyan; kullanım hakkında ihale/tahsis usulü, idari ücret ve kullanım hakkı ücreti. İspat ve belge yükü başvurucudadır; eksiklik ret/iade doğurur.
3. **Yükümlülükler**: 5809 — idari ücret, evrensel hizmet katkısı, raporlama, tüketici hakları (m.47-50) ve gizlilik (m.51) uyumu; tesis paylaşımı/arabağlantı (m.17-21) yükümlülükleri ilgili pazarda etkin piyasa gücüne (EPG) bağlı olabilir.
4. **Tadil/yenileme/iade**: Yetkilendirme süresi, yenileme ve devir BTK iznine tabi; kaynak iadesi ve hizmet sonlandırmada abone koruma yükümlülükleri gözetilir.
5. **İptal/sona erme**: Yükümlülük ihlali, ücret ödenmemesi veya kaynak amacına aykırı kullanım yetkilendirme iptalini doğurabilir; iptal idari işlem olduğundan İYUK m.7 süresinde dava ve m.27 yürütmenin durdurulması değerlendirilir.

İlkesel içtihat için BTK yetkilendirme/iptal uyuşmazlıklarında karararama.danistay.gov.tr (13. Daire ağırlıklı) taranır; künye doğrulanmadan [doğrulanacak] işaretlenir.

## Çıktı modülleri
- Yetkilendirme uyum kontrol listesi (yükümlülük/durum/eksik).
- Kaynak tahsisi ve ücret riski tablosu.
- Tadil/yenileme başvurusu veya iptale karşı dava stratejisi taslağı.

## Plugin bağlamı

Bu beceri `telekomunikasyon-bilisim` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
