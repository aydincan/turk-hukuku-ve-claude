---
name: itirazin-iptali-kaldirilmasi-menfi-tespit
description: "Ödeme emrine itiraz nedeniyle duran takipte hangi davanın açılacağına karar vermek; itirazın iptali, itirazın kaldırılması veya menfi tespit-istirdat davasını kurgulamak ve icra inkâr/kötüniyet tazminatını değerlendirmek için kullanılır."
---

# İtirazın İptali, İtirazın Kaldırılması ve Menfi Tespit

## Görev
Duran takibi devam ettirmek için itirazın iptali (m.67) ile itirazın kaldırılması (m.68 vd.) arasında seçim yapmak; borçlu tarafında menfi tespit/istirdat (m.72) ile savunma kurmak; tazminat risk ve fırsatlarını yönetmek.

## Soğuk başlangıç (intake)
- Elde m.68'deki belge (imzası ikrar/noterlikçe onaylı belge, resmî kayıt) var mı?
- İtiraz tebliğ/öğrenme tarihi nedir (iptal 1 yıl, kaldırma 6 ay)?
- Borç gerçekten var mı; ödeme/takas/zamanaşımı def'i var mı?
- Tazminat (icra inkâr/kötüniyet) talebi gündemde mi?

## Denetim şeması
1. **Yol seçimi**: m.68'deki nitelikli belge varsa hızlı yol olan **itirazın kaldırılması** (icra mahkemesi, dar inceleme); belge yoksa **itirazın iptali** (genel mahkeme, tam yargılama, m.67).
2. **İtirazın iptali (m.67)**: 1 yıllık hak düşürücü süre; dava kabul edilirse itiraz iptal edilir, takip devam eder. Borçlu itirazında haksız ve alacak likit ise alacaklı lehine en az %20 **icra inkâr tazminatı**; dava reddedilir ve takip kötüniyetli ise borçlu lehine aynı oranda tazminat.
3. **İtirazın kaldırılması (m.68, m.68/a, m.69)**: 6 aylık süre; icra mahkemesi yalnızca belge üzerinden karar verir, yargılama yapmaz. İmzaya itirazın kaldırılması m.68/a usulüne tabidir.
4. **Menfi tespit/istirdat (m.72)**: Borçlu, borçlu olmadığının tespitini takipten önce/sonra isteyebilir; takipten sonra teminatla icranın durdurulması mümkündür. Ödedikten sonra istirdat 1 yıl içinde açılır. Haksız takipte borçlu lehine %20 tazminat.
5. **İspat yükü**: İtirazın kaldırılmasında alacaklı belgeyle; menfi tespitte kural olarak borçlu borcun bulunmadığını, ancak alacağın varlığını alacaklı ispatlar (ispat yükü ters çevrilmez).
6. **Ara sonuç**: Hız/maliyet/ispat gücüne göre yol ve tazminat stratejisi netleşir.

## Çıktı modülleri
- Yol seçim notu (belge envanteri + süre).
- Dava dilekçesi iskeleti (iptal/kaldırma/menfi tespit).
- Tazminat ve teminat değerlendirmesi.

## Plugin bağlamı

Bu beceri `icra-iflas-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
