---
name: tarhiyat-iptali-davasi
description: "Vergi veya ceza ihbarnamesi ile tebliğ edilen ikmalen, re'sen ya da idarece yapılan tarhiyata karşı iptal davası kurarken matrah, vergi aslı ve cezayı ayrı ayrı denetlemek için kullanılır."
---

# Tarhiyatın İptali Davası

## Görev
İhbarname ile tebliğ edilen tarhiyatın (vergi aslı + ceza) hukuka aykırılığını ortaya koyan iptal davasını kurmak; matrah tespitindeki, tarh yöntemindeki ve ceza kesme işlemindeki sakatlıkları gerekçelendirmek.

## Soğuk başlangıç (intake)
1. Tarhiyat ikmalen mi (VUK m.29), re'sen mi (m.30), idarece mi yapıldı; gerekçesi ne?
2. Dayanak ne: inceleme raporu, takdir komisyonu kararı, sahte belge tespiti, beyan dışı hasılat?
3. İhbarname kaç gün önce tebliğ edildi; uzlaşma talep edildi mi?
4. Vergi aslına mı, cezaya mı yoksa her ikisine mi itiraz edilecek?

## Denetim şeması
1. **Süre.** İYUK m.7 — tebliğden itibaren 30 gün. Tarhiyat öncesi/sonrası uzlaşma talebi varsa VUK Ek m.7 uyarınca süre durur; uzlaşmanın vaki olmaması/temin edilememesi halinde kalan süre (en az 15 gün) içinde dava açılır.
2. **Yetki-görev.** İYUK m.37 — işlemi yapan vergi dairesinin bulunduğu yer vergi mahkemesi.
3. **Matrah denetimi.** Re'sen tarhda (VUK m.30) takdir sebebinin gerçekliği, defter-belge ibraz edilmiş mi, takdir komisyonu kararının dayanağı ve yöntemi denetlenir. Hasılat/gider tespitinin maddi delile dayanması aranır.
4. **Ceza denetimi.** Vergi ziyaı cezası (VUK m.341, 344) için ziyaın ve kusurun varlığı; bir kat / üç kat ayrımı (m.359'a giren fiil var mı); usulsüzlük/özel usulsüzlük (m.351-353, mük.355) için fiilin tipe uygunluğu ayrı incelenir.
5. **İspat yükü.** VUK m.3/B — vergiyi doğuran olayın gerçek mahiyeti esas; iktisadi icaplara aykırı veya olağan olmayan durumu iddia eden ispatla yükümlü. Sahte belge iddiasında idarenin somut tespit yükü ile mükellefin emtia/ödeme gerçekliği karşı ispatı karşılaştırılır. Ara sonuç: her bir kalem için iptal sebebi güçlü mü, kısmi iptal mi hedefleniyor.
6. **Şekil sakatlıkları.** İhbarnamenin ve inceleme raporunun tebliği, vergilendirme döneminin doğruluğu, zamanaşımı (VUK m.114 tarh zamanaşımı 5 yıl) kontrol edilir.

## Çıktı modülleri
- Kalem kalem (asıl/ceza) iptal gerekçesi tablosu.
- Dava dilekçesi iskeleti (talep sonucu: asıl + ceza + faiz yönünden).
- Delil listesi ve YD talep gerekçesi.

## Plugin bağlamı

Bu beceri `vergi-davalari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
