---
name: dogruluk-denetimi-risk
description: "Üretilmiş bir sade dil metnini kaynakla karşılaştırıp anlam kaybı, düşen hak/süre/şart ve yanıltıcı mutlaklaştırma açısından denetlemek; yayımdan önce risk kontrolü yapmak gerektiğinde kullanılır."
---

# Sadeleştirme Doğruluk Denetimi ve Risk Kontrolü

## Görev
Hazır bir sade dil metnini (özet, çeviri, bilgilendirme) kaynak hukuki belgeyle karşılaştırarak
denetlemek; anlam kaybı, düşen hak/süre/şart, yanıltıcı kesinlik ve kaynak hijyeni ihlali var mı
belirlemek. Bu beceri, metni yayımdan/iletmeden önceki son süzgeçtir.

## Soğuk başlangıç (intake)
1. Denetlenecek sade metin ve kaynağı elinizde mi (ikisi birlikte gerekir)?
2. Metin kime gidecek (risk eşiği okuyucuya göre değişir)?
3. Metinde tarih, tutar, süre, koşul gibi sayısal/şart içeren ifadeler var mı?

## Denetim şeması
1. SATIR KARŞILAŞTIRMA: Sade metnin her iddiası kaynaktaki karşılığına bağlanır; karşılığı
   olmayan ("uydurma") veya kaynakta olup metinden düşen unsur işaretlenir.
2. HAK/SÜRE/ŞART KAYBI (ispat yükü): Tüm süreler, tutarlar, koşullu ifadeler ("…hâlinde",
   "…koşuluyla", "…saklı kalmak kaydıyla") kaynakla birebir doğrulanır; mutlaklaştırma düzeltilir.
3. NÜANS DENETİMİ: Tehlikeli terimler (zamanaşımı/hak düşürücü süre, fesih/iptal/dönme,
   müteselsil/müşterek, def'i/itiraz) yanlış eşanlamlıyla değiştirilmiş mi kontrol edilir.
4. KAYNAK HİJYENİ: Atıflar madde/fıkra düzeyinde doğru mu; içtihat zikredilmişse künye
   (mahkeme/daire/esas-karar/tarih) doğrulanmış mı, uydurma numara var mı denetlenir; teyit için
   karararama.yargitay.gov.tr, karararama.danistay.gov.tr, mevzuat.gov.tr kullanılır.
5. YANILTICI KESİNLİK: "Kesinlikle kazanırsınız" gibi vaatler, hukuki tavsiye yerine geçen ifadeler
   ve eksik çekince taranır; beklenti yönetimi notu eklenir.
6. ARA SONUÇ: Bulgular düzeltildi mi; "[doğrulanacak]"/"[doldurulacak]" yer tutucuları yerinde mi.

## Çıktı modülleri
- Denetim bulguları tablosu (düşen / eklenen / mutlaklaştırılan / yanlış terim).
- Düzeltilmiş sade metin veya düzeltme önerileri.
- Kaynak hijyeni kontrol satırı.
- Kalan belirsizlikler ve okuyucuya çekince notu.

## Plugin bağlamı

Bu beceri `sade-hukuk-dili` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
