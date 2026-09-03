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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
