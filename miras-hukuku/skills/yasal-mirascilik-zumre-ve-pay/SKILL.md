---
name: yasal-mirascilik-zumre-ve-pay
description: "Vasiyet ya da atama yokken kimin mirasçı olduğunu ve paylarını hesaplamak; eş ile zümrelerin birlikte mirasçılığı, halefiyet, evlatlık ve evlilik dışı çocuk durumları söz konusu olduğunda kullanılır."
---

# Yasal Mirasçılık, Zümre Sistemi ve Pay Hesabı

## Görev
Ölüme bağlı geçerli bir tasarruf yoksa veya tasarruf terekenin bir kısmını kapsıyorsa, yasal mirasçıları ve paylarını TMK m.495-501 ve m.499 uyarınca kesin kesirlerle belirlemek.

## Soğuk başlangıç (intake)
- Mirasbırakanın altsoyu (çocuk, torun) var mı, hayatta mı?
- Sağ kalan eş var mı? Mal rejimi tasfiyesi yapıldı mı?
- Altsoy yoksa ana-baba veya kardeşler/yeğenler hayatta mı?
- Evlatlık, evlilik dışı (soybağı kurulu) çocuk var mı?
- Önceden ölen mirasçının yerine halefiyet (torunlar) söz konusu mu?

## Denetim şeması
1. **Mal rejimini önce tasfiye et.** Edinilmiş mallara katılmada sağ kalan eşin katılma alacağı (TMK m.236) terekeye dahil değildir; önce ayrılır, kalan tereke paylaşılır. Bu sıra atlanırsa pay hesabı yanlış çıkar.
2. **Zümreyi belirle.** Birinci zümre altsoy (m.495); yoksa ikinci zümre ana-baba ve altsoyu (m.496); yoksa üçüncü zümre büyük ana-baba ve altsoyu (m.497). Üst zümre varsa alt zümre mirasçı olamaz.
3. **Halefiyeti uygula (m.495/2, m.496/2).** Önceden ölen mirasçının payı kök içinde onun altsoyuna geçer (örn. ölen çocuğun payı torunlara eşit).
4. **Sağ kalan eşin payını ekle (m.499):** altsoyla 1/4, ikinci zümreyle 1/2, üçüncü zümreyle 3/4; üçüncü zümrede büyük ana-baba altsoyu yoksa eş tek başına mirasçı olur (m.499/4 sınırı).
5. **Özel durumlar:** evlatlık ve altsoyu mirasçıdır ama evlat edinenin mirasçısı olmaz (m.500); evlilik dışı çocuk soybağı kurulunca altsoy gibidir (m.498); mirasçı yoksa Devlet (m.501).
6. **Ara sonuç:** her mirasçının kesirli payını yaz; ispat için nüfus kaydı/vukuatlı aile belgesi ve soybağı kaydını dayanak göster (TMK m.6).

## Çıktı modülleri
- Kesirli pay tablosu (mal rejimi tasfiyesi ayrıştırılmış)
- Mirasçılık belgesi (veraset ilamı) talebi taslağı (TMK m.598)
- Halefiyet/kök şeması
- Eksik belge listesi (nüfus, soybağı, evlat edinme kararı)

## Plugin bağlamı

Bu beceri `miras-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
