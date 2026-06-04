---
name: idari-dava-dilekcesi-iyuk
description: "İptal veya tam yargı davası için İYUK m.3 ve m.5 unsurlarına uygun dilekçe; dava açma süresi, üst makama başvuru ve yürütmenin durdurulması talebini kurmak gerektiğinde kullanılır."
---

# İdari Dava Dilekçesi (İYUK)

## Görev
İptal veya tam yargı davası dilekçesini İYUK m.3 unsurlarına uygun kurmak; en kritik unsur olan dava açma süresini doğru hesaplamak ve gerektiğinde yürütmenin durdurulmasını istemek.

## Soğuk başlangıç (intake)
- Dava konusu idari işlemin tarihi ve tebliğ/öğrenme tarihi nedir?
- İptal davası mı, tam yargı (tazminat) mı, ikisi birlikte mi?
- Üst makama (ihtiyari/zorunlu) başvuru yapıldı mı (m.11)?
- Telafisi güç zarar ve açık hukuka aykırılık var mı (YD talebi)?

## Denetim şeması
1. Dilekçe unsurları (İYUK m.3): Mahkeme, taraflar, davanın konusu ve sebepleri, dava konusu işlemin yazılı bildirim tarihi, sonuç (talep), deliller. İdari işlemin örneği eklenir (m.3/3).
2. Dava açma süresi (m.7): Kural olarak Danıştay ve idare mahkemelerinde 60 gün, vergi mahkemelerinde 30 gün; süre yazılı bildirimi izleyen günden işler. Özel kanunlardaki farklı süreleri kontrol edin. Süre kamu düzeninden, re'sen incelenir.
3. Üst makama başvuru (m.11): İşlemin kaldırılması/değiştirilmesi için dava süresi içinde üst makama başvuru süreyi durdurur; cevap verilmez/red gelirse kalan süre işler.
4. İptal sebepleri: İdari işlemin beş unsuru — yetki, şekil, sebep, konu, maksat — üzerinden sakatlık iddialarını altlayın.
5. Yürütmenin durdurulması (m.27): İki şart birlikte — telafisi güç/imkânsız zarar ve açık hukuka aykırılık; talebi gerekçelendirip teminat hususunu belirtin. Tam yargıda zarar ve idari kusur/sorumluluk dayanağını kurun. Ara sonuç: süre içinde ve unsurlar tamsa dilekçe hazır.

## Çıktı modülleri
- İptal/tam yargı dava dilekçesi taslağı (İYUK m.3 başlıklı)
- Süre hesabı notu (tebliğ → son gün)
- Yürütmenin durdurulması gerekçeli talebi
- Ek listesi (işlem örneği, başvuru evrakı)

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
