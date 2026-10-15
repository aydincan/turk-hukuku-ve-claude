---
name: itiraz-ve-idari-surec
description: "Gümrük işlem, ek tahakkuk veya ceza kararına karşı dava yolundan önceki zorunlu idari itiraz ve uzlaşma süreçlerini yönetmek gerektiğinde; mercileri, süreleri ve başvuru stratejisini kurmak için kullanılır."
---

# İdari İtiraz ve Uzlaşma Süreci

## Görev
Gümrük idaresinin işlem, ek tahakkuk veya ceza kararına karşı 4458 m.242 idari itiraz yolunu ve m.244 uzlaşma müessesesini doğru mercii ve süreyle yürütmek; dava öncesi en uygun çözüm yolunu seçmek.

## Soğuk başlangıç (intake)
- Karar hangi gümrük idaresince düzenlendi ve hangi tarihte tebliğ edildi?
- İtiraz süresi geçti mi (tebliğden itibaren 15 gün)?
- Uzlaşmaya konu edilebilir bir vergi/ceza farkı var mı; tutar uzlaşma kapsamında mı?
- İtiraz daha önce yapıldı mı, reddedildi mi (açık ret/zımni ret)?

## Denetim şeması
1. İdari itiraz mercii ve süre: 4458 m.242 uyarınca karara karşı, tebliğ tarihinden itibaren 15 gün içinde kararı veren idarenin bağlı olduğu üst mercie (Gümrük Müdürlüğü kararına karşı Bölge/Gümrük ve Dış Ticaret Bölge Müdürlüğü) itiraz edilir. İtiraz idari dava açma süresinden önce tüketilmesi gereken bir aşamadır.
2. İtirazın sonuçlanması: İtiraz mercii 30 gün içinde karar verir; süresinde cevap verilmemesi zımni ret sayılır ve dava süresini başlatır.
3. Uzlaşma (m.244): Beyan ile idare arasındaki kıymet, sınıflandırma, menşe gibi konulardan kaynaklanan vergi farkları ve bunlara bağlı cezalar uzlaşmaya konu olabilir; uzlaşma başvurusu dava açma süresini etkiler ve uzlaşılan tutarda dava açılamaz. İtiraz ve uzlaşma yollarının ilişkisi ve mükerrer kullanılamayacağı gözetilir.
4. Strateji süzgeci: Hukuki sebep güçlüyse itiraz/dava; tutar belirsiz ve uzlaşma indirimi avantajlıysa uzlaşma tercih edilir. Ödeme yapılırken ihtirazi kayıt ve dava hakkının saklanması değerlendirilir.
5. İspat ve dosya: İtiraz dilekçesine beyanname, fatura, menşe belgeleri, ekspertiz raporu ve hukuki gerekçeler eklenir; süre tutum delili (tebliğ alındısı) saklanır.
6. Ara sonuç: Uygun mercii, süre ve yol (itiraz/uzlaşma/dava) belirlenir; başvuru hazırlanır ve dava süresine köprü kurulur.

## Çıktı modülleri
- Süre ve mercii haritası (tebliğ → itiraz → ret → dava)
- Gerekçeli idari itiraz dilekçesi taslağı [doldurulacak yer tutucularıyla]
- Uzlaşma-itiraz-dava karşılaştırmalı karar notu

## Plugin bağlamı

Bu beceri `gumruk-disticaret` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
