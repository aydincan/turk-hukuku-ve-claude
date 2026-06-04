---
name: el-atmanin-onlenmesi-ve-ecrimisil
description: "Taşınmaza haksız müdahale, tecavüz, işgal veya izinsiz kullanım halinde müdahalenin men'i ve haksız işgal tazminatı (ecrimisil) talep edileceğinde; paylı/elbirliği mülkiyette ortaklar arası el atma ve kötüniyetli zilyedin sorumluluğu değerlendirilirken kullanılır."
---

# El Atmanın Önlenmesi ve Ecrimisil

## Görev
Taşınmaza haksız el atmanın önlenmesi ve haksız işgalden doğan ecrimisil talebini unsur, taraf, süre ve hesap yönünden kurmak.

## Soğuk başlangıç (intake)
- Müdahale türü: fiziki işgal, izinsiz inşaat, geçiş, ortak alanın tek başına kullanımı mı?
- Mülkiyet türü: tek malik mi, paylı (müşterek) mı, elbirliği (iştirak) mi?
- İşgalci kötüniyetli mi; daha önce ihtar/men talebi yapıldı mı?
- Talep men ile birlikte ecrimisil mi; geçmiş kullanım dönemi nedir?

## Denetim şeması
1. **Mülkiyet hakkına dayan.** Malik, haksız el atmaya karşı el atmanın önlenmesini (müdahalenin men'i) ve eski hale getirmeyi isteyebilir (TMK m.683/2). Zilyet de zilyetliğin korunması yollarına başvurabilir (TMK m.982-984).
2. **Müdahalenin haksızlığını kur.** Davalının taşınmazı kullanma hakkı (kira, intifa, irtifak, muvafakat) yoksa müdahale haksızdır. Hukuka uygunluk savunması (rıza, ayni/kişisel hak) öncelikle tüketilir.
3. **Paydaşlar arası el atmayı ayır.** Paylı mülkiyette bir paydaş diğerlerinin payına el atarsa, diğer paydaş kendi payı oranında men ve ecrimisil isteyebilir; intifadan men koşulu kural olarak aranmaz (yerleşik uygulama, künye `[doğrulanacak]`, karararama.yargitay.gov.tr).
4. **Ecrimisil temelini kur.** Ecrimisil, kötüniyetli zilyedin (haksız işgalcinin) malike ödeyeceği haksız işgal tazminatıdır; kötüniyetli zilyedin sorumluluğu TMK m.995'e dayanır (geri verme + tazminat). Hesap, emsal kira/getiri üzerinden bilirkişiyle yapılır.
5. **Süre.** Ecrimisil için geriye dönük 5 yıllık dönem istenir (haksız fiil/zilyetlik tazminatı zamanaşımı uygulaması, künye `[doğrulanacak]`); men davası mülkiyete dayandığı için ayni nitelikte ve kural olarak zamanaşımına tabi değildir.
6. **Görev/yetki.** Görevli asliye hukuk; yetki taşınmaz yeri (HMK m.12). Husumet fiilen işgal eden(ler)e.
7. **Ara sonuç.** Men edilebilir mi, ecrimisil dönemi ve hesabı, kötüniyet ispatı.

## Çıktı modülleri
- Müdahale–hak–talep matrisi (men + ecrimisil).
- Dava dilekçesi iskeleti (keşif, fen ve hesap bilirkişisi talebi, [doldurulacak] dönem).
- Ecrimisil dönemi/zamanaşımı ve emsal kira ispat notu.

## Plugin bağlamı

Bu beceri `tapu-kadastro` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
