---
name: tasinmaz-rehni-ipotek
description: "Bir alacağın taşınmaz teminatına bağlanması, ipoteğin kurulması/derecesi/paraya çevrilmesi veya fekki gündeme geldiğinde; ipotek, ipotekli borç senedi ayrımı, üst sınır ipoteği ve takip yolu için kullanılır."
---

# Taşınmaz Rehni ve İpotek

## Görev
Taşınmaz rehni ilişkisini kurmak ve yönetmek: ipoteğin tesisi, kapsamı, derecesi ve paraya çevrilmesi (icra) yolunu belirlemek; anapara ve üst sınır (azami meblağ) ipoteği ayrımını yapmak.

## Soğuk başlangıç (intake)
- Teminat altına alınan alacak mevcut/belirli mi, yoksa doğacak/değişken bir borç mu (örn. cari kredi)?
- İpotek hangi taşınmaz üzerinde, hangi derecede kuruluyor; başka rehinler var mı?
- Borç ödenmedi mi; talep ipoteğin paraya çevrilmesi mi, yoksa fek (terkin) mi?
- Taşınmaz sahibi ile borçlu aynı kişi mi (üçüncü kişi rehni var mı)?

## Denetim şeması
1. **Türler (TMK m.881)**: Taşınmaz rehni ipotek, ipotekli borç senedi ve irat senedi şeklinde kurulabilir; uygulamada ipotek esastır.
2. **Anapara/üst sınır ipoteği (m.851)**: Mevcut ve belirli alacak için anapara ipoteği; doğacak veya tutarı belirsiz alacak için belirli azami meblağ üzerinden üst sınır (limit) ipoteği kurulur. Faiz ve giderler kapsamı bu ayrıma göre değişir.
3. **Kuruluş**: İpotek resmî senet ve tapuya tescille doğar; rehin yükü taşınmazın bütünleyici parça ve eklentilerini de kapsar (m.862).
4. **Sıra ve derece (m.870-871)**: Rehin hakları derece sistemine tabidir; boşalan dereceden yararlanma (sabit dereceler ilkesi) kayıtla belirlenir.
5. **Paraya çevirme**: Borç ödenmezse alacaklı, rehnin paraya çevrilmesi yoluyla takip (İİK m.145 vd.) başlatır; doğrudan mülkiyeti edinmeyi öngören lex commissoria yasaktır (m.873/2).
6. **Fek/terkin**: Alacak sona erince malik ipoteğin terkinini isteyebilir (m.883); alacaklı terkine yanaşmazsa dava açılır.
7. **Ara sonuç**: Geçerli kuruluş ve kapsamın tespiti; ihtilafta ya paraya çevirme takibi ya da fek davası.

## Çıktı modülleri
- İpotek tesis/fek talebi ve resmî senet kontrol listesi.
- Anapara/üst sınır ipoteği nitelendirme notu (faiz-gider kapsamı).
- Rehnin paraya çevrilmesi takibine geçiş notu (İİK m.145 vd.).

## Plugin bağlamı

Bu beceri `esya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
