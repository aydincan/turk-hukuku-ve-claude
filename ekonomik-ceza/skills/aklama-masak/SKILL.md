---
name: aklama-masak
description: "Suçtan kaynaklanan malvarlığı değerlerini aklama (TCK m.282) iddiası, öncül suç tartışması, MASAK şüpheli işlem bildirimi ve yükümlü sorumluluğu söz konusu olduğunda; aklama soruşturmasında savunma veya uyum kurgusu gerektiğinde kullanılır."
---

# Aklama (Kara Para) ve MASAK Yükümlülükleri

## Görev
TCK m.282 aklama suçunun unsurlarını öncül suç ekseninde denetlemek; 5549 sayılı Kanun kapsamında yükümlü (banka, aracı kurum, gerçek/tüzel kişi) sorumluluğunu ve MASAK sürecini ele almak.

## Soğuk başlangıç (intake)
- Öncül (kaynak) suç ne, sabit mi, yoksa iddia mı?
- Hangi malvarlığı değeri, hangi işlemle "akladı" iddia ediliyor?
- Müvekkil yükümlü mü (banka/aracı kurum) yoksa fail mi konumunda?
- MASAK/şüpheli işlem bildirimi veya elkoyma kararı var mı?

## Denetim şeması
1. **Öncül suç (TCK m.282/1)**: Aklamanın ön şartı, malvarlığı değerinin "suçtan kaynaklanması"dır. Öncül suçun varlığı/kanıtı tartışılır; öncül suç sabit değilse aklama da sakatlanır. Öncül suçun kesin mahkûmiyeti şart değildir, ancak suç teşkil eden bir kaynak ortaya konmalıdır.
2. **Fiil**: Değeri "yurt dışına çıkarma" veya "gayrimeşru kaynağını gizleme/niteliğini değiştirme" fiilleri. Salt elde bulundurma yetmez; aklama fiili (gizleme/dönüştürme/aklamaya yönelik işlem) aranır.
3. **Manevi unsur**: Kast; failin değerin suçtan kaynaklandığını bilmesi (TCK m.21).
4. **Nitelikli haller ve etkin pişmanlık**: TCK m.282/3 (kamu görevlisi/belli meslek) ve m.282/6 etkin pişmanlık (soruşturma başlamadan önce değerlerin teslimi) kontrol edilir.
5. **Yükümlü sorumluluğu**: 5549 sayılı Kanun — müşterini tanı, şüpheli işlem bildirimi (ŞİB), muhafaza-ibraz. İhlal idari para cezası doğurur; ŞİB'in gizliliği (ifşa yasağı) önemlidir.
6. **Elkoyma/müsadere**: CMK m.128 (taşınmaz, hak, alacak) ve TCK m.54-55 müsadere; aklama dosyalarının ekonomik ağırlığı buradadır.
7. **Ara sonuç**: Öncül suç-aklama bağı, aklama fiilinin gerçekliği, kast ve yükümlülük ihlali ayrı ayrı değerlendirilir.

## Çıktı modülleri
- Öncül suç-aklama bağ analizi
- Fiil tipi (gizleme/dönüştürme/yurt dışı) nitelendirmesi
- Yükümlü uyum/ihlal değerlendirmesi
- Elkoyma-müsadere risk notu
- Savunma veya etkin pişmanlık stratejisi taslağı

## Plugin bağlamı

Bu beceri `ekonomik-ceza` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
