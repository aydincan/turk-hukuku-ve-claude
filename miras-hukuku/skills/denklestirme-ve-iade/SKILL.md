---
name: denklestirme-ve-iade
description: "Mirasbırakanın sağlığında yasal mirasçılara yaptığı karşılıksız kazandırmaların paylaşmada hesaba katılması ya da terekeye iadesi gerektiğinde; çeyiz, kuruluş sermayesi, eğitim gideri ve malvarlığı devri tartışmalarında kullanılır."
---

# Denkleştirme (İade) Davası

## Görev
Yasal mirasçıların mirasbırakandan sağlararası aldıkları karşılıksız kazandırmaların paylaşmada denkleştirilmesini (iade veya hesaba katma) TMK m.669-675 uyarınca sağlamak.

## Soğuk başlangıç (intake)
- Kazandırmayı alan yasal mirasçı mı? (denkleştirme yalnızca yasal mirasçılar arası)
- Kazandırma türü: çeyiz, kuruluş sermayesi, borç ödeme, malvarlığı devri, eğitim gideri?
- Mirasbırakan iadeden açıkça bağışık tuttu mu (m.669/1)?
- Kazandırma tarihi ve ölüm tarihindeki değeri?
- Alan kişi mirası reddetti mi? (m.674 — reddedende iade yükü farklı)

## Denetim şeması
1. **İade yükümlülüğünü belirle (m.669):** Yasal mirasçılar, miras payına mahsuben yapılan kazandırmaları iadeyle yükümlüdür. Mirasbırakanın aksi iradesi (bağışıklık) açık olmalı; altsoya çeyiz/kuruluş sermayesi/malvarlığı devri için iade karinesi vardır (m.669/2).
2. **Kapsam dışını ayır (m.670):** Olağan eğitim-öğretim giderleri, mutat hediyeler kural olarak iadeye tabi değildir; aşırı olanlar tabidir.
3. **İade biçimini seç (m.671):** Mirasçı, aldığını aynen geri verebilir veya değerini miras payına mahsup edebilir; kazandırma miras payını aşsa bile aşan kısım — mirasbırakanın iradesi ve tenkis kuralları saklı — iade edilmeyebilir (m.672).
4. **Değerleme (m.673):** İade, kazandırmanın denkleştirme anındaki (paylaşma anı) değerine göre; elden çıkarılmışsa sürüm değeri esas alınır.
5. **Çocukların çocukları (m.675):** Önceden ölen mirasçının yerine geçenler, onun almadığı kazandırmaları iade etmez ama kendi aldıklarını iade eder. Ara sonuç: iadeye tabi tutar + biçim (aynen/mahsup) + paylaşmaya etkisi.

## Çıktı modülleri
- Denkleştirme hesap tablosu (kazandırma, değer, mahsup)
- Tenkis ile denkleştirme ayrımı notu (hangisi uygulanır)
- Paylaşma/ortaklığın giderilmesi davasına entegre talep
- İspat için kazandırma belgeleri dizini

## Plugin bağlamı

Bu beceri `miras-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
