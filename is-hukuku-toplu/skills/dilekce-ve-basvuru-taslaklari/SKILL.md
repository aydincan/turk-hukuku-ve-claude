---
name: dilekce-ve-basvuru-taslaklari
description: "Yetki tespiti/itirazi, toplu gorusme cagri yazisi, uyusmazlik tutanagi, grev karari, YHK basvurusu ve sendikal tazminat davasi gibi toplu is hukuku belgelerinin taslaklarini uretir; bir belge kaleme almak gerektiginde kullanilir."
---

# Dilekçe, Tutanak ve Başvuru Taslakları

## Görev
Toplu iş hukukunun tipik belgelerini doğru madde dayanağı ve usul mimarisiyle taslaklamak. Boş bırakılması gereken her yer `[doldurulacak]` ile işaretlenir; uydurma bilgi konmaz.

## Soğuk başlangıç (intake)
- Hangi belge isteniyor (çağrı, itiraz dilekçesi, grev kararı, dava dilekçesi, YHK başvurusu)?
- Taraflar, işkolu, düzey ve tarihler nedir?
- Mahkeme/Bakanlık/YHK gibi muhatap kim?
- Dayanılacak temel vakıalar ve talep nedir?

## Denetim şeması
1. **Belge türünü ve dayanağını eşle:** Yetki itirazı → 6356 m.43 + HMK genel dilekçe unsurları (HMK m.119). TİS yorum/sendikal tazminat davası → HMK m.119 dava dilekçesi (taraflar, vakıa, hukuki sebep, deliller, talep sonucu). Çağrı/tutanak → 6356 m.46-47.
2. **Görevli/yetkili mercii doğrula:** Dava ve yetki itirazı İş Mahkemesi (7036 m.5); yetki tespiti başvurusu Bakanlık; menfaat uyuşmazlığında arabuluculuk (m.50) ve YHK (m.51).
3. **İskelet kur:** Başlık ve muhatap; taraf/vekil bilgileri `[doldurulacak]`; konu; açıklamalar (vakıa kronolojisi + madde altlaması); hukuki sebepler (6356 ilgili maddeleri, HMK); deliller; talep sonucu; tarih-imza.
4. **Süre uyarısı ekle:** İlgili hak düşürücü süre (örn. 6 işgünü itiraz) belge başında not düşülür.
5. **Doğrulama:** Madde numaraları ve tarihler kontrol edilir; içtihat anılacaksa künye `[doğrulanacak]` ve kaynak (karararama.yargitay.gov.tr) belirtilir.

Ara sonuç: Eksiksiz bir taslak + doldurulacak alan listesi + süre uyarısı.

## Çıktı modülleri
- İstenen belgenin tam taslağı (`[doldurulacak]` yer tutucularıyla).
- Dayanak madde ve görevli mercii notu.
- Doldurulacak alan ve ek/delil kontrol listesi.

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
