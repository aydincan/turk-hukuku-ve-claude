---
name: marka-olabilirlik-mutlak-ret
description: "Bir işaretin tescil edilebilirliği tartışmalıysa veya TÜRKPATENT re'sen ret kararı verdiyse; ayırt edicilik, tasvirilik, yanıltıcılık ve şekil markası sınırlarını m.5 üzerinden denetlemek için kullanılır."
---

# Marka Olabilirlik ve Mutlak Ret Sebepleri

## Görev
İşareti SMK m.4 (marka olabilirlik) ve m.5 (mutlak ret) süzgecinden geçirmek. Mutlak ret sebepleri kamu yararına dayanır ve TÜRKPATENT tarafından re'sen incelenir; hükümsüzlükte de herkes ileri sürebilir. Kullanımla kazanılmış ayırt edicilik (m.5/2) tek kurtarıcı istisnadır.

## Soğuk başlangıç (intake)
- İşaret ne (kelime, şekil, renk, üç boyutlu, slogan)?
- Hangi mal/hizmet için tescil isteniyor?
- İşaret malın özelliğini/cinsini/kalitesini doğrudan anlatıyor mu?
- İşaret piyasada yoğun ve süreli kullanılmış mı (m.5/2 dayanağı)?

## Denetim şeması
1. **Ayırt edicilik (m.5/1-b).** İşaret, malı/hizmeti bir teşebbüsünkinden ayırt edebiliyor mu? Sıradan, vasıfsız işaret reddedilir.
2. **Tasviri işaret (m.5/1-c).** Cins, çeşit, vasıf, kalite, miktar, coğrafi kaynak, üretim zamanını gösteren işaretler. Doğrudan tasvir reddedilir; çağrıştırıcı (suggestive) işaret tescil edilebilir.
3. **Yaygın/jenerik işaret (m.5/1-d).** Ticarette herkesçe veya belirli meslek grubunca kullanılan işaretler.
4. **Şekil engeli (m.5/1-e).** Malın doğal yapısından doğan, teknik zorunluluk içeren veya mala asli değerini veren şekil — kullanımla dahi aşılamaz (m.5/2 dışında).
5. **Yanıltıcılık ve kamu düzeni (m.5/1-f, -i).** Mal/hizmetin niteliği-kaynağı konusunda yanıltıcı; kamu düzeni-genel ahlaka aykırı işaretler.
6. **Önceki aynı/ayırt edilemeyecek marka (m.5/1-ç).** Aynı/aynı tür mal-hizmet için aynı veya ayırt edilemeyecek benzer önceki tescil/başvuru re'sen ret sebebidir.
7. **İstisna (m.5/2).** İşaret başvuru tarihinden önce kullanımla ayırt edicilik kazandıysa b-c-d bentleri uygulanmaz; ispat yükü başvurana aittir (yoğun kullanım, pazar payı, tanıtım delilleri).

## Çıktı modülleri
- Ret sebebi-bent eşleştirme tablosu (var/yok/şüpheli).
- m.5/2 kullanımla ayırt edicilik delil listesi.
- Tescil şansı değerlendirmesi ve mal/hizmet daraltma önerisi.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
