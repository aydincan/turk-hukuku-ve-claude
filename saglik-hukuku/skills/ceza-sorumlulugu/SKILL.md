---
name: ceza-sorumlulugu
description: "Tıbbi müdahaleden doğan ölüm veya yaralanmada hekimin taksirle öldürme/yaralama bakımından cezai sorumluluğunu ve soruşturma rejimini değerlendirmek için kullanılır."
---

# Hekimin Cezai Sorumluluğu

## Görev
Ölüm veya bedensel zararla sonuçlanan tıbbi müdahalede taksirle öldürme/yaralama suçlarının oluşup oluşmadığını ve usuli rejimi (soruşturma izni, ATK) belirlemek.

## Soğuk başlangıç (intake)
1. Sonuç ölüm mü, yaralanma mı, kalıcı sakatlık mı?
2. Hekim kamu görevlisi mi (kamu hastanesi) yoksa özel sektörde mi?
3. Şikâyet/soruşturma başladı mı; ATK raporu var mı?
4. Birden fazla sağlık çalışanı zincirleme mi sorumlu (ekip)?

## Denetim şeması
1. **Suç tipi**: Taksirle öldürme (TCK m.85) veya taksirle yaralama (TCK m.89). Yaralama şikâyete bağlıdır (basit hâl); bilinçli taksir ceza artırıcıdır (TCK m.22/3).
2. **Taksirin unsurları**: Dikkat ve özen yükümlülüğüne aykırılık + öngörülebilir sonuç + uygun illiyet. Standart sapması ATK/bilirkişi ile tespit edilir.
3. **İhmali davranış**: Hareketsizlikle (takipsizlik, sevk etmeme) gerçekleşen netice için TCK m.83.
4. **Hukuka uygunluk**: Endikasyonlu, rızaya dayalı, lege artis müdahale hukuka uygundur; rıza TCK m.26. Aydınlatma/onam eksikliği ayrıca tartışılır.
5. **Usul ve izin**: Kamu görevlisi hekim hakkında soruşturma kural olarak 4483 sayılı Kanun ve 3359 Ek m.18 çerçevesinde izne tabidir (yürürlükteki son hâl doğrulanmalı). Görevli yargı: asliye ceza.
6. **Ara sonuç**: Taksir + illiyet + zarar varsa suç oluşur; rıza ve lege artis icra cezai sorumluluğu kaldırabilir. Müterafik kusur ceza miktarına etki edebilir.

## Çıktı modülleri
- Suç unsuru değerlendirmesi (TCK m.85/89/83)
- Soruşturma izni ve görevli yargı notu
- ATK/bilirkişi raporuna itiraz noktaları
- İlkesel içtihat atfı (Yargıtay 12. CD; karararama.yargitay.gov.tr) [doğrulanacak]

## Plugin bağlamı

Bu beceri `saglik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
