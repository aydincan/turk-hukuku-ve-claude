---
name: banka-sirri-mahremiyet
description: "Banka/müşteri sırrının açıklanması, bilgi paylaşımı talepleri (mahkeme, icra, idari kurum, üçüncü kişi), sır ihlali iddiası ve KVKK ile kesişen veri talepleri değerlendirilirken kullanılır."
---

# Banka Sırrı, Müşteri Sırrı ve Bilgi Talepleri

## Görev
Bir bilgi/belge paylaşımının banka sırrı ve müşteri sırrı rejimi (5411 m.73) ile KVKK karşısında hukuka uygun olup olmadığını belirlemek; sır ihlali iddiasında sorumluluğu ve istisnaları denetlemek.

## Soğuk başlangıç (intake)
- Bilgiyi kim istiyor: mahkeme/savcılık, icra dairesi, idari kurum (BDDK, MASAK, vergi, SGK), üçüncü kişi, başka banka mı?
- Talep edilen bilgi müşteri sırrı/banka sırrı kapsamında mı; rızası var mı?
- Açıklama tek taraflı bir personel ifşası mı, yoksa kanuni bir talebe yanıt mı?
- KVKK boyutu (kişisel veri aktarımı) var mı?

## Denetim şeması
1. **Sır kavramı (5411 m.73)**: Banka faaliyetlerine ve müşterilerine ilişkin sır niteliğindeki bilgileri, sıfat ve görevleri dolayısıyla öğrenenler açıklayamaz; bu yasak işten ayrılsalar dahi sürer. Müşteri sırrı, müşterinin kimliği ve hesap/işlem bilgilerini kapsar.
2. **İstisnalar**: Açıklama yasağı, kanunla açıkça yetkili kılınan mercilere (yargı mercileri, MASAK, BDDK, vergi inceleme yetkilileri vb.) yapılan ve görev kapsamıyla sınırlı bildirimleri kapsamaz. Her talepte mercinin kanuni yetkisi ve talebin kapsamı ayrı doğrulanır; genel/ölçüsüz talepler sınırlandırılır.
3. **Rıza ve risk merkezi**: Müşterinin açık rızası veya kanuni dayanak olmadan üçüncü kişiye paylaşım yapılamaz; risk merkezi (5411 m.73/A) paylaşımları kendi rejimine tabidir.
4. **KVKK kesişimi**: Sır niteliğindeki bilgi aynı zamanda kişisel veri ise 6698 sayılı KVKK işleme/aktarım şartları (m.5, m.8-9) ayrıca aranır; sır rejimi ile KVKK kümülatif uygulanır.
5. **İhlal ve yaptırım**: Sırrın hukuka aykırı açıklanması 5411 m.159 uyarınca adli yaptırıma ve TBK m.49 vd. kapsamında tazminata yol açar. Ara sonuç olarak talebin karşılanıp karşılanmayacağını ve hangi kapsamla karşılanacağını yaz.

## Çıktı modülleri
- Talep değerlendirme matrisi (yetki / kapsam / hukuka uygunluk).
- Sınırlı paylaşım veya ret yazısı taslağı.
- Sır ihlali iddiasında sorumluluk ve tazminat analizi.

## Plugin bağlamı

Bu beceri `bankacilik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
