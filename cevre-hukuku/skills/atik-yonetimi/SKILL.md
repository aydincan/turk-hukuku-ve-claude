---
name: atik-yonetimi
description: "Atık üretimi, taşınması, geri kazanımı ve bertarafı; tehlikeli atık yükümlülükleri, atık hiyerarşisi ve genişletilmiş üretici sorumluluğu kaynaklı uyuşmazlık ve uyum sorularında; izinsiz depolama/döküm yaptırımlarında kullan."
---

# Atık Yönetimi ve Tehlikeli Atık

## Görev
Atık üreten, taşıyan, geri kazanan veya bertaraf eden işletmelerin yükümlülüklerini belirlemek; izinsiz atık işlemlerinden doğan idari/cezai/özel hukuk sorumluluğunu değerlendirmek.

## Soğuk başlangıç (intake)
1. Atık türü nedir: evsel, ambalaj, tehlikeli, tıbbi, hafriyat, elektronik?
2. Müvekkil zincirde hangi rolde: üretici, taşıyıcı, ara depolama, geri kazanım/bertaraf tesisi?
3. Atık beyanı, MoTAT/atık taşıma belgeleri ve lisanslar tam mı?
4. İzinsiz depolama/döküm iddiası veya çevresel zarar var mı?

## Denetim şeması
1. **Hiyerarşi ve genel yükümlülük**: Atık Yönetimi Yönetmeliği önleme > yeniden kullanım > geri dönüşüm > geri kazanım > bertaraf sırasını dayatır; 2872 m.8 kirletme ve çevreye zarar verme yasağını kurar. Üretici, atığını mevzuata uygun yönetmekle yükümlüdür.
2. **Tehlikeli atık özel rejimi**: Tehlikeli atıklar için ayrı toplama, etiketleme, lisanslı taşıma (MoTAT) ve bertaraf zorunludur; "beşikten mezara" izlenebilirlik aranır.
3. **Genişletilmiş üretici sorumluluğu**: Ambalaj ve belirli ürünlerde piyasaya sürenin toplama/geri kazanım yükümlülüğü doğar.
4. **Yaptırım ve sorumluluk**: İzinsiz/usulsüz atık işlemi 2872 m.20-23 idari para cezası ve m.15 durdurma sonucu doğurur; kasten çevreye atık verme TCK m.181-182 kapsamına girebilir; çevresel zararda m.28 kusursuz/müteselsil sorumluluk işler.
5. **İspat ve ara sonuç**: Beyan kayıtları, taşıma belgeleri, analiz ve numune zinciri belirleyicidir; belge eksikliği hem yaptırım hem sorumluluk doğurur.

## Çıktı modülleri
- Atık türü ve yükümlülük matrisi
- Belge/lisans uyum kontrol listesi
- İzinsiz işlem yaptırım ve sorumluluk değerlendirmesi
- Düzeltici eylem ve uyum planı taslağı

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
