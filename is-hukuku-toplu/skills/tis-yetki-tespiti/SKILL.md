---
name: tis-yetki-tespiti
description: "Sendikanin TIS yapma yetkisini, isyeri/isletme/iskolu barajlarini, yetki tespiti basvurusunu ve yetki belgesini ele alir; sendikanin coklugu, baraj ve yetki belgesi sorunlarinda kullanilir."
---

# Toplu İş Sözleşmesi Yetkisi ve Yetki Tespiti

## Görev
Bir sendikanın TİS yapma yetkisini barajlar üzerinden değerlendirmek, yetki tespiti sürecini yürütmek ve yetki belgesine giden yolu kurmak. Toplu pazarlığın kapısıdır.

## Soğuk başlangıç (intake)
- Hangi işkolu, hangi işyeri/işletme düzeyi?
- İşyerinde/işletmede toplam işçi sayısı ve sendika üye sayısı nedir?
- Sendikanın işkolu barajını (%1) tutan güncel istatistiği var mı?
- Daha önce yetki tespiti veya itiraz oldu mu?

## Denetim şeması
1. **İşkolu barajı:** 6356 m.41/1 — sendikanın kurulu bulunduğu işkolundaki işçilerin en az **%1**inin üyesi olması (geçici m.6 ile geçmişte farklı oranlar uygulanmıştı; güncel %1). Baraj, Bakanlığın Ocak/Temmuz işkolu istatistik tebliğleriyle saptanır.
2. **İşyeri/işletme çoğunluğu:** 6356 m.41/1 — işyeri TİS için o işyerindeki işçilerin **yarıdan fazlasının (%50+1)**; işletme TİS için işletme kapsamındaki işçilerin **%40**ının üyesi olmak.
3. **Yetki tespiti başvurusu:** 6356 m.42 — sendika Çalışma ve Sosyal Güvenlik Bakanlığına başvurur; Bakanlık tespiti tarafların kayıtlarına göre yapar ve ilgililere bildirir.
4. **Yetki itirazı:** 6356 m.43 — taraflar veya işveren, tespite karşı kararın tebliğinden itibaren **6 işgünü** içinde görevli mahkemeye (İş Mahkemesi) itiraz edebilir; itiraz, kayıt yetersizliği veya başka sendikanın çoğunluğu gibi nedenlere dayanır.
5. **Yetki belgesi:** 6356 m.44 — itiraz süresi geçtikten veya itiraz reddedildikten sonra Bakanlık yetki belgesi verir. Belge alınmadan TİS bağıtlanamaz.
6. **Ara sonuç:** Barajlar tutuyorsa yetki tespiti talep edilir; tartışmalıysa kayıt düzeltme / itiraz stratejisi kurulur.

İspat: üyelik kayıtları (e-Devlet, sendika defterleri), Bakanlık istatistikleri ve işyeri işçi sayısı belirleyicidir.

## Çıktı modülleri
- Baraj hesap tablosu (işkolu %1, işyeri %50+1 / işletme %40).
- Yetki tespiti başvuru veya yetki itirazı dilekçesi iskeleti.
- Süre/usul takvimi (6 işgünü itiraz, tebligat tarihleri).

## Plugin bağlamı

Bu beceri `is-hukuku-toplu` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
