---
name: talep-tazminat-hesabi
description: "Hangi taleplerin (tecavüzün ref'i, men'i, tazminat, kazancın iadesi, m.68 bedel) ileri sürüleceğini ve tazminatın nasıl hesaplanacağını belirlemek gerektiğinde; kusur şartı ve üç katına kadar bedel seçeneklerini değerlendirmek için kullanılır."
---

# Talep Türleri ve Tazminat Hesabı

## Görev
İhlal karşısında ileri sürülebilecek talepleri sıralamak, koşullarını test etmek ve tazminat/bedel kalemlerini madde dayanaklı biçimde hesaplamak.

## Soğuk başlangıç (intake)
- İhlal devam ediyor mu, durmuş mu (men ya da ref ihtiyacı)?
- Davalının kusuru var mı; ihlalden kazanç elde etti mi?
- Eser için emsal lisans/sözleşme bedeli var mı?
- Manevi zarar (ad belirtmeme, eserin tahrifi) söz konusu mu?

## Denetim şeması
1. Tecavüzün ref'i (m.66-68): Devam eden veya sonuçları süren ihlalin giderilmesi. Kusur şart değildir. Mali hak ihlalinde eser sahibi, sözleşme yapılsaydı isteyebileceği bedelin veya emsal bedelin üç katını talep edebilir (m.68/1) — bu, ihlalin caydırılması işlevini görür ve ayrı bir tazminat hesabı gerektirmeden uygulanabilir.
2. Tecavüzün men'i (m.69): Muhtemel veya devam eden ihlalin önlenmesi; kusur ve zarar şartı aranmaz.
3. Maddi tazminat (m.70/1-2): Manevi hak ihlalinde m.70/1; mali hak ihlalinde kusur varsa uğranılan zararın tazmini (TBK m.49 vd. atfıyla). Davacı m.68 bedeli ile m.70 tazminatı arasında lehine olanı seçer; mükerrer talep edilmez.
4. Manevi tazminat (m.70/1): Manevi hakların ihlalinde duyulan elem-üzüntü için; takdiri hâkime aittir (TBK m.58 ölçütleriyle).
5. Kazancın iadesi/temin (m.70/3): Kusur aranmadan, ihlal edenin elde ettiği kârın talebi; vekâletsiz iş görme hükümleri kıyasen uygulanır.
6. Hesap unsurları: Emsal lisans bedeli, kullanım süresi/adedi, mecra, eserin niteliği belirlenir; bilirkişiyle desteklenir. Faiz başlangıcı (haksız fiilde olay tarihi) ve zamanaşımı (TBK m.72) kontrol edilir.

İspat yükü: zarar ve miktarı davacı ispatlar; m.68 bedelinde emsal/sözleşme bedeli esas alınır.

## Çıktı modülleri
- Talep matrisi (ref/men/tazminat/m.68 bedel/kazanç — koşul — kusur şartı).
- Tazminat ve m.68 bedel hesap tablosu (emsal, çarpan, faiz).
- Seçimlik haklar arası tercih notu.

## Plugin bağlamı

Bu beceri `telif-haklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
