---
name: musteri-iletisimi-ve-islem-yonetimi
description: "M&A işleminin yol haritasını müvekkile sade biçimde anlatmak, riskleri ve karar noktalarını özetlemek, term sheet aşamasından kapanışa süreç ve sorumluluk dağılımını yönetmek için kullanılır."
---

# Müvekkil İletişimi ve İşlem Yönetimi

## Görev
İşlemi müvekkilin anlayacağı dille çerçevelemek, kritik karar noktalarını ve riskleri özetlemek, term sheet'ten kapanışa süreci ve görev dağılımını yönetmek.

## Soğuk başlangıç (intake)
- Müvekkilin işlemdeki önceliği ne (hız, fiyat, risk minimizasyonu)?
- Müvekkil M&A deneyimi olan kurumsal bir aktör mü, ilk kez mi?
- Karşı tarafın danışmanları ve müzakere üslubu nasıl?
- İşlem gizliliği ve kamuya açıklama hassasiyeti var mı?

## Denetim şeması
1. **Term sheet / niyet mektubu**: Bağlayıcı (gizlilik, münhasırlık) ve bağlayıcı olmayan hükümlerin ayrımı net yapılır; yanlış anlaşılma TBK m.1 anlamında erken bağlanma riski yaratır.
2. **Gizlilik (NDA)**: Bilgi paylaşımı öncesi gizlilik sözleşmesi ve veri odası kuralları.
3. **Süreç planı**: Signing → CP → closing → post-closing aşamaları, her aşamada müvekkilden beklenen kararlar ve onaylar.
4. **Risk iletişimi**: DD kırmızı bayrakları, indemnity sınırları ve earn-out belirsizlikleri sade dille; karar müvekkile bırakılır, hukuki sonuç açıklanır.
5. **Çıkar çatışması ve gizlilik**: Avukatlık Kanunu (1136) ve meslek kuralları çerçevesinde çatışma taraması ve sır saklama.
6. **İspat/kayıt hijyeni**: Önemli kararlar yazılı teyitle (e-posta/karar notu) belgelenir.
7. **Ara sonuç**: Müvekkile karar matrisi (seçenek, sonuç, öneri) sunulur.

## Çıktı modülleri
- İşlem yol haritası (sade dilli, aşamalı)
- Karar noktaları ve risk özeti (yönetici özeti)
- Term sheet bağlayıcılık ayrım notu
- Görev/sorumluluk dağılım tablosu (responsibility matrix)

## Plugin bağlamı

Bu beceri `birlesme-devralma-ma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
