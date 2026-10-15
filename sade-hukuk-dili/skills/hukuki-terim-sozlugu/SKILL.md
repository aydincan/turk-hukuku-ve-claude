---
name: hukuki-terim-sozlugu
description: "Bir metindeki hukuki ve Latince terimleri, kalıpları ve kısaltmaları müvekkile açıklayan sözlük üretmek; terimin yanlış eşanlamlıyla değiştirilmeden doğru karşılığını ve anlam farkını vermek gerektiğinde kullanılır."
---

# Hukuki Terim Açıklama ve Sözlük

## Görev
Bir belgedeki hukuki terimleri, Latince ifadeleri ve kısaltmaları okuyucuya açıklayan, anlam
nüanslarını koruyan bir sözlük/açıklama listesi üretmek. Amaç terimi yok etmek değil, doğru
anlamını yalın bir cümleyle vermek.

## Soğuk başlangıç (intake)
1. Hangi belge ve hangi hukuk alanı (terimlerin anlamı bağlama göre değişir)?
2. Okuyucunun seviyesi (hiç bilmeyen / temel bilen)?
3. Tüm terimler mi, yoksa işaretli olanlar mı açıklanacak?

## Denetim şeması
1. TERİM AVI: Metindeki teknik terimler, Latince kalıplar (inter alia, prima facie, per se, ex nunc/
   ex tunc) ve kısaltmalar (TBK, HMK, İİK, BAM/BİM, ATK) çıkarılır.
2. BAĞLAMA GÖRE TANIM: Her terim, kullanıldığı hukuk dalına göre tanımlanır; aynı kelime farklı
   alanda farklı anlam taşıyabilir ("ifa", "zilyetlik", "def'i").
3. NÜANS AYRIMI (anlam yükü): Karıştırılan çiftler ayrı ayrı açıklanır — zamanaşımı (borç durur
   ama def'i gerekir, TBK m.146 vd.) ≠ hak düşürücü süre (hak kendiliğinden düşer); fesih ≠ iptal
   ≠ dönme ≠ cayma; itiraz ≠ def'i; müteselsil ≠ müşterek sorumluluk; tazminat ≠ ceza.
4. YANLIŞ EŞANLAMLI YASAĞI: Hiçbir terim, hukuki sonucu değiştiren bir günlük kelimeyle eşitlenmez;
   tanım açıklayıcıdır, eşitleyici değildir.
5. ATIF: Terimin dayandığı temel madde varsa parantezle verilir (ör. muacceliyet — TBK m.90 vd.).
6. ARA SONUÇ: Açıklamalar bağlama uygun ve nüans koruyor mu denetlenir.

## Çıktı modülleri
- Alfabetik veya metin sırasına göre terim listesi.
- Her terim için: yalın tanım + (varsa) madde atfı + karıştırılan terimden farkı.
- "Aynı kelime başka anlamda" uyarı kutusu.

## Plugin bağlamı

Bu beceri `sade-hukuk-dili` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
