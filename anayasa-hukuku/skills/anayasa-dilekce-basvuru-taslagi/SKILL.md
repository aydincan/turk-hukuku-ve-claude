---
name: anayasa-dilekce-basvuru-taslagi
description: "AYM bireysel başvuru formu, norm denetimi başvuru gerekçesi veya anayasaya aykırılık itirazı gibi anayasal metinlerin yapılandırılmış taslağını üretmek; başvurunun biçim ve içerik şartlarına uygun iskelet gerektiğinde kullanılır."
---

# Anayasal Başvuru ve Dilekçe Taslağı

## Görev
Anayasa hukukuna özgü metinlerin — AYM bireysel başvuru formu, iptal davası dilekçesi, görülmekte olan davada Anayasaya aykırılık itirazı — biçim ve içerik şartlarına uygun, gerekçeli ve yer tutuculu bir taslağını üretmek.

## Soğuk başlangıç (intake)
1. Üretilecek metin türü: bireysel başvuru, iptal davası dilekçesi, yoksa aykırılık itirazı mı?
2. İhlal/aykırılık iddiasının dayandığı Anayasa maddeleri ve AİHS karşılıkları neler?
3. Başvurucunun sıfatı, ihlali doğuran nihai işlem ve tarihleri belli mi?
4. Talep edilen sonuç: iptal, ihlal tespiti, yeniden yargılama, yoksa tazminat mı?

## Denetim şeması
1. **Tür ve form belirleme.** Bireysel başvuruda 6216 ve AYM İçtüzüğü'nün öngördüğü resmî form ve zorunlu unsurlar; iptal davasında m.150 ehliyeti ve 60 günlük süre; itirazda m.152 ciddiyet ve uygulanacak norm şartı.
2. **Zorunlu unsurları yerleştir.** Başvurucu/kanuni temsilci kimliği, ihlale yol açan işlem, tüketilen yollar, başvuru tarihleri, ihlal edilen Anayasa ve AİHS maddeleri, açık ve gerekçeli ihlal iddiası, talep. Ara sonuç: zorunlu unsur eksikse başvuru reddi riski.
3. **Gerekçe mimarisi.** Her hak için: koruma alanı → müdahale → m.13/m.15 testi → somut olaya uygulama. Eşitlikte m.10 matrisi. Adil yargılanmada güvence bazlı inceleme.
4. **Süre ve tüketme beyanı.** Bireysel başvuruda otuz günlük süre (6216 m.47/5) ve yolların tüketildiği açıkça belirtilir; iptal davasında 60 gün hesaplanır.
5. **Atıf ve yer tutucu disiplini.** İçtihat künyeleri `[doğrulanacak]`; bilinmeyen tarih/numara/ad alanları `[doldurulacak]` olarak işaretlenir. Sahte esas/karar numarası yazılmaz.

## Çıktı modülleri
- Seçilen tür için başlıklandırılmış dilekçe/form iskeleti.
- Hak bazlı gerekçe blokları ve talep sonucu.
- Eksik bilgi (`[doldurulacak]`) ve doğrulanacak içtihat (`[doğrulanacak]`) listesi ile süre/teslim uyarısı.

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
