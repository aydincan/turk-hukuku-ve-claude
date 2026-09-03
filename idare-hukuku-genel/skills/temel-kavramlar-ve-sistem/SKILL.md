---
name: temel-kavramlar-ve-sistem
description: "İdare hukukunun temel kavramlarını ve yapısını oturtmak; idari işlem, idari eylem, idari sözleşme, kamu hizmeti ve yargı yolu ayrımını netleştirmek için kullanılır; dosyanın hangi rejime tabi olduğu belirsizse buradan başlanır."
---

# Temel Kavramlar ve Sistematik

## Görev
İdare hukukunun çerçevesini kurmak: önündeki ilişkinin idari mi özel hukuk mu olduğunu, idari işlem/eylem/sözleşme ayrımını ve buradan doğan yargı yolunu (idari/adli) belirlemek. Bu beceri, sonraki tüm denetimlerin zeminini hazırlar.

## Soğuk başlangıç (intake)
1. İşlemi/eylemi yapan makam kim; kamu gücü mü kullanıyor yoksa özel hukuk kişisi gibi mi hareket ediyor?
2. Elinde tek yanlı bir karar mı (işlem), maddi bir faaliyet/davranış mı (eylem), yoksa bir sözleşme mi var?
3. Karar kesin ve yürütülebilir mi, yoksa hazırlık/iç işlem mi?
4. Tebliğ/öğrenme tarihi nedir?

## Denetim şeması
1. **İdarilik testi.** İlişki bir kamu makamının kamu gücü ayrıcalığıyla tesis ettiği bir ilişki mi? Anayasa m.123 (idarenin kanuniliği) ve m.125 (yargı yolu) çerçevesinde değerlendir. İdarenin özel hukuk ilişkileri (kira, satım, eser) kural olarak adli yargıda görülür.
2. **İdari işlem unsurları.** Tek yanlılık, icrailik, kesinlik. İYUK m.14/d uyarınca kesin ve yürütülebilir olmayan işlem dava edilemez; hazırlık işlemleri, görüş, mütalaa, iç genelge kural olarak icrai değildir.
3. **İşlem türünü ayır.** Bireysel-düzenleyici (yönetmelik/genelge), bağlı-takdiri, basit-zincirleme işlem ayrımını yap; düzenleyici işlemlere karşı dava açma süresi ve yetkili mahkeme farklılaşır.
4. **İdari sözleşme mi?** Konusu kamu hizmeti, tarafı idare ve içinde kamu gücü ayrıcalığı/üstün hükümler varsa idari sözleşmedir (imtiyaz, hizmet sözleşmesi); bunlar idari yargıdadır.
5. **Yargı yolu sonucu.** İdari işlem/eylem/idari sözleşme → idari yargı (İYUK). Aksi → adli yargı. **Ara sonuç:** dosyanın rejimi ve gidilecek mahkeme.
6. **İspat yükü.** İdari yargıda re'sen araştırma ilkesi geçerlidir (İYUK m.20); yine de işlemin dayanağı belgeleri ve hukuka aykırılık iddialarını davacı somutlaştırmalıdır.

## Çıktı modülleri
- İlişkinin nitelendirilmesi (idari/özel hukuk) tablosu.
- İşlem/eylem/sözleşme ayrımı ve gerekçesi.
- Yargı yolu ve muhtemel görevli mahkeme önerisi.
- Bir sonraki adım: hangi alt-beceriye geçileceği (iptal denetimi, sorumluluk, kamulaştırma vb.).

## Plugin bağlamı

Bu beceri `idare-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
