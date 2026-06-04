---
name: iddianame-ve-kovusturma
description: "İddianamenin unsurları ve iadesi, kovuşturmanın başlaması, duruşma düzeni ve sanık haklarının değerlendirilmesi gerektiğinde kullanılır."
---

# İddianame Denetimi ve Kovuşturma Evresi

## Görev
İddianamenin yasal unsurlarını ve iade sebeplerini denetlemek; kovuşturma evresinde duruşma düzenini, sanık haklarını ve usulü takip etmek.

## Soğuk başlangıç (intake)
- İddianame kabul edildi mi, tensip tutanağı var mı?
- Yüklenen suç ve sevk maddeleri net mi; olay anlatımı yeterli mi?
- İddianamede gösterilen deliller ile yüklenen suç örtüşüyor mu?
- Duruşma günü belli mi; sanık tutuklu mu?
- Esasa girilmeden ileri sürülecek ilk itirazlar var mı (görev, yetki)?

## Denetim şeması
1. **İddianame unsurları.** İddianamede şüphelinin kimliği, yüklenen suç ve uygulanacak kanun maddeleri, olayın ve delillerin gösterilmesi, suçun işlendiği yer-zaman gibi zorunlu unsurlar bulunmalıdır (CMK m.170). Olayla deliller arasında bağ kurulmalıdır.
2. **İade.** Mahkeme, m.170'e aykırılık, eksik soruşturma veya ön ödeme/uzlaştırma yoluna gidilmemesi hallerinde iddianameyi 15 gün içinde iade eder (m.174); süresinde iade edilmezse kabul edilmiş sayılır.
3. **Kovuşturmanın başlaması.** İddianamenin kabulüyle kovuşturma başlar ve sanık sıfatı doğar (m.175). Tensiple duruşma hazırlığı yapılır.
4. **Duruşma düzeni.** Yargılama kural olarak aleni (m.182), sözlü ve doğrudandır. Sanığın hazır bulunma (m.193), son söz hakkı (m.216/3) ve çapraz sorgu güvenceleri uygulanır.
5. **İlk itirazlar.** Görevsizlik (m.5), yetkisizlik (m.18, ilk oturumda), davaya katılma talepleri esasa girilmeden değerlendirilir.
6. **Ara sonuç.** İddianame sakatsa iade talebi; geçerliyse savunma planı, delil ikamesi ve duruşma stratejisi kurulur.

## Çıktı modülleri
- İddianame unsur denetim tablosu (m.170 maddeleriyle eşlenmiş).
- İddianamenin iadesi/itiraz gerekçesi taslağı.
- Sanık savunma planı ve delil listesi.
- Duruşma hazırlık notu (itirazlar, tanık, talepler).

## Plugin bağlamı

Bu beceri `ceza-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
