---
name: el-atmanin-onlenmesi-mudahalenin-meni
description: "Taşınmaza haksız tecavüz, işgal, geçiş, akıntı veya komşunun taşkın kullanımı söz konusu olduğunda; el atmanın önlenmesi, kal (yıkım) ve ecrimisil taleplerini kurmak ve müşterek mülkiyette husumeti çözmek için kullanılır."
---

# El Atmanın Önlenmesi (Müdahalenin Meni) ve Ecrimisil

## Görev
Malikin taşınmazına yönelen fiilî veya hukuki müdahaleyi durdurmak; gereğinde haksız yapının kaldırılmasını (kal) ve geçmiş işgal döneminin haksız kullanım bedelini (ecrimisil) talep etmek.

## Soğuk başlangıç (intake)
- Müdahale ne biçimde: fiilî işgal, sınır tecavüzü/taşkın yapı, izinsiz geçiş, akıntı/koku/gürültü mü?
- Taşınmaz tapuda kimin adına; paylı/elbirliği mülkiyet mi söz konusu?
- Müdahale ne zaman başladı, devam ediyor mu; karşı taraf bir hakka (geçit, kira, tapu) mı dayanıyor?
- Ecrimisil isteniyorsa işgal süresi ve emsal kira/getiri verisi var mı?

## Denetim şeması
1. **Hukuki dayanak**: El atmanın önlenmesi mülkiyet hakkının korunmasından doğar (TMK m.683/2). Malikin taşınmazına haklı sebep olmaksızın yapılan her müdahale önlenebilir.
2. **Unsurlar**: (a) Davacının malik (veya sınırlı ayni hak sahibi) olması, (b) davalının müdahalesinin varlığı ve sürmesi/tekrar tehlikesi, (c) müdahalenin haksızlığı (geçit/intifa/kira gibi bir hakka dayanmaması).
3. **Komşuluk hukuku süzgeci**: Taşkın kullanım iddiasında m.737 (komşuluk hakkı sınırı), taşkın yapıda m.725 (iyiniyetli/kötüniyetli yapan ayrımı), zorunlu geçit/mecra taleplerinde m.747-744 değerlendirilir.
4. **Müşterek mülkiyette husumet**: Paylı mülkiyette her paydaş tek başına el atmanın önlenmesi isteyebilir (koruma işi, m.693). Elbirliği mülkiyetinde kural birlikte hareket olsa da koruyucu davalarda tek mirasçının açabileceği kabul edilir [doğrulanacak — karararama.yargitay.gov.tr].
5. **Kal (yıkım) talebi**: Müdahale bir yapı ise el atmanın önlenmesiyle birlikte yapının kaldırılması istenir; iyiniyetli taşkın yapıda m.725 dengesi gözetilir.
6. **Ecrimisil**: Haksız işgal süresince kötüniyetli/haksız zilyetten kullanım bedeli istenir; talep geriye dönük olup zamanaşımına tabidir. İstihkak veya el atmayla birlikte yan talep olarak ileri sürülür.
7. **Ara sonuç**: Müdahalenin önlenmesi (ve gerekirse kal) + işgal dönemi ecrimisili.

## Çıktı modülleri
- El atmanın önlenmesi dava dilekçesi iskeleti (taşınmaz, müdahale tarifi, talep sonucu).
- Kal talebi ve m.725 iyiniyet değerlendirmesi.
- Ecrimisil hesap çerçevesi (işgal süresi, emsal getiri, zamanaşımı).
- Yetki/görev notu: HMK m.12 (taşınmazın yeri), asliye hukuk.

## Plugin bağlamı

Bu beceri `esya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
