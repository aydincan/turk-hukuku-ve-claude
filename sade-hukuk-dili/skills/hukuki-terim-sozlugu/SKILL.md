---
name: hukuki-terim-sozlugu
description: "Bir metindeki hukuki ve Latince terimleri, kalıpları ve kısaltmaları müvekkile açıklayan sözlük üretmek; terimin yanlış eşanlamlıyla değiştirilmeden doğru karşılığını ve anlam farkını vermek gerektiğinde kullanılır."
---

# Hukuki Terim Açıklama ve Sözlük

## Görev
Bir belgedeki hukuki terimleri, Latince ifadeleri ve kısaltmaları okuyucuya açıklayan, anlam
nüanslarını koruyan bir sözlük/açıklama listesi üretmek. Amaç terimi yok etmek değil, doğru
anlamını yalın bir cümleyle vermek.

## Soğuk başlangıç (intake)
1. Hangi belge ve hangi hukuk alanı (terimlerin anlamı bağlama göre değişir)?
2. Okuyucunun seviyesi (hiç bilmeyen / temel bilen)?
3. Tüm terimler mi, yoksa işaretli olanlar mı açıklanacak?

## Denetim şeması
1. TERİM AVI: Metindeki teknik terimler, Latince kalıplar (inter alia, prima facie, per se, ex nunc/
   ex tunc) ve kısaltmalar (TBK, HMK, İİK, BAM/BİM, ATK) çıkarılır.
2. BAĞLAMA GÖRE TANIM: Her terim, kullanıldığı hukuk dalına göre tanımlanır; aynı kelime farklı
   alanda farklı anlam taşıyabilir ("ifa", "zilyetlik", "def'i").
3. NÜANS AYRIMI (anlam yükü): Karıştırılan çiftler ayrı ayrı açıklanır — zamanaşımı (borç durur
   ama def'i gerekir, TBK m.146 vd.) ≠ hak düşürücü süre (hak kendiliğinden düşer); fesih ≠ iptal
   ≠ dönme ≠ cayma; itiraz ≠ def'i; müteselsil ≠ müşterek sorumluluk; tazminat ≠ ceza.
4. YANLIŞ EŞANLAMLI YASAĞI: Hiçbir terim, hukuki sonucu değiştiren bir günlük kelimeyle eşitlenmez;
   tanım açıklayıcıdır, eşitleyici değildir.
5. ATIF: Terimin dayandığı temel madde varsa parantezle verilir (ör. muacceliyet — TBK m.90 vd.).
6. ARA SONUÇ: Açıklamalar bağlama uygun ve nüans koruyor mu denetlenir.

## Çıktı modülleri
- Alfabetik veya metin sırasına göre terim listesi.
- Her terim için: yalın tanım + (varsa) madde atfı + karıştırılan terimden farkı.
- "Aynı kelime başka anlamda" uyarı kutusu.

## Plugin bağlamı

Bu beceri `sade-hukuk-dili` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
