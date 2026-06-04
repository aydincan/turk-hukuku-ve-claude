---
name: basvuru-dilekcesi-taslagi
description: "Sulh ceza hâkimliğine başvuru veya itiraz dilekçesini; taraf-merci bilgisi, talep sonucu, gerekçe ve delil mimarisiyle taslak olarak üretmek gerektiğinde kullanılır."
---

# Başvuru ve İtiraz Dilekçesi Taslağı

## Görev
5326 m.27/29 usulüne uygun, gerekçeli ve delillere bağlı bir başvuru/itiraz dilekçesi taslağı üretmek; yer tutucularla eksik bilgiyi işaretlemek.

## Soğuk başlangıç (intake)
- Başvurucu kim, yaptırımı veren idare hangisi, dosya/karar numarası ne?
- Tebliğ tarihi ve kalan süre nedir?
- Hangi sakatlık iddiaları öne çıkacak (yetki, şekil, sübut, miktar, zamanaşımı)?
- Hangi deliller (tutanak eleştirisi, tanık, belge, bilirkişi) sunulacak?

## Denetim şeması
1. **Başlık ve merci:** "... Sulh Ceza Hâkimliğine" (yetkili: yaptırımı veren idarenin yeri — 5326 m.27/1). İtirazda izleyen numaralı hâkimlik (m.29).
2. **Taraflar:** Başvurucu/vekil ve karşı taraf (ilgili idare) tam künyeyle; `[doldurulacak]` yer tutucular.
3. **Konu ve süre:** "... tarihli ve ... sayılı idari yaptırım kararının kaldırılması" talebi; tebliğ tarihi belirtilerek 15 günlük sürede olunduğu vurgulanır.
4. **Açıklamalar (gerekçe):** Sırasıyla zamanaşımı (m.20-21), yetki, şekil/tebligat (m.25, 7201), kabahatin unsurlarının oluşmadığı (m.4, m.9), miktar/takdir hatası (m.17). Her iddia somut maddeye altlanır.
5. **Deliller:** İdari yaptırım kararı, tutanak, tebligat zarfı, tanık listesi, belge, gerekirse bilirkişi/keşif talebi. İspat yükünün idarede olduğu hatırlatılır.
6. **Talep sonucu:** Öncelikle kararın kaldırılması; kademeli olarak miktarın indirilmesi; yargılama gideri ve vekâlet ücreti. İtirazda "kararın kaldırılarak başvurunun kabulü" talebi.

## Çıktı modülleri
- Başvuru dilekçesi tam taslağı (yer tutuculu).
- İtiraz dilekçesi varyantı (m.29).
- Delil dizini ve eksik bilgi listesi.

## Plugin bağlamı

Bu beceri `kabahatler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
