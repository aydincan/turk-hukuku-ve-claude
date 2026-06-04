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
