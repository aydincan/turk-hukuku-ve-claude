---
name: akademik-kaynak-hijyeni
description: "Roma hukuku metni veya akademik çalışma için birincil kaynak (Corpus Iuris Civilis), Latince maxim ve doktrin atıflarının doğru künyeyle verilmesi gerektiğinde kullanılır; uydurma fragman, sahte künye ve yanlış Latince kullanımını engeller."
---

# Roma Hukuku Kaynak ve Atıf Hijyeni

## Görev
Roma hukuku ve hukuk tarihi metinlerinde birincil kaynak, Latince maxim ve doktrin atıflarının doğru ve doğrulanabilir biçimde verilmesini sağlamak; uydurma fragman, sahte künye ve hatalı Latince kullanımını önlemek.

## Soğuk başlangıç (intake)
- Çıktı akademik metin mi, ders notu mu, mütalaa eki mi?
- Birincil Roma kaynağı (Digesta/Institutiones/Codex) atfı gerekli mi?
- Latince maxim kullanılacak mı; tam lafız mı isteniyor?
- Doktrin künyesi tam mı, yoksa ilkesel atıf mı yeterli?

## Denetim şeması
1. Birincil kaynak atıf standardını uygula:
   - Digesta: D. kitap.başlık.fragman.paragraf (ör. D.41.1.20).
   - Institutiones (Iustinianus): Inst. kitap.başlık.paragraf; Gaius için Gai. kitap.paragraf (ör. Gai. 2.12).
   - Codex: C. kitap.başlık.fragman; Novellae: Nov. numara.
   Fragman numarasından emin değilsen numara uydurma; kurumu anlat ve atfı [doğrulanacak] olarak işaretle.
2. Latince maximi doğru lafızla yaz: tam ve klasik biçimde; eksik/uydurma Latince kullanma. Çeviriyi mutlaka ekle ve yürürlükteki maddeyle bağla.
3. Doktrin atfını düzenle: Türk Roma hukuku literatüründe başlıca eserler ilkesel olarak anılabilir (Ziya Umur — Roma Hukuku Lügatı/Ders Notları; Türkân Rado — Roma Hukuku Dersleri; Belgin Erdoğmuş; Bülent Tahiroğlu/Belgin Erdoğmuş). Tam künye (baskı, sayfa) gerekiyorsa [doğrulanacak] işareti koy; sayfa numarası uydurma.
4. Yürürlükteki norm ile tarihî kaynağı ayrı tut: tarihî bilgi yürürlükteki hukukun yerine geçmez. Çıktıda yürürlükteki madde (TMK/TBK) ile Roma kaynağını farklı katmanlarda göster.
5. İçtihat gerekirse: tarihî-sistematik yorumun mahkemece kullanıldığı kararları karararama.yargitay.gov.tr veya karararama.danistay.gov.tr üzerinden doğrula; esas/karar numarası asla uydurma, doğrulanmamışsa ilkesel atıfla yetin ve [doğrulanacak] işaretle.
6. Ara sonuç: her atfı kaynak türüne göre standartlaştır; doğrulanmamış olanları açıkça etiketle.

İspat/dayanak: birincil kaynak fragman standardıyla; doktrin yazar-eser ile; yürürlükteki norm madde ile.

## Çıktı modülleri
- Atıf listesi (birincil kaynak / doktrin / yürürlükteki norm ayrı bloklar).
- Doğrulama notları ([doğrulanacak] etiketli kalemler).
- Latince maxim sözlüğü (lafız + çeviri + madde bağı).

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
