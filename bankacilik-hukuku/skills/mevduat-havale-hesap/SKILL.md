---
name: mevduat-havale-hesap
description: "Mevduat/katılım hesabı, hesaptan yetkisiz çekim, havale-EFT hatası, dolandırıcılıkla yapılan transfer veya bankanın özen yükümlülüğü ihlali iddialarını değerlendirmek ve bankanın sorumluluğunu denetlemek gerektiğinde kullanılır."
---

# Mevduat, Hesap ve Havale/EFT Uyuşmazlıkları

## Görev
Mevduat/hesap ilişkisinden doğan uyuşmazlıklarda (yetkisiz çekim, hatalı/dolandırıcılıkla yapılan havale-EFT, hesap bloke, faiz işletme) bankanın özen ve iade yükümlülüğünü, müşterinin kusurunu ve sorumluluğun dağılımını belirlemek.

## Soğuk başlangıç (intake)
- Hesap türü: vadesiz/vadeli mevduat, katılım fonu, ticari hesap?
- Olay: yetkisiz para çekme, sahte talimatla havale, EFT'nin yanlış hesaba gitmesi, internet/mobil bankacılık dolandırıcılığı mı?
- Müşterinin bilgi/şifre paylaşımı, ihmal veya talimatı var mı; banka bildirim/doğrulama yapmış mı?
- Zarar tutarı ve bankaya bildirim tarihi nedir?

## Denetim şeması
1. **İlişkinin niteliği**: Mevduat, banka açısından usulsüz tevdi/karz benzeri ilişkidir; banka parayı iade ve hesabı doğru tutma borcu altındadır. Banka, basiretli bir tacir gibi yüksek özen yükümlülüğü taşır (TTK m.18/2; TBK m.506/2 benzeri özen ölçütü).
2. **Yetkisiz işlem ve ispat**: Hesaptan çıkan parada bankanın geçerli bir talimata dayandığını ve kimlik/doğrulama kontrolünü yaptığını ispatı gerekir. Sahtecilik/yetkisiz işlemde kural, bankanın kusursuz sorumluluğa yakın ağır özen sorumluluğudur; Yargıtay yerleşik içtihadı bankanın objektif özen ölçüsüyle sorumlu tutulduğu yönündedir [doğrulanacak — karararama.yargitay.gov.tr, 11. HD].
3. **Müşterinin kusuru ve birlikte kusur**: Müşterinin şifre/OTP paylaşımı, oltalama bağlantısına bilgi girmesi gibi ağır kusuru varsa TBK m.52 uyarınca tazminattan indirim veya sorumluluğun kalkması gündeme gelir. Banka ile müşteri kusuru oranlanır.
4. **Havale/EFT (TBK m.555-560)**: Havalede bankanın talimata uygunluğu, yanlış hesaba transferde sebepsiz zenginleşen lehtara karşı iade (TBK m.77 vd.) ve bankanın aracı sorumluluğu değerlendirilir.
5. **Süre ve usul**: Sözleşmeden doğan iade talebinde zamanaşımı kural olarak TBK m.146 (10 yıl); haksız fiil unsuru varsa TBK m.72 süreleri. Ara sonuç olarak bankanın/müşterinin sorumluluk payını ve talep edilebilir tutarı yaz.

## Çıktı modülleri
- Sorumluluk ve birlikte kusur analizi.
- İspat yükü dağılımı tablosu (bankadan istenecek kayıtlar).
- Talep/dava ya da bankaya başvuru taslağı iskeleti.

## Plugin bağlamı

Bu beceri `bankacilik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
