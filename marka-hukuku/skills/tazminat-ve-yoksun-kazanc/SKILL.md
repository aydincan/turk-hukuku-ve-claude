---
name: tazminat-ve-yoksun-kazanc
description: "Tecavüz nedeniyle maddi-manevi tazminat veya itibar tazminatı talep edilecekse; m.150-151 hesap yöntemlerini ve yoksun kalınan kazancın üç seçenekli hesabını yürütmek için kullanılır."
---

# Marka Tecavüzünde Tazminat ve Yoksun Kalınan Kazanç

## Görev
Tecavüz nedeniyle SMK m.150 (maddi-manevi tazminat) ve m.151 (yoksun kalınan kazancın hesabı) kapsamında tazminat talebini kurmak; marka sahibinin seçimlik hesap yöntemini belirlemek ve itibar tazminatını (m.150/2) değerlendirmek.

## Soğuk başlangıç (intake)
- Tecavüz kusurlu mu (kast/ihmal), zarar somutlaştırılabiliyor mu?
- Marka sahibinin kaybı mı, tecavüz edenin kazancı mı, lisans bedeli mi daha kolay ispatlanabilir?
- Markanın itibarı zarar gördü mü (kötü/uygunsuz kullanım)?
- Zamanaşımı süresi (öğrenmeden 2 yıl) işliyor mu?

## Denetim şeması
1. **Sorumluluğun temeli.** Tecavüzün varlığı (m.29) + kusur. Maddi tazminat için kusur aranır; tecavüzün tespiti/men'i kusursuz da istenebilir.
2. **Fiili zarar + yoksun kalınan kazanç (m.150/1).** Marka sahibinin malvarlığında azalma (fiili zarar) ve elde edemediği kazanç birlikte talep edilebilir.
3. **Yoksun kalınan kazanç hesabı (m.151).** Marka sahibi üç yöntemden birini seçer: (a) tecavüz olmasaydı elde edeceği muhtemel gelir, (b) tecavüz edenin elde ettiği net kazanç, (c) lisans verilseydi istenecek makul lisans bedeli. Seçim hak sahibinindir.
4. **İtibar tazminatı (m.150/2).** Marka kötü/uygunsuz biçimde kullanılarak itibarı zarar gördüyse ayrıca itibar tazminatı istenebilir.
5. **Manevi tazminat.** Koşulları varsa TBK m.58 ile birlikte manevi tazminat değerlendirilir.
6. **Zamanaşımı.** SMK m.157 atfıyla TBK m.72: zarar ve failin öğrenilmesinden 2 yıl, her halde fiil tarihinden 10 yıl; tecavüz suç da oluşturuyorsa ceza zamanaşımı uygulanır.

## Çıktı modülleri
- Hesap yöntemi seçim tablosu (m.151/a-b-c karşılaştırması).
- Zarar kalemleri ve delil/bilirkişi dayanağı listesi.
- Zamanaşımı kontrolü ve tazminat talep dilekçesi iskeleti.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
