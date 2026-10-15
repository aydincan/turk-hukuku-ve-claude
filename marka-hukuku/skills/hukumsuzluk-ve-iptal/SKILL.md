---
name: hukumsuzluk-ve-iptal
description: "Tescilli bir markanın geçersiz kılınması veya sonradan kullanmama/jenerikleşme nedeniyle iptali gündemdeyse; m.25 hükümsüzlük ve m.26 iptal sebeplerini, sessiz kalma ve kullanmama süzgecini denetlemek için kullanılır."
---

# Marka Hükümsüzlüğü ve İptali

## Görev
Tescilli markayı geçmişe etkili ortadan kaldıran **hükümsüzlük** (m.25, tescil anındaki sakatlık) ile ileriye etkili sona erdiren **iptal** (m.26, tescil sonrası gelişen sebep) ayrımını net kurmak ve doğru davayı seçmek. İki kurumun sebebi, etkisi ve süresi farklıdır.

## Soğuk başlangıç (intake)
- Markanın geçersizliği tescil anına mı (m.5/6 sebepleri) yoksa sonraki gelişmeye mi dayanıyor?
- Marka kaç yıldır tescilli; kullanılıyor mu, hangi mal/hizmette?
- İtiraz eden uzun süre sessiz mi kaldı (m.25/6)?
- İptal sebebi kullanmama mı, jenerikleşme mi, yanıltıcılık mı?

## Denetim şeması
1. **Hükümsüzlük sebepleri (m.25).** Tescil anındaki m.5 (mutlak) ve m.6 (nispi) sebepleri; başvuruda kötüniyet. Mutlak sebeplerde ilgili herkes; nispi sebeplerde menfaati olanlar dava açabilir.
2. **Sessiz kalma yoluyla hak kaybı (m.25/6).** Önceki hak sahibi, sonraki markanın kullanıldığını bilerek/bilmesi gerekerek beş yıl sessiz kalmışsa hükümsüzlük talep edemez; kötüniyetli tescilde bu sınır işlemez.
3. **İptal sebepleri (m.26).** (a) 5 yıl haklı sebep olmaksızın kullanmama (m.9 atfı), (b) marka sahibinin davranışıyla jenerik hale gelme, (c) kullanım sonucu yanıltıcı hale gelme, (d) garanti/ortak markada teknik şartnameye aykırılık.
4. **Kullanmama (m.9/m.26/1-a).** Beş yıllık sürede ciddi kullanım; sembolik kullanım yetersiz. İspat yükü marka sahibinde; haklı sebep (ithalat yasağı vb.) savunması değerlendirilir.
5. **Etki ve usul.** Hükümsüzlük kural olarak geçmişe etkili (m.27); iptal talep/dava tarihinden ileriye etkili. Görevli mahkeme FSHHM (m.156); kısmî hükümsüzlük/iptal mümkündür.

## Çıktı modülleri
- Hükümsüzlük mü iptal mi karar ağacı.
- Sebep-madde-ispat yükü tablosu.
- Sessiz kalma ve kullanmama süre kontrolü; dava dilekçesi iskeleti.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
