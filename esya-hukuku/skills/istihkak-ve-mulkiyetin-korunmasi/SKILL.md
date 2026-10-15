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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
