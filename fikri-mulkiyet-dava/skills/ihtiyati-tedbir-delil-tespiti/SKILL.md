---
name: ihtiyati-tedbir-delil-tespiti
description: "Tecavüzün durdurulması, üretim/satışın engellenmesi, ürünlere el konulması için ihtiyati tedbir; tecavüzün veya delillerin kaybolma riski karşısında delil tespiti gerektiğinde kullanılır."
---

# İhtiyati Tedbir ve Delil Tespiti

## Görev
Tecavüzü hızla durdurmak ve delili güvenceye almak için SMK m.159 ve HMK m.389 vd. uyarınca ihtiyati tedbir; HMK m.400 vd. uyarınca delil tespiti taleplerini hazırlamak.

## Soğuk başlangıç (intake)
- Tecavüz devam ediyor mu, yakın mı; gecikme telafisi güç zarar doğurur mu?
- Hangi tedbir isteniyor: durdurma, ürünlere/araçlara el koyma, teminat, gümrükte durdurma?
- Hak ve tecavüz yaklaşık olarak ispatlanabiliyor mu (sicil kaydı, numune, fatura)?
- Delil kaybolma riski var mı; karşı tarafın elindeki kayıtlar gerekiyor mu?

## Denetim şeması
1. Tedbir dayanağı: Sınai mülkiyette ihtiyati tedbir SMK m.159; genel rejim HMK m.389-399. Talep edilebilecek tedbirler: tecavüz fiilinin durdurulması, ürün/araçlara el koyma ve muhafazası, teminat (SMK m.159/2).
2. Yaklaşık ispat: Davacı hem hakkın varlığını hem tecavüzü/tecavüz tehlikesini yaklaşık ispatlamalı (HMK m.390/3). Tam ispat aranmaz, ancak sicil kaydı + numune + tespit dosyası güçlü dayanaktır.
3. Teminat: Kural olarak teminat alınır (HMK m.392); haksız tedbir tazminat sorumluluğu doğurur. Tedbir talebi dava açılmadan da istenebilir; bu halde 2 hafta içinde dava açma zorunluluğu (HMK m.397/1).
4. Delil tespiti: Tecavüzün ve kapsamının belirlenmesi için HMK m.400 vd.; hâkim keşif/bilirkişi ile ürünü, üretim yerini, kayıtları tespit eder. Acele hallerde karşı taraf dinlenmeden (m.401/3).
5. Gümrükte durdurma: Hak sahibi başvurusu üzerine taklit ürünlerin gümrükte alıkonulması (SMK m.159/2 ve Gümrük Kanunu m.57); alıkoymadan sonra dava/tedbir süresi izlenir.
6. Ara sonuç: Tedbir kararı icra edilir; itiraz (HMK m.394) ve tedbire muhalefetin sonuçları (m.398) takip edilir.

## Çıktı modülleri
- İhtiyati tedbir talep dilekçesi iskeleti (yaklaşık ispat + talep + teminat).
- Delil tespiti talebi taslağı.
- Gümrük başvurusu ve süre takvimi.

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
