---
name: dilekce-sablonlari
description: "Vergi/ceza ihbarnamesinin iptali (yürütmeyi durdurma talepli), ödeme emrine itiraz ve istinaf için usule uygun dilekçe iskeletleri gerektiğinde kullanılır; dava açma süresi ve tutar kontrolüyle birlikte."
---

# Dilekçe Şablonları — Vergi Davaları

## Görev
İhbarnamenin iptali (yürütmeyi durdurma talepli), ödeme emrine itiraz ve istinaf için
usule uygun, doldurulabilir dilekçe iskeletleri sunmak. Süre ve tutar mutlaka kontrol
edilir; künye uydurulmaz.

## Soğuk başlangıç (intake)
- Dava konusu işlem ne (vergi/ceza ihbarnamesi mi, ödeme emri mi)?
- Tebliğ tarihi ve dava açma süresi (genel 30 gün — İYUK m.7; ödeme emri 15 gün — 6183 m.58)?
- Vergi türü, dönem, matrah farkı ve ceza tutarı?
- Yürütmeyi durdurma isteniyor mu (İYUK m.27)?

## Şablon 1 — İhbarname İptali Davası (YD talepli) (İYUK m.2, m.27)
```
… VERGİ MAHKEMESİ BAŞKANLIĞINA
(YÜRÜTMENİN DURDURULMASI TALEPLİDİR)

DAVACI : [Ad/Unvan], VKN/TCKN [doldurulacak], adres
VEKİLİ : Av. [Ad Soyad]
DAVALI : [doldurulacak] Vergi Dairesi Müdürlüğü
TEBLİĞ TARİHİ : [doldurulacak]
D. KONUSU : [tarih-sayı] vergi/ceza ihbarnamesi ile tarh edilen [vergi türü] vergisi
([dönem]) ve [vergi ziyaı/usulsüzlük] cezasının İPTALİ ile İYUK m.27 uyarınca
YÜRÜTMENİN DURDURULMASI istemidir.
TUTAR : [vergi] TL + [ceza] TL.

AÇIKLAMALAR
1. İnceleme/olay özeti: [doldurulacak].
2. Re'sen takdir sebebi oluşmamıştır (VUK m.30): [gerekçe].
3. Matrah farkı somut, hukuken geçerli tespite dayanmamaktadır: [gerekçe].
4. Vergi ziyaı cezası şartları yoktur (VUK m.341, 344); [varsa] tek fiil-tek ceza.
5. İhbarnamenin/tebligatın şekil/usul sakatlığı: [VUK m.35, 93-109 — doldurulacak].
6. YD ŞARTLARI mevcuttur: açık hukuka aykırılık + telafisi güç/imkânsız zarar (İYUK m.27/2).

HUKUKİ NEDENLER : 213 s. VUK; 2577 s. İYUK m.2, 7, 27; [ilgili maddi vergi kanunu].
DELİLLER : İhbarname, vergi inceleme/takdir raporu, defter-belge, [doldurulacak].
SONUÇ VE İSTEM : Öncelikle YÜRÜTMENİN DURDURULMASINA; esastan dava konusu tarhiyat ve
cezanın İPTALİNE; yargılama gideri ve vekâlet ücretinin davalı idareye yükletilmesine
karar verilmesini saygıyla talep ederiz. [tarih] — Davacı Vekili [imza]
```

## Şablon 2 — Ödeme Emrine İtiraz (6183 m.58 / İYUK)
```
… VERGİ MAHKEMESİ BAŞKANLIĞINA

DAVACI / VEKİLİ : [doldurulacak]
DAVALI : [doldurulacak] Vergi Dairesi Müdürlüğü
TEBLİĞ TARİHİ : [doldurulacak]  (Dava süresi: 15 gün — 6183 s.K. m.58)
D. KONUSU : [tarih-sayı] ödeme emrinin İPTALİ istemidir.

AÇIKLAMALAR (6183 m.58 sınırlı itiraz sebepleri)
1. "Böyle bir borç yoktur": [gerekçe — örn. tarhiyat dava konusu/iptal edilmiş].
2. "Borç kısmen ödenmiştir": [gerekçe/dekont].
3. "Borç zamanaşımına uğramıştır": (tahsil zamanaşımı 5 yıl — 6183 m.102) [gerekçe].

HUKUKİ NEDENLER : 6183 s.K. m.58, 102; 2577 s. İYUK.
SONUÇ : Ödeme emrinin İPTALİNE karar verilmesini talep ederiz. [tarih] — Vekil [imza]
```

## Şablon 3 — İstinaf Dilekçesi (İYUK m.45)
```
… BÖLGE İDARE MAHKEMESİ İLGİLİ VERGİ DAVA DAİRESİNE
(… Vergi Mahkemesi aracılığıyla)

KARAR NO : [doldurulacak]   (İstinaf süresi: kararın tebliğinden 30 gün — İYUK m.45)
İSTİNAF EDEN / VEKİLİ : [doldurulacak]
KONU : [tarih-sayı] kararın KALDIRILMASI istemidir.

İSTİNAF SEBEPLERİ
1. Hukuka aykırı değerlendirme: [doldurulacak].
2. Eksik inceleme / delil değerlendirme hatası: [doldurulacak].
3. [varsa] usul hatası.

HUKUKİ NEDENLER : 2577 s. İYUK m.45, 46.
SONUÇ : Kararın KALDIRILARAK davanın kabulüne / [talep] karar verilmesini talep ederiz.
[tarih] — Vekil [imza]
```

## Çıktı modülleri
- Olaya uyarlanmış dilekçe metni (yer tutucular doldurulmuş).
- Süre tablosu (tebliğ → son gün; 30/15 gün ayrımı).
- Tutar ve hesaplama özeti; eklenecek belge dizini.
- `[doğrulanacak]` işaretli içtihat yeri (varsa).

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
