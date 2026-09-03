---
name: otomatik-karar-profilleme
description: "Bireyi etkileyen kredi skoru, işe alım eleme, sigorta fiyatlama, içerik moderasyonu gibi münhasıran otomatik kararlar ve profilleme söz konusu olduğunda KVKK m.11/1-g itiraz hakkı, hukuki dayanak ve insan denetimi gerekliliği değerlendirildiğinde kullanılır."
---

# Otomatik Karar ve Profilleme Denetimi

## Görev
Bir yapay zekâ sisteminin kişi hakkında ürettiği kararın "münhasıran otomatik" olup olmadığını, hukuki dayanağını ve ilgili kişinin KVKK m.11/1-g kapsamındaki itiraz hakkını denetleyerek uyum ve savunma stratejisi çıkarmak.

## Soğuk başlangıç (intake)
1. Karar neyi etkiliyor: kredi, sigorta primi, işe alım, abonelik, içerik kaldırma, fiyatlandırma?
2. Sürece insan müdahalesi var mı; varsa anlamlı/etkin bir gözden geçirme mi yoksa biçimsel onay mı?
3. Hangi veriler işleniyor; özel nitelikli (sağlık, biyometrik, etnik) veri var mı?
4. İlgili kişiye otomatik karar uygulandığı aydınlatma metninde belirtilmiş mi?

## Denetim şeması
1. **Münhasıran otomatik mi**: KVKK m.11/1-g, kişinin "münhasıran otomatik sistemlerle analiz edilmesi suretiyle aleyhine bir sonucun ortaya çıkmasına itiraz" hakkını tanır. Anlamlı insan denetimi varsa "münhasıran otomatik" değildir; biçimsel onay yeterli sayılmaz. Ara sonuç: itiraz hakkı doğar mı.
2. **İşleme şartı**: m.5 — açık rıza ya da sözleşmenin kurulması/ifası, hukuki yükümlülük, meşru menfaat gibi bir şart; özel nitelikli veride m.6 daha dar şartlar. Dayanak yoksa işlemenin kendisi hukuka aykırı.
3. **İlkeler**: m.4 — amaçla bağlılık, ölçülülük, doğruluk. Modelin yanlı/güncel olmayan veriyle aleyhe sonuç üretmesi doğruluk ilkesine aykırılık delili olabilir.
4. **Aydınlatma**: m.10 — otomatik karar/profilleme yapıldığı, mantığı ve sonuçları konusunda bilgilendirme. Eksikse aydınlatma ihlali.
5. **Sonuç ve yol**: İhlalde m.13 ilgili kişi başvurusu, ardından m.14 Kurula şikâyet; aleyhe sonuçta tazminat için TBK/haksız fiil değerlendirilir. AB'ye dokunuyorsa GDPR m.22 (kural olarak yasak) karşılaştırmalı kontrol.

İlke kararı ve rehberler için kvkk.gov.tr; doğrulanmamış Kurul/yargı künyesini [doğrulanacak] işaretle.

## Çıktı modülleri
- Münhasıran otomatik karar testi sonucu (evet/hayır + gerekçe).
- İşleme şartı ve aydınlatma uyum tablosu.
- İtiraz/başvuru dilekçesi veya savunma stratejisi taslağı.

## Plugin bağlamı

Bu beceri `yapay-zeka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
