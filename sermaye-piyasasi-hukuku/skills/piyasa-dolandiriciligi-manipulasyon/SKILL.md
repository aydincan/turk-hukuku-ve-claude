---
name: piyasa-dolandiriciligi-manipulasyon
description: "İşleme dayalı veya bilgiye dayalı manipülasyon, fiyat-miktarda yapay görüntü oluşturma, yanlış/yanıltıcı bilgi yayma iddiaları ve SPK m.107 sorumluluğu değerlendirileceğinde kullanılır."
---

# Piyasa Dolandırıcılığı (Manipülasyon)

## Görev
Piyasa dolandırıcılığı iddiasını SPK m.107'nin iki türü (işleme dayalı ve bilgiye dayalı) üzerinden çözümlemek; yapay fiyat/arz-talep görüntüsü veya yanıltıcı bilgi unsurlarını delillerle bağlayarak sorumluluk değerlendirmesi yapmak.

## Soğuk başlangıç (intake)
- İddia hangi türde: işlem/emir bazlı yapaylık mı, yoksa yanlış/yanıltıcı bilgi yayma mı?
- Hangi araçta, hangi dönemde; anormal fiyat/hacim hareketi var mı?
- İşlemleri yapan/koordine eden kim; bağlantılı hesaplar, eşleştirilmiş emirler söz konusu mu?
- Müvekkil şüpheli/sanık mı yoksa Kurul incelemesine yanıt mı hazırlıyor?

## Denetim şeması
1. **Tür ayrımı:** SPK m.107/1 işleme dayalı (alım-satım, emir, emir iptali yoluyla fiyat/arz-talep/değerde yapay görünüm); m.107/2 bilgiye dayalı (yalan, yanlış, yanıltıcı bilgi vererek, haber yayarak ya da yorumla fiyatı etkileme) olarak ayrıştırılır.
2. **İşleme dayalı unsurlar:** Fiyatı, değeri veya yatırımcı kararlarını etkilemek amacıyla yapay arz-talep/fiyat görüntüsü oluşturulması aranır; eşleştirilmiş emirler, wash trade, hesaplar arası bağlantı, emir-iptal örüntüleri incelenir.
3. **Bilgiye dayalı unsurlar:** Verilen bilginin yanlış/yanıltıcı niteliği, yayılma kanalı ve fiyat üzerindeki etkisi kurulur; gerçek bilgilendirme ile manipülatif yayma ayrılır. Ara sonuç: hangi tür ve seçimlik hareketin oluştuğu netleşir.
4. **Kast ve illiyet:** Yapaylık veya yanıltma kastı; işlem/emir kayıtları, hesap sahipliği, KAP-haber zamanlaması ve fiyat etkisi analiziyle bağlanır. İspat iddia makamında (CMK m.217).
5. **Yaptırım ve usul:** Ceza m.107; idari boyut m.103 vd.; menfaat iadesi m.104; soruşturma için Kurul mütalaası m.115; etkin pişmanlık m.109. İçtihat Yargıtay bankasından doğrulanır, künye `[doğrulanacak]`.

## Çıktı modülleri
- Tür ve unsur analizi (m.107/1 ve /2)
- İşlem/emir örüntüsü ve fiyat-hacim kronolojisi
- Savunma/iddia stratejisi ve menfaat iadesi/etkin pişmanlık notu
- Kurul mütalaası ve usul yol haritası

## Plugin bağlamı

Bu beceri `sermaye-piyasasi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
