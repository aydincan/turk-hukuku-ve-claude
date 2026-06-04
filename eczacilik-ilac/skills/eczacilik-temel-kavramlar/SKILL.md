---
name: eczacilik-temel-kavramlar
description: "Eczacılık-ilaç alanına ilk girişte hangi katmanda (meslek, ürün, geri ödeme) olunduğunu ve görevli yargı yolunu belirlemek; kavram ve norm haritası kurmak gerektiğinde kullanılır."
---

# Eczacılık ve İlaç Hukuku Temel Kavramları

## Görev
Önündeki olayı ilaç-eczacılık hukukunun doğru katmanına yerleştirmek, başat normu ve görevli yargı yolunu seçmek, sonraki uzman beceriye yönlendirmek.

## Soğuk başlangıç (intake)
- Uyuşmazlık kişiye mi (eczacı, mesul müdür, ecza deposu), ürüne mi (ruhsat, fiyat, tanıtım), ödemeye mi (SGK/MEDULA kesintisi) ilişkin?
- Karşı taraf kim: TİTCK, SGK, eczacı odası, ecza deposu, hasta/tüketici, bir başka eczacı?
- Ortada bir idari işlem (ruhsat reddi/iptali, ceza, kesinti) veya bir sözleşme/alacak mı var?
- Elinizde denetim tutanağı, idari yaptırım kararı, sözleşme, ihbarname var mı; tebliğ tarihi nedir?

## Denetim şeması
1. **Katman tespiti.** Meslek icrası → 6197 sayılı Kanun ve Eczaneler Yönetmeliği (RG 12.04.2014). Ürün → 1262 sayılı Kanun + Beşeri Tıbbi Ürünler Ruhsatlandırma Yönetmeliği (RG 11.12.2021) + TİTCK düzenlemeleri (663 sayılı KHK dayanağı). Geri ödeme → 5510 m.63 + SUT.
2. **Yargı yolu.** TİTCK/SGK/oda gibi kamu işlemleri idari yargıda (2577 İYUK); eczane devri, muvazaa, depo-eczane cari hesabı, alacak adli yargıda; 1262 m.18-19, TCK m.187 ceza yargısında; hasta-eczane ilişkisi koşullara göre tüketici mahkemesinde.
3. **Norm hiyerarşisi.** İdari işlemin dayanağı tebliğ/yönetmelik üst normu aşıyorsa Anayasa m.124 ve İYUK çerçevesinde normun uygulanmaması savı kurulur. Ara sonuç: dayanak norm geçerli mi, işlem yetki-şekil-sebep-konu-maksat yönünden sakat mı (idari işlem unsurları).
4. **Süre kapısı.** İdari işlemde İYUK m.7 (60 gün); idari para cezasında özel kanun yoksa 5326 sayılı Kabahatler Kanunu; SGK kesintisinde önce sözleşmesel itiraz kademesi. İspat yükü: idari işlemin sebep unsurunu (denetim bulgusu) idare; iptal sebebini davacı ortaya koyar.

## Çıktı modülleri
- Katman ve yargı yolu tespit notu.
- Uygulanacak normlar listesi (madde/RG tarihiyle).
- Hangi uzman beceriye geçileceğine dair yönlendirme ve eksik bilgi listesi.

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
