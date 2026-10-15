---
name: muvekkil-ve-kurul-iletisimi
description: "Kurul incelemesine/savunma istemine yanıt, müvekkile risk ve seçeneklerin sade anlatımı, KAP açıklama dili ve karşı tarafla yazışma tonunun kurulması gerektiğinde kullanılır."
---

# Müvekkil ve Kurul ile İletişim

## Görev
Sermaye piyasası dosyasında üç yönlü iletişimi yönetmek: Kurul'a savunma/yanıt, müvekkile sade bilgilendirme ve karşı taraf/yatırımcıyla yazışma; her birinde doğru ton ve içerik dengesini kurmak.

## Soğuk başlangıç (intake)
- İletişim muhatabı kim: Kurul, müvekkil (yönetici/şirket), yatırımcı, karşı taraf mı?
- Aşama nedir: inceleme/savunma istemi, açıklama yapma, müzakere, dava mı?
- Açıklanması gereken/gereksiz bilgi sınırı nerede; gizlilik ve özel durum yükümlülüğü etkili mi?
- Acil bir süre veya KAP açıklama zorunluluğu var mı?

## Denetim şeması
1. **Kurul savunması:** Savunma isteminde isnat edilen ihlal, dayanak madde/tebliğ ve istenen bilgi netleştirilir; yanıt, vakıaları doğru ama lehe çerçeveleyerek, belge ekleriyle ve süresinde verilir. Ara sonuç: savunma iskeleti ve ek listesi.
2. **Müvekkile bilgilendirme:** Riskler (idari para cezası, cezai sorumluluk, itibar) ve seçenekler sade dille, abartısız ve karar verdirici biçimde anlatılır; tavsiye ile karar arasındaki sınır korunur.
3. **KAP/kamuya açıklama dili:** Özel durum açıklamaları tam, doğru, anlaşılır ve yanıltıcı olmayacak şekilde kurulur (SPK m.15); fazla/eksik açıklamanın sorumluluk etkisi (m.32) gözetilir.
4. **Karşı taraf/yatırımcı yazışması:** Talep/uzlaşma yazışmalarında tanıma anlamına gelebilecek ifadelerden kaçınılır; sulh-tahkim-dava seçenekleri açık tutulur.
5. **Gizlilik ve etik:** İçsel bilgi, müvekkil sırrı ve meslek kuralları (1136 sayılı Kanun) gözetilir; iletişimin yazılı iz bırakması ve tutarlılığı sağlanır.

## Çıktı modülleri
- Kurul savunma yazısı iskeleti ve ek listesi
- Müvekkil bilgilendirme notu (sade dil, risk-seçenek)
- KAP açıklama taslağı
- Karşı taraf/uzlaşma yazışma çerçevesi

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
