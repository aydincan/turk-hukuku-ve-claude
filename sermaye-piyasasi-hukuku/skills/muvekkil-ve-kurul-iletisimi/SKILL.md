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
