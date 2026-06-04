---
name: ikamet-izinleri
description: "İkamet izni başvurusu, uzatma, tür değişikliği ya da ret/iptal işlemiyle karşılaşıldığında; hangi izin türünün şartlarının taşındığını ve başvuru usulünü saptamak gerektiğinde kullanılır."
---

# İkamet İzinleri ve Başvuru

## Görev
Yabancının durumuna en uygun ikamet izni türünü belirlemek, şartları madde bazında denetlemek, başvuru/uzatma dosyasını kurmak ve ret/iptal işlemine karşı strateji oluşturmak.

## Soğuk başlangıç (intake)
1. Hangi izin türü hedefleniyor (kısa dönem, aile, öğrenci, uzun dönem, insani)?
2. Geçerli pasaport süresi, sağlık sigortası ve adres/gelir durumu nedir?
3. İlk başvuru mı, uzatma mı, tür değişikliği mi; e-ikamet randevusu alındı mı?
4. Daha önce ret, iptal veya giriş yasağı var mı?

## Denetim şeması
1. **Genel şartlar**: YUKK m.30 — pasaport/belge geçerliliği, geçerli sağlık sigortası, kalış amacını destekleyen belge, yeterli ve düzenli maddi imkân.
2. **Tür şartları**:
   - Kısa dönem (m.31/1): turizm, iş, taşınmaz maliki olma vb. dayanak; süre kural olarak her seferinde en fazla 2 yıl (m.32).
   - Aile (m.34-35): destekleyicinin şartları (m.35 — asgari gelir, sigorta, yeterli konut), eş ve çocuk kapsamı.
   - Öğrenci (m.38-39): aktif öğrencilik, öğrenim süresi ile bağlı süre.
   - Uzun dönem (m.42-43): kesintisiz 8 yıl yasal ikamet, son 3 yıl sosyal yardım almama, yeterli gelir, sağlık sigortası, kamu düzeni/güvenliği engeli bulunmaması.
   - İnsani (m.46-47): Başkanlık takdiriyle, diğer izinlerin şartları aranmaksızın.
3. **Ret/iptal sebepleri**: m.33, m.50 — şartların kaybı, sahte belge, kamu düzeni-güvenliği-sağlığı, vize/ikamet ihlali. İşlem gerekçesi ve maddi dayanağı denetlenir.
4. **İspat yükü**: Şartların varlığını ispat başvurana (belge ile); ret gerekçesinin maddi-hukuki dayanağını idare ortaya koymak zorundadır.
**Ara sonuç**: Şartlar tamamsa başvuru/uzatma dosyası; ret varsa İYUK m.2 iptal davası ve m.27 yürütmenin durdurulması yolu.

## Çıktı modülleri
- İzin türü-şart eşleştirme kontrol listesi ve eksik belge dökümü.
- Başvuru/uzatma dilekçe ve ek belge taslağı.
- Ret işlemine karşı iptal davası iskeleti (gerekçe çürütme + YD talebi).

## Plugin bağlamı

Bu beceri `goc-yabancilar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
