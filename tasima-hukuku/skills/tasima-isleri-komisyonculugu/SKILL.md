---
name: tasima-isleri-komisyonculugu
description: "Müvekkil veya karşı tarafın freight forwarder/taşıma işleri komisyoncusu olduğu, taşımanın organizasyonu üstlenildiği ilişkilerde komisyoncunun sorumluluk rejiminin ve taşıyıcı gibi sorumlu sayılma hallerinin değerlendirilmesi gerektiğinde kullanılır."
---

# Taşıma İşleri Komisyonculuğu (Forwarder)

## Görev
Taşıma işleri komisyoncusunun (freight forwarder) borçlarını, özen ve sorumluluk ölçüsünü belirlemek; hangi hallerde taşıyıcı gibi tam sorumlu sayılacağını saptamak.

## Soğuk başlangıç (intake)
1. Müvekkil taşımayı kendi mi üstleniyor, yoksa taşıyıcılarla sözleşip organizasyonu mu sağlıyor?
2. Ücret nasıl belirlenmiş: sabit/maktu (kapsamlı) ücret mi, yoksa komisyon mu?
3. Eşya başkalarının yüküyle birlikte toplu (gruppage) taşımaya mı verildi?
4. Komisyoncu bizzat taşımayı (kendi aracıyla) üstlendi mi?

## Denetim şeması
1. **Tanım ve borç:** TTK m.917 — komisyoncu, ücret karşılığı kendi adına ve müvekkil hesabına eşya taşıtmayı üstlenir. Taşıma sözleşmelerini yapma, gönderme ve özen borcu vardır.
2. **Özen ve sorumluluk:** TTK m.918 — komisyoncu işleri tedbirli bir tacir özeniyle görmekle yükümlüdür; kendi kusurundan ve seçtiği kişilerden sorumludur.
3. **Taşıyıcı gibi sorumluluk halleri:** 
   - **Sabit ücret (m.926):** Komisyoncu müvekkille maktu/sabit bir taşıma ücreti kararlaştırmışsa, yalnızca taşıyıcının hak ve borçlarına sahip olur ve taşıyıcı gibi sorumlu olur.
   - **Toplu yük/gruppage (m.927):** Eşyayı başkalarının eşyasıyla birlikte toplu taşımaya verirse taşıyıcı gibi sorumlu tutulur.
   - **Bizzat taşıma (m.928):** Komisyoncu taşımayı kendisi yaparsa taşıyıcının hak ve yükümlülüklerine de sahip olur.
4. **Sorumluluk sınırı:** Taşıyıcı gibi sorumlu sayılan komisyoncu, TTK m.882 sınırından yararlanır; m.886 halinde sınır kalkar.
5. **Zamanaşımı:** TTK m.855 (1/3 yıl) komisyonculuk istemleri için de esas alınır.
6. **Ara sonuç:** Komisyoncunun özen sorumluluğu mu yoksa taşıyıcı gibi objektif sorumluluğu mu söz konusu.

## Çıktı modülleri
- Sıfat ve ücret yapısına göre sorumluluk rejimi tablosu (m.917/926/927/928).
- Taşıyıcı gibi sorumluluk tetiklenip tetiklenmediği değerlendirmesi.
- Rücu ve zincir sorumluluk (alt taşıyıcı) haritası.

## Plugin bağlamı

Bu beceri `tasima-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
