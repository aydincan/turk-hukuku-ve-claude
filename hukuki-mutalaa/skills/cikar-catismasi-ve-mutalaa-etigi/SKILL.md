---
name: cikar-catismasi-ve-mutalaa-etigi
description: "Mütalaa hazırlamadan önce çıkar çatışması, sır saklama ve bilimsel mütalaa veren akademisyen/uzmanın tarafsızlık yükümlülüğünü denetlemek gerektiğinde kullanılır; mütalaanın kabul edilebilirliğini ve güvenilirliğini korur."
---

# Çıkar Çatışması ve Mütalaa Etiği

## Görev
Mütalaa işini kabul etmeden önce çıkar çatışması, sır saklama ve tarafsızlık yükümlülüklerini denetlemek; özellikle HMK m.293 uyarınca dosyaya sunulacak uzman görüşlerinde mütalaayı verenin bağımsızlığını ve metnin güvenilirliğini korumak.

## Soğuk başlangıç (intake)
- Mütalaayı talep eden ve karşı taraf kim; daha önce bu taraflardan biriyle ilişki kuruldu mu?
- Görüş mahkemeye uzman görüşü olarak mı sunulacak (HMK m.293), yoksa danışmanlık mı?
- Talep edilen sonuç önceden dayatılıyor mu ("şu sonucu çıkaran mütalaa")?
- Sır niteliğinde bilgi içeriyor mu?

## Denetim şeması
1. Çıkar çatışması taraması: Aynı uyuşmazlıkta karşı tarafa daha önce hizmet verildi mi, taraflardan biriyle menfaat bağı var mı? Avukat için 1136 sayılı Avukatlık Kanunu m.38 (işi reddetme zorunluluğu) ve meslek kuralları; çatışma varsa iş reddedilir.
2. Sır saklama: Avukatlık Kanunu m.36 ve TBK vekâlet hükümleri — mütalaa hazırlanırken öğrenilen bilgiler sır kapsamındadır; üçüncü kişiyle paylaşılmaz.
3. Bilimsel mütalaada tarafsızlık: HMK m.293 uzman görüşü, ücreti tarafça ödense de bilimsel dürüstlükle yazılmalıdır; sipariş üzerine sonuç üretmek (advokatlaşmış mütalaa) belgenin ispat değerini düşürür ve etik sorun doğurur. Aleyhe argüman tartışılır.
4. Sonuç dayatması testi: Talep eden belirli bir sonucu zorluyorsa, mütalaa ya gerçek hukuki durumu yazar ya da iş reddedilir; gerçeğe aykırı görüş üretilmez.
5. Hukuki danışmanlık sınırı: Mütalaa genel hukuki değerlendirmedir; vekâlet ilişkisi ve fiili dava temsili ayrı sözleşme gerektirir; bu sınır belirtilir.
6. Ara sonuç: İş kabul edilebilir mi + etik uyarılar + tarafsızlık/sır notları.

## Çıktı modülleri
- Çıkar çatışması kontrol listesi (taraf | önceki ilişki | sonuç)
- Sır saklama ve gizlilik notu
- Tarafsızlık beyanı taslağı (HMK m.293 görüşü için)
- İş kabul/ret değerlendirmesi

## Plugin bağlamı

Bu beceri `hukuki-mutalaa` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
