---
name: olume-bagli-tasarruflar-vasiyet-miras-sozlesmesi
description: "Vasiyetname veya miras sözleşmesi düzenlenmesi, yorumu, şekil ve ehliyet denetimi gerektiğinde; resmi/el yazılı/sözlü vasiyet, mirasçı atama, belirli mal bırakma (muayyen mal vasiyeti) ve koşul-yükleme konularında kullanılır."
---

# Ölüme Bağlı Tasarruflar — Vasiyetname ve Miras Sözleşmesi

## Görev
Bir ölüme bağlı tasarrufun türünü, şeklini, ehliyet ve içerik geçerliliğini denetlemek; mirasçı atama, muayyen mal vasiyeti, art/yedek mirasçı, koşul ve yükleme kurmak ya da yorumlamak.

## Soğuk başlangıç (intake)
- Tasarruf vasiyetname mi, miras sözleşmesi mi? Tarihi ve düzenleniş şekli?
- Resmi (noter/sulh hâkimi), el yazılı mı, sözlü mü düzenlendi?
- Tasarruf anında mirasbırakanın yaşı ve ayırt etme gücü?
- İçerik: mirasçı atama mı, belirli mal bırakma mı, koşul/yükleme var mı?
- Sonradan değiştirildi/geri alındı mı? Sonraki tasarruf var mı?

## Denetim şeması
1. **Tür ve şekil:** Vasiyetname tek taraflı, her zaman dönülebilir (m.542 geri alma). Şekiller: resmi (m.532-537), el yazılı — baştan sona el yazısı, tarih, imza (m.538), sözlü — olağanüstü hal, iki tanık (m.539-541). Miras sözleşmesi iki taraflı, daima resmi şekilde (m.545); olumlu/olumsuz (feragat) olabilir.
2. **Ehliyet:** Vasiyet için ayırt etme gücü + 15 yaş (m.502); miras sözleşmesi için ayırt etme gücü + ergin + kısıtlı olmama (m.503).
3. **İrade sakatlığı:** Yanılma, aldatma, korkutma, zorlama varsa iptal sebebi (m.557/3, m.504). Hatalı saik açık ve belirleyiciyse dikkate alınır (m.504/2).
4. **İçerik denetimi:** Mirasçı atama (m.516), muayyen mal vasiyeti (m.517), art mirasçı (m.521-523), yedek mirasçı (m.520), koşul ve yükleme (m.515), vakıf kurma (m.526). Hukuka/ahlaka aykırı, imkânsız koşul yazılmamış sayılır (m.515/2).
5. **Yorum:** Mirasbırakanın gerçek iradesi esas (m.504, lehe yorum); muayyen mal vasiyeti mi mirasçı atama mı ayrımı pay sonuçlarını değiştirir.
6. **Ara sonuç:** Geçerlilik haritası; iptal sebebi varsa iptal davası becerisine, saklı pay aşımı varsa tenkis becerisine yönlendir.

## Çıktı modülleri
- Vasiyetname/miras sözleşmesi taslağı (şekil şartlı, [doldurulacak] yer tutuculu)
- Geçerlilik/şekil denetim çizelgesi
- Yorum notu ve tür tayini (atama vs. muayyen mal)
- Geri alma/değiştirme metni taslağı

## Plugin bağlamı

Bu beceri `miras-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
