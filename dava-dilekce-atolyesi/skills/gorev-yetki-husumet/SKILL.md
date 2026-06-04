---
name: gorev-yetki-husumet
description: "Davanın doğru mahkemede ve doğru taraflara karşı açılıp açılmadığını; görev, yetki, sıfat ve dava şartlarını denetlemek gerektiğinde kullanılır."
---

# Görev, Yetki ve Husumet Denetimi

## Görev
Layihayı yazmadan önce davanın doğru mahkemede, doğru davalıya karşı ve dava şartları sağlanarak açıldığını denetlemek. Görev ve dava şartları kamu düzenindendir; eksikse esasa girilmeden dava reddedilir.

## Soğuk başlangıç (intake)
- Talep konusu ve değeri nedir? (görevli mahkemeyi belirler)
- Davalının yerleşim yeri / işlemin yapıldığı yer / ifa yeri neresi?
- Taraflar doğru tespit edildi mi (gerçek/tüzel kişi, temsil)?
- Zorunlu arabuluculuk/idari başvuru gibi bir dava şartı var mı?

## Denetim şeması
1. Görev (HMK m.1-4): Görev kanunla belirlenir, kamu düzenindendir ve dava şartıdır (m.114/1-c). Asliye hukuk genel görevlidir; sulh hukukun görevi HMK m.4'te sayılıdır. Özel görevli mahkemeleri kontrol edin (tüketici, iş, ticaret, aile, fikri-sınai). İstisna: özel kanun aksini öngörebilir.
2. Yetki (HMK m.5-19): Genel yetki davalının yerleşim yeri (m.6). Özel yetki: sözleşmede ifa yeri (m.10), haksız fiilde m.16, taşınmazda kesin yetki m.12. Kesin yetki hâkimce re'sen gözetilir; kesin olmayan yetkiye ilk itiraz gerekir (m.116, m.117).
3. Sıfat/husumet (TMK m.6; HMK genel): Aktif/pasif husumet maddi hukuktan doğar; sıfat yokluğu esastan reddi gerektirir, dava şartı değildir.
4. Dava şartları (HMK m.114-115): Eksik dava şartı tamamlanabilir nitelikteyse süre verilir; değilse usulden ret. Zorunlu arabuluculuk (ör. ticari/işçi-işveren/tüketici uyuşmazlıkları) dava şartıdır; tutanak eklenmeli.
5. İdari yargıda: İYUK m.33-37 yetki kuralları; idari merci tecavüzü ve süre (m.11).
Ara sonuç: görev/yetki/şart sağlanmıyorsa düzeltme yolu (görevsizlik/yetkisizlik, gönderme) veya doğru mahkemeye yönlendirme.

## Çıktı modülleri
- Görevli ve yetkili mahkeme tespiti (madde gerekçeli)
- Taraf/husumet doğrulama tablosu
- Dava şartı kontrol listesi (arabuluculuk, harç, ehliyet)
- Eksiklik halinde düzeltme/yönlendirme önerisi

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
