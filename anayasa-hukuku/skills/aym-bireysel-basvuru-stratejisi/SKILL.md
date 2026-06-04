---
name: aym-bireysel-basvuru-stratejisi
description: "Bir temel hak ihlali iddiasının Anayasa Mahkemesine bireysel başvuru yoluyla taşınıp taşınamayacağını ve kabul edilebilirlik şartlarını değerlendirmek; başvuru yollarının tüketilmesi, süre ve konu yönünden yetki analizinin gerektiği hallerde kullanılır."
---

# AYM Bireysel Başvuru Stratejisi

## Görev
Anayasa ve AİHS ortak koruması altındaki bir temel hakkın kamu gücü işlemiyle ihlal edildiği iddiasını, Anayasa m.148/3 ve 6216 sayılı Kanun çerçevesinde bireysel başvuruya hazırlamak; kabul edilebilirlik eşiklerini önceden test etmek.

## Soğuk başlangıç (intake)
1. İhlal hangi temel haktan kaynaklanıyor ve hem Anayasa hem AİHS kapsamında mı (ortak koruma alanı)?
2. İhlali doğuran kesinleşmiş işlem/karar hangisi ve ne zaman tebliğ edildi?
3. Olağan kanun yolları (istinaf, temyiz, gerekirse karar düzeltme) tüketildi mi?
4. İhlalden doğan güncel ve kişisel bir mağduriyet var mı?

## Denetim şeması
1. **Konu bakımından yetki.** Hak hem Anayasa hem AİHS (ve ek protokoller) kapsamında ortak korunan bir hak olmalı (m.148/3, 6216 m.45). Yasama işlemleri ve düzenleyici işlemler doğrudan başvuru konusu olamaz; idari/yargısal uygulama işlemi aranır.
2. **Kişi bakımından yetki.** Başvurucu güncel ve kişisel olarak, doğrudan etkilenen mağdur olmalı (6216 m.46). Kamu tüzel kişileri başvuramaz.
3. **Başvuru yollarının tüketilmesi.** İhlali gidermeye elverişli tüm olağan idari ve yargısal yollar tüketilmelidir (6216 m.45/2). Ara sonuç: tüketilmemişse başvuru reddedilir.
4. **Süre.** Başvuru yollarının tüketildiği, yoksa ihlalin öğrenildiği tarihten itibaren **otuz gün** içinde yapılır (6216 m.47/5). Mazeret rejimi sınırlıdır.
5. **Kabul edilebilirlik.** Açıkça dayanaktan yoksunluk, anayasal ve kişisel önemden yoksunluk (önemli zarar yokluğu) elemeleri uygulanır. Esasta ihlal tespit edilirse AYM ihlali ve sonuçlarını giderme yolunu (yeniden yargılama, tazminat) gösterir.
6. **AİHM ile ilişki.** AYM, iç hukukta etkili başvuru yolu olarak görülür; AİHM'e gitmeden önce kural olarak tüketilmesi gereken bir aşamadır.
Künye verirken başvuru numarası ve karar tarihini `[doğrulanacak]` işaretleyin; kaynak kararlarbilgibankasi.anayasa.gov.tr.

## Çıktı modülleri
- Kabul edilebilirlik ön testi (yetki, tüketme, süre, mağdur sıfatı) tablosu.
- İhlal iddiasının hak bazlı gerekçesi ve talep edilecek giderim (yeniden yargılama/tazminat).
- Süre takvimi ve eksik belge listesi.

## Plugin bağlamı

Bu beceri `anayasa-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
