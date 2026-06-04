---
name: tapu-iptali-tescil-muvazaa
description: "Tapu kaydı gerçek hak durumunu yansıtmadığında (muvazaa, mirastan mal kaçırma, sahtecilik, vekâlet kötüye kullanımı, hata) tapu iptali ve tescil davasını kurmak; tescile güven ve iyiniyetli üçüncü kişi savunmalarını değerlendirmek için kullanılır."
---

# Tapu İptali-Tescil, Muris Muvazaası ve Yolsuz Tescil

## Görev
Tapu kaydı ile gerçek hak durumu arasındaki çelişkiyi gidermek: yolsuz veya muvazaalı tescili iptal ettirip gerçek hak sahibi adına tescili sağlamak; tescile güvenen iyiniyetli üçüncü kişinin korunup korunmadığını belirlemek.

## Soğuk başlangıç (intake)
- Tapu şu an kimin adına; müvekkil hak iddiasını neye dayandırıyor (miras, muvazaa, sahtecilik, vekâlet aşımı, hata)?
- Devir bedelli görünüp gerçekte bedelsiz mi (muris muvazaası şüphesi); mirasçıdan mal kaçırma iddiası var mı?
- Yolsuz/muvazaalı devirden sonra taşınmaz üçüncü kişiye geçti mi; o kişi iyiniyetli mi?
- Kayıt üzerinde ipotek, haciz, şerh var mı; ihtiyati tedbir gerekiyor mu?

## Denetim şeması
1. **Sicilin gücü**: Tapu kaydı doğruluk karinesi taşır (TMK m.7, m.992); ayni haklar tescille doğar (m.1021). İddia eden aksini ispatla yükümlüdür (m.6).
2. **Yolsuz tescil (m.1024-1025)**: Geçerli hukuki sebebe dayanmayan tescil yolsuzdur; gerçek hak sahibi tapu iptali ve tescil ister (m.1025). Sahtecilik, vekâletin kötüye kullanılması, ehliyetsizlik bu kapsamdadır.
3. **Muris muvazaası**: Miras bırakanın, mirasçıdan mal kaçırmak amacıyla gerçekte bağışladığı taşınmazı satış/ölünceye kadar bakma gibi göstermesi hâlinde işlem muvazaa nedeniyle geçersizdir (TBK m.19; TMK m.2). Saklı paya bağlı olmaksızın tüm mirasçılar dava açabilir; amaç (mal kaçırma kastı) ve bedel-emsal karşılaştırması ile araştırılır [ilkeler için karararama.yargitay.gov.tr].
4. **Tenkis ile ayrım**: Gerçek bir bağış varsa muvazaa değil, saklı pay ihlali söz konusudur ve yol tenkistir (TMK m.560 vd.); muvazaa ile tenkis talebi terditli ileri sürülebilir.
5. **Tescile güven savunması (m.1023)**: Yolsuz/muvazaalı kayda iyiniyetle güvenip ayni hak kazanan üçüncü kişi korunur; bu hâlde aynen iade mümkün olmaz, tazminata gidilir. İyiniyetin sınırı m.3'tür; durumun gerektirdiği özen gösterilmemişse koruma yoktur.
6. **Tedbir**: Kaydın üçüncü kişiye devrini önlemek için tapuya ihtiyati tedbir şerhi istenir (HMK m.389 vd.; TMK m.1010).
7. **Ara sonuç**: İyiniyetli kazanım yoksa iptal-tescil; varsa gerçek hak sahibine tazminat (gerekirse m.1007 yolu).

## Çıktı modülleri
- Tapu iptali ve tescil dava dilekçesi iskeleti (kayıt, sebep, terditli tenkis talebi).
- Muvazaa/iyiniyet değerlendirme tablosu (bedel-emsal, özen, devir zinciri).
- İhtiyati tedbir/şerh dilekçesi notu; yetki HMK m.12 (taşınmazın yeri).

## Plugin bağlamı

Bu beceri `gayrimenkul-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
