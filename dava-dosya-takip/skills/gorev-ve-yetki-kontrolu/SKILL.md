---
name: gorev-ve-yetki-kontrolu
description: "Davanın doğru görevli ve yetkili mahkemede açılıp açılmadığını, görevsizlik-yetkisizlik veya gönderme riskini denetlemek gerektiğinde kullan."
---

# Görev ve Yetki Kontrolü

## Görev
Dosyanın görevli mahkeme (dava konusuna göre) ve yetkili mahkeme (yer itibarıyla) bakımından doğru yerde olup olmadığını denetlemek; görevsizlik/yetkisizlik ile zaman kaybı riskini erken yakalamak.

## Soğuk başlangıç (intake)
- Dava konusu ve türü ne (alacak, tazminat, tüketici, iş, ticari, aile)?
- Dava hangi mahkemede ve hangi yerde açılmış?
- Taraflar arasında yetki sözleşmesi veya tahkim şartı var mı?
- Kesin yetki gerektiren bir dava türü söz konusu mu?

## Denetim şeması
1. Görev: HMK m.1 gereği görev kamu düzenindendir ve re'sen incelenir. Genel görevli asliye hukuk (HMK m.2) ile özel görevli mahkemeleri ayırt et: tüketici mahkemesi (6502 TKHK m.73), iş mahkemesi (7036 m.5), ticari dava-asliye ticaret (TTK m.4-5), aile mahkemesi, FSHM. Yanlış görevli mahkeme → görevsizlik kararı ve gönderme.
2. Yetki: genel yetki davalının yerleşim yeri (HMK m.6); özel/kesin yetki halleri (taşınmazda taşınmazın yeri HMK m.12; sözleşmede ifa yeri HMK m.10; haksız fiilde HMK m.16). Kesin yetki re'sen gözetilir.
3. Yetki sözleşmesi/tahkim: tacir-kamu tüzel kişisi arasında yetki sözleşmesi (HMK m.17) geçerli mi; tahkim şartı varsa tahkim ilk itirazı (HMK m.116) riski.
4. İtiraz zamanı: yetki ilk itirazdır, cevap süresinde ileri sürülmezse düşer (HMK m.116, m.117, m.19); görev her aşamada gözetilir.
5. Ara sonuç: görev/yetki uygun mu, değilse hangi mahkemeye gönderme ve süre etkisi. Mevzuat dışı varsayım yapılmaz.

## Çıktı modülleri
- Görev/yetki değerlendirme notu (doğru mahkeme + dayanak madde).
- Görevsizlik/yetkisizlik riski ve gönderme senaryosu.
- İtiraz süresi ve usul uyarısı.

## Plugin bağlamı

Bu beceri `dava-dosya-takip` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
