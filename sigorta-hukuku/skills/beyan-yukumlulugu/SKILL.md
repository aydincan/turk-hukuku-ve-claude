---
name: beyan-yukumlulugu
description: "Sigortacının eksik veya yanlış beyan nedeniyle sözleşmeden cayması, tazminatı reddetmesi veya prim farkı talep etmesi söz konusu olduğunda; sigortalının bildirim yükümlülüğünün ihlal edilip edilmediğini ve sonucunu denetlemek için kullanılır."
---

# Sözleşme Öncesi Beyan (İhbar) Yükümlülüğü

## Görev
Sigorta ettirenin sözleşme kurulurken rizikoyu etkileyecek hususları doğru ve eksiksiz beyan edip etmediğini, ihlal varsa bunun kasıt/kusur ayrımıyla doğuracağı sonucu (cayma, prim farkı, tazminattan indirim) tespit etmek.

## Soğuk başlangıç (intake)
1. Beyan, sigortacının yazılı sorularına mı dayanıyor, yoksa serbest beyan mı?
2. Hangi husus eksik/yanlış beyan edildi; bu husus rizikoyu ne ölçüde etkiliyor?
3. Sigorta ettiren bunu bilerek mi (kasıt) yoksa kusurla mı yaptı?
4. Sigortacı durumu ne zaman öğrendi; cayma süresine uyuldu mu?

## Denetim şeması
1. **Yükümlülüğün kapsamı.** TTK m.1435: sigorta ettiren bildiği veya bilmesi gereken, rizikonun değerlendirilmesi için önemli hususları bildirmek zorundadır. Sigortacının yazılı sorduğu hususlar önemli sayılır (m.1435/2).
2. **İhlalin tespiti.** Beyan ile gerçek durum arasında, sigortacının sözleşmeyi yapmamasına ya da farklı şartla yapmasına yol açacak bir fark var mı? Ara sonuç: önemli husus eksik/yanlış mı?
3. **Yaptırım — kasıt halinde.** TTK m.1439/1: sigortacı sözleşmeden cayabilir; riziko gerçekleşmişse tazminatı ödemez, primler sigortacıya kalır.
4. **Yaptırım — kusur/kusursuzluk halinde.** TTK m.1439/2: caymanın riziko gerçekleşmesine etkisi varsa tazminat, ödenen prim ile ödenmesi gereken prim oranında indirilir (orantılı indirim). İhlalin riziko ile illiyeti yoksa tam ödeme.
5. **Süre ve usul.** TTK m.1440: sigortacı, ihlali öğrendiği tarihten itibaren on beş gün içinde cayma hakkını kullanmalı; süre geçerse hak düşer. İspat yükü: ihlali ve önemliliği sigortacı, illiyetsizliği/iyiniyeti sigorta ettiren ileri sürer.

## Çıktı modülleri
- Beyan ihlali tespit tablosu (husus / soruldu mu / önemli mi / kasıt-kusur).
- Yaptırım sonucu (cayma / orantılı indirim / etkisiz).
- Cayma süresi ve usul kontrolü.
- Sigortalı veya sigortacı için savunma/itiraz argümanı.

## Plugin bağlamı

Bu beceri `sigorta-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
