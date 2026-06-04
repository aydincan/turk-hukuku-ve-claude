---
name: dava-dilekcesi-hazirlama
description: "Kullanıcı mahkemeye verilecek dava dilekçesini yazmak istediğinde, talep sonucunu netleştirmek, vakıaları sıralamak ve delilleri bağlamak istediğinde kullanılır."
---

# Dava Dilekçesi Hazırlama (HMK m.119)

## Görev
HMK m.119'a uygun, eksiksiz, talep sonucu net ve delilleri bağlanmış bir dava dilekçesi iskeleti üretmek.

## Soğuk başlangıç (intake)
- Tarafların tam ad, T.C. kimlik no ve adresleri nedir?
- Tam olarak ne talep ediyorsunuz (para ise tutar, fer'iler dâhil)?
- Olay nasıl gelişti (tarih sırasıyla)?
- Her iddianızı hangi belge/tanıkla ispatlayacaksınız?
- Zorunlu arabuluculuk/ön başvuru yapıldıysa belgesi var mı?

## Denetim şeması
1. **Zorunlu unsurlar (HMK m.119):** Mahkeme adı; tarafların ad-soyad, TCKN, adres; varsa kanuni temsilci; davanın konusu ve değeri; **açık talep sonucu**; dayanılan vakıaların sıra numarasıyla açık özeti; her vakıanın hangi delille ispatlanacağı (vakıa-delil bağlantısı); dayanılan hukuki sebepler; imza. Eksik unsurda hâkim bir haftalık kesin süre verir (m.119/2); giderilmezse dava açılmamış sayılabilir.
2. **Talep sonucu:** Net ve infaza elverişli olmalı. Belirsiz alacak davası açılacaksa şartları (HMK m.107) ayrıca değerlendirilir; aksi halde kısmî/tam talep tercihi yapılır.
3. **Vakıa-delil eşlemesi (m.119/1-e,f ve m.194 somutlaştırma yükü):** Her maddi vakıa somut anlatılır; soyut iddia yetersizdir.
4. **Ek belgeler:** Deliller dilekçeye eklenir veya nerede olduğu gösterilir; tanık varsa ad-adres bildirilir. Harç ve gider avansı (m.120) yatırılmadan dava işleme alınmaz.
5. **İddianın genişletilmesi yasağı (m.141):** Dava açıldıktan sonra serbestçe yeni vakıa/talep eklenemeyeceği için ilk dilekçe kapsamlı olmalıdır.
6. **Ara sonuç:** Unsurlar tam + talep net + deliller bağlı + harç/avans hazır ise dava açılmaya hazırdır.

## Çıktı modülleri
- m.119 başlıklarına oturtulmuş dava dilekçesi taslağı.
- Vakıa-delil eşleme tablosu.
- Harç/gider avansı ve ek belge kontrol listesi.

## Plugin bağlamı

Bu beceri `kendini-temsil-asliye` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
