---
name: idari-para-cezasi-ve-mufettis-denetimi
description: "İş müfettişi denetimi, çalışma ve sosyal güvenlik mevzuatı ihlali, idari para cezası tutanağı veya bu cezalara itiraz/dava gündeme geldiğinde kullanılır."
---

# İdari Para Cezası ve İş Müfettişi Denetimi

## Görev
İşvereni iş ve sosyal güvenlik mevzuatı idari para cezası riskine karşı hazırlamak; müfettiş denetimini yönetmek; kesilmiş idari para cezasına karşı başvuru/dava yolunu doğru kurmak.

## Soğuk başlangıç (intake)
1. Tespit konusu ne (kayıt dışı çalışma, fazla mesai sınırı, İSG eksiği, bildirim ihlali)?
2. Tutanak/ceza kararı tebliğ edildi mi, tebliğ tarihi nedir?
3. Tespit edilen ihlal maddi olarak doğru mu, savunma dayanağı var mı?
4. Ceza İş Kanunu kapsamında mı (4857 m.99 vd.) yoksa SGK kaynaklı mı (5510)?

## Denetim şeması
1. **Hukuki dayanak**: İş Kanunu cezaları m.99-108'de düzenli (her ihlal türü ayrı madde ve tutar; tutarlar her yıl yeniden değerlemeyle artar — **rakam vermeden yürürlük yılını doğrula**). SGK kaynaklı cezalar 5510'a tabidir.
2. **Tebliğ ve süre**: Ceza kararı tebliğden itibaren işleyen süre içinde başvuruya tabi. İş Kanunu idari para cezalarına karşı **idare mahkemesinde** dava açılır (4857 m.108 atfı ve idari yargı rejimi); SGK prim/idari para cezalarında ise süreç farklılaşır (itiraz komisyonu + iş mahkemesi/idare mahkemesi ayrımı) → **yol haritasını cezanın kaynağına göre belirle**.
3. **Erken ödeme indirimi**: Kabahatler Kanunu (5326) genel rejimi uyarınca peşin ödemede indirim imkânı kontrol edilir.
4. **Savunma stratejisi**: Tutanaktaki maddi tespitin gerçekliği, usul (yetki/şekil), zamanaşımı ve orantılılık denetlenir.
5. **Önleyici uyum**: Bordro, puantaj, İSG eğitimi, işe giriş/çıkış bildirimi ve özlük dosyası eksiklerinin denetim öncesi giderilmesi.
6. **Ara sonuç**: Maddi tespit doğru ve usul sağlamsa indirimden yararlanarak ödeme; sakatlık varsa süresinde iptal başvurusu.

## Çıktı modülleri
- Denetime hazırlık/özlük eksik kontrol listesi.
- İdari para cezasına itiraz/iptal başvuru taslağı (doğru yargı yolu notlu).
- Risk ve erken ödeme değerlendirme notu.

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
