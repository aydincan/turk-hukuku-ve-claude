---
name: belge-ispat-dosya
description: "Gümrük uyuşmazlığında ispat yükünü karşılayacak belge setini derlemek, ekspertiz/laboratuvar ve bilirkişi raporlarını değerlendirmek gerektiğinde; delil dizini ve eksik/çelişki kontrolü yapmak için kullanılır."
---

# Belge, İspat ve Dosya Hazırlığı

## Görev
Gümrük uyuşmazlığında ispat yükünü karşılayacak belge setini sistematik biçimde derlemek; ekspertiz, laboratuvar ve bilirkişi raporlarını denetlemek; delil dizini ile eksik ve çelişki listesi üretmek.

## Soğuk başlangıç (intake)
- Uyuşmazlık ekseni nedir (kıymet, menşe, sınıflandırma, rejim)?
- Hangi belgeler mevcut (beyanname, fatura, taşıma/sigorta, menşe ispat belgeleri, ödeme dekontu)?
- İdarenin dayandığı tespit nedir (ekspertiz, laboratuvar, sonradan kontrol raporu)?
- Bilirkişi/ATK incelemesi söz konusu mu?

## Denetim şeması
1. Belge envanteri: Beyanname ve ekleri, ticari fatura, proforma, sözleşme, navlun/sigorta belgeleri, banka ödeme kanıtları, menşe ispat belgeleri (EUR.1, A.TR, menşe şahadetnamesi, fatura beyanı), GTİP/BTB yazışmaları toplanır.
2. İspat yükü dağılımı: Beyanın doğruluğunu kural olarak yükümlü gösterir; idare beyanın aksini somut tespitle (kıymet araştırması, laboratuvar, sonradan kontrol) ortaya koymalıdır. Soyut iddia ispat değildir.
3. Ekspertiz/laboratuvar denetimi: Numune alma usulü, analiz yöntemi, GTİP sonucunun İzahname ile tutarlılığı ve raporun tarafların incelemesine açıklığı kontrol edilir; usule aykırı numune/analiz rapora itiraz gerekçesidir.
4. Bilirkişi raporu: Görev kapsamına uygunluk, kullanılan yöntem ve dayanak, hesap doğruluğu ve çelişki yönünden denetlenir (HMK/İYUK çerçevesinde); gerekirse ek rapor veya yeni bilirkişi talep edilir.
5. Çelişki ve eksik tespiti: Belgeler arası tutarsızlık (fatura-beyanname, menşe-sevk), eksik belge ve idare dosyasındaki boşluklar listelenir.
6. Ara sonuç: İspat stratejisini destekleyen delil dizini, eksik belge listesi ve rapor itiraz noktaları hazır hale gelir.

## Çıktı modülleri
- Delil dizini ve belge envanter tablosu
- Ekspertiz/laboratuvar ve bilirkişi raporu itiraz notu
- Eksik belge ve çelişki listesi

## Plugin bağlamı

Bu beceri `gumruk-disticaret` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
