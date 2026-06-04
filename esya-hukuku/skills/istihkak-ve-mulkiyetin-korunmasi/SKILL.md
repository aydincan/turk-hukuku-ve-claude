---
name: istihkak-ve-mulkiyetin-korunmasi
description: "Malik, malını haksız elinde bulunduran kişiden geri istemek (istihkak) veya mülkiyetine yönelen haksız müdahaleyi durdurmak istediğinde; taşınır/taşınmaz farkı, ispat yükü ve iyiniyetli kazanım savunmaları için kullanılır."
---

# İstihkak ve Mülkiyetin Korunması

## Görev
Malikin, malını fiilen elinde tutan kişiye karşı geri verme (istihkak) talebini ve mülkiyete yönelen her türlü haksız müdahaleyi giderme talebini kurmak; karşı tarafın iyiniyetli kazanım ve üstün hak savunmalarını değerlendirmek.

## Soğuk başlangıç (intake)
- Mal hâlen kimin elinde; müvekkil malik olduğunu hangi belgeyle (tapu, fatura, ruhsat, teslim) gösteriyor?
- Mal karşı tarafa nasıl geçti: çalındı/kayboldu mu, emanet/kira ile mi verildi, satın mı alındı?
- Karşı taraf malı bir başkasından satın aldığını ve durumu bilmediğini ileri sürüyor mu?
- Talep yalnızca geri verme mi, yoksa kullanım bedeli (ecrimisil) de isteniyor mu?

## Denetim şeması
1. **Hak sahipliği**: Malik, mülkiyetini ispatla yükümlüdür (TMK m.683/2, m.6). Taşınmazda tapu kaydı doğruluk karinesi taşır (m.7, m.992); taşınırda zilyetlik mülkiyet karinesi doğurur (m.985).
2. **İstihkak talebi (TMK m.683/2)**: Malik, malını haksız olarak elinde bulundurandan geri isteyebilir. Davalının zilyetliğinin haklı bir sebebe (kira, intifa, rehin) dayanmadığı ortaya konmalıdır.
3. **Taşınırda iyiniyetli kazanım istisnası**: Emin sıfatıyla zilyetten (örn. kiracı, ödünç alan) iyiniyetle taşınır edinen, malik olmasa bile korunur (TMK m.988). Ancak mal çalınmış, kaybolmuş veya rızası dışında elden çıkmışsa malik 5 yıl içinde geri isteyebilir (m.989); para ve hamile yazılı senetlerde bu istisna işlemez (m.990).
4. **İyiniyetin denetimi**: İyiniyet karine olarak vardır (m.3) ama durumun gerektirdiği özeni göstermeyen iyiniyet iddiasında bulunamaz; alış koşulları (fiyat, satıcı, belge) sorgulanır.
5. **El atmanın önlenmesi ile yarışma**: Mal hâlen malikteyse ama müdahale varsa istihkak değil el atmanın önlenmesi gündeme gelir.
6. **Ara sonuç**: Geri verme şartları varsa malın aynen iadesi; mümkün değilse bedel; ayrıca haksız kullanım için ecrimisil.

## Çıktı modülleri
- İstihkak dava dilekçesi iskeleti (taraflar, malın tanımı, mülkiyet delili, talep sonucu).
- İyiniyetli kazanım/üstün hak savunması analizi.
- Ecrimisil yan talebi için süre ve hesap notu.

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
