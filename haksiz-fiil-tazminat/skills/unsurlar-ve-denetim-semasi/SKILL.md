---
name: unsurlar-ve-denetim-semasi
description: "Bir zarar olayının haksız fiil sorumluluğu doğurup doğurmadığını baştan sona değerlendirmek gerektiğinde; fiil, hukuka aykırılık, kusur, zarar ve illiyet unsurlarını sırayla altlamak için ilk adımda kullanılır."
---

# Haksız Fiilin Unsurları ve Genel Denetim Şeması

## Görev
Somut olayı TBK m.49 çerçevesinde beş unsurun (fiil, hukuka aykırılık, kusur, zarar, uygun illiyet bağı) tek tek varlığına göre denetlemek; sonra olaya özgü objektif sorumluluk normuyla yarışmayı kontrol etmek. Eksik tek unsur talebi tümden düşürür; bu yüzden zincir baştan sona kurulur.

## Soğuk başlangıç (intake)
- Ne oldu, kim yaptı, zarar tam olarak nedir (mal varlığı mı, beden/can mı, kişilik hakkı mı)?
- Olay tarihi ve zarar görenin bunu/faili öğrendiği tarih?
- Taraflar arasında sözleşme ilişkisi var mı (yarışma ihtimali)?
- Olaya özgü bir özel rejim var mı (trafik, işveren, ürün, yapı)?

## Denetim şeması
1. **Fiil (m.49).** İnsan davranışı: olumlu eylem ya da hukuken yapma yükümü varken kaçınma (ihmali davranış). Failin belirlenebilirliği saptanır.
2. **Hukuka aykırılık (m.49).** Mutlak hak ihlali (yaşam, beden, mülkiyet, kişilik) doğrudan; salt malvarlığı zararında ihlal edilen koruma normu veya ahlaka aykırı kasıtlı davranış (m.49/2) aranır. Hukuka uygunluk sebebi (m.63) varsa aykırılık kalkar.
3. **Kusur (m.49).** Kast ya da ihmal. Ölçü objektifleştirilmiş özen (basiretli kişi). Kusursuz sorumluluk normu uygulanacaksa bu unsur aranmaz.
4. **Zarar.** Fiili zarar + yoksun kalınan kâr (maddi) ve/veya manevi zarar. Malvarlığında istem dışı azalma; farazi malvarlığı ile gerçek arasındaki fark esas alınır.
5. **Uygun illiyet bağı.** Fiil ile zarar arasında hayatın olağan akışına ve genel hayat tecrübesine göre uygun nedensellik; mücbir sebep, zarar görenin/üçüncü kişinin ağır kusuru bağı kesebilir.
6. **Ara sonuç.** Beş unsur tamsa sorumluluk kurulur; eksikse hangi unsurun düştüğü ve ispat yükünün kimde olduğu (TMK m.6) not edilir. Objektif sorumluluk normu (m.65-71) seçimlik olarak değerlendirilir.

## Çıktı modülleri
- Unsur-vakıa-delil altlama tablosu (her unsur için var/yok/şüpheli).
- Yarışma notu (sözleşme ↔ haksız fiil; süre/ispat etkisi).
- Eksik unsur ve ispat yükü haritası.

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
