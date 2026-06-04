---
name: hava-su-gurultu-kirliligi
description: "Emisyon, atıksu deşarjı, hava kalitesi ve çevresel gürültü kaynaklı kirlilik iddialarında, limit aşımı tespitinde ve komşuluk hukuku ile kesişen rahatsızlık uyuşmazlıklarında; ölçüm ve numune usulünün denetiminde kullan."
---

# Hava, Su ve Gürültü Kirliliği

## Görev
Hava emisyonu, su deşarjı ve çevresel gürültü kaynaklı kirlilik iddialarını sınır değerler ve ölçüm usulü üzerinden denetlemek; idari yaptırım, faaliyet durdurma ve özel hukuk taleplerini birlikte ele almak.

## Soğuk başlangıç (intake)
1. Hangi unsur: hava emisyonu, atıksu deşarjı, içme/yüzey suyu, çevresel gürültü?
2. Limit aşımı iddiası hangi ölçüme dayanıyor; ölçümü kim, hangi yöntemle yaptı?
3. Etkilenen taraf var mı (komşu tesis, yerleşim, sulak alan)?
4. Talep idari yaptırım mı, faaliyet durdurma mı, tazminat/el atma mı?

## Denetim şeması
1. **Sınır değerler**: Sanayi Kaynaklı Hava Kirliliğinin Kontrolü ve Su Kirliliği Kontrolü Yönetmelikleri ile Çevresel Gürültü Yönetmeliği sektörel limitleri belirler; 2872 m.8 ve m.11 kirletme yasağı ve arıtma yükümlülüğünün dayanağıdır.
2. **Ölçüm/numune usulü**: Numunenin akredite laboratuvarca, usulüne uygun alınması ve zincirin korunması esastır; usulsüz ölçüm hem yaptırımı hem de iddiayı çürütür.
3. **İdari sonuç**: Limit aşımında 2872 m.20-23 idari para cezası ve m.15 faaliyet durdurma uygulanır; tekerrür ağırlaştırıcıdır.
4. **Özel hukuk kesişimi**: Sürekli kirlilik/rahatsızlık komşuluk hukukunda el atmanın önlenmesi (TMK m.683, m.737 katlanma sınırı) ve TBK m.49 vd. tazminat talebi doğurabilir; görevli mahkeme adli yargıdır.
5. **İspat ve ara sonuç**: Bilirkişi, keşif ve karşı ölçüm belirleyicidir; ölçümler arasındaki çelişki ek/yeniden bilirkişiyi gerektirir.

## Çıktı modülleri
- Limit aşımı tespit tablosu (parametre + sınır + ölçüm)
- Ölçüm/numune usul denetim notu
- İdari yaptırım ve özel hukuk talep ayrımı
- Bilirkişi/keşif delil planı

## Plugin bağlamı

Bu beceri `cevre-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
