---
name: calisma-izni
description: "Yabancının çalışma izni başvurusu, uzatması, ret/iptali veya izinsiz çalışma yaptırımı söz konusu olduğunda; 6735 sayılı Kanun kapsamında izin türü ve usulünü saptamak için kullanılır."
---

# Çalışma İzni ve Uluslararası İşgücü

## Görev
Yabancının çalışma iznini 6735 sayılı Uluslararası İşgücü Kanunu çerçevesinde yapılandırmak, doğru izin türünü ve başvuru kanalını belirlemek, ret/iptal ve izinsiz çalışma yaptırımlarına karşı strateji geliştirmek.

## Soğuk başlangıç (intake)
1. İşveren üzerinden mi (bağımlı), bağımsız mı yoksa Turkuaz Kart yoluyla mı çalışma planlanıyor?
2. Yabancının mevcut ikamet izni ve Türkiye'de bulunma süresi nedir?
3. İşveren şirketin durumu (sermaye, mevcut Türk personel sayısı) nedir?
4. Ret, iptal veya idari para cezası tebliğ edildi mi, tarihi?

## Denetim şeması
1. **İzin türleri**: 6735 m.10 — süreli çalışma izni (kural olarak ilk başvuruda belirli işveren/işyeri ve süre bağlı), süresiz çalışma izni, bağımsız çalışma izni; Turkuaz Kart (m.11 — nitelikli işgücü/yatırım için süresiz hak veren belge).
2. **Çalışma izni-ikamet ilişkisi**: m.13 — geçerli çalışma izni ve Turkuaz Kart ikamet izni yerine geçer; ayrıca ikamet izni aranmaz.
3. **Başvuru usulü**: Yurt içinden geçerli ikamet izni varsa doğrudan, yurt dışından ise temsilcilik üzerinden; başvuru Çalışma ve Sosyal Güvenlik Bakanlığına yapılır, değerlendirme kriterleri (uluslararası işgücü politikası, istihdam etkisi) uygulanır.
4. **Ret/iptal**: m.15-16 — politika kriterlerine uymama, sahte/eksik belge, fiilen çalışmama, iznin amacı dışında kullanımı. İşlem idari nitelikte olup İYUK yolu açıktır.
5. **İzinsiz çalışma yaptırımı**: m.23 — izinsiz çalışan yabancıya ve çalıştıran işverene idari para cezası; tekrarda artış; yabancı için sınır dışı riski (YUKK m.54 ile bağlantı).
**İspat yükü**: İzin şartlarını ve fiilî çalışmayı başvuran/işveren ispatlar; idari para cezasının maddi dayanağını (tespit tutanağı) idare ortaya koyar.

## Çıktı modülleri
- İzin türü seçim matrisi ve başvuru belge listesi.
- Ret kararına karşı iptal davası dilekçe iskeleti.
- İdari para cezasına karşı itiraz/dava ve yaptırım-risk notu.

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
