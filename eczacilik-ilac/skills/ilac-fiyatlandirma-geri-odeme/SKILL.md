---
name: ilac-fiyatlandirma-geri-odeme
description: "İlaç fiyat kararları, referans fiyat, kâr marjları ile SGK geri ödeme listesi, SUT ve Ödeme Komisyonu kararlarına ilişkin uyuşmazlıklarda kullanılır."
---

# İlaç Fiyatlandırma ve Geri Ödeme

## Görev
Bir ilacın fiyatlandırma (TİTCK) ve geri ödeme (SGK/SUT) süreçlerini ayrıştırmak, fiyat veya listeye alma/çıkarma işlemine karşı hukuki yolu kurmak.

## Soğuk başlangıç (intake)
- Sorun fiyatla mı (referans fiyat, depocu/eczacı kâr marjı, KDV), geri ödeme ile mi (EK-4 listesi, SUT koşulu) ilgili?
- İşlem: fiyat onayının reddi/düşürülmesi mi, listeye alınmama mı, listeden çıkarılma mı, eşdeğer grup/fiyat kırılması mı?
- Avro kuru/referans fiyat dönemi hangi karara tabi; hangi tebliğ yürürlükte?
- Ürün hayat kurtarıcı/alternatifi yok mu (ölçülülük argümanı için)?

## Denetim şeması
1. **Fiyat rejimi.** Farmasötik Müstahzarların/Beşeri İlaçların Fiyatlandırılmasına Dair Karar ve TİTCK fiyat tebliği: referans fiyat sistemi, avro değeri, depocu ve eczacı kâr oranları. İşlem idari işlemdir → idari yargı, İYUK m.7 (60 gün).
2. **Geri ödeme rejimi.** 5510 m.63 ve SUT; Ödeme Komisyonu Çalışma Usul ve Esasları; EK-4/A, EK-4/B listeleri. Listeye alma/çıkarma ve SUT koşulları idari düzenleyici işlem/birel işlem niteliğinde; iptal davası açılabilir.
3. **Ayrım kapısı.** Fiyat TİTCK’nın, geri ödeme SGK/Komisyonun yetkisindedir; doğru muhatap ve doğru işlem seçilmezse husumet/ehliyet sorunu doğar. Ara sonuç: dava hangi işleme, kime karşı?
4. **Esas denetimi.** Düzenleyici işlemde normlar hiyerarşisi ve ölçülülük; birel işlemde sebep ve gerekçe. İspat: idare fiyat/listenin dayanağını; davacı eşit muamele ihlali, hesaplama hatası veya ölçüsüzlüğü gösterir.
5. **Yürütmenin durdurulması.** Listeden çıkarma gibi hastayı doğrudan etkileyen işlemlerde telafisi güç zarar somutlaştırılarak İYUK m.27 talep edilir.

## Çıktı modülleri
- Fiyat/geri ödeme ayrım ve muhatap tespiti.
- İptal + yürütmeyi durdurma dilekçe iskeleti [doldurulacak].
- Kâr marjı/referans fiyat hesap denetimi tablosu.

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
