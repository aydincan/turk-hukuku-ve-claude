---
name: aydinlatma-acik-riza-denetimi
description: "Mevcut aydınlatma metinlerinin ve açık rıza beyanlarının m.10, Aydınlatma Tebliği ve Rıza Tebliği'ne uygunluğu denetlenirken ya da bu metinler taslaklanırken kullanılır."
---

# Aydınlatma ve Açık Rıza Metni Denetimi

## Görev
Kuruluşun aydınlatma metinlerini ve açık rıza beyanlarını madde madde denetlemek; zorunlu unsur, zamanlama ve ikisinin birbirinden ayrı tutulması kurallarına uygunluğu test edip eksikleri bulgu listesine bağlamak.

## Soğuk başlangıç (intake)
1. Hangi kanallarda aydınlatma yapılıyor (web formu, işe alım, sözleşme, çağrı merkezi, kamera tabelası)?
2. Her kanal için ayrı metin var mı, yoksa tek genel metin mi kullanılıyor?
3. Açık rıza alınıyor mu; alınıyorsa aydınlatmadan ayrı bir onay olarak mı?
4. Rızanın geri alınması için bir mekanizma var mı?

## Denetim şeması
1. **Zorunlu unsur testi (m.10/1)**: Her metinde (a) veri sorumlusu/temsilci kimliği, (b) işleme amaçları, (c) aktarılan alıcı grupları ve amacı, (ç) toplama yöntemi ve hukuki sebebi, (d) m.11 hakları bulunmalı. "vb.", "gerektiğinde" gibi muğlak ifadeler eksiklik sayılır (Aydınlatma Tebliği).
2. **Zamanlama**: Aydınlatma, verinin elde edildiği anda yapılmalı; sonradan yapılan aydınlatma ihlaldir.
3. **Ayrılık ilkesi**: Aydınlatma ile açık rıza tek metinde/tek onay kutusunda birleştirilemez; aydınlatma rıza şartına bağlanamaz. Birleşik kullanım kırmızı bulgudur.
4. **Açık rızanın geçerliliği (m.3/1-a)**: Rıza özgür irade + belirli konu + bilgilendirme unsurlarını taşımalı; ön işaretli kutu, hizmet şartına bağlı rıza ("rıza vermezsen hizmet yok") geçersizdir.
5. **Hukuki sebebin doğru gösterimi**: Metinde her amaç için m.5/m.6 sebebi açık rıza ile karıştırılmadan gösterilmeli.
6. **Ara sonuç**: Eksik/geç aydınlatma m.18/1-a yaptırım riski; geçersiz rıza ise işlemenin tümünü hukuka aykırı kılar.

İspat yükü: Aydınlatmanın usulüne uygun yapıldığını ve rızanın geçerli alındığını veri sorumlusu kayıt/onay loguyla ispatlar.

## Çıktı modülleri
- Metin başına m.10 unsur kontrol listesi (Uygun/Eksik).
- Aydınlatma–açık rıza ayrımı uygunsuzluk raporu.
- Kanal bazlı düzeltilmiş aydınlatma/rıza taslakları ([doldurulacak] yer tutucularıyla).

## Plugin bağlamı

Bu beceri `kvkk-uyum-checker` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
