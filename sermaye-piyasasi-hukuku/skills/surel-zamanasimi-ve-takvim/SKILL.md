---
name: surel-zamanasimi-ve-takvim
description: "Sermaye piyasası uyuşmazlıklarında dava açma süreleri, idari yaptırım ve suçlarda zamanaşımı, izahname/kamuyu aydınlatma sorumluluğunda zamanaşımı ve hak düşürücü sürelerin hesaplanması gerektiğinde kullanılır."
---

# Süreler, Zamanaşımı ve Takvim

## Görev
Dosyadaki tüm süreleri (dava açma, zamanaşımı, hak düşürücü) ilgili norma göre hesaplamak; başlangıç anı, durma/kesilme ve son günü belgelemek.

## Soğuk başlangıç (intake)
- Talep türü nedir: idari yaptırıma iptal, tazminat, cezai sorumluluk mu?
- Tetikleyici olay ve öğrenme/tebliğ tarihi nedir?
- Süreyi durduran/kesen işlem (başvuru, dava, Kurul kararı) var mı?
- Birden çok eksen (idari + adli) varsa her biri için ayrı takvim gerekiyor mu?

## Denetim şeması
1. **Eksen ayrımı:** İdari yaptırıma iptal süresi İYUK'a; izahname/kamuyu aydınlatma tazminatı SPK m.10/m.32 ve TBK'ya; piyasa suçlarında dava zamanaşımı TCK'ya tabidir. Her eksen ayrı hesaplanır.
2. **İptal davası süresi:** İYUK m.7 uyarınca kararın tebliğinden itibaren işleyen dava açma süresi; üst makama/Kurul'a başvuru (İYUK m.11) süreyi durdurabilir. Hak düşürücüdür, re'sen dikkate alınır.
3. **Tazminat zamanaşımı:** İzahname/kamuyu aydınlatma sorumluluğunda SPK özel hükmü ile TBK m.72 (haksız fiilde öğrenmeden 2, her hâlde 10 yıl) birlikte değerlendirilir; sözleşmesel sorumlulukta TBK m.146 (10 yıl) esas alınır.
4. **Ceza zamanaşımı:** Piyasa suçlarında (SPK m.106-107) dava zamanaşımı, suçun cezası üzerinden TCK m.66'ya göre belirlenir; Kurul mütalaası şartı (m.115) süreçle birlikte not edilir.
5. **Takvim kurma:** Başlangıç anı, durma/kesilme sebepleri ve son gün tarih olarak yazılır; ara sonuç olarak en yakın kritik tarih öne çıkarılır. Tatil/adli tatil etkisi kontrol edilir.

## Çıktı modülleri
- Eksen bazlı süre tablosu (başlangıç-durma-son gün)
- Kritik tarih uyarı listesi
- Zamanaşımı/hak düşürücü ayrımı notu
- Sonraki adım ve hatırlatma planı

## Plugin bağlamı

Bu beceri `sermaye-piyasasi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
