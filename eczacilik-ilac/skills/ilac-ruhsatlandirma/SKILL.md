---
name: ilac-ruhsatlandirma
description: "Beşeri tıbbi ürün ruhsat başvurusu, varyasyon, ruhsat red/askı/iptali ve veri/dosya gizliliği konularında ruhsatlandırma yönetmeliği şartlarını denetlemek gerektiğinde kullanılır."
---

# Beşeri Tıbbi Ürün Ruhsatlandırma

## Görev
Bir beşeri tıbbi ürünün ruhsat başvurusu, varyasyonu veya ruhsat işlemine (red, askıya alma, iptal) karşı süreci Beşeri Tıbbi Ürünler Ruhsatlandırma Yönetmeliği çerçevesinde değerlendirmek.

## Soğuk başlangıç (intake)
- Ürün orijinal mi, jenerik (eşdeğer) mi, biyobenzer mi; başvuru türü nedir?
- Hangi aşama: dosya değerlendirme, eksiklik yazısı, ruhsat reddi, askı, iptal, varyasyon reddi?
- TİTCK’nın gerekçesi nedir (etkililik/güvenlilik, GMP, dosya eksikliği, ruhsat sahibinin yükümlülüğü)?
- İşlemin tebliğ tarihi ve süre durumu?

## Denetim şeması
1. **Dayanak.** Beşeri Tıbbi Ürünler Ruhsatlandırma Yönetmeliği (RG 11.12.2021) ve 1262 sayılı Kanun m.1 vd. (ruhsatsız müstahzar yasağı); TİTCK’nın yetkisi 663 sayılı KHK’ya dayanır.
2. **Başvuru unsurları.** CTD formatında kalite, klinik, klinik-dışı modüller; jenerikte biyoeşdeğerlik ve referans ürünle kıyas; GMP uygunluğu. Ara sonuç: dosya tam mı, eksiklik yazısına süresinde cevap verildi mi?
3. **İdari işlem denetimi.** Ruhsat reddi/askısı/iptali idari işlemdir; yetki-şekil-sebep-konu-maksat yönünden incelenir. Sebep unsuru (bilimsel değerlendirme) teknik takdire dayanır; ancak takdir yetkisi ölçülülük ve eşitlikle sınırlıdır. İspat: idare sebebi (örn. güvenlilik sinyali) somut göstermelidir.
4. **Yargı yolu ve süre.** İptal davası Danıştay/idare mahkemesi; İYUK m.7 ile 60 gün; ivedi durumlarda yürütmenin durdurulması (İYUK m.27) — telafisi güç zarar ve açık hukuka aykırılık birlikte gösterilir.
5. **Veri ve dosya korunması.** Ruhsat dosyasındaki gizli bilgilerin korunması; jenerik başvurularda veri münhasıriyeti süreleri yönetmelik ve ilgili düzenlemelerden teyit edilir.

## Çıktı modülleri
- Başvuru/varyasyon eksiklik kontrol listesi.
- Ruhsat işlemine karşı iptal + yürütmeyi durdurma dilekçe iskeleti [doldurulacak].
- Bilimsel-teknik itiraz için bilirkişi/uzman görüşü planı.

## Plugin bağlamı

Bu beceri `eczacilik-ilac` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
