---
name: yurutmenin-durdurulmasi
description: "Vergi davası açılmasının tahsile etkisini ve İYUK m.27 kapsamında yürütmenin durdurulması talebinin koşullarını değerlendirerek tahsilat baskısını yönetmek için kullanılır."
---

# Yürütmenin Durdurulması ve Tahsilatın Önlenmesi

## Görev
Dava açmanın tahsil üzerindeki etkisini doğru saptamak ve gerektiğinde İYUK m.27 uyarınca yürütmenin durdurulması (YD) talebini koşullarıyla kurmak; haciz, e-haciz ve banka blokesi gibi tahsilat işlemlerinin baskısını yönetmek.

## Soğuk başlangıç (intake)
1. Dava konusu işlem tarhiyat (ihbarname) mı, ödeme emri mi, ihtirazi kayıtlı beyan mı?
2. Halihazırda haciz, e-haciz veya banka bloke uygulandı mı?
3. İşlemin uygulanması telafisi güç/imkânsız bir zarar doğuruyor mu (nakit akışı, iş sürekliliği)?
4. Teminat gösterilebilir mi (banka teminat mektubu, gayrimenkul)?

## Denetim şeması
1. **Otomatik durma var mı.** İYUK m.27/4 — tarhiyata karşı vergi mahkemesinde dava açılması, tahsil işlemlerini **kendiliğinden durdurur**; ayrı YD talebine gerek yoktur. Bu istisna yalnızca tarhiyat davasına özgüdür.
2. **Otomatik durmanın olmadığı haller.** Ödeme emrine karşı davada ve ihtirazi kayıtla beyana dayalı davada otomatik durma yoktur; tahsili durdurmak için İYUK m.27 uyarınca YD talebi şarttır.
3. **YD'nin iki koşulu.** İYUK m.27/2 — (i) işlemin açıkça hukuka aykırı olması ve (ii) uygulanması halinde telafisi güç veya imkânsız zararların doğması; bu iki şart birlikte aranır. Gerekçe somut maddi-hukuki dayanakla yazılır.
4. **Teminat.** YD kararıyla birlikte teminat istenebilir; AATUHK m.10'daki teminat türleri değerlendirilir. Tecil (AATUHK m.48) paralel seçenek olarak tartılır.
5. **İtiraz yolu.** İlk derece YD kararına karşı BİM'e itiraz süresi ve usulü (İYUK m.27/7) not edilir. Ara sonuç: hangi işlem için otomatik durma, hangisi için aktif YD talebi gerektiği netleştirilir.

## Çıktı modülleri
- İşlem türüne göre durma haritası (otomatik / talep gerekli).
- YD talep gerekçesi (iki koşulu somutlaştıran metin).
- Teminat/tecil alternatifi notu.

## Plugin bağlamı

Bu beceri `vergi-davalari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
