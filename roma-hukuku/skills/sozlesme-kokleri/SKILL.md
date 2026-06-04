---
name: sozlesme-kokleri
description: "TBK sözleşme tiplerinin (satış, kira, eser, vekâlet, ortaklık, kefalet) Roma contractus sistematiğine (re-verbis-litteris-consensu) bağlanması; rıza sözleşmesi, ifa, hasarın geçişi gibi konularda tarihî-dogmatik temel gerektiğinde kullanılır."
---

# Sözleşme Hukukunun Roma Kökleri

## Görev
TBK'daki sözleşme hukuku kavramlarını ve isimli sözleşme tiplerini Roma'nın contractus sistematiğine bağlamak; rıza ile kuruluş, ifa, hasarın geçişi gibi dogmatik düğümleri tarihî kökenleriyle açıklamak.

## Soğuk başlangıç (intake)
- Hangi sözleşme tipi veya kavram (kuruluş, hasar, ifa, sözleşme özgürlüğü)?
- Klasik contractus tasnifi mi yoksa tek bir kurum mu inceleniyor?
- Çıktı akademik mi, yorum argümanı mı?

## Denetim şeması
1. Modern temeli sabitle: sözleşme rıza ile kurulur (TBK m.1 icap-kabul; TBK m.26 sözleşme özgürlüğü). İsimli sözleşmeler: satış TBK m.207, kira TBK m.299, eser TBK m.470, vekâlet TBK m.502, adi ortaklık TBK m.620, kefalet TBK m.581.
2. Roma contractus tasnifini kur: borç doğuran rıza sözleşmeleri Roma'da consensu doğan dört tiptir — emptio venditio (satış), locatio conductio (kira/hizmet/eser), societas (ortaklık), mandatum (vekâlet). Bunların yanında re (ödünç, vedia, rehin), verbis (stipulatio) ve litteris doğan sözleşmeler vardır.
3. Eşleştir: modern isimli sözleşmenin Roma karşılığını ve consensu/re/verbis kategorisini belirle. Locatio conductio'nun üçe bölünmesini (rei = kira, operarum = hizmet, operis = eser/istisna) modern TBK ayrımıyla karşılaştır.
4. Rıza ilkesini temellendir: consensu sözleşmelerde şekilsiz rıza yeterliydi — bu, TBK m.1 ve şekil serbestisinin (TBK m.12) kökenidir. Şekle bağlı istisnaları (TMK m.706 taşınmaz devri resmî şekil) Roma'nın şekilci verbis/litteris kurumlarıyla kıyasla.
5. Hasarın geçişini bağla: periculum est emptoris (satışta hasar alıcıya geçer) Roma kuralıyken, TBK m.208 farklı bir denge kurar — bu sapmayı açıkça işaretle ve yürürlükteki kuralın TBK m.208 olduğunu vurgula.
6. İfa ve ahde vefa: pacta sunt servanda ilkesinin TBK sözleşme bağlılığındaki yansımasını; aşırı ifa güçlüğü (TBK m.138) ile clausula rebus sic stantibus tarihî düşüncesini bağla. Ara sonuç: sözleşme tipini ve dogmatik düğümü doğru köke oturt.

İspat/dayanak: modern sözleşme maddeleri ile; Roma kuralları/maximleri fragmanla; hasarda yürürlükteki kural TBK m.208 olarak sabit; doktrin [doğrulanacak].

## Çıktı modülleri
- Sözleşme tipi eşleştirme tablosu (TBK maddesi / Roma contractus / kategori).
- Rıza ve şekil notu.
- Hasar ve ahde vefa karşılaştırması (sapma uyarısıyla).

## Plugin bağlamı

Bu beceri `roma-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
