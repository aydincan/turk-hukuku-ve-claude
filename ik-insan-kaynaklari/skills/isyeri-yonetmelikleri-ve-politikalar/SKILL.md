---
name: isyeri-yonetmelikleri-ve-politikalar
description: "Personel yönetmeliği, disiplin yönetmeliği, etik kod, uzaktan çalışma veya kılık-kıyafet politikası gibi iç düzenlemeler hazırlanacak veya mevcutları gözden geçirilecekse kullanılır."
---

# İşyeri Yönetmelikleri ve İK Politikaları

## Görev
İşverenin iç düzenlemelerini (personel/disiplin yönetmeliği, etik kod, izin, uzaktan çalışma politikası) hukuken bağlayıcı ve dava dayanağı oluşturacak biçimde kurgulamak; bunların çalışma koşulu hâline gelmesini ve değiştirilmesini doğru yönetmek.

## Soğuk başlangıç (intake)
1. Hangi politika hazırlanıyor (disiplin, etik, uzaktan çalışma, bilgi güvenliği)?
2. Yönetmelik sözleşmenin eki mi, yoksa tek taraflı işveren talimatı mı olacak?
3. Çalışanlara nasıl tebliğ ve kabul ettirilecek?
4. Mevcut bir yönetmelik değiştiriliyor mu (kazanılmış koşul riski)?

## Denetim şeması
1. **Hukuki nitelik**: İç yönetmelik, çalışana tebliğ edilip kabul gördüğünde veya sözleşmeye atıfla **çalışma koşulu** hâline gelir; bu durumda lehe hükümler kazanılmış hak doğurur, aleyhe değişiklik m.22'ye tabi olur.
2. **Disiplin yönetmeliği**: Ceza skalası, fiil-yaptırım eşleşmesi ve orantılılık içermeli; ölçütsüz/keyfî yaptırım eşit davranma borcuna (m.5) ve fesih denetimine takılır.
3. **Talimat hakkı sınırı**: Yönetmelik, emredici hükümlere (asgari ücret, çalışma süresi, izin, fazla mesai sınırı) aykırı olamaz; aykırı kayıt geçersizdir.
4. **Uzaktan çalışma (m.14)**: Yazılı yapılma, ekipman/gider, iletişim ve veri koruma kayıtları; İSG yükümlülüğü uzaktan çalışmada da sürer.
5. **Tebliğ ve ispat**: Politikanın çalışana ulaştığı imza/KEP/sistem kaydıyla ispatlanmalı; aksi halde fesihte dayanak olamaz.
6. **KVKK kesişimi**: İzleme/bilgi güvenliği politikaları KVKK aydınlatmasıyla uyumlu olmalı.
7. **Ara sonuç**: Tebliğ edilmemiş veya emredici hükme aykırı yönetmelik dava dayanağı olmaz.

## Çıktı modülleri
- Politika/yönetmelik taslağı (kapsam + yaptırım skalası + yürürlük).
- Tebliğ-kabul formu taslağı.
- Emredici hükme uygunluk ve değişiklik usulü notu.

## Plugin bağlamı

Bu beceri `ik-insan-kaynaklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
