---
name: yolsuz-tescil-ve-duzeltim
description: "Tapu kaydındaki yolsuzluğun veya teknik/maddi hatanın (isim, soyadı, ada-parsel, pay, kimlik, mevki, yüzölçüm) giderilmesi gerektiğinde; idari düzeltme yolu ile düzeltim davası arasında ayrım yapmak ve iyiniyetli üçüncü kişi korumasını değerlendirmek için kullanılır."
---

# Yolsuz Tescil ve Tapu Kaydının Düzeltilmesi

## Görev
Yolsuz tescili veya kayıttaki maddi/teknik hatayı uygun yolla (idari düzeltme ya da düzeltim davası) gidermek; iyiniyetli üçüncü kişi korumasının sınırını çizmek.

## Soğuk başlangıç (intake)
- Hata türü ne: malik kimliği (ad-soyad-baba adı-TC), pay oranı, ada-parsel/mevki, yüzölçüm, sınır mı?
- Hata kayıttan mı (yazım/teknik) yoksa hukuki sebepten mi (geçersiz devir) kaynaklanıyor?
- Kayıt üzerinde sonradan iyiniyetli üçüncü kişi kazanımı oluşmuş mu?
- Tapu müdürlüğüne idari başvuru yapıldı mı, sonuç ne oldu?

## Denetim şeması
1. **Hatanın kaynağını ayır.** Salt yazım/teknik hata (kimlik bilgisi, yüzölçüm, mevki) → idari düzeltme yolu (2644 sayılı Tapu Kanunu m.31 ve Tapu Sicili Tüzüğü; tapu müdürlüğü re'sen veya talep üzerine düzeltir). Hukuki sebepten kaynaklanan yolsuzluk → düzeltim/iptal davası.
2. **Yolsuz tescili tanımla.** Bağlayıcı olmayan bir hukuki işleme dayanan veya hukuki sebepten yoksun tescil yolsuzdur (TMK m.1024). Gerçek hak sahibi düzeltme isteyebilir (TMK m.1025).
3. **Üçüncü kişi süzgeci.** Yolsuz tescile güvenerek iyiniyetle ayni hak kazanan üçüncü kişi korunur (TMK m.1023); düzeltim ona karşı ileri sürülemez, bu halde TMK m.1007 tazminatı gündeme gelir.
4. **İdari yolun sınırı.** İdari düzeltme yalnızca tarafların ve üçüncü kişilerin haklarını etkilemeyen, çekişmesiz teknik hatalarda mümkündür. Maliki/payı değiştirecek nitelikte ise dava şarttır.
5. **Görev/yetki ve husumet.** Düzeltim davasında görevli asliye hukuk, yetki taşınmaz yeri (HMK m.12); husumet kayıt maliki/ilgililer ve gerektiğinde Hazine.
6. **İspat.** Nüfus kaydı, veraset ilamı, eski akit tablosu, kadastro tutanağı, fen bilirkişisi (yüzölçüm/sınır).
7. **Ara sonuç.** İdari düzeltme yeterli mi yoksa dava mı; üçüncü kişi engeli var mı.

## Çıktı modülleri
- İdari yol mu / dava mı karar ağacı.
- Tapu müdürlüğüne düzeltme dilekçesi veya düzeltim davası iskeleti.
- İyiniyetli üçüncü kişi / TMK m.1007 tazminat alternatifi notu.

## Plugin bağlamı

Bu beceri `tapu-kadastro` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
