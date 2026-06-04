---
name: tuketici-kredisi-konut-finansmani
description: "Tüketici kredisi, konut finansmanı ve bağlı kredilerde sözleşme şartlarını, cayma hakkını, erken ödeme indirimini, masraf/ücret iadesini ve temerrüt sonuçlarını değerlendirmek gerektiğinde kullanılır."
---

# Tüketici Kredisi ve Konut Finansmanı

## Görev
Tüketici kredisi ve konut finansmanı sözleşmelerini TKHK rejimine göre denetlemek; cayma, erken ödeme indirimi, haksız masraf/ücret iadesi, bağlı kredi sonuçları ve temerrüt halinde muacceliyet kurallarını altlamak.

## Soğuk başlangıç (intake)
- Kredi türü ne (ihtiyaç/tüketici, konut finansmanı, bağlı kredi)?
- Sözleşme tarihi, tutar, faiz ve tahsil edilen masraflar neler?
- Tüketici cayma, erken ödeme, masraf iadesi ya da temerrüze itiraz mı istiyor?
- Kredi bir mal/hizmet alımıyla bağlantılı mı (bağlı kredi)?

## Denetim şeması
1. **Sözleşme şartı (TKHK m.22-23):** Tüketici kredisi sözleşmesi yazılı şekilde kurulur; zorunlu unsurları içermeyen sözleşmenin geçersizliği tüketici aleyhine ileri sürülemez. Tüketicinin imzaladığı nüshanın verilmesi zorunludur.
2. **Cayma (m.24):** Tüketici 14 gün içinde gerekçe göstermeden krediden cayabilir; anaparayı ve tahakkuk eden faizi azami 30 gün içinde geri öder.
3. **Erken ödeme (m.27):** Tüketici borcun tamamını veya bir kısmını erken ödeyebilir; bu halde gerekli faiz ve komisyon indirimi yapılır.
4. **Masraf/ücret denetimi (m.4, m.5):** Tüketiciden alınan ve sözleşmede açıkça öngörülmeyen ya da hizmet karşılığı olmayan masraf/ücretler haksızdır; iadeye konu olur. Dosya masrafı, hesap işletim ücreti gibi kalemler somut olarak denetlenir.
5. **Bağlı kredi (m.30):** Kredi belirli bir mal/hizmet alımı için verilmişse ve mal/hizmet hiç ya da gereği gibi teslim edilmezse, tüketici satıcı ve kredi veren karşısında haklarını kullanabilir; bağlı kredide kredi veren de sorumluluk üstlenir.
6. **Konut finansmanı (m.32-35) ve temerrüt:** Konut finansmanında muacceliyet için kanunda öngörülen ardışık taksit ve ihtar koşulları (m.34) aranır; bu koşullar oluşmadan tüm borç muaccel kılınamaz.
7. **Ara sonuç:** Hangi hak süre içinde, hangi masraf iadesi mümkün, temerrüt usulüne uygun mu?

## Çıktı modülleri
- Masraf/ücret iade hesabı.
- Cayma veya erken ödeme bildirimi taslağı.
- Bağlı kredi sorumluluk analizi.
- Temerrüt/muacceliyet itiraz argümanları.

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
