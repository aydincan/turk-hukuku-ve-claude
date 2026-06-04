---
name: kira-bedeli-tespit-ve-artis
description: "Yenilenen dönemde uygulanacak kira artış oranı, sözleşmedeki artış kaydının geçerliliği, beş yılı aşan kiralarda hakkaniyet belirlemesi veya kira tespit davası açma şartları ve hesabı söz konusu olduğunda bu beceriyi kullan."
---

# Kira Bedelinin Belirlenmesi, Artışı ve Kira Tespit Davası

## Görev
Yenilenen kira döneminde geçerli kira bedelini hesaplamak; sözleşmedeki artış kaydını TBK m.344 sınırına göre denetlemek; kira tespit davasının (TBK m.345) şartlarını, süresini ve etkisini ortaya koymak.

## Soğuk başlangıç (intake)
- Sözleşmedeki artış kaydı ne (sabit oran, TÜFE, döviz)?
- Sözleşme kaç yıldır sürüyor; beş yıl doldu mu?
- Talep eden kim, hangi dönem için ne istiyor?
- Emsal kira ve taşınmazın durumu hakkında veri var mı?

## Denetim şeması
1. **Artış sınırı (TBK m.344/1)**: Tarafların yenilenen dönem için anlaştığı artış oranı, bir önceki kira yılında **on iki aylık ortalama TÜFE** oranını geçemez; aşan kısım geçersiz, sınıra çekilir. Bu kural sözleşmede daha yüksek oran kararlaştırılmış olsa da uygulanır.
2. **Anlaşma yoksa (m.344/2)**: Hâkim, TÜFE on iki aylık ortalamasını aşmamak üzere ve kiralananın durumunu gözeterek hakkaniyete göre belirler.
3. **Beş yıldan uzun/beşinci yıl sonrası (m.344/3)**: Beş yıldan uzun süreli veya beş yıldan sonra yenilenen sözleşmelerde, beşinci yılın sonunda hâkim; TÜFE oranı, kiralananın durumu ve **emsal kira bedelleri** ışığında **hakkaniyet** ile yeni bedeli belirler. Sonraki her beş yılda aynı şekilde.
4. **Yabancı para (m.344/4)**: Sözleşme döviz üzerinden ise beş yıl geçmedikçe değişiklik yapılamaz (kambiyo mevzuatı ve aşırı ifa güçlüğü — TBK m.138 saklı).
5. **Kira tespit davası (TBK m.345)**: Her zaman açılabilir; ancak yeni dönem başından önceki son otuz gün içinde açılır veya kiraya veren bu süre içinde yazılı bildirimde bulunmuşsa dava yeni dönem boyunca açılabilir ve karar yeni dönem başından itibaren etkili olur. Görev sulh hukuk mahkemesi.
6. **İspat ve ara sonuç**: Emsal kira, bilirkişi/keşif; hesabın oran + emsal + hakkaniyet üçlüsüyle gerekçelendirilmesi.

## Çıktı modülleri
- Dönem bazlı kira hesap tablosu.
- Artış kaydı geçerlilik notu.
- Kira tespit davası dilekçesi iskeleti (görev, süre, talep).

## Plugin bağlamı

Bu beceri `kira-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
