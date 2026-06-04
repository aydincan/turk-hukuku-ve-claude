---
name: norm-cesitleri-ve-uygulama-alani
description: "Bir kuralın emredici mi yedek mi olduğu, kural-istisna ilişkisi, normun zaman (geçmişe etki) ve yer bakımından uygulanması veya çatışan iki normun hangisinin önce geleceği belirlenmek istendiğinde kullanın."
---

# Norm Çeşitleri ve Normun Uygulama Alanı

## Görev
Normları niteliklerine göre sınıflamak (emredici/yedek, genel/özel, kural/istisna) ve normun
zaman, yer ve kişi bakımından uygulama alanını ile norm çatışmalarının çözüm ilkelerini
belirlemek. Bu, "hangi kural, bu olaya, ne zamandan itibaren uygulanır" sorusunun cevabıdır.

## Soğuk başlangıç (intake)
- Kural emredici mi (aksi kararlaştırılamaz) yoksa yedek/tamamlayıcı mı (aksi serbestçe
  kararlaştırılabilir)?
- Olay, yeni bir kanunun yürürlüğünden önce mi gerçekleşti (zaman bakımından uygulama)?
- İki norm çatışıyor mu? Biri özel/sonraki/üst mü?
- Yabancılık unsuru var mı (yer bakımından/MÖHUK devrede mi)?

## Denetim şeması
1. **Niteliği belirle.** Emredici hüküm (kamu düzeni/zayıf koruması; aksi sözleşme TBK m.27
   uyarınca hükümsüz) ile yedek hüküm (tarafların aksini kararlaştırabildiği) ayrımını yap.
   Sözleşme serbestisi (TBK m.26) sınırı buradadır.
2. **Kural-istisna mantığını kur.** İstisna hükmü dar yorumlanır; istisnayı ileri süren
   ispatla yükümlüdür. Genel-özel ilişkisinde özel norm önceliklidir (lex specialis).
3. **Zaman bakımından uygula.** Kanunların geriye yürümezliği esastır; kazanılmış haklar ve
   hukuki güvenlik korunur. Usul kurallarında derhal uygulama, maddi kurallarda yürürlük anı
   esastır. Yürürlük ve uygulama için ilgili yürürlük kanunu/geçiş hükümlerine bak (ör. TMK
   ve TBK'nın yürürlük ve uygulama şekli hakkındaki kanunları).
4. **Çatışmayı çöz.** Lex superior (üst norm; Anayasa m.11), lex specialis (özel norm) ve
   lex posterior (sonraki norm) ilkelerini sırayla uygula; üstünlük ilkesi diğerlerini bastırır.
   Ara sonuç: uygulanacak tek norm.
5. **Yer/kişi bakımından.** Yabancılık unsuru varsa uygulanacak hukuk MÖHUK (5718) bağlama
   kurallarıyla belirlenir; ceza için TCK m.8 vd. mülkilik/şahsilik ilkeleri devreye girer.
   İlkesel atıf yeterli, somut karar künyesi gerekiyorsa [doğrulanacak].

## Çıktı modülleri
- Norm nitelik etiketi (emredici/yedek; genel/özel).
- Zaman bakımından uygulama notu (geçiş hükmü atfıyla).
- Çatışma çözüm zinciri (üst/özel/sonraki).
- Yer-kişi bakımından uygulanacak hukuk tespiti.

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
