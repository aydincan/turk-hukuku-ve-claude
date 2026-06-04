---
name: savunma-strateji-mutalaa
description: "Bir ceza dosyasında şüpheli/sanık savunması veya katılan/mağdur stratejisi kurmak, lehe-aleyhe argümanları tartmak ve gerekçeli bir hukuki değerlendirme üretmek gerektiğinde kullanılır."
---

# Savunma Stratejisi ve Ceza Mütalaası

## Görev
Suç vasfı ve delil analizinden hareketle taraf konumuna göre (savunma veya katılan) bütüncül bir strateji kurmak; lehe-aleyhe argümanları gerekçeli bir mütalaada toplamak.

## Soğuk başlangıç (intake)
- Müvekkil hangi konumda: şüpheli/sanık mı, mağdur/katılan mı, malen sorumlu mu?
- Hedef ne: beraat/vasıf düşürme, ceza indirimi/erteleme/HAGB, yoksa mahkûmiyet ve tazminat mı?
- Dosyanın aşaması nedir (soruşturma, kovuşturma, istinaf/temyiz)?
- Etkin pişmanlık, uzlaştırma, takdiri indirim gibi imkânlar değerlendirildi mi?

## Denetim şeması
1. Hedef belirleme: Konuma göre öncelikli hedefi netleştir. Savunmada katmanlı strateji kurulur: önce unsur yokluğu/beraat, olmazsa vasıf düşürme, olmazsa lehe hükümlerle ceza minimizasyonu.
2. Lehe argüman havuzu (savunma): Tipiklik/kast eksikliği, hukuka uygunluk sebepleri (meşru savunma m.25, hakkın kullanılması m.26), kusurluluğu kaldıran/azaltan haller (haksız tahrik m.29, hata m.30, cebir m.28), teşebbüs/gönüllü vazgeçme (m.35-36), delil yasakları, zamanaşımı/şikâyet eksikliği.
3. Ceza minimizasyon araçları: Etkin pişmanlık (örn. m.168 malvarlığı suçlarında, m.221 örgüt suçlarında ilgili tipe göre), takdiri indirim (m.62), seçenek yaptırım (m.50), erteleme (m.51), HAGB (CMK m.231), uzlaştırma (CMK m.253). Her birinin şartlarını dosyaya uygula.
4. Katılan/mağdur stratejisi: Eksik soruşturma noktaları, ek delil/şikâyet talepleri, suç vasfının ağırlaştırılması, katılma talebi (CMK m.237), şahsi hak/tazminat için ceza-tazminat ilişkisi ve ayrı hukuk davası yolu.
5. Risk haritası: Aleyhe deliller, beklenen ceza aralığı, tutukluluk/adli kontrol riski, infaz sonuçları (5275 sayılı Kanun); olası senaryolar olasılıklarıyla.
6. Ara sonuç: Gerekçeli mütalaa iskeleti — olay tespiti, hukuki sorun, unsur altlaması, lehe-aleyhe değerlendirme, sonuç ve eylem önerisi (her iddia madde/içtihat atıflı, doğrulanmamış künyeler `[doğrulanacak]`).

## Çıktı modülleri
- Katmanlı strateji notu (birincil/yedek hedefler ve dayanakları).
- Lehe-aleyhe argüman tablosu (madde atıflı).
- Risk haritası ve gerekçeli ceza mütalaası taslağı.

## Plugin bağlamı

Bu beceri `ceza-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
