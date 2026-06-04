---
name: temerrut-takip-icra
description: "Kredi borçlusunun temerrüdü, muacceliyet ihtarı, genel kredi sözleşmesine veya kambiyo senedine dayalı icra takibi, itirazın iptali/kaldırılması ve rehnin paraya çevrilmesi süreçlerini kurmak veya bunlara karşı savunma geliştirmek gerektiğinde kullanılır."
---

# Kredi Temerrüdü, Muacceliyet ve İcra Takibi

## Görev
Kredi alacağının tahsili için doğru takip yolunu seçmek ve usul adımlarını kurmak; borçlu/kefil tarafında ise muacceliyet, faiz ve takibe karşı savunma stratejisi geliştirmek.

## Soğuk başlangıç (intake)
- Alacağın dayanağı: genel kredi sözleşmesi, taksitli tüketici kredisi, bono/çek, ipotek/rehinli kredi?
- Temerrüt gerçekleşti mi; muacceliyet ihtarı/önel verildi mi?
- Teminat var mı (ipotek/rehin/kefil); rehinden önce takip yasağı (İİK m.45) söz konusu mu?
- Borçlu tüketici mi (TKHK m.27 muacceliyet sınırı uygulanır mı)?

## Denetim şeması
1. **Temerrüt ve muacceliyet**: Borçlunun temerrüdü TBK m.117 vd. ile kurulur. Sözleşmedeki muacceliyet kaydı geçerli ise ihtarla tüm borç muaccel olur; tüketici kredisinde TKHK m.27 gereği en az iki taksidin ödenmemesi ve 30 gün önelli ihtar şartı aranır, aksi halde muacceliyet işlemez.
2. **Takip yolu seçimi**: Rehinle temin edilmiş alacakta kural olarak önce rehnin paraya çevrilmesi yoluyla takip gerekir (İİK m.45); kambiyo senedi varsa İİK m.167 vd. kambiyo senetlerine özgü takip; aksi halde genel haciz yoluyla ilamsız takip ve itiraz halinde itirazın iptali davası (İİK m.67) veya itirazın kaldırılması (İİK m.68 — belge koşulu).
3. **Faiz ve hesap**: Akdi faizden temerrüt faizine geçiş, bileşik faiz dayanağı (TTK m.8-9 istisnaları), masraf kalemleri denetlenir; aşan/dayanaksız kalemler takibe itiraz konusu olur.
4. **Savunma cephesi**: Borçlu/kefil için muacceliyetin oluşmadığı, genel işlem koşulu/haksız şart nedeniyle bazı kalemlerin geçersizliği, kefaletin şekil eksikliği (TBK m.583-584), zamanaşımı (kambiyoda kısa süreler) def'ileri kurulur.
5. **Ticari uyuşmazlıkta arabuluculuk**: Genel kredi sözleşmesine dayalı alacak davasında (icra takibi hariç, dava aşamasında) TTK m.5/A dava şartı arabuluculuk kontrol edilir. Ara sonuç olarak takip yolu, açılacak dava ve süreleri yaz.

## Çıktı modülleri
- Takip yolu karar ağacı ve usul adımları.
- Takip talebi / itirazın iptali dava iskeleti.
- Borçlu/kefil için def'i ve itiraz listesi.

## Plugin bağlamı

Bu beceri `bankacilik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
