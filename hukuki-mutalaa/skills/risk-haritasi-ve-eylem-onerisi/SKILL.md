---
name: risk-haritasi-ve-eylem-onerisi
description: "Hukuki değerlendirmeden çıkan riskleri olasılık ve etki ekseninde haritalandırıp somut, sıralı eylem önerileri üretmek gerektiğinde kullanılır; mütalaayı uygulanabilir kılan bölümdür."
---

# Risk Haritası ve Eylem Önerisi

## Görev
Hukuki değerlendirmenin ortaya çıkardığı riskleri yapılandırmak (hukuki, mali, itibari, süre riski) ve müvekkilin atması gereken somut adımları öncelik sırasıyla önermek. Mütalaa burada teoriden eyleme döner.

## Soğuk başlangıç (intake)
- Müvekkil davacı/talep eden mi, savunan mı?
- Yaklaşan bir süre, zamanaşımı veya hak düşürücü süre var mı?
- Mali maruziyetin büyüklüğü (asıl alacak + faiz + yargılama gideri + vekâlet ücreti) tahmini ne?
- Müvekkilin risk iştahı ve önceliği ne?

## Denetim şeması
1. Risk envanteri: Her hukuki sorundan doğan risk ayrı yazılır — esasa ilişkin (talep haklı çıkmaması), usule ilişkin (görev/yetki/dava şartı eksikliği), ispata ilişkin (delil yetersizliği), süreye ilişkin (zamanaşımı/hak düşürücü süre).
2. Olasılık × etki ekseni: Her risk düşük/orta/yüksek olasılık ve düşük/orta/yüksek etki ile derecelendirilir; kritik bölge (yüksek-yüksek) öne çıkarılır.
3. Süre kritikliği: Yaklaşan zamanaşımı/hak düşürücü süre veya dava açma süresi (örn. İYUK m.7 iptal davasında genel altmış gün; işe iadede İş K. m.20 bir aylık başvuru) en üst öncelikli uyarı olarak işaretlenir.
4. Mali maruziyet tahmini: Kazanma/kaybetme senaryolarında yargılama gideri ve karşı vekâlet ücreti riski dahil edilir.
5. Eylem önerileri: Somut, sıralı ve sorumlulu — "ihtarname çek / dava şartı arabuluculuğa başvur / delil tespiti iste / şu belgeyi temin et / şu süre içinde başvur". Her öneri bir riski azaltmaya bağlanır.
6. Ara sonuç: Risk matrisi + kritik süre uyarısı + numaralı eylem planı.

## Çıktı modülleri
- Risk matrisi (risk | olasılık | etki | azaltıcı tedbir)
- Kritik süre/zamanaşımı uyarı kutusu
- Mali maruziyet senaryoları (kazanma/kaybetme)
- Öncelik sıralı eylem planı

## Plugin bağlamı

Bu beceri `hukuki-mutalaa` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
