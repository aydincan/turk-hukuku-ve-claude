---
name: temel-kavramlar-ve-sistem
description: "Sermaye piyasası ilişkisinin nitelendirilmesi, ihraççı ve sermaye piyasası aracı tespiti, hangi rejimin (SPK madde, Kurul tebliği, BİST kuralı) uygulanacağının ve görevli mercinin belirlenmesi gerektiğinde kullanılır."
---

# Temel Kavramlar ve Sistematik

## Görev
Önündeki olayı sermaye piyasası hukuku süzgecinden geçirip doğru nitelendirmek; uygulanacak normu (SPK maddesi → Kurul tebliği → BİST/MKK/Takasbank prosedürü) ve görevli mercii (Kurul, idari yargı, adli yargı, tahkim) belirlemek.

## Soğuk başlangıç (intake)
- İlgili ortaklık halka açık mı, payları borsada işlem görüyor mu, yoksa halka kapalı ihraççı mı?
- Söz konusu araç nedir (pay, borçlanma aracı, yatırım fonu katılma payı, türev)?
- İşlem halka arz mı, tahsisli/nitelikli yatırımcıya satış mı, ikincil piyasa işlemi mi?
- Sorun ihraç, kamuyu aydınlatma, piyasa dürüstlüğü, kurumsal yönetim mi yoksa yaptırım boyutu mu?

## Denetim şeması
1. **İhraççı/halka açıklık sıfatı:** Pay sahibi sayısı veya borsada işlem görme üzerinden halka açık ortaklık niteliği (SPK m.16) belirlenir. Halka açıklık, sürekli yükümlülükleri (m.14-15) tetikler.
2. **Araç niteliği:** İşleme konu unsurun "sermaye piyasası aracı" (SPK m.3) olup olmadığı saptanır; değilse SPK rejimi dışıdır.
3. **İşlem tipi:** Halka arz mı (SPK m.4, izahname zorunluluğu) yoksa istisna kapsamında tahsisli satış mı (m.11 ve ilgili tebliğ) olduğu ayrılır; ara sonuç olarak izahname/ihraç belgesi gerekip gerekmediği netleşir.
4. **Görevli merci:** İdari yaptırım uyuşmazlıkları idari yargıda (İYUK m.2, m.7); izahname sorumluluğu/tazminat adli yargıda; piyasa suçları (m.106-107) ağır ceza mahkemesinde, Kurul mütalaası şartıyla (m.115); yatırımcı-aracı kurum uyuşmazlığında sözleşmesel tahkim/BİST yolu değerlendirilir.
5. **Norm güncelliği:** Atıf yapılan Kurul tebliğinin yürürlük ve değişiklik durumu doğrulanır; ispat yükü, iddia eden tarafa aittir (HMK m.190; idari işlemde idarenin gerekçelendirme yükü).

## Çıktı modülleri
- Nitelendirme notu: ortaklık/araç/işlem tipi ve uygulanacak rejim
- Görevli/yetkili merci tespiti ve süre uyarısı
- İlgili SPK maddeleri ve tebliğ atıfları listesi (güncellik kaydıyla)
- Sonraki adım önerisi ve uzman beceriye yönlendirme

## Plugin bağlamı

Bu beceri `sermaye-piyasasi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
