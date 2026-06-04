---
name: infaz-ertelenmesi-saglik
description: "Hapis cezası infazının hastalık, gebelik, yaşlılık veya başka zorunlu nedenlerle ertelenmesi ya da geri bırakılması taleplerini değerlendirmek gerektiğinde kullanılır."
---

# İnfazın Ertelenmesi ve Sağlık Nedeniyle Geri Bırakma

## Görev
Hapis cezasının infazının ertelenmesi (CMK m.16-17 ve 5275 m.16-17) için zorunlu nedenlerin varlığını, usulünü ve süre sınırlarını değerlendirmek.

## Soğuk başlangıç (intake)
- Erteleme talebinin sebebi nedir (hastalık, gebelik, yakının ağır hastalığı, eğitim, ekonomik)?
- Hükümlü tutuklu/hükümlü hangi statüde; infaza başlandı mı?
- Sağlık nedeniyse ATK/üniversite hastanesi raporu var mı?
- Daha önce erteleme verildi mi (süre sınırı için)?

## Denetim şeması
1. Hastalık nedeniyle geri bırakma: akıl hastalığı veya kurumda hayatı için kesin tehlike oluşturan hastalık hâlinde infaz geri bırakılır (5275 m.16). Gebe veya doğum yapmış kadın için kanunda belirtilen süre kadar geri bırakma (m.16/4). İspat: Adli Tıp Kurumu veya tam teşekküllü hastane sağlık kurulu raporu.
2. Zorunlu/olağan erteleme: hükümlünün istemiyle, belirli süreli hapiste ve belirli üst sınır altında, eğitim/aile/ekonomik gibi makul nedenlerle erteleme (5275 m.17); güvence istenebilir ve kaçma şüphesi yoksa uygulanır. Suç tipi ve mükerrirlik istisnaları kontrol edilir.
3. Süre ve tekrar: erteleme süreleri ve toplam üst sınır; sürenin sonunda hükümlü teslim olmazsa erteleme hükümsüz kalır.
4. Karar mercii: erteleme/geri bırakma kararı Cumhuriyet Başsavcılığınca verilir; reddine karşı infaz hâkimliği yolu (4675 sayılı Kanun) açıktır. Ara sonuç: yetkili makam ve başvuru yolu.
5. İlkesel içtihat: hastalık nedeniyle geri bırakmada raporun yeterliliği ve insani infaz ölçütleri için karararama.yargitay.gov.tr ve AYM kararları (kararlarbilgibankasi.anayasa.gov.tr); künye `[doğrulanacak]`.
6. Ara sonuç: erteleme uygunluğu + dayanak rapor/belge + süre.

## Çıktı modülleri
- Erteleme sebebi ve dayanak tablosu.
- Rapor/güvence eksik listesi.
- Erteleme talebi ve red kararına itiraz dilekçesi tetiği.

## Plugin bağlamı

Bu beceri `infaz-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
