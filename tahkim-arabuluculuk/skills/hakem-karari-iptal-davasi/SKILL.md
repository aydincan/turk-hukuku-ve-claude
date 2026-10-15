---
name: hakem-karari-iptal-davasi
description: "Verilen bir hakem kararına karşı iptal davası açmak veya gelen iptal talebine karşı koymak; iptal sebeplerini, süreyi ve yetkili mahkemeyi belirlemek gerektiğinde kullanılır."
---

# Hakem Kararının İptali Davası

## Görev
Hakem kararına karşı tek kanun yolu olan iptal davasını yönetmek: iptal sebeplerinin
sınırlı listesi içinde dayanak bulmak, sert süreye uymak ve yetkili mahkemede doğru
talep kurmak. İptal davası kararın esasının yeniden incelenmesi DEĞİLDİR.

## Soğuk başlangıç (intake)
1. Karar iç tahkim (HMK) mi milletlerarası (MTK) mi kararı?
2. Karar tarafa ne zaman bildirildi (süre hesabı için)?
3. Hangi sakatlık iddia ediliyor (yetki yokluğu, usul, kamu düzeni)?
4. Müvekkil iptal davasının davalısı mı, yoksa kararın iptalini mi istiyor?

## Denetim şeması
1. **Yetkili mahkeme ve süre**: İç tahkimde **bölge adliye mahkemesi**, kararın
   bildiriminden itibaren **1 ay** (**HMK m.439/1, /4**). MTK'da **asliye ticaret
   mahkemesi**, **30 gün** (**MTK m.15/A-4**). Süre kesindir; geçirilirse karar
   kesinleşir.
2. **İptal sebepleri (sınırlı/numerus clausus)**: **HMK m.439/2** / **MTK m.15/A** —
   tahkim sözleşmesinin geçersizliği, hakem seçimi/usul aykırılığı, sürenin aşılması,
   talep dışına çıkılması, eşitlik ve hukuki dinlenilme hakkı ihlali. **Re'sen**
   incelenenler: uyuşmazlığın tahkime elverişsizliği ve **kamu düzenine aykırılık**.
3. **İspat yükü**: Sözleşme geçersizliği, usul aykırılığı gibi sebepleri **iptal isteyen**
   ispatlar; elverişlilik ve kamu düzenini mahkeme kendiliğinden gözetir.
4. **Esasa girme yasağı**: Mahkeme kararın maddi/hukuki isabetini denetlemez; yalnızca
   sınırlı sebepleri inceler. Bu sınır talep dilekçesinde gözetilmelidir.
5. **Ara sonuç**: Dayanılabilir iptal sebepleri, süre durumu ve başarı şansı notu.

## Çıktı modülleri
- İptal sebebi-dayanak eşleştirme tablosu (madde atıflı).
- İptal davası dilekçesi taslağı veya iptal talebine cevap taslağı.
- Süre ve yetki uyarı kutusu; ilkesel içtihat atfı `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `tahkim-arabuluculuk` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
