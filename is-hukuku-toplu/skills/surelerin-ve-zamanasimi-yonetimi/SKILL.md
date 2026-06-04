---
name: surelerin-ve-zamanasimi-yonetimi
description: "Toplu is hukukundaki usuli sureleri (yetki itirazi, cagri, gorusme, grev bildirimi) ve sendikal tazminat ile TIS alacaklarinda zamanasimini hesaplar; herhangi bir surenin kacirilmamasi veya zamanasimi savunmasi gerektiginde kullanilir."
---

# Süreler, Hak Düşürücü Süreler ve Zamanaşımı

## Görev
Toplu iş hukukundaki kritik usuli süreleri ve zamanaşımını tek yerde toplayıp somut tarihlere bağlamak. Süre kaçırmak yetkiyi, davayı veya alacağı doğrudan düşürür.

## Soğuk başlangıç (intake)
- Hangi tetikleyici işlem oldu (yetki tespiti tebliği, çağrı, uyuşmazlık tutanağı, fesih)?
- İşlemin tebliğ/öğrenme tarihi tam olarak nedir?
- Talep edilen şey: yetki itirazı mı, sendikal tazminat mı, TİS alacağı mı?
- Süre durduran/kesen bir işlem var mı?

## Denetim şeması
1. **Yetki süreçleri:** Yetki tespitine itiraz **6 işgünü** (6356 m.43). Toplu görüşmeye çağrı **15 gün** (m.46), çağrıdan ilk toplantıya **30 gün** (m.46), toplu görüşme süresi **60 gün** (m.47).
2. **Grev/lokavt:** Uyuşmazlık tutanağının/arabuluculuk tutanağının tebliğinden itibaren grev kararı **60 gün** içinde alınmalı; uygulamadan **6 işgünü** önce bildirim (m.60). Süreler kaçırılırsa yetki düşer.
3. **Sendikal tazminat:** Sendikal tazminat talebinde, fesihle bağlantılı ise iş güvencesi başvuru süreleri (4857 m.20 — feshin tebliğinden itibaren bir aylık dava/arabuluculuk süresi) ile birlikte değerlendirilir; bağımsız sendikal tazminat talebinde genel zamanaşımı tartışılır (künye/uygulama için Yargıtay kararı `[doğrulanacak]`).
4. **TİS'ten doğan alacaklar:** TİS'in normatif hükümlerinden doğan ücret/ikramiye türü alacaklarda iş hukuku zamanaşımı rejimi (ücret alacakları 5 yıl — TBK m.147; kıdem/ihbar gibi tazminat alacaklarında 7036 sayılı Kanun ek/geçici düzenlemeleri ile 5 yıl) gözetilir.
5. **Ara sonuç:** Her tetikleyici için son gün hesaplanır; işgünü/takvim günü ayrımına dikkat edilir (yetki itirazı işgünü, görüşme süresi takvim günü).

İspat: tebliğ mazbatası, tutanak tarihi ve PTT/UYAP kayıtları esastır.

## Çıktı modülleri
- Süre takvimi tablosu (tetikleyici – süre türü – son gün).
- Zamanaşımı/hak düşürücü süre risk notu.
- Hatırlatma/kontrol listesi.

## Plugin bağlamı

Bu beceri `is-hukuku-toplu` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
