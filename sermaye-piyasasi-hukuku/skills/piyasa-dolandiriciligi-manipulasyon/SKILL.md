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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
