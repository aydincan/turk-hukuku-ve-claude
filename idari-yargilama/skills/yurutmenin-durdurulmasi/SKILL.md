---
name: yurutmenin-durdurulmasi
description: "İdari işlemin uygulanması telafisi güç zarar doğuracaksa ve işlem açıkça hukuka aykırıysa geçici koruma talebinin hazırlanmasında kullanılır; YD şartlarının değerlendirilmesi, teminat ve itiraz yolları gündeme geldiğinde başvurulur."
---

# Yürütmenin Durdurulması (YD)

## Görev
İYUK m.27 koşullarını somut olaya uygulayarak güçlü gerekçeli bir yürütmenin durdurulması talebi kurmak; itiraz yolu ve usule ilişkin özellikleri yönetmek.

## Soğuk başlangıç (intake)
- İşlemin uygulanması hangi somut ve telafisi güç zararı doğurur?
- İşlemin açık hukuka aykırılığı hangi unsurda ve hangi delille gösterilebilir?
- İşlem henüz uygulanmaya başladı mı; aciliyet derecesi nedir?
- Talep dava dilekçesiyle birlikte mi, ayrı dilekçeyle mi ileri sürülecek?

## Denetim şeması
1. **İki şartın birlikteliği** (İYUK m.27/2): YD kararı için (i) işlemin uygulanması hâlinde **telafisi güç veya imkânsız zarar** doğması ve (ii) işlemin **açıkça hukuka aykırı** olması şartlarının **birlikte** gerçekleşmesi ve kararda **gerekçe** gösterilmesi zorunludur.
2. **Gerekçe zorunluluğu**: YD isteminin reddi veya kabulü gerekçeli olmalıdır; standart kalıp gerekçe yeterli değildir. Talepte iki şart ayrı ayrı somutlaştırılır.
3. **Teminat** (İYUK m.27/6): Kural olarak YD kararı teminat karşılığında verilir; ancak durumun gereklerine göre teminat aranmayabilir. İdareden ve adli yardımdan yararlananlardan teminat alınmaz.
4. **Vergi davalarında özel rejim**: Vergi mahkemelerinde dava açılması tarh edilen vergi/cezanın tahsilini kural olarak durdurur (İYUK m.27/4); bu nedenle ayrı YD talebine her zaman gerek olmayabilir. İhtirazi kayıt ve ödeme emri hâlleri ayrıdır.
5. **İtiraz** (İYUK m.27/7): YD istemleri hakkındaki kararlara karşı, kararın tebliğini izleyen günden itibaren **7 gün** içinde bir defaya mahsus itiraz edilebilir. İtirazı, idare/vergi mahkemesi kararlarında bölge idare mahkemesi inceler.
6. **Ara sonuç**: YD kararı işlemin tesisinden önceki hukuki durumu askıya alır; idare kararın gereğini gecikmeksizin uygulamak zorundadır (Anayasa m.138/4; İYUK m.28).

## Çıktı modülleri
- m.27 iki şart için somut gerekçe metni
- Teminat ve aciliyet değerlendirmesi
- YD talep paragrafı (dilekçeye eklenebilir)

## Plugin bağlamı

Bu beceri `idari-yargilama` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
