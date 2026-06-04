---
name: spor-uyusmazlik-dilekce-basvuru
description: "Federasyon disiplin kuruluna savunma, uyuşmazlık çözüm kuruluna başvuru, tahkim kuruluna itiraz ya da CAS başvurusu için yapılandırılmış taslak üretmek gerektiğinde kullanın."
---

# Spor Uyuşmazlıklarında Dilekçe ve Başvuru Taslağı

## Görev
Spor uyuşmazlığında doğru mercie hitap eden, talimat/madde atıflı, vakıa-hukuki sebep-talep mimarisine sahip dilekçe veya başvuru taslağı üretmektir (savunma, itiraz, başvuru, CAS başvurusu).

## Soğuk başlangıç (intake)
1. Hangi mercie hitap edilecek (disiplin kurulu, uyuşmazlık çözüm kurulu, tahkim kurulu, CAS)?
2. Talep ne: ceza/kararın kaldırılması veya hafifletilmesi, alacak, tedbir?
3. Karar/sevk tebliğ tarihi ve başvuru süresi?
4. Dayanak vakıalar ve eldeki deliller neler?
5. Tahkim şartı ve dil (CAS için) durumu nedir?

## Denetim şeması
1. **Merci ve format**: Hedef mercie uygun başlık, taraf ve temsil bilgileri; CAS için dil ve usul kuralları (ilgili federasyonun atıf yaptığı CAS Kodu) kontrol edilir.
2. **Süre kontrolü**: Başvuru süresinin dolup dolmadığı en başta doğrulanır; süre kısa ve genelde hak düşürücüdür.
3. **Vakıa kısmı**: Olaylar kronolojik, tartışmasız ve ihtilaflı ayrımıyla; her vakıaya delil bağlanır (rapor, görüntü, sözleşme).
4. **Hukuki sebepler**: İlgili talimat maddesi, 7405/6222/5894 veya TBK/HMK hükümleri pinpoint atıfla; tipiklik yokluğu, usul ihlali, orantısızlık gibi argümanlar sıralanır.
5. **Talep sonucu**: Açık, infaz edilebilir talep (kararın kaldırılması/değiştirilmesi, tedbir, alacak tutarı); kademeli talep gerekiyorsa asıl-fer'i ayrımı yapılır.
6. **Yer tutucu disiplini**: Bilinmeyen veriler `[doldurulacak]` ile işaretlenir; uydurma tarih/numara yazılmaz. İçtihat `[doğrulanacak]` notuyla verilir.

## Çıktı modülleri
- Tam dilekçe/başvuru taslağı (başlık, vakıa, hukuki sebep, talep)
- Delil listesi ve dizini
- Süre ve merci doğrulama notu
- Doldurulacak alanların kontrol listesi

## Plugin bağlamı

Bu beceri `spor-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
