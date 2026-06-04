---
name: dava-gorev-yetki-ve-ihtarname
description: "Sebepsiz zenginleşme alacağı için ihtarname çekmek, görevli ve yetkili mahkemeyi belirlemek, dava şartı arabuluculuğu kontrol etmek ve dava dilekçesi iskeleti kurmak gerektiğinde kullanılır."
---

# Dava Yolu, Görev-Yetki ve İhtar/Dilekçe Taslağı

## Görev
İade talebini ihtardan davaya taşıyan usul rotasını kurmak: temerrüt için ihtar, görevli ve yetkili mahkeme, dava şartı arabuluculuk kontrolü ve HMK'ya uygun dilekçe iskeleti. Eksik ön şart veya yanlış mahkeme, dava şartı yokluğundan usulden ret doğurur.

## Soğuk başlangıç (intake)
- Tarafların sıfatı (gerçek kişi, tacir); iş ticari mi?
- Talep para alacağı mı, aynen iade mi; miktar ne?
- Borçluya ihtar çekildi mi; temerrüt oluştu mu?
- Daha önce arabuluculuğa başvuruldu mu?

## Denetim şeması
1. **Temerrüt ve ihtar (TBK m.117).** Sebepsiz zenginleşme borcu kural olarak muaccel; alacaklının ihtarıyla borçlu temerrüde düşer ve temerrüt faizi (TBK m.120; ticari işte 3095 s.K.) ihtardan itibaren işler. İhtar, faiz başlangıcı için kritik belge.
2. **Görevli mahkeme.** Genel kural Asliye Hukuk (HMK m.2). İki tarafın da tacir olduğu ve işin ticari sayıldığı hallerde Asliye Ticaret (TTK m.4-5). Tüketici işleminden kaynaklanıyorsa Tüketici Mahkemesi/Hakem Heyeti (6502 m.73) kapsamı kontrol edilir.
3. **Yetkili mahkeme.** Genel yetki davalının yerleşim yeri (HMK m.6); sözleşme ilişkisinden doğan iadelerde ifa yeri mahkemesi de yetkili olabilir (HMK m.10). Para borçlarında alacaklının yerleşim yeri kuralı (TBK m.89) ifa yeri belirlemede gözetilir.
4. **Dava şartı arabuluculuk.** İki tarafın tacir olduğu, konusu para olan alacak/tazminat talepleri için TTK m.5/A uyarınca arabuluculuk dava şartıdır; başvurulmadan açılan dava usulden reddedilir. Genişleyen kapsam (7445 s.K.) ayrıca kontrol edilir.
5. **Dilekçe mimarisi (HMK m.119).** Taraflar, vakıalar (kazandırma + sebepsizlik), hukuki sebep (TBK m.77 vd.), deliller ve açık talep sonucu (anapara + faiz başlangıcı + tip). Tip (geçerli olmayan/gerçekleşmeyen/sona eren sebep) açıkça belirtilir.
6. **Ara sonuç.** İhtar → arabuluculuk (gerekirse) → doğru mahkemede dava sıralaması; görev kamu düzeninden resen, yetki itirazı ilk itiraz olarak süresinde ileri sürülür.

## Çıktı modülleri
- İade ihtarnamesi taslağı (temerrüt + faiz başlangıcı vurgulu).
- Görev-yetki-arabuluculuk karar ağacı.
- Dava dilekçesi iskeleti (HMK m.119 unsurları + [doldurulacak] yer tutucular).

## Plugin bağlamı

Bu beceri `sebepsiz-zenginlesme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
