---
name: marka-sozlesmeleri-devir-lisans
description: "Markanın devri, lisanslanması, rehni veya teminat gösterilmesi söz konusuysa; m.148 vd. tasarruf işlemlerinin şekil, sicil ve içerik şartlarını denetlemek ve sözleşme taslağı kurmak için kullanılır."
---

# Marka Sözleşmeleri — Devir, Lisans ve Rehin

## Görev
Marka üzerindeki hukuki işlemleri (devir, lisans, rehin, teminat, miras) SMK m.148 vd. çerçevesinde kurmak; şekil şartı, sicile şerh ve üçüncü kişilere etki kurallarını denetlemek. Geçerlilik ve ihticaca (üçüncü kişilere karşı ileri sürülebilirlik) şartları ayrıdır.

## Soğuk başlangıç (intake)
- İşlem türü ne: tam/kısmî devir, inhisari/inhisari olmayan lisans, rehin, teminat?
- Marka tescilli mi, başvuru aşamasında mı?
- Lisansta alt lisans, münhasırlık, coğrafya, süre, kalite kontrolü nasıl?
- İşlem sicile şerh ediliyor mu?

## Denetim şeması
1. **Devir (m.148/1, m.148/4).** Marka bağımsız olarak veya işletmeyle devredilebilir; devir yazılı şekilde ve taraflarca imzalı olmalıdır (geçerlilik şartı). Aksi kararlaştırılmadıkça işletmenin devri markayı da kapsar.
2. **Sicile şerh ve etki (m.148/5).** Devir/lisans/rehin sicile kaydedilmezse iyiniyetli üçüncü kişilere karşı ileri sürülemez; kayıt kurucu değil, ihticaca yarar etki sağlar.
3. **Lisans (m.24).** İnhisari (münhasır) veya inhisari olmayan lisans; aksi sözleşmede yoksa inhisari olmayan sayılır. İnhisari lisans sahibi kural olarak dava açabilir; inhisari olmayan lisans sahibi marka sahibine bildirip talep etmedikçe açamaz (sözleşmede aksi düzenlenebilir).
4. **İçerik dengeleri.** Kapsam (mal/hizmet, coğrafya, süre), alt lisans yetkisi, kalite/kullanım denetimi, ücret/royalti, tecavüze karşı dava yetkisi, fesih ve devir sonrası kullanım açıkça düzenlenmelidir.
5. **Rehin/teminat (m.148/3).** Marka rehnedilebilir, haczedilebilir; rehin sicile tescil edilir.
6. **Garanti.** Devredende markanın geçerliliği/sınırlamasız oluşu yönünden TBK genel hükümleri (ayıp/zapt) ve sözleşmesel beyan-tekeffüller değerlendirilir.

## Çıktı modülleri
- İşlem türü-şekil-sicil şartı tablosu.
- Lisans/devir sözleşmesi madde iskeleti ([doldurulacak] yer tutucularla).
- Sicile şerh ve üçüncü kişiye etki kontrol listesi.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
