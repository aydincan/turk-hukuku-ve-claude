---
name: kadastro-tespitine-itiraz
description: "Kadastro çalışması sırasında veya askı ilanından sonra tespit edilen malik, sınır, yüzölçüm ya da nitelik hatasına itiraz edilirken; kadastro tutanağının kesinleşmesi, 10 yıllık hak düşürücü süre ve kadastro mahkemesinin görevi söz konusu olduğunda kullanılır."
---

# Kadastro Tespitine İtiraz ve Kadastro Davası

## Görev
Kadastro tespitindeki malik/sınır/yüzölçüm hatasına karşı doğru zaman, mercii ve dayanakla itiraz/dava kurmak; tutanağın kesinleşip kesinleşmediğini ve hangi yolun açık olduğunu belirlemek.

## Soğuk başlangıç (intake)
- Kadastro çalışması hangi aşamada: tespit anı mı, 30 günlük askı ilanı mı, tutanak kesinleşmiş mi?
- İtiraz neye: malik tespiti mi, sınır/yüzölçüm mü, niteliğe (mera, yol, orman) mı?
- Taşınmaz tapulu mu, tapusuz zilyetlik mi; dayanak kayıt/zilyetlik var mı?
- Tutanağın kesinleşme tarihi ve üzerinden geçen süre nedir?

## Denetim şeması
1. **Aşamayı belirle.** Tespite itiraz kadastro teknisyenliğine/komisyona; askı ilanı 30 gün (3402 sayılı Kanun m.11). İlana itiraz çözülmezse iş kadastro mahkemesine taşınır (m.25 vd.).
2. **Tespit dayanağını denetle.** Kayda dayalı tespit (m.13), kayıt dışı/zilyetliğe dayalı tespit (m.14): 20 yıl çekişmesiz nizasız malik sıfatıyla zilyetlik, vergi kaydı, kültür arazisi 40 dönüm / sulu-kuru sınırları; kamu malları kadastro dışı (m.16, m.18).
3. **Kesinleşme ve hak düşürücü süreyi kontrol et.** Kadastro tutanağının kesinleştiği tarihten itibaren 10 yıl geçmedikçe önceki hukuki sebebe dayanan iddia dinlenir; 10 yıl geçtikten sonra kadastrodan önceki sebebe dayanılarak dava açılamaz (3402 m.12/3). Bu süre hak düşürücüdür, re'sen gözetilir.
4. **Görev ve husumet.** Kesinleşmeden önce kadastro mahkemesi münhasıran görevli (m.25); kesinleştikten sonra genel mahkemede tapu iptali-tescil. Husumet kayıt malikine, Hazineye veya ilgili kamu idaresine yöneltilir.
5. **İspat planı.** Eski tapu/zabıt kaydı, vergi kaydı, keşif + fen bilirkişisi (sınır/yüzölçüm), yerel bilirkişi ve tanık (zilyetliğin süresi/niteliği), hava fotoğrafı; orman/mera niteliğinde uzman bilirkişi.
6. **Ara sonuç.** Açık yol (komisyon itirazı / kadastro mahkemesi / genel mahkeme) ve süre durumu netleştirilir.

## Çıktı modülleri
- Aşama–mercii–süre tablosu (hangi yol, hangi süre, hak düşürücü mü).
- İtiraz/dava dilekçesi iskeleti, talep sonucu ve delil listesi.
- 10 yıllık hak düşürücü süre risk notu.

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
