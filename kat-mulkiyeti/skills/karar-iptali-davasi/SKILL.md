---
name: karar-iptali-davasi
description: "Kat malikleri kurulunun bir kararı kanuna, yönetim planına veya dürüstlük kuralına aykırı bulunduğunda ya da kurul kararı eksik/gereken kararı almaktan kaçındığında; KMK m.33 kapsamında iptal ya da hâkimin müdahalesi davasını süreleri ve husumetiyle kurmak için kullanılır."
---

# Kurul Kararının İptali ve Eksikliğin Giderilmesi

## Görev
Kanuna, yönetim planına veya dürüstlük kuralına aykırı kat malikleri kurulu kararının iptalini sağlamak; ayrıca kurulun karar almaktan kaçındığı veya yönetimin işlemediği hâllerde hâkimin müdahalesini (m.33) istemek. Süre ve husumetin doğru kurulması bu davada belirleyicidir.

## Soğuk başlangıç (intake)
- İptali istenen karar hangi toplantıda, hangi gündem maddesiyle alındı; tutanak var mı?
- Müvekkil toplantıya katıldı/aykırı oy kullandı mı, yoksa katılmadı mı (süre buna göre değişir)?
- Karar ne yönden sakat: usul (çağrı/nisap) mu, içerik (kanuna/plana/dürüstlüğe aykırılık) mı?
- Karar tarihinden bu yana ne kadar süre geçti?

## Denetim şeması
1. **Hukuki dayanak (KMK m.33/1)**: Kat malikleri kurulunca verilen karara razı olmayan veya kanuna/yönetim planına aykırı karar alındığını ileri süren her kat maliki, anagayrimenkulün bulunduğu yer **sulh hukuk mahkemesine** başvurabilir.
2. **Dava açma süreleri (m.33/1)**: Toplantıya katılıp karara **aykırı oy kullanan** malik karar tarihinden başlayarak **bir ay** içinde; **toplantıya katılmayan** malik kararı öğrenmesinden başlayarak bir ay ve **her hâlde karar tarihinden başlayarak altı ay** içinde dava açabilir. Süreler hak düşürücüdür, re'sen gözetilir.
3. **İptal sebepleri**: (a) Usul sakatlığı — çağrı eksikliği, yetersiz nisap, gündem dışı karar; (b) içerik sakatlığı — KMK'nın emredici hükmüne (örn. oybirliği gereken konuda çoğunlukla karar), yönetim planına veya TMK m.2 dürüstlük kuralına aykırılık.
4. **Yokluk/butlan ayrımı**: Hiç toplantı yapılmadan veya çağrısız "karar" görüntüsü yoklukla maluldür ve süreye bağlı olmaksızın ileri sürülebilir; bu hâlde tespit istenir. Süreye bağlı iptal ile sürekli ileri sürülebilen yokluk ayrımına dikkat et [ilkeler için karararama.yargitay.gov.tr].
5. **Hâkimin müdahalesi (m.33/2-3)**: Kurul, kanunen alması gereken kararı almaktan kaçınır veya yönetim işlemezse, hâkim kat malikinin istemiyle gerekli tedbiri alır ve eksikliği giderir; aykırı davranan malike idari para cezası benzeri yaptırım uygulanabilir (m.33/son).
6. **Husumet**: Dava, kararı uygulayan/yöneten sıfatıyla diğer kat maliklerine veya temsilci olarak yöneticiye yöneltilir; toplu yapıda ilgili kurul esas alınır.
7. **Ara sonuç**: Süre içindeyse iptal/tespit; süre geçmiş ama yokluk varsa tespit; karar eksikliği varsa hâkimin müdahalesi.

## Çıktı modülleri
- İptal davası dilekçesi iskeleti (karar künyesi, sakatlık sebebi, talep, süre beyanı).
- Süre hesap tablosu (katılan/katılmayan; 1 ay / 6 ay).
- Yokluk-iptal ayrım notu ve tedbir (kararın icrasının durdurulması) talebi.

## Plugin bağlamı

Bu beceri `kat-mulkiyeti` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
