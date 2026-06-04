---
name: eczane-acilis-nakil-devir
description: "Eczane açma, nakil, devir, mesul müdür ve ikinci eczacı işlemlerinde 6197 sayılı Kanun ve Yönetmelik şartlarını, sayı sınırlaması ve muvazaa riskini denetlemek gerektiğinde kullanılır."
---

# Eczane Açılışı, Nakli ve Devri

## Görev
Eczane açma, nakil ve devir başvurularında 6197 sayılı Kanun ve Eczaneler Yönetmeliği şartlarını adım adım denetlemek, ruhsat reddi/iptaline veya muvazaa iddiasına karşı savunma kurmak.

## Soğuk başlangıç (intake)
- İşlem türü: yeni açılış, nakil, devir, mesul müdür/ikinci eczacı atanması mı?
- Eczacının diploma, kayıt ve varsa mecburi hizmet durumu nedir?
- Yerleşim yeri nüfusu ve mevcut eczane sayısı; nüfusa göre kontenjan uygun mu?
- Devir varsa: devreden vefat/emeklilik mi, bedel ve cari nasıl belirlendi, muvazaa şüphesi var mı?

## Denetim şeması
1. **Eczacı şartları.** 6197 m.2-4: Türk vatandaşlığı, eczacılık diploması, mesleği yapmaya engel hâl bulunmaması. Ara sonuç: kişi ehliyeti tamam mı?
2. **Açılış ve kontenjan.** 6197 m.5 ve Yönetmelik: nüfusa göre eczane sayısı sınırlaması, mevcut eczanelere mesafe, bölge eczacı odası ve il sağlık müdürlüğü süreci. İl sağlık müdürlüğünün ruhsat işlemi idari işlemdir; reddi İYUK m.7 ile 60 günde idari yargıya taşınır.
3. **Nakil.** Yönetmelikteki nakil şartları (taşınılacak yerin kontenjana uygunluğu, asgari donanım). Sebep unsuru eksikse iptal sebebi doğar.
4. **Devir ve muvazaa.** Eczanenin gerçekte eczacı dışı kişi/sermaye tarafından işletilmesi muvazaadır; 6197 ve Yönetmelik muvazaayı yasaklar, tespitinde ruhsat iptali gündeme gelir. İspat: işletme defterleri, banka hareketleri, kira ve cari kayıtları. Devir bedeli ve alacak uyuşmazlığı ise adli yargıda (TBK genel hükümler).
5. **Mesul müdür/ikinci eczacı.** Belirli ciro/nüfus eşiklerinde ikinci eczacı veya yardımcı eczacı zorunluluğu; mesul müdürün sorumluluk kapsamı.

## Çıktı modülleri
- Başvuru/dava uygunluk kontrol listesi (eksik belge dahil).
- Ruhsat reddi/iptaline karşı iptal dilekçesi iskeleti [doldurulacak].
- Muvazaa savunması veya tespiti için delil planı.

## Plugin bağlamı

Bu beceri `eczacilik-ilac` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
