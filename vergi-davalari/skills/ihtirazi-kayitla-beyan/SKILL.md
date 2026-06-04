---
name: ihtirazi-kayitla-beyan
description: "Mükellefin kendi beyanı üzerine tahakkuk eden vergiye karşı dava hakkını saklı tutmak için ihtirazi kayıt koyma ve buna dayalı dava açma stratejisini kurarken kullanılır."
---

# İhtirazi Kayıtla Beyan ve Dava

## Görev
Beyana dayalı tarhta dava yolunu açık tutmak için ihtirazi kaydı doğru kurgulamak; tereddütlü ya da idari görüşe aykırı bir matrah/vergi unsurunu beyan ederken hakkı saklı tutarak iade veya iptal davasına zemin hazırlamak.

## Soğuk başlangıç (intake)
1. Hangi vergi ve dönem için beyanname veriliyor; tereddütlü unsur ne (istisna, indirim, KDV iadesi, stopaj)?
2. Beyan, bir tebliğ/sirküler/özelge görüşüne uyularak mı yapılıyor, yoksa o görüşe rağmen mi?
3. Beyanname elektronik mi veriliyor; ihtirazi kayıt nasıl işaretlenecek?
4. Vergi ödendi mi, ödenecek mi; amaç iade mi yoksa tahakkukun iptali mi?

## Denetim şeması
1. **Hukuki dayanak.** VUK m.378/2 — mükellef kendi beyanına karşı dava açamaz; istisna, beyana ihtirazi kayıt konulması ve/veya idari hata-hukuka aykırılık iddiasıdır. İYUK m.27/4 kapsamında ihtirazi kayıtla beyanda tahsil kendiliğinden durmaz.
2. **İhtirazi kaydın şekli.** Beyanname üzerinde (e-beyanname sisteminde ilgili alanda) ihtirazi kayıt açıkça belirtilmeli; hangi unsurun ihtirazi kayda konu olduğu somutlaştırılmalı. Kayıtsız beyandan sonra dava hakkı kural olarak doğmaz.
3. **Süre.** Tahakkuk fişinin düzenlenmesi/beyannamenin verilmesi ile dava süresi (İYUK m.7, 30 gün) işlemeye başlar. Tahakkuk fişinin tebliği esas alınır.
4. **Esas denetimi.** İhtirazi kayda konu unsur (örn. bir istisnanın uygulanmaması, bir giderin kabul edilmemesi) için maddi vergi kanunu hükmü ve idari görüşün hukuka uygunluğu altlanır. Ara sonuç: idari görüşün kanuna aykırılığı gösterilebiliyorsa dava ve iade şansı yüksektir.
5. **İade boyutu.** Dava kazanılırsa fazla/yersiz ödenen vergi VUK ve ilgili tebliğ çerçevesinde iade edilir; faiz/red faizi talebi ayrıca kurulur.

## Çıktı modülleri
- İhtirazi kayıt metni (beyannameye eklenecek somut ifade).
- İhtirazi kayda dayalı dava dilekçesi iskeleti.
- İade/faiz talep notu.

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
