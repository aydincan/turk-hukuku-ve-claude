---
name: gorev-yetki-yargi-yolu
description: "Bilişim/siber bir uyuşmazlıkta hangi yargı koluna, hangi mahkemeye/mercie, hangi yetki kuralıyla başvurulacağını belirlemek; ceza-idari-hukuk yolları arasında doğru tercihi yapmak gerektiğinde kullanılır."
---

# Görev, Yetki ve Yargı Yolu Haritası

## Görev
Bilişim/siber uyuşmazlıkta doğru yargı kolunu, görevli ve yetkili mercii ve başvuru yolunu belirlemek; eş zamanlı yürüyen süreçleri koordine etmek.

## Soğuk başlangıç (intake)
1. Talep ne? (ceza/şikâyet, idari yaptırım itirazı, tazminat, içerik kaldırma, uyum?)
2. Taraflar kim, biri tacir/tüketici mi, idare mi?
3. Olayın yeri/zararın doğduğu yer neresi?
4. Süre kısıtı veya acil tedbir ihtiyacı var mı?

## Denetim şeması
1. **Ceza yolu.** Bilişim suçlarında (TCK m.243-245) şikâyet/ihbar Cumhuriyet başsavcılığına yapılır; kovuşturmada görev kural olarak asliye ceza, ağırlaştırılmış hallerde ağır ceza mahkemesindedir. Yetki suçun işlendiği yer (CMK m.12). Soruşturma gizliliği ve koruma tedbirleri (CMK m.134) bu yolda işler.
2. **5651 tedbir yolu.** İçerik çıkarma/erişim engellemede görevli mercі sulh ceza hâkimliği (m.9), özel hayatta BTK (m.9/A); kararlara itiraz CMK itiraz usulüne tabidir.
3. **İdari yol (KVKK).** Kurul kararlarına (idari para cezası, ilgili kişi başvurusu sonucu) karşı dava idari yargıda açılır; idari para cezasına karşı yol ise niteliğine göre değerlendirilir (Kabahatler Kanunu/idari yargı tartışması). Dava açma süresi (2577 İYUK m.7) gözetilir.
4. **Hukuk yolu.** Tazminat ve sözleşme uyuşmazlıklarında görev: taraflar tacir ve iş ticari ise asliye ticaret (TTK m.4-5); tüketici işlemiyse tüketici mahkemesi/hakem heyeti; aksi halde asliye hukuk. Yetki HMK m.6 (genel) ve haksız fiilde HMK m.16 (haksız fiilin işlendiği/zararın doğduğu yer). Acil koruma için ihtiyati tedbir/delil tespiti (HMK m.389 vd., m.400 vd.).
5. **Ara sonuç.** Eş zamanlı işleyebilecek yollar (ceza + KVKK + tazminat) ve sıralaması, görev-yetki ve süreler tabloya bağlanır. İspat yükü her yolda ayrıca ele alınır.

## Çıktı modülleri
- Yargı yolu/görev/yetki tablosu (yol, mercі, kural, süre).
- Süre ve acil tedbir takvimi.
- Yol koordinasyon notu (eş zamanlı süreçler).

## Plugin bağlamı

Bu beceri `bilisim-hukuku-siber` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
