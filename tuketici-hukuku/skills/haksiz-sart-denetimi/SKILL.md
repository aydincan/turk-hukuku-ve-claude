---
name: haksiz-sart-denetimi
description: "Standart/matbu tüketici sözleşmelerinde müzakere edilmemiş, dengesizlik yaratan haksız şartları tespit etmek ve geçersizliğini ileri sürmek gerektiğinde; banka, abonelik, sigorta, üyelik sözleşmeleri için kullanılır."
---

# Haksız Şart Denetimi

## Görev
Tüketici sözleşmesindeki tek tek şartları haksız şart denetiminden geçirmek; müzakere edilmemiş, dürüstlük kuralına aykırı ve tüketici aleyhine dengesizlik yaratan şartların kesin hükümsüzlüğünü (yazılmamış sayılma) ortaya koymak ve sözleşmenin kalan kısmının akıbetini değerlendirmek.

## Soğuk başlangıç (intake)
- Sözleşme matbu/standart mı, şartlar tüketiciyle ayrı ayrı görüşüldü mü?
- İtiraz edilen şart hangisi (ücret, masraf, cezai şart, tek taraflı değişiklik, yetki)?
- Şart tüketici aleyhine nasıl bir dengesizlik yaratıyor?
- Şarta dayanılarak tüketiciden bir bedel tahsil edildi mi?

## Denetim şeması
1. **Kapsam (TKHK m.5/1):** Tüketiciyle müzakere edilmeden sözleşmeye konan, tarafların hak ve yükümlülüklerinde dürüstlük kuralına aykırı biçimde tüketici aleyhine dengesizliğe yol açan şart haksız şarttır.
2. **Müzakere edilmemiş olma karinesi (m.5/3):** Bir şartın önceden hazırlanması ve tüketicinin içeriğine etki edememesi (özellikle standart sözleşme) halinde, o şart müzakere edilmemiş sayılır; aksini, yani şartın ayrıca görüşüldüğünü ispat satıcı/sağlayıcıya düşer.
3. **Yaptırım (m.5/2):** Haksız şart kesin olarak hükümsüzdür; tüketici yönünden yazılmamış (bağlamayan) sayılır. Sözleşme, haksız şart olmadan da varlığını sürdürebiliyorsa diğer hükümlerle ayakta kalır (m.5/4).
4. **Şeffaflık ve yorum:** Şart açık ve anlaşılır olmalıdır; tereddüt halinde tüketici lehine yorumlanır (m.5/5 ve TBK m.23 ilkesi).
5. **İçerik denetimi örnekleri:** Tek taraflı ücret/faiz değiştirme yetkisi, orantısız cezai şart, ispat yükünü tüketiciye yükleyen kayıt, fahiş gecikme faizi, tüketiciyi belirli yetkili mahkemeye zorlayan kayıt tipik haksız şart adaylarıdır; her biri somut dengesizlik testinden geçirilir.
6. **Ara sonuç:** İtiraz edilen şart haksız mı, hangi ödemenin iadesi gündeme gelir, sözleşmenin kalanı ayakta kalır mı?

## Çıktı modülleri
- Şart şart haksızlık değerlendirme tablosu.
- İade edilecek bedel/masraf hesabı.
- Hükümsüzlük ve istirdat talebi argümanları.
- Sözleşmenin geçerli kalan kısmına ilişkin değerlendirme.

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
