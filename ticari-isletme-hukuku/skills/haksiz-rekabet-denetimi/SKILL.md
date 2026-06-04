---
name: haksiz-rekabet-denetimi
description: "Bir ticari davranisin (aldatici reklam, kotuleme, sirlarin ifsasi, baskasinin emegi/itibarindan yararlanma, calisanlari ayartma) haksiz rekabet olusturup olusturmadigini ve tespit-men-ref-tazminat yaptirimlarini belirlemek gerektiginde kullanilir."
---

# Haksız Rekabet Denetimi ve Yaptırımları

## Görev
Bir davranışın TTK anlamında haksız rekabet oluşturup oluşturmadığını saptamak ve uygun hukuki/cezai yaptırımları kurmak. Haksız rekabet, dürüst rekabeti ve katılanların menfaatini korur; tacir-tacir dışı herkese karşı uygulanır.

## Soğuk başlangıç (intake)
1. Şikâyet edilen davranış ne (reklam, kötüleme, taklit, sır ifşası, ayartma)?
2. Davranış rekabeti etkiliyor mu; aldatıcı/dürüstlüğe aykırı mı?
3. Zarar veya zarar tehlikesi var mı; müvekkilin durumu nasıl etkilendi?
4. Davranışın öğrenildiği ve gerçekleştiği tarihler ne (zamanaşımı)?

## Denetim şeması
1. **Genel hüküm:** TTK m.54 — rakipler arasında veya tedarik edenlerle müşteriler arasındaki ilişkileri etkileyen aldatıcı veya dürüstlük kuralına aykırı davranışlar haksız rekabettir. Kusur şart değildir (tespit/men için); tazminat için kusur aranır.
2. **Örnek haller:** TTK m.55 — (a) dürüstlüğe aykırı reklam ve satış yöntemleri (kötüleme, yanıltıcı bilgi, gerçeğe aykırı üstünlük iddiası), (b) sözleşmeyi ihlale veya sona erdirmeye yöneltme, (c) başkasının iş ürünlerinden yetkisiz yararlanma, (d) üretim/iş sırlarını hukuka aykırı ifşa, (e) iş şartlarına uymama, (f) dürüstlüğe aykırı genel işlem koşulları kullanma. Liste örnekleyicidir; m.54 genel hükmü tamamlar.
3. **Hukuki sorumluluk talepleri:** TTK m.56 — menfaati ihlal edilen veya tehlikeye giren: (i) fiilin haksız olduğunun tespiti, (ii) men (durdurma/önleme), (iii) sonucun ortadan kaldırılması (ref) ve beyanların düzeltilmesi, (iv) kusur varsa maddi tazminat, (v) TBK m.58 koşullarıyla manevi tazminat, (vi) lehe sağlanan menfaatin devri (vekâletsiz iş görme). Müşteriler ve mesleki kuruluşlar da m.56/2 ile dava açabilir.
4. **Cezai sorumluluk:** TTK m.62 — sayılan hallerde şikâyet üzerine cezai yaptırım; tüzel kişiler için m.63.
5. **Zamanaşımı:** TTK m.60 — dava hakkı, öğrenmeden itibaren 1 yıl ve her hâlde doğumundan itibaren 3 yıl geçince zamanaşımına uğrar. İhtiyati tedbir (TTK m.61) ile durum dondurulabilir. Ara sonuç: m.54/55 unsuru + menfaat ihlali → m.56 talepleri + gerekiyorsa tedbir.

## Çıktı modülleri
- Davranışın m.55 alt bendiyle eşleştirilmesi ve nitelendirme notu.
- Talep matrisi (tespit/men/ref/maddi-manevi tazminat) ve zamanaşımı durumu.
- İhtiyati tedbir talebi ve dava dilekçesi talep sonucu taslağı.

## Plugin bağlamı

Bu beceri `ticari-isletme-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
