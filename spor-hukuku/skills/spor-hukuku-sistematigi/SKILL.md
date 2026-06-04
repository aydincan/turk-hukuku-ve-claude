---
name: spor-hukuku-sistematigi
description: "Bir spor uyuşmazlığında devlet mevzuatı, federasyon talimatları, sözleşme ve milletlerarası lex sportiva katmanlarını ayırmak, uyuşmazlığı doğru nitelemek ve uygulanacak normu belirlemek gerektiğinde kullanın."
---

# Spor Hukuku Sistematiği ve Norm Katmanları

## Görev
Spor uyuşmazlığını doğru nitelemek (disiplin, sözleşme, transfer, doping, idari, ceza), hangi norm katmanının ve hangi federasyonun uygulanacağını belirlemek ve devlet hukuku ile özerk spor düzeni (lex sportiva) arasındaki ilişkiyi kurmaktır.

## Soğuk başlangıç (intake)
1. Hangi branş ve hangi federasyon? (TFF mi, bağımsız bir federasyon mu?)
2. Uyuşmazlığın türü ne: disiplin cezası, sözleşmesel alacak, transfer/uygunluk, doping, idari işlem, ceza?
3. Taraflar kim: sporcu, kulüp, menajer, federasyon, üçüncü kişi?
4. Milletlerarası unsur var mı (yabancı kulüp, FIFA/uluslararası federasyon, CAS)?
5. Daha önce bir kurul/merci karar verdi mi; eldeki karar ve tarihi nedir?

## Denetim şeması
1. **Branş ve federasyon tespiti**: Futbolsa 5894 sayılı Kanun ve TFF talimatları; diğer branşlarda 3289 sayılı Kanun çerçevesinde ilgili bağımsız federasyonun ana statüsü ve talimatları uygulanır.
2. **Katman ayrımı**: (a) devlet mevzuatı (7405, 6222, TCK, TBK); (b) federasyon ana statüsü ve talimatları; (c) özel hukuk sözleşmeleri; (d) milletlerarası düzen (FIFA, WADA Kodu, CAS). Aynı olay birden çok katmana değebilir (ör. şike hem TFF disiplinine hem 6222 m.11 ceza normuna girer).
3. **Nitelendirme**: Disiplin → federasyon disiplin kurulu + tahkim. Sözleşmesel → federasyon uyuşmazlık çözüm kurulu/tahkim ya da genel mahkeme (tahkim şartına göre). İdari → kural olarak federasyon tahkimi; istisnaen idari yargı. Ceza → adli yargı.
4. **Özerklik ve Anayasa m.59**: Federasyonların yönetsel ve disipline ilişkin kararlarında zorunlu tahkim ve tahkim kararlarının kesinliği anayasal temele dayanır; bu, devlet yargısına başvuru imkânını sınırlar.
5. **Ara sonuç**: Uygulanacak norm metni, görevli merci ve süre rejimi tek cümlede sabitlenir.

## Çıktı modülleri
- Katman ve nitelendirme tablosu (olay → katman → norm → merci)
- Uygulanacak talimat/madde listesi (yürürlük tarihiyle)
- Görev-yetki ve süre özeti
- Açık sorular ve doğrulanacak içtihat notu

## Plugin bağlamı

Bu beceri `spor-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
