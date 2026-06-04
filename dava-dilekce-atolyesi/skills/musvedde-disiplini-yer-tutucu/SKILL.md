---
name: musvedde-disiplini-yer-tutucu
description: "Taslak layihada eksik bilgileri uydurmadan yer tutucularla işaretlemek, kontrol listesi ve eksik raporu üretmek, avukat denetimine hazır müsvedde teslim etmek gerektiğinde kullanılır."
---

# Müsvedde Disiplini ve Yer Tutucu Yönetimi

## Görev
Üretilen her layiha müsveddesini avukat denetimine hazır, eksiksiz işaretlenmiş ve doğrulanabilir biçimde teslim etmek. Eksik bilgi asla uydurulmaz; yer tutucularla işaretlenir ve listelenir. Bu beceri atölyenin kalite kapısıdır.

## Soğuk başlangıç (intake)
- Müsveddede hangi bilgiler eksik (tarih, bedel, taraf, delil)?
- Hangi madde atıfları teyit edilmeli (yürürlük/tutar)?
- Hangi içtihat künyesi doğrulanmamış durumda?
- Son kontrol listesi (süre, harç, görev) tamam mı?

## Denetim şeması
1. Yer tutucu standardı: Eksik bilgileri `[doldurulacak]`, `[tarih]`, `[bedel]`, `[TC/vergi no]`, `[delil eki]` gibi tutarlı işaretlerle gösterin; metne tahmini değer yazmayın.
2. Madde teyidi: Süre, tutar ve harç gibi güncellenen normları (parasal sınırlar, faiz oranı) `[yürürlük teyit edilecek]` ile işaretleyin; yürürlük tarihini kontrol önerisi ekleyin.
3. İçtihat hijyeni: İlkesel atıf yapın; karar künyesini doğrulamadan yazmayın. Doğrulanmamış her künyeyi `[doğrulanacak]` ile işaretleyip karararama.yargitay.gov.tr / karararama.danistay.gov.tr / kararlarbilgibankasi.anayasa.gov.tr kaynağını anın.
4. Son kontrol listesi: Görev-yetki, dava şartı/arabuluculuk, süre, harç, talep sonucu netliği, delil-vakıa bağı, imza/vekâletname. Her kalemi tamam/eksik olarak işaretleyin.
5. Teslim notu: Müsveddenin avukat onayı gerektirdiğini, kritik risklerin (süre, teksif) makinece kapatılamadığını belirtin. Ara sonuç: eksik listesi ve kontrol listesi olmadan müsvedde teslim edilmez.

## Çıktı modülleri
- İşaretlenmiş layiha müsveddesi
- Eksik bilgi/yer tutucu raporu
- Doğrulanacak madde ve içtihat listesi
- Teslim öncesi son kontrol listesi

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
