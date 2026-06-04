---
name: latin-maximleri
description: "Bir hukuki argümanda Latin maximi (pacta sunt servanda, nemo plus iuris, in dubio pro reo, lex specialis) doğru biçimde kullanılacak, çevrilecek ve yürürlükteki maddeye bağlanacaksa kullanılır; uydurma Latince ve yanlış atfı önler."
---

# Latin Hukuk Maximleri ve Doğru Kullanımı

## Görev
Hukuki metinlerde Latin maximlerini doğru lafız, doğru çeviri ve doğru yürürlükteki madde bağlantısıyla kullanmak; maximin bağlayıcı norm değil yardımcı argüman olduğu sınırını korumak.

## Soğuk başlangıç (intake)
- Hangi argüman için maxim aranıyor (sözleşme, ayni hak, ceza, yorum, usul)?
- Maxim mütalaa/dilekçeye mi girecek yoksa açıklama amaçlı mı?
- Yürürlükteki hangi maddeyle bağlanacak?

## Denetim şeması
1. Maximi doğru lafızla seç ve çevir (uydurma Latince yazma):
   - pacta sunt servanda — sözleşmeler bağlayıcıdır (TBK m.1, m.26 ile bağla).
   - nemo plus iuris ad alium transferre potest quam ipse haberet — kimse sahip olduğundan fazlasını devredemez (TMK m.683 devir, m.1023 istisna).
   - clausula rebus sic stantibus — şartların değişmezliği kaydı; aşırı ifa güçlüğü (TBK m.138).
   - res perit domino / periculum est emptoris — hasara mülkiyet sahibi katlanır; satışta yürürlükteki kural TBK m.208 olarak sabit, maximi mutlak kural saymadan kullan.
   - lex specialis derogat legi generali — özel norm genel normu bertaraf eder (norm çatışması, TMK m.1 sistematik yorum).
   - lex posterior derogat legi priori — sonraki kanun öncekini ilga eder.
   - in dubio pro reo — şüpheden sanık yararlanır (CMK 5271 ispat ve masumiyet karinesi, Anayasa m.38).
   - nulla poena sine lege / nullum crimen sine lege — kanunsuz suç ve ceza olmaz (TCK m.2, Anayasa m.38 kanunilik).
   - audiatur et altera pars — diğer taraf da dinlenir (hukuki dinlenilme hakkı, HMK m.27).
   - nemo iudex in causa sua — kimse kendi davasına hâkim olamaz (hâkimin reddi/yasaklılığı, HMK m.34 vd.).
   - in dubio contra stipulatorem / contra proferentem — şüphede düzenleyen aleyhine yorum (genel işlem koşulları, TBK m.23).
2. Maximi yürürlükteki maddeye altla: maxim tek başına gerekçe değildir; ilgili madde ile birlikte ve onu açıklayan yardımcı argüman olarak konumla.
3. İstisna ve sapmayı işaretle: maximin mutlak olmadığı, yürürlükteki normun farklı dengelediği halleri (ör. iyiniyetli üçüncü kişi korumasının nemo plus iuris'i sınırlaması) belirt.
4. Ceza ve usul maximlerinde anayasal dayanağı ekle (Anayasa m.38, m.36). Ara sonuç: maxim + çeviri + yürürlükteki madde + sınır üçlüsünü tamamla.

İspat/dayanak: yürürlükteki madde atfı ile; maxim klasik lafzıyla; Latince kaynak gerekirse fragman [doğrulanacak].

## Çıktı modülleri
- Maxim kartı: Latince lafız / Türkçe çeviri / yürürlükteki madde / sınır notu.
- Argümana yerleştirme önerisi (yardımcı argüman uyarısıyla).
- Yanlış kullanım uyarıları (uydurma Latince, mutlaklaştırma).

## Plugin bağlamı

Bu beceri `roma-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
