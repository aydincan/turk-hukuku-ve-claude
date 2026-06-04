---
name: zamanasimi-ve-sureler
description: "Tarh, ceza kesme ve tahsil zamanaşımı ile dava-uzlaşma-düzeltme sürelerini hesaplamak ve durma/kesilme hallerini tespit etmek; her vergi dosyasında süre riski yönetilirken kullanılır."
---

# Süreler ve Zamanaşımı Haritası

## Görev
Vergi dosyasındaki tüm hak düşürücü süreleri ve zamanaşımlarını tek bir takvimde toplayıp durma/kesilme hallerini hesaplamak; süre kaynaklı hak kaybı riskini ortadan kaldırmak.

## Soğuk başlangıç (intake)
1. Vergiyi doğuran olay hangi takvim yılında gerçekleşti?
2. İhbarname/ödeme emri/işlem hangi tarihte tebliğ edildi?
3. Uzlaşma, düzeltme veya inceleme talebi/işlemi var mı?
4. Borcun vadesi ne zaman doldu?
5. Mücbir sebep veya adli tatil etkisi olabilir mi?

## Denetim şeması
1. **Tarh zamanaşımı:** VUK m.114 — vergi alacağının doğduğu takvim yılını izleyen yılın başından itibaren 5 yıl. Takdir komisyonuna sevk, işleyen zamanaşımını durdurur (m.114/2); duran süre, kararın vergi dairesine tevdiini izleyen günden itibaren işlemeye devam eder (azami bir yıl durma).
2. **Ceza kesme zamanaşımı:** VUK m.374 — vergi ziyaı cezasında tarh zamanaşımı süresi (5 yıl); usulsüzlükte 2 yıl. Süreler vergiyi doğuran olay/usulsüzlüğün işlendiği yılı izleyen yılbaşından işler.
3. **Tahsil zamanaşımı:** AATUHK m.102 — vadeyi izleyen yılbaşından 5 yıl; m.103 kesen haller (ödeme, haciz, teminat, mal bildirimi, cebren tahsil) ve her kesilmede sürenin yeniden başlaması.
4. **Dava/itiraz süreleri:** İYUK m.7 (30 gün), ödeme emri AATUHK m.58 (15 gün), uzlaşma başvurusu 30 gün (VUK Ek m.1), düzeltme talebi tarh zamanaşımı içinde (VUK m.126).
5. **Durma/uzama:** Uzlaşma talebi dava süresini durdurur (VUK Ek m.7); İYUK m.8 sürelerin hesabı, adli/idari tatil; mücbir sebep VUK m.13 ve sürelerin işlememesi VUK m.15. Ara sonuç: her sürenin başlangıç-bitiş tarihi ve kritik gün netleşir.
6. **İspat:** Tebliğ tarihi ve kesen-durduran işlemlerin tarihi belgeyle sabitlenir; tartışmalı tebligatta delil eksikliği işaretlenir.

## Çıktı modülleri
- Birleşik süre takvimi (tarh / ceza / tahsil / dava / uzlaşma — başlangıç ve dolum tarihleriyle).
- Durma-kesilme olay günlüğü (madde dayanağıyla).
- Kritik gün uyarı listesi (en yakın hak düşürücü tarih).
- Belgelendirilmesi gereken tebliğ/kesinti tarihleri listesi.

## Plugin bağlamı

Bu beceri `vergi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
