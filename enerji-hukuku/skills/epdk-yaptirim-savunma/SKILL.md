---
name: epdk-yaptirim-savunma
description: "EPDK tarafından verilen idari para cezası, lisans iptali, faaliyet durdurma gibi yaptırımlara karşı savunma ve dava hazırlığı gerektiğinde; yaptırım soruşturması başladığında kullanılır."
---

# EPDK İdari Yaptırımları ve Savunma

## Görev
EPDK kaynaklı idari yaptırımlara (para cezası, lisans iptali, faaliyet durdurma) karşı yazılı savunma, idari başvuru ve iptal davası stratejisini kurmak; usul ve esas sakatlıklarını tespit etmek.

## Soğuk başlangıç (intake)
1. Yaptırımın türü ve dayanağı (hangi madde/yönetmelik ihlali)?
2. Savunma istem yazısı/tebligat tarihi ve verilen süre nedir?
3. İhlal iddiasının somut konusu ve EPDK'nın delili nedir?
4. Daha önce ihtar/savunma alındı mı, tekerrür var mı?

## Denetim şeması
1. **Dayanak ve oran**: 6446 m.16 (elektrik) veya 4646 ilgili maddesi — yaptırım türü ve para cezası tutarının hesabı, üst sınır ve oransallık. Ara sonuç: uygulanan yaptırım türü/oranı dayanakla uyumlu mu.
2. **Usul denetimi**: Savunma hakkının tanınıp tanınmadığı, makul süre verilip verilmediği, gerekçe ve bilgi/belgeye erişim. Usul sakatlığı tek başına iptal sebebi olabilir (idari işlemde şekil/yetki unsuru).
3. **Esas denetimi**: İhlalin maddi olarak gerçekleşip gerçekleşmediği; teknik/lisans yükümlülüğünün ihlali iddiası karşı delil ve uzman raporuyla çürütülür. İspat yükü idarede; ancak müvekkil lehine vakıaları belgeleyin.
4. **Ölçülülük ve eşit muamele**: Benzer ihlallere uygulanan yaptırımlarla karşılaştırma; ağırlaştırıcı/hafifletici unsurlar.
5. **Dava yolu**: İdari yaptırım EPDK işlemi olduğundan İYUK m.7 (kural 60 gün) içinde iptal davası; m.27 yürütmenin durdurulması istemi para cezası tahsili/lisans iptali sonuçlarını dondurmak için kritik. Görevli yargı yeri idari yargıdır.

İlkesel içtihat için karararama.danistay.gov.tr (özellikle 13. Daire) taranır; künye [doğrulanacak] işaretlenir, esas/karar no uydurulmaz.

## Çıktı modülleri
- EPDK savunma yazısı taslağı (usul + esas).
- İptal davası dilekçesi ve YD istemi iskeleti.
- Sakatlık ve karşı delil tablosu.

## Plugin bağlamı

Bu beceri `enerji-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
