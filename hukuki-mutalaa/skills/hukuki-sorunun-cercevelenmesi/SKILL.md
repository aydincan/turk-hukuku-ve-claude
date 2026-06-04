---
name: hukuki-sorunun-cercevelenmesi
description: "Karmaşık bir uyuşmazlığı cevaplanabilir alt hukuki sorulara bölmek, doğru hukuk dalı ve normları belirleyip değerlendirme sırasını kurmak gerektiğinde kullanılır; mütalaanın yol haritasını oluşturur."
---

# Hukuki Sorunun Çerçevelenmesi

## Görev
Maddi olaydan doğan hukuki uyuşmazlığı, sistematik olarak cevaplanabilir alt sorulara ayırmak ve hangi normların hangi sırayla uygulanacağını belirlemek. İyi çerçevelenmemiş bir soru, dağınık ve sonuçsuz bir mütalaa üretir.

## Soğuk başlangıç (intake)
- Müvekkilin asıl öğrenmek istediği nihai soru ne? (Talep haklı mı / borçlu muyum / dava açayım mı?)
- Olay hangi hukuk dal(lar)ına giriyor? (Birden çok dal kesişiyor olabilir.)
- Birbirine bağlı ön sorunlar var mı? (Önce geçerlilik, sonra ifa gibi)
- İstenen yalnızca hukuki nitelendirme mi, yoksa strateji önerisi mi?

## Denetim şeması
1. Nihai sorudan alt sorulara: Üst soru mantıksal bileşenlerine ayrılır. Örnek (sözleşmeden cayma): (a) Sözleşme geçerli kuruldu mu? (b) Geçerliyse, fesih/dönme şartları gerçekleşti mi? (c) Gerçekleştiyse, talep edilebilecek tazminat ne? (d) Talep zamanaşımına uğradı mı?
2. Mantıksal sıralama: Ön sorun sonraki sorunun cevabını belirliyorsa önce ele alınır (geçersiz sözleşmede ifa tartışılmaz; sebepsiz zenginleşme/TBK m.77 devreye girer).
3. Hukuk dalı eşlemesi: Her alt soru ilgili dala ve başat norma bağlanır (borç ilişkisi → TBK; ayni hak → TMK; ticari iş → TTK; usul → HMK/İYUK/CMK). Kesişen alanlarda özel hükmün genel hükme üstünlüğü gözetilir.
4. Emredici/yedek hüküm taraması: Tarafların aksini kararlaştıramayacağı emredici normlar belirlenir; bunlar değerlendirmenin sınırıdır.
5. Zaman bakımından uygulama: Olaya yürürlükteki mi yoksa mülga mevzuatın mı uygulanacağı, geçici maddeler kontrol edilir.
6. Ara sonuç: Numaralandırılmış alt soru listesi + her sorunun norm dayanağı + değerlendirme sırası.

## Çıktı modülleri
- Nihai soru → alt sorular ağacı
- Her alt soru için başat norm eşlemesi
- Değerlendirme sırası gerekçesiyle
- Emredici hüküm uyarı kutusu

## Plugin bağlamı

Bu beceri `hukuki-mutalaa` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
