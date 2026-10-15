---
name: velayet-ve-kisisel-iliski
description: "Velayetin hangi tarafa verileceği, kişisel ilişki (görüş) düzeninin kurulması, velayetin değiştirilmesi veya kaldırılması ve çocuğun üstün yararının somutlaştırılması gerektiğinde kullanılır."
---

# Velayet ve Çocukla Kişisel İlişki

## Görev
Çocuğun üstün yararı ölçütüyle velayetin tevdii (TMK m.182, m.336), kişisel ilişki düzeninin (m.182-183, m.323-324) kurulması ve velayetin değiştirilmesi/kaldırılması şartlarının denetlenmesi.

## Soğuk başlangıç (intake)
1. Çocuğun yaşı, sağlık/eğitim durumu ve kiminle, nerede yaşadığı nedir?
2. Ebeveynlerin bakım kapasitesi, çalışma düzeni ve çocukla bağı nasıl?
3. İhmal, şiddet, bağımlılık, çocuğun kaçırılması gibi bir risk var mı?
4. İstenen kişisel ilişki sıklığı (hafta içi/sonu, yarıyıl, yaz, dini bayram) nedir?

## Denetim şeması
1. **Velayetin tevdii.** Evlilik içinde velayet ana-baba tarafından birlikte kullanılır (m.336/1); boşanmada hâkim çocuğu velayeti kendisine bırakılmayan taraf ile kişisel ilişki dahil düzenler (m.182). Ölçüt münhasıran **çocuğun üstün yararıdır**; ekonomik üstünlük tek başına belirleyici değildir. İdrak çağındaki çocuğun görüşü alınır (BM Çocuk Hakları Sözleşmesi m.12; uygulamada pedagog/uzman raporu).
2. **Kişisel ilişki düzeni.** m.182-183, m.323: velayet kendisinde olmayan taraf ile çocuk arasında somut, uygulanabilir bir takvim kurulur; ana-babadan başka kişilerle (örn. büyükanne-baba) kişisel ilişki m.325.
3. **Değiştirme/kaldırma.** Durumun değişmesi (m.183) — örn. velayet sahibinin ağır ihmali, başka yere yerleşmesi, çocuğun yararının zedelenmesi — velayetin değiştirilmesini gerektirebilir. Ağır hallerde velayetin kaldırılması (m.348) ve çocuğun korunmasına ilişkin tedbirler (m.346-347).
4. **İcra ve uluslararası boyut.** Kişisel ilişki kararlarının yerine getirilmesinde teslim/kişisel ilişki tesisi ADM (Adalet Bakanlığı/müdürlük) ve 5395 sK. ile ilgili mekanizmalar; çocuk kaçırma hallerinde 1980 Lahey Sözleşmesi.
5. **Ara sonuç.** Velayet önerisi + kişisel ilişki takvimi + risk/koruma tedbiri değerlendirmesi.

## Çıktı modülleri
- Üstün yarar değerlendirme matrisi (bakım, istikrar, bağ, risk).
- Somut kişisel ilişki takvimi taslağı.
- Velayetin değiştirilmesi/kaldırılması için dayanak ve delil listesi.

## Plugin bağlamı

Bu beceri `aile-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
