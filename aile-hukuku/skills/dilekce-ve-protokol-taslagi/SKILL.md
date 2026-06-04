---
name: dilekce-ve-protokol-taslagi
description: "Boşanma, nafaka, velayet, mal rejimi tasfiyesi dava dilekçeleri ile anlaşmalı boşanma protokolü ve 6284 başvurusu gibi belgeleri HMK formatında taslaklaştırmak gerektiğinde kullanılır."
---

# Dava Dilekçesi ve Anlaşmalı Boşanma Protokolü Taslağı

## Görev
Aile hukuku belgesini (dava/cevap dilekçesi, anlaşmalı boşanma protokolü, 6284 başvurusu) HMK m.119 mimarisine ve [doldurulacak] yer tutucu disiplinine uygun taslaklaştırmak.

## Soğuk başlangıç (intake)
1. Hangi belge isteniyor (dava dilekçesi, protokol, başvuru, cevap)?
2. Taraflar, çocuklar ve talep kalemleri (boşanma, nafaka türü ve miktarı, velayet, tazminat, tasfiye) net mi?
3. Hangi deliller mevcut (tanık, mesaj, rapor, tapu, banka kaydı)?
4. Anlaşmalı ise taraflar tüm mali ve çocuk konularında mutabık mı?

## Denetim şeması
1. **Dava dilekçesi iskeleti (HMK m.119).** Mahkeme; taraf ve vekil bilgileri; konu; **açık talep sonucu** (boşanma + her bir fer'i ayrı ayrı ve miktarlı); vakıalar (sebep ve kusur olgularının kronolojisi); hukuki sebepler (TMK m.166/166/3 vd., m.174, m.175, m.182, m.169); **deliller her vakıaya bağlanarak** (tanık, isticvap, sosyal/ekonomik araştırma, uzman raporu); harç ve imza. Eksik bilgiler [doldurulacak] ile işaretlenir, uydurulmaz.
2. **Anlaşmalı boşanma protokolü (TMK m.166/3).** Şartlar: evlilik en az 1 yıl; tarafların özgür iradesi; hâkimce uygun bulunma. Protokol mutlaka şunları içermeli: boşanma iradesi, yoksulluk/iştirak nafakası (tür-miktar-artış), velayet ve kişisel ilişki takvimi, maddi/manevi tazminat, mal rejimi/ev eşyası paylaşımı, ziynet, soyadı; hâkim çocuğun yararına aykırı düzenlemeyi değiştirebilir (m.166/3 son cümle).
3. **6284 başvurusu.** Sade dille olay anlatımı + talep edilen tedbirler (m.5 önleyici / m.3-4 koruyucu) + aciliyet beyanı; harç muafiyeti notu.
4. **Tutarlılık denetimi.** Talep sonucu ile vakıa ve hukuki sebepler örtüşüyor mu; nafaka türleri karışmış mı; tasfiye talebi ayrı davaya mı bırakılacak; süre/hak düşürücü süre dilekçede gözetilmiş mi?
5. **Ara sonuç.** Belge taslağı + eksik veri (yer tutucu) listesi + ekler dizini.

## Çıktı modülleri
- İlgili belgenin HMK uyumlu tam taslağı (yer tutuculu).
- Talep-vakıa-hukuki sebep-delil eşleme kontrolü.
- Ekler ve delil dizini ile imza/harç notu.

## Plugin bağlamı

Bu beceri `aile-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
