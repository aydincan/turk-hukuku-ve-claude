---
name: sporcu-sozlesmesi-transfer
description: "Profesyonel sporcu sözleşmesi, transfer, geçici transfer veya tek taraflı fesih uyuşmazlıklarını değerlendirmek, sözleşme taslağı veya fesih/alacak stratejisi hazırlamak gerektiğinde kullanın."
---

# Sporcu Sözleşmeleri ve Transfer Hukuku

## Görev
Profesyonel sporcu sözleşmesinin kuruluşu, içeriği, transferi ve feshini ilgili federasyon statü/transfer talimatı ve TBK çerçevesinde değerlendirmek; sözleşme taslağı, fesih bildirimi veya tazminat/alacak hesabı üretmektir.

## Soğuk başlangıç (intake)
1. Sözleşme türü: profesyonel sporcu sözleşmesi, geçici transfer (kiralık), menajer sözleşmesi?
2. Süre, ücret, prim ve fesih hükümleri nasıl düzenlenmiş?
3. Uyuşmazlık ne: ödenmeyen ücret/prim, tek taraflı fesih, transfer engeli?
4. Sözleşmede tahkim/uyuşmazlık çözüm şartı var mı?
5. Milletlerarası transfer ve FIFA boyutu var mı?

## Denetim şeması
1. **Geçerlilik ve şekil**: Profesyonel sözleşmenin federasyona tescili ve şekil şartları (Profesyonel Futbolcuların Statüsü ve Transferleri Talimatı ya da ilgili branş statüsü) kontrol edilir; tescilsiz sözleşmenin sonuçları değerlendirilir.
2. **İçerik denetimi**: Ücret, prim, opsiyon, satın alma/geri alma hükümleri, bonservis ve cezai şart (TBK m.179-182) incelenir; aşırı cezai şartta TBK m.182/3 indirimi gündeme gelir.
3. **Fesih**: Haklı sebeple fesih (sporcu açısından ödememe, kulüp açısından disiplinsizlik) ile haksız tek taraflı fesih ayrımı; sözleşmenin korunması ilkesi (sportif haklı sebep, korumalı dönem) ve fesih tazminatının hesabı.
4. **Transfer**: Transfer dönemi kuralları, kiralık (geçici transfer) şartları, dayanışma katkı payı ve yetiştirme tazminatı (uluslararası transferde FIFA RSTP esasları) kontrol edilir.
5. **Görevli merci**: Talimattaki uyuşmazlık çözüm kurulu/tahkim; sözleşmedeki tahkim şartı ve milletlerarası unsurda FIFA/CAS.
6. **Ara sonuç**: Talebin türü (alacak, fesih tazminatı, transfer engelinin kaldırılması) ve dayanağı sabitlenir.

## Çıktı modülleri
- Sözleşme/transfer risk tablosu (madde madde)
- Fesih bildirimi veya alacak dilekçesi taslağı
- Tazminat/prim hesap çerçevesi
- Görevli merci ve süre notu

## Plugin bağlamı

Bu beceri `spor-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
