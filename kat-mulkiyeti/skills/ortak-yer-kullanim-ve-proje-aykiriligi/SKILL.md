---
name: ortak-yer-kullanim-ve-proje-aykiriligi
description: "Ortak yerlerin (çatı, cephe, bahçe, çekme kat, sığınak, otopark) izinsiz işgali/değiştirilmesi, bağımsız bölümün projeye veya tahsis amacına aykırı kullanımı (mesken-işyeri dönüşümü dahil) söz konusu olduğunda; eski hâle getirme ve men talebini kurmak için kullanılır."
---

# Ortak Yer Kullanımı ve Projeye Aykırılığın Giderilmesi

## Görev
Ortak yerlerde izinsiz değişiklik/işgali ve bağımsız bölümün projeye, yönetim planına veya tahsis amacına aykırı kullanımını tespit edip durdurmak; eski hâle getirme (men ve aykırılığın giderilmesi) talebini kurmak.

## Soğuk başlangıç (intake)
- Aykırılık nerede: ortak yerde mi (cephe, çatı, bahçe, kapıcı dairesi, otopark) yoksa bağımsız bölümde mi?
- Yapılan değişiklik nedir: çatı katı/ilave inşaat, cephe kapatma, ortak yere el atma, mesken→işyeri dönüşümü?
- Değişiklik için kurul kararı/oybirliği alındı mı; projeye uygun mu?
- Aykırılık ne zaman başladı; ruhsat/yapı kayıt belgesi var mı?

## Denetim şeması
1. **Ortak yerde değişiklik yasağı (KMK m.19)**: Kat malikleri, anagayrimenkulün bakım ve mimari durumu ile estetiğini titizlikle korumakla yükümlüdür. Kendi bağımsız bölümünde dahi, anataşınmaza zarar verecek veya mimari durumu/estetiği bozacak onarım/tesis/değişiklik yapamaz (m.19/2). Ortak yerlerde esaslı değişiklik **bütün maliklerin oybirliğini** gerektirir.
2. **İzinsiz yapılan değişiklik**: Oybirliği/izin olmadan yapılan değişiklik için her kat maliki eski hâle getirme (men ve refi) talep edebilir; mahkeme aykırılığın giderilmesine karar verir (m.33 ile m.19 birlikte).
3. **Tahsis amacına aykırı kullanım (m.24)**: Anagayrimenkulün, kütükte mesken, iş veya ticaret yeri olarak gösterilen bağımsız bölümü, başka türde kullanılamaz; özellikle hastane, dispanser, klinik, ECZane, sinema, kahvehane, gazino, dans salonu, fırın, lokanta, pavyon gibi yerler **mesken bağımsız bölümde** ancak yönetim planında izin verilmiş veya **bütün maliklerin oybirliğiyle** karar alınmışsa açılabilir (m.24/2). Bazı işyerleri kütükte mesken görünse de açılamaz.
4. **Faydalı/lüks yenilik ayrımı (m.42)**: Ortak yerlerde herkesin yararına yenilik (örn. asansör, ısı yalıtımı) sayı ve arsa payı çoğunluğuyla; çok masraflı/lüks yenilikler ise yararlanmayan malikin katılımı zorunlu kılınmadan yapılabilir, masrafı isteyenler öder.
5. **İlave inşaat / kat ilavesi (m.44)**: Anagayrimenkule yeni kat/eklenti yapılması, arsa payı yeniden düzenlenmesini gerektirir ve **oybirliği** ile mümkündür.
6. **İspat ve keşif**: Projeye/ruhsata aykırılık genellikle onaylı proje karşılaştırması ve keşif-bilirkişi (mimar/inşaat) ile saptanır.
7. **Ara sonuç**: İzinsiz/oybirliksiz değişiklik veya amaç dışı kullanım varsa men + eski hâle getirme; yenilik ise m.42 nisabı denetimi.

## Çıktı modülleri
- Aykırılığın giderilmesi (men + eski hâle getirme) dava dilekçesi iskeleti.
- Onaylı proje / yapılan değişiklik karşılaştırma notu (keşif-bilirkişi talebi).
- Nisap/oybirliği taraması (m.19, m.24, m.42, m.44).
- İhtiyati tedbir notu (devam eden inşaatın durdurulması).

## Plugin bağlamı

Bu beceri `kat-mulkiyeti` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
