---
name: risk-strateji-ve-fto
description: "Bir ürünü piyasaya sürmeden önce patent ihlali riskinin taranması, dava açma/savunma stratejisinin kurulması ya da patent portföyü kararları gündeme geldiğinde kullanılır; ticari kararı hukuki riskle dengeleyen üst beceridir."
---

# Risk, Strateji ve Kullanım Serbestisi (FTO)

## Görev
Bir ürün/teknolojinin üçüncü kişi patentlerini ihlal etme riskini (freedom to operate) değerlendirmek; hak sahibi veya muhatap konumuna göre saldırı/savunma stratejisi kurmak ve ticari kararı hukuki riskle dengelemek.

## Soğuk başlangıç (intake)
1. Konumun ne: piyasaya girecek ürün sahibi mi, hakkını koruyan patent sahibi mi, ihtarname alan muhatap mı?
2. İlgili teknik alanda hangi geçerli patent/faydalı modeller var; sicil taraması yapıldı mı?
3. Ürünü değiştirme/etrafından dolaşma (design-around) imkânı var mı?
4. Karşı tarafın hakkı hükümsüzlük açısından kırılgan mı?

## Denetim şeması
1. **Hak envanteri.** İlgili alandaki yürürlükteki patent/faydalı modelleri TPMK ve EPO/Espacenet üzerinden tara; süresi dolmuş/ücreti ödenmemiş/hükümsüz kılınmış hakları ele. Ara sonuç: hangi haklar canlı engel?
2. **Kapsam-ürün eşleştirmesi.** Her canlı hakkın bağımsız istemlerini ürünle karşılaştır (SMK m.89; istem yorumu becerisi). Literal/eşdeğer kapsama giren var mı?
3. **Hükümsüzlük kırılganlığı.** Engel oluşturan haklar için prior art ve açıklama yeterliliği (SMK m.138) açısından zayıflık ara; saldırıda hükümsüzlük davası/def'i seçeneğini hazırla.
4. **Tasarım etrafından dolaşma.** Kapsam içine sokan öğeyi çıkararak/değiştirerek (eşdeğer doğurmadan) ürünü kapsam dışına taşıma imkânını teknik ekiple değerlendir.
5. **Yol ve maliyet kararı.** Lisans almak, design-around, hükümsüzlük saldırısı veya riski göze almak arasında; ihtiyati tedbir, tazminat (SMK m.151) ve itibar riskini birlikte tart. Muhatap isen ihtarnameye cevap ve süre yönetimini planla.

## Çıktı modülleri
- Canlı hak envanteri ve engel skoru.
- İstem-ürün risk haritası (yüksek/orta/düşük).
- Hükümsüzlük kırılganlık notu.
- Strateji önerisi (lisans / design-around / saldırı / bekle) ve gerekçe.

## Plugin bağlamı

Bu beceri `patent-faydali-model` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
