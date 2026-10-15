---
name: muvekkil-iletisimi-ve-bilgilendirme
description: "Müvekkili dosyanın seyri, riskleri ve seçenekleri hakkında bilgilendirme yazısı veya teklif/kapsam mektubu (engagement letter) hazırlanırken ve beklenti yönetimi gerektiğinde kullanılır."
---

# Müvekkil İletişimi ve Bilgilendirme

## Görev
Müvekkili dosyanın durumu, hukuki riskler, olası sonuçlar, süreler ve maliyetler hakkında sade ve doğru biçimde bilgilendirmek; beklentiyi yönetmek ve önemli kararları yazılı onaya bağlamak.

## Soğuk başlangıç (intake)
1. Bilgilendirmenin konusu ne (yeni iş teklifi, gelişme bildirimi, strateji kararı, olumsuz haber)?
2. Müvekkilin hukuki bilgi düzeyi ve tercih ettiği dil/ton nedir?
3. Müvekkilden bir karar/onay isteniyor mu (örn. sulh teklifi, kanun yoluna başvurma)?
4. Aktarılacak risk veya maliyet kalemleri neler?

## Denetim şeması
1. **Özen ve sadakat (TBK m.506; 1136 özen yükümü)**: Müvekkile dürüst, gerçekçi ve zamanında bilgi verilir; başarı garantisi verilmez, riskler gizlenmez.
2. **Kapsam netliği**: Engagement/kapsam mektubunda işin sınırı, dahil olmayan işler ve varsayımlar yazılır.
3. **Risk ve seçenek sunumu**: Her seçenek için olası sonuç, süre, maliyet ve risk dengeli biçimde aktarılır; karar müvekkilindir.
4. **Karar onayı**: Kritik kararlar (sulh, davadan feragat, kanun yolundan vazgeçme) yazılı talimata bağlanır (talimata uyma — TBK m.505); bu hem müvekkili korur hem de avukatın sorumluluğunu sınırlar.
5. **Sır ve gizlilik (1136 m.36)**: İletişim kanalı ve içeriği sır kapsamında; üçüncü kişilere paylaşım yapılmaz.
6. **Ara sonuç**: Doğru bilgi + dengeli risk + gereken yerde yazılı onay sağlanmışsa bilgilendirme tamamdır.

## Çıktı modülleri
- Müvekkil bilgilendirme/gelişme yazısı (sade dil).
- Kapsam/teklif mektubu (engagement letter) taslağı.
- Karar onay formu ([doldurulacak] seçenek ve sonuçları ile).

## Plugin bağlamı

Bu beceri `hukuk-burosu-yonetimi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
