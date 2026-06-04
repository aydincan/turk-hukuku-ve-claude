---
name: lisans-devir-ve-zorunlu-lisans
description: "Patent hakkının lisanslanması, devri, rehni ya da zorunlu lisans talebi gündeme geldiğinde kullanılır; sözleşmesel hak transferi ve kullanmama/kamu yararı senaryoları için temel beceridir."
---

# Lisans, Devir ve Zorunlu Lisans

## Görev
Patent/faydalı model üzerindeki hukuki işlemleri (devir, lisans, rehin) SMK m.148 çerçevesinde kurmak; zorunlu lisans koşullarını (SMK m.129-137) değerlendirmek; sicile şerh ve geçerlilik şartlarını netleştirmek.

## Soğuk başlangıç (intake)
1. İşlem türü ne: devir, inhisari/inhisari olmayan lisans, rehin, haciz?
2. Lisansın kapsamı (alan, süre, bölge, alt lisans) nasıl belirlenecek?
3. Hak ayakta mı; sicilde takyidat/önceki lisans var mı?
4. Zorunlu lisans gündemdeyse hangi sebep: kullanmama, bağımlılık, kamu yararı, ihracat?

## Denetim şeması
1. **Hukuki işlem ve şekil (SMK m.148).** Patent başvurusu/patent devredilebilir, lisans verilebilir, rehnedilebilir. Devir yazılı ve geçerlilik için noter onayı gerektirir; sicile kayıt iyiniyetli üçüncü kişilere karşı ileri sürülebilirlik için önemlidir. Ara sonuç: işlem geçerli ve sicile işlenebilir mi?
2. **Lisans türü.** İnhisari lisansta hak sahibi başkasına lisans veremez ve aksi kararlaştırılmadıkça kendisi de kullanamaz; inhisari olmayan lisansta birden çok lisans mümkündür. Lisans sözleşmesinde alan/süre/bölge/alt lisans/asgari kullanım kayıtlarını belirle.
3. **Lisans alanın dava hakkı.** İnhisari lisans alan, aksi sözleşmede yoksa tecavüz davalarını kendi adına açabilir; inhisari olmayan lisans alan kural olarak hak sahibine bildirimle harekete geçirir.
4. **Zorunlu lisans (SMK m.129-137).** Sebepler: patentin kullanılmaması (m.130), bağımlılık (m.131), kamu yararı (m.132), ıslahçı/bitki çeşidi bağımlılığı, ihracat amaçlı ilaç. Koşullar, başvuru yolu (mahkeme) ve bedel tespiti m.133 vd.
5. **Kullanım yükümlülüğü.** Patent sahibi patenti kullanmakla yükümlüdür; kullanmama, zorunlu lisans için dayanak oluşturabilir (m.130).

## Çıktı modülleri
- İşlem türü ve geçerlilik/şekil kontrol listesi.
- Lisans sözleşmesi ana kayıtları (kapsam/süre/dava hakkı) iskeleti.
- Sicile şerh ve takyidat uyarısı.
- Zorunlu lisans uygunluk değerlendirmesi.

## Plugin bağlamı

Bu beceri `patent-faydali-model` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
