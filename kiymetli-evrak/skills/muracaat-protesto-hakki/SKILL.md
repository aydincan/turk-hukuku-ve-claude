---
name: muracaat-protesto-hakki
description: "Ödememe/kabul etmeme halinde başvurma hakkının doğumu, protesto zorunluluğu ve başvurma bedelinin kapsamını incelemek; cirantalara ve avalistlere rücu imkânı değerlendirilirken kullanılır."
---

# Müracaat Hakkı ve Protesto

## Görev
Senedin ödenmemesi veya kabul edilmemesi halinde hamilin başvurma (müracaat) hakkını, bu hakkın korunması için gereken protesto/işlemleri ve başvurma bedelinin kapsamını belirlemek.

## Soğuk başlangıç (intake)
- Senet vadesinde ibraz edildi mi; ödenmedi mi, kabul mü edilmedi?
- Protesto çekildi mi (ödememe/kabul etmeme protestosu) ya da "protestosuz/masrafsız" kaydı var mı?
- Hamil hangi borçlulara (düzenleyen, cirantalar, avalistler) başvurmak istiyor?
- İbraz ve protesto süreleri tutuldu mu?

## Denetim şeması
1. Başvurma hakkının doğumu: vadede ödememe ya da vadeden önce kabul etmeme/ödememe ihtimali (iflas, ödemelerin tatili) hallerinde hamil cirantalara, düzenleyene ve diğer borçlulara başvurabilir (TTK m.713).
2. Protesto şartı: kural olarak başvurma hakkı, ödememe/kabul etmeme protestosunun süresinde düzenlenmesine bağlıdır (TTK m.714, m.722). Protesto noter aracılığıyla yapılır.
3. Muafiyet: "masrafsız/protestosuz iadesi" kaydı protesto zorunluluğunu kaldırır ama ibraz ve süre yükümlülüğünü kaldırmaz (TTK m.722).
4. İhbar: hamil, ödememe/kabul etmemeyi kendinden önceki borçluya süresinde ihbar eder (m.723); ihmal tazminat sorumluluğu doğurabilir, hakkı düşürmez.
5. Başvurma bedeli: hamil senet bedeli, işlemiş faiz, protesto ve ihbar masrafları ile komisyonu isteyebilir (TTK m.725); ödeyen ciranta kendinden öncekilerden m.726 kapsamında talep eder.
6. Ara sonuç: süre/protesto yükümlülükleri yerine getirilmemişse cirantalara ve onların avalistlerine başvurma hakkı düşer (m.730); ancak asıl borçluya (kabul eden/düzenleyen) karşı hak, zamanaşımına dek korunur.

## Çıktı modülleri
- Müracaat hakkı kontrol listesi (ibraz + protesto + süre).
- Başvurma bedeli hesap kalemleri tablosu (bedel/faiz/masraf [doldurulacak]).
- Protesto/ihbar taslağı veya hak düşümü savunma notu.

## Plugin bağlamı

Bu beceri `kiymetli-evrak` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
