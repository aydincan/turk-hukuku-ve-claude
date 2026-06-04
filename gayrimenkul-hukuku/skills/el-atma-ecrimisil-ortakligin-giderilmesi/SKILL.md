---
name: el-atma-ecrimisil-ortakligin-giderilmesi
description: "Taşınmaza haksız tecavüz/işgal olduğunda, geçmiş işgal bedeli (ecrimisil) istendiğinde ya da paydaşlar arası ortaklık sona erdirilmek istendiğinde; el atmanın önlenmesi, ecrimisil ve izale-i şuyu davalarını kurmak için kullanılır."
---

# El Atmanın Önlenmesi, Ecrimisil ve Ortaklığın Giderilmesi

## Görev
Taşınmaz üzerindeki fiilî uyuşmazlıkları çözmek: haksız müdahaleyi durdurmak (el atmanın önlenmesi), haksız işgal dönemi için kullanım bedeli almak (ecrimisil) ve birlikte mülkiyeti sona erdirmek (ortaklığın giderilmesi/izale-i şuyu).

## Soğuk başlangıç (intake)
- Müdahale ne biçimde: fiilî işgal, sınır/taşkın yapı, izinsiz kullanım mı?
- Taşınmaz tek malikte mi, paylı/elbirliği mülkiyette mi?
- Ecrimisil isteniyorsa işgal süresi ve emsal kira/getiri verisi var mı?
- Talep müdahalenin durdurulması mı, ortaklığın tamamen giderilmesi mi?

## Denetim şeması
1. **El atmanın önlenmesi (TMK m.683/2)**: Malik, taşınmazına haklı sebep olmaksızın yapılan her müdahalenin önlenmesini ister. Unsurlar: davacının malik (veya ayni hak sahibi) olması, müdahalenin varlığı/sürmesi ve haksızlığı. Yapı varsa kal (yıkım) talebi eklenir; iyiniyetli taşkın yapıda m.725 dengesi gözetilir.
2. **Paylı mülkiyette husumet**: Her paydaş tek başına el atmanın önlenmesi isteyebilir (koruma işlemi, m.693); elbirliği mülkiyetinde koruyucu davaların tek mirasçıca açılabileceği kabul edilir [doğrulanacak — karararama.yargitay.gov.tr].
3. **Ecrimisil (haksız işgal tazminatı)**: Kötüniyetli/haksız zilyetten, işgal süresince kullanım bedeli istenir; talep geriye dönük olup zamanaşımına (TBK m.146, 10 yıl; haksız fiil yönüyle m.72 değerlendirmesi) ve emsal getiri-keşfe dayanır. Paydaşlar arası ecrimisilde önceden intifadan men koşulu (kural olarak) aranır [ilkeler için karararama.yargitay.gov.tr].
4. **Ortaklığın giderilmesi (m.698-699)**: Her paydaş, aksine engel yoksa her zaman paylaşma isteyebilir. Mahkeme önce **aynen taksimi** (m.699/2) araştırır; mümkün değilse **satış suretiyle paylaştırma** (açık artırma, m.699/3) yapar. Elbirliği mülkiyetinde tüm ortaklar davaya dahil edilir (zorunlu dava arkadaşlığı); muhdesat ve takyidat bedel paylaşımında dikkate alınır.
5. **Ara sonuç**: Müdahale varsa men (+ gerekirse kal) ve ecrimisil; birlikte mülkiyette aynen taksim ya da satış.

## Çıktı modülleri
- El atmanın önlenmesi + ecrimisil dava dilekçesi iskeleti.
- Ortaklığın giderilmesi dilekçesi (paydaş listesi, pay oranları, aynen taksim/satış talebi).
- Görev/yetki notu: el atma asliye hukuk, ortaklığın giderilmesi sulh hukuk (HMK m.4), yetki taşınmazın yeri (HMK m.12).

## Plugin bağlamı

Bu beceri `gayrimenkul-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
