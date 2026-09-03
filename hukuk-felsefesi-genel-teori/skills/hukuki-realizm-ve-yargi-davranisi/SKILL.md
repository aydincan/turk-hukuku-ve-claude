---
name: hukuki-realizm-ve-yargi-davranisi
description: "Lafzen açık kuralın uygulamada nasıl farklı sonuç verdiği, içtihat istikrarsızlığı veya yargıcın takdirini etkileyen kurum-dışı etkenler tartışıldığında; Amerikan/İskandinav realizmi ve menfaatler içtihadı çerçevesinde kullanın."
---

# Hukuki Realizm ve Yargısal Karar Davranışı

## Görev
"Kitaptaki hukuk" ile "uygulamadaki hukuk" arasındaki farkı çözümlemek; içtihadın neden
sapabildiğini, yargıcın takdir alanını ve karar gerekçesinin gerçek belirleyicilerini realist
araçlarla incelemek. Amaç gerekçeyi küçümsemek değil, öngörülebilirliği artırmaktır.

## Soğuk başlangıç (intake)
- Lafzen açık görünen kural pratikte neden farklı uygulanıyor — somut bir karar serisi var mı?
- Daireler/mahkemeler arasında içtihat çelişkisi mi gözleniyor?
- Soru "norm ne der" mi, yoksa "mahkeme fiilen ne yapar/yapacak" mı (tahmin sorusu)?
- Takdir yetkisinin (TMK m.4) devrede olduğu bir alanda mıyız?

## Denetim şeması
1. **Realist ayrımı kur.** Kâğıt üstündeki kural (rule in books) ile fiilî karar pratiği
   (rule in action) ayrımını yap; realizm, kuralın değil yargıcın davranışının sonucu
   belirlediğini ileri sürer. Bunu mutlak değil, tahmin gücü artıran bir merceğe çevir.
2. **Takdir alanını haritalandır.** TMK m.4 (hâkimin hukuka ve hakkaniyete göre takdiri),
   TBK m.51 (tazminatın belirlenmesi), m.52 (indirim) gibi takdir tanıyan normlarda sonucun
   öngörülemezliği yapısaldır; burada realist analiz en güçlüdür.
3. **Menfaat dengesini oku.** Menfaatler içtihadı (Heck) ışığında, kararın hangi çatışan
   menfaati hangi gerekçeyle üstün tuttuğunu çıkar; yargıcın "gerçek gerekçesi" çoğu zaman
   menfaat tartımıdır. Bunu lafzî gerekçeyle karşılaştır.
4. **İstikrar/sapma analizi.** İçtihat çelişkisi varsa, içtihadı birleştirme kararı (HMK m.;
   Yargıtay Kanunu ilgili hükümleri) yolunu ve birleştirme kararının bağlayıcılığını işaretle;
   somut karar serisini künyeleriyle ele al, doğrulanmadıkça [doğrulanacak]. Ara sonuç:
   öngörülebilirlik tahmini.
5. **Strateji çıktısı.** Realist analiz, müvekkile "kazanma olasılığı" sunarken normatif
   argümanın yerine değil yanına konur; etik sınır (uydurma değil, gözlemlenen eğilim) korunur.

## Çıktı modülleri
- Kâğıt-pratik fark notu.
- Takdir alanı haritası (madde atıflarıyla).
- Menfaat tartımı çözümlemesi.
- Öngörülebilirlik/strateji değerlendirmesi (içtihat künyeleri [doğrulanacak]).

## Plugin bağlamı

Bu beceri `hukuk-felsefesi-genel-teori` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
