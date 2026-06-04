---
name: vergi-kacakciligi-vuk-359
description: "Sahte/muhteviyatı itibarıyla yanıltıcı belge düzenleme veya kullanma, defter-belge gizleme, çift defter gibi VUK m.359 fiilleri; mütalaa/dava şartı, pişmanlık ve idari vergi cezasıyla paralel süreç söz konusu olduğunda kullanılır."
---

# Vergi Kaçakçılığı Suçları (VUK m.359)

## Görev
213 sayılı VUK m.359 kaçakçılık fiillerini unsurlarına göre denetlemek; mütalaa şartını (m.367), pişmanlığı (m.371) ve idari vergi ziyaı cezasıyla (m.344) ilişkiyi yönetmek.

## Soğuk başlangıç (intake)
- Hangi fiil iddia ediliyor? (sahte belge düzenleme mi kullanma mı; defter gizleme; çift defter)
- Vergi incelemesi/VDK raporu ve vergi suçu raporu düzenlendi mi?
- Mütalaa (VUK m.367) verildi mi, iddianame buna dayanıyor mu?
- Mükellefin pişmanlık (m.371) veya uzlaşma kullanma imkânı var mı?

## Denetim şeması
1. **Fiilin tespiti (VUK m.359)**: (a) bendi — defter/kayıtta hile, sahte fatura kullanma/düzenleme dışı yanıltıcı fiiller, defter-belge gizleme, muhteviyatı itibarıyla yanıltıcı belge; (b) bendi — sahte belge düzenleme/kullanma; (c) bendi — Maliye ile anlaşması olmayan matbaada belge basma. Fiilin hangi benoe girdiğini netleştir; cezalar farklıdır.
2. **Sahtelik vs. yanıltıcılık**: Sahte belge (gerçek bir muamele olmadan düzenlenen) ile muhteviyatı itibarıyla yanıltıcı belge (gerçek muamele var, tutar/nitelik yanlış) ayrımı esastır; nitelendirme cezayı belirler.
3. **Manevi unsur**: Kast aranır; "bilerek" kullanma. İyiniyetli/bilmeden kullanım savunması belge zinciri ve karşıt inceleme ile değerlendirilir.
4. **Mütalaa/dava şartı (m.367)**: Cumhuriyet savcılığı, ilgili vergi dairesi başkanlığı/defterdarlık mütalaası olmadan dava açamaz/sonuçlandıramaz. Her dosyada ilk kontrol.
5. **Pişmanlık ve etkin düzenleme (m.371)**: Şartları varsa cezayı kaldırır/azaltır; m.359 son fıkrasındaki indirim/ödeme şartlarını da gözden geçir.
6. **Paralel süreç**: Vergi mahkemesindeki tarhiyat/ceza davası ile ceza yargısı ayrı yürür; idari yargıdaki tespitlerin ceza dosyasına etkisini ve non bis in idem tartışmasını not et. Dava zamanaşımı TCK m.66'ya göre, üst sınır esas alınarak hesaplanır.
7. **Ara sonuç**: Fiil-bent eşleşmesi, sahtelik nitelendirmesi, kast, mütalaa şartı ve pişmanlık imkânı tablolaşır.

## Çıktı modülleri
- Fiil-bent nitelendirme notu
- Sahte/yanıltıcı belge ayrım analizi
- Mütalaa şartı kontrol çıktısı
- Pişmanlık/ödeme senaryosu
- İdari-cezai paralel süreç haritası

## Plugin bağlamı

Bu beceri `ekonomik-ceza` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
