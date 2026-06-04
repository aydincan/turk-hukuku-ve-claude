---
name: malvarligi-suclari
description: "Hırsızlık, yağma, dolandırıcılık, güveni kötüye kullanma ve mala zarar verme suçlarının ayrımını yapmak, nitelikli hallerini ve etkin pişmanlığı denetlemek gerektiğinde kullanılır."
---

# Malvarlığına Karşı Suçlar (Hırsızlık, Yağma, Dolandırıcılık)

## Görev
Malvarlığına karşı suçlarda doğru tipi seçmek, nitelikli halleri tespit etmek ve etkin pişmanlık/şahsî cezasızlık imkânlarını değerlendirmek.

## Soğuk başlangıç (intake)
- Mal faile nasıl geçti: rıza dışı alma mı, hile ile teslim mi, rızayla teslim sonrası mal edinme mi, cebir/tehditle alma mı?
- Olay gece mi, konutta/işyerinde mi, birden fazla kişiyle mi, silahla mı işlendi?
- Araç olarak bilişim sistemi, banka/kamu kurumu kullanıldı mı?
- Fail ile mağdur arasında akrabalık var mı; zarar giderildi mi?

## Denetim şeması
1. Tip ayrımı (kilit adım): Hırsızlık (TCK m.141) zilyedin rızası olmadan malın alınması; dolandırıcılık (m.157) hileyle kişiyi yanıltıp yarar sağlama; güveni kötüye kullanma (m.155) zilyetliği devredilen mal üzerinde devir amacı dışında tasarruf; yağma (m.148) cebir/tehditle alma; mala zarar verme (m.151) malın yok edilmesi/bozulması.
2. Hırsızlık nitelikli haller (TCK m.142): bina/eklenti, gece, kilit kırma/açık kalan, beden/ruh bakımından kendini savunamayacak kişiye karşı, bilişim sistemiyle, örgüt faaliyeti. Daha az ceza m.144; kullanma hırsızlığı m.146; zorunluluk hali m.147.
3. Yağma nitelikli haller (TCK m.149): silahla, gece, birden fazla kişiyle, yol kesme, konutta, beden/ruh bakımından savunamayacak kişiye karşı. Daha az ceza m.150 (değerin azlığı, hukuki ilişkiye dayanan alacak tahsili).
4. Dolandırıcılık nitelikli haller (TCK m.158): dinî inanç istismarı, bilişim sistemi/banka-kredi kurumu araç, kamu kurumu/kamu görevi araç, sigorta, kamu zararı doğurma vb. Basit/nitelikli ayrımı ceza ve uzlaştırma açısından belirleyici.
5. Etkin pişmanlık ve şahsî cezasızlık: Zarar tamamen veya kısmen giderilirse TCK m.168 (kovuşturma öncesi/sonrası farklı oranlar; yağmada da uygulanır). Belirli akrabalar arası mala karşı suçlarda şahsî cezasızlık/şikâyet m.167.
6. Ara sonuç: Seçilen tip + uygulanacak nitelikli hal fıkrası + etkin pişmanlık imkânı + şikâyet/uzlaştırma durumu.

## Çıktı modülleri
- Tip ayrım kararı ve gerekçesi (neden hırsızlık değil dolandırıcılık vb.).
- Nitelikli hal tablosu (madde/fıkra/bent atıflı).
- Etkin pişmanlık ve savunma stratejisi notu.

## Plugin bağlamı

Bu beceri `ceza-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
