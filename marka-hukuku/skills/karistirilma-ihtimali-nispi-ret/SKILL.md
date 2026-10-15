---
name: karistirilma-ihtimali-nispi-ret
description: "İki marka arasında benzerlik ve karıştırılma riski değerlendirilecekse veya yayına itiraz/hükümsüzlük m.6 dayanaklı ileri sürülecekse; işaret-mal benzerliği ve global değerlendirmeyi yürütmek için kullanılır."
---

# Karıştırılma İhtimali ve Nispi Ret Sebepleri

## Görev
Önceki hak sahibinin itirazı/davası karşısında SMK m.6 nispi ret sebeplerini, özellikle karıştırılma ihtimalini (m.6/1) denetlemek. Nispi sebepler kamu yararı değil özel menfaat korur; re'sen incelenmez, itiraz/dava ile ileri sürülür. Değerlendirme bütünsel (global) yapılır.

## Soğuk başlangıç (intake)
- Önceki markanın tescil/başvuru tarihi ve kapsamı (mal/hizmet) nedir?
- İki işaret görsel-işitsel-kavramsal olarak ne kadar benzer?
- Mal/hizmetler aynı mı, aynı tür mü, benzer mi?
- Önceki marka tanınmış mı; tescilsiz öncelik (m.6/3) var mı?

## Denetim şeması
1. **Öncelik/üstünlük.** İtiraz edenin önceki tarihli tescil/başvurusu veya m.6/3 kapsamında ticarette kullanılan eski tarihli işareti var mı?
2. **İşaret benzerliği (m.6/1).** Görsel, işitsel ve kavramsal benzerlik; ortalama tüketicinin belleğinde kalan bütünsel izlenim; baskın-ayırt edici unsur tespiti.
3. **Mal/hizmet benzerliği.** Aynı/aynı tür/benzer mal-hizmet; benzerlikte amaç, kullanım, dağıtım kanalı, tamamlayıcılık ölçütleri (Nice sınıfı tek başına belirleyici değildir).
4. **Karıştırılma ihtimali (global).** İşaret benzerliği ile mal benzerliği etkileşimli değerlendirilir; ilişkilendirme ihtimali (m.6/1) dahil. Önceki markanın ayırt ediciliği yüksekse koruma genişler.
5. **Tanınmış marka (m.6/4-5).** Tescilli tanınmış marka farklı mal/hizmette de korunur (haksız yarar, itibara/ayırt ediciliğe zarar koşuluyla).
6. **Diğer nispi sebepler.** Vekil/temsilci markası (m.6/2), telif-isim-fotoğraf-sınai hak (m.6/6), kötüniyet (m.6/9).
7. **Kullanmama def'i (m.19/2).** İtiraz dayanağı marka 5 yıldır tescilliyse, itiraz edilenin talebiyle kullanım ispatı istenir; ispatlanamazsa itiraz reddedilir.

## Çıktı modülleri
- İşaret-mal benzerlik matrisi (görsel/işitsel/kavramsal + sınıf).
- Karıştırılma ihtimali global değerlendirme notu.
- İtiraz/cevap stratejisi ve kullanmama def'i kontrolü.

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
