---
name: aydinlatilmis-onam
description: "Bir tıbbi müdahalede rızanın geçerli olup olmadığını ve aydınlatmanın yeterliğini denetlemek için kullanılır; onam kusurunun başlı başına sorumluluk doğurup doğurmadığını değerlendirir."
---

# Aydınlatılmış Onam Denetimi

## Görev
Tıbbi müdahaleye verilen rızanın hukuken geçerli, aydınlatmanın ise içerik ve usul olarak yeterli olup olmadığını saptamak ve onam kusurunun sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
1. Müdahale öncesi yazılı/sözlü aydınlatma yapıldığını gösteren belge var mı?
2. Hastaya hangi riskler, alternatifler ve başarısızlık olasılığı anlatıldı?
3. Hasta reşit/ehliyetli miydi; acil durum/bilinç kaybı var mıydı?
4. Onam formu matbu mu, müdahaleye özgü mü, makul süre öncesinde mi alındı?

## Denetim şeması
1. **Rızanın hukuki temeli**: TCK m.26 (ilgilinin rızası — hukuka uygunluk sebebi), Hasta Hakları Yönetmeliği m.24-31, Biyotıp Sözleşmesi (5013) m.5, 1219 m.70. Rıza yoksa müdahale kural olarak hukuka aykırıdır.
2. **Aydınlatmanın kapsamı**: Tanı, önerilen tedavi, başarı/başarısızlık olasılığı, riskler ve ciddi komplikasyonlar, alternatif yöntemler, hiç tedavi edilmeme sonucu. Estetik gibi zorunlu olmayan müdahalelerde aydınlatma yükü ağırlaşır.
3. **Usul ve zamanlama**: Hastanın karar vermesine yetecek makul süre, anlayabileceği dil, baskısız ortam. Ameliyat masasında alınan onam zayıftır.
4. **Ehliyet ve temsil**: Küçük/kısıtlı için veli/vasi onamı; acil ve bilinç kaybında varsayılan rıza/zorunluluk hâli (TCK m.25).
5. **İspat yükü**: Aydınlatmanın yapıldığını ve onamın alındığını hekim/hastane ispatlar (karine davacı/hasta lehine).
6. **Ara sonuç**: Aydınlatma eksikse, müdahale teknik olarak kusursuz olsa dahi gerçekleşen komplikasyondan hekim sorumlu olabilir; çünkü hasta o riski üstlenmemiş sayılır.

## Çıktı modülleri
- Onam geçerlilik kontrol listesi
- Aydınlatma içerik boşluğu raporu
- İspat durumu ve belge eksikliği notu
- Müdahaleye özgü onam metni taslağı (yer tutuculu)

## Plugin bağlamı

Bu beceri `saglik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
