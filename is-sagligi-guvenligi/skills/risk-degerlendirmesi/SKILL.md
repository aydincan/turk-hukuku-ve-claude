---
name: risk-degerlendirmesi
description: "İşyerinde risk değerlendirmesinin yapılıp yapılmadığını, kapsam ve güncelliğini değerlendirmek ve 6331 m.5 önleme hiyerarşisine uygun tedbir tasarlamak için kullanılır."
---

# Risk Değerlendirmesi ve Önleme Hiyerarşisi

## Görev
6331 m.10 ve Risk Değerlendirmesi Yönetmeliği çerçevesinde risk değerlendirmesinin varlığı, kapsamı, yöntemi ve güncelliğini denetlemek; m.5 önleme hiyerarşisine göre tedbir önerilerini sıralamak. Hem uyum hem de kaza dosyasında kusur tartışmasının çekirdeğidir.

## Soğuk başlangıç (intake)
- Risk değerlendirmesi yapılmış mı; tarihi ve kullanılan yöntem (ör. matris/L tipi) nedir?
- Tehlike sınıfı nedir (değerlendirmenin yenileme periyodunu belirler)?
- İşyerinde değişiklik (yeni makine, süreç, kaza, ramak kala) sonrası güncelleme yapıldı mı?
- Değerlendirmeye çalışan temsilcisi ve İSG profesyonelleri katıldı mı?

## Denetim şeması
1. **Varlık ve zaman (m.10):** Risk değerlendirmesi yapılmamışsa bu başlı başına yükümlülük ihlalidir; kaza sonrası kusur değerlendirmesinde belirleyici olur.
2. **Kapsam:** Tüm tehlikeler (mekanik, kimyasal, ergonomik, psikososyal, biyolojik) ve etkilenebilecek çalışanlar (genç, gebe, engelli, alt işveren çalışanı) kapsanmış mı?
3. **Yöntem ve güncellik:** Tehlike sınıfına göre yenileme süresi (genelde çok tehlikeli 2, tehlikeli 4, az tehlikeli 6 yıl) ile değişiklik/kaza halinde derhal güncelleme yükümlülüğü.
4. **Önleme hiyerarşisi (m.5):** Önerilen tedbirler sırasıyla: riski ortadan kaldırma → kaynağında önleme → ikame → mühendislik/toplu koruma → idari önlem → kişisel koruyucu donanım. KKD daima son sırada; sadece KKD verilmiş olması yetersizdir.
5. **İspat ve illiyet:** Gerçekleşen kazadaki tehlikenin değerlendirmede öngörülüp öngörülmediği, öngörüldüyse tedbirin uygulanıp uygulanmadığı kusur oranını doğrudan etkiler. **Ara sonuç:** Öngörülmüş + tedbir alınmamış = ağır kusur karinesi.

## Çıktı modülleri
- Risk değerlendirmesi yeterlilik kontrol listesi.
- Tehlike-tedbir-hiyerarşi eşleştirme tablosu.
- Kaza dosyası için "öngörülebilirlik" değerlendirme notu.

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
