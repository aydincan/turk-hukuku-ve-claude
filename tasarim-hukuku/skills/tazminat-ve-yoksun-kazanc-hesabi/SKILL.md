---
name: tazminat-ve-yoksun-kazanc-hesabi
description: "Tasarım tecavüzünde maddi/manevi tazminatın ve yoksun kalınan kazancın SMK m.150-151 yöntemleriyle hesaplanması, itibar tazminatı ve faiz başlangıcının belirlenmesi; tecavüzün parasal sonuçlarının talep veya savunma için sayısallaştırılması gerektiğinde kullanılır."
---

# Tazminat ve Yoksun Kalınan Kazanç Hesabı

## Görev
Tasarım tecavüzünün parasal sonucunu kurmak: fiili zarar, yoksun kalınan kazanç, manevi ve itibar tazminatı kalemlerini SMK'ye uygun hesap yöntemiyle ortaya koymak ve bilirkişi denetimine hazır hâle getirmek.

## Soğuk başlangıç (intake)
1. Tecavüz fiili ve süresi belirli mi (üretim/satış adetleri, dönem)?
2. Hak sahibinin kâr marjı, lisans bedeli emsalleri veya satış kaybı verisi var mı?
3. Tasarımın ürünün talebini yaratmadaki ekonomik önemi (m.151/3) nedir?
4. Manevi/itibar zararı doğuran somut olgu var mı (kalitesiz taklitle itibar kaybı)?

## Denetim şeması
1. Kalemler (SMK m.150/1): Maddi tazminat = fiili zarar + yoksun kalınan kazanç. Ayrıca manevi tazminat (genel hükümler) ve itibar tazminatı (SMK m.150/2 — taklidin kötü üretimi/uygunsuz kullanımı hakkın itibarına zarar verdiğinde) istenebilir.
2. Yoksun kalınan kazanç yöntem seçimi (SMK m.151/2): Hak sahibi üç yöntemden birini seçer: (a) tecavüz olmasaydı elde edilebilecek muhtemel gelir, (b) tecavüz edenin elde ettiği net kazanç, (c) lisans verilseydi istenecek makul lisans bedeli. Seçim davacıya aittir; verisi en güçlü yöntemi seçin.
3. Tasarımın katkı payı (SMK m.151/3): Tasarımın ürüne olan ekonomik katkısı belirleyiciyse, kazanç hesaplanırken bu etken dikkate alınır (ürün talebinin tasarımdan kaynaklanma oranı).
4. İspat ve veri: Karşı tarafın ticari defter/satış kayıtları (delil tespiti/sunma yükümlülüğü), gümrük/üretim kayıtları; bilirkişiye yöntemi ve verileri net biçimde sunun.
5. Faiz ve zamanaşımı: Faiz başlangıcı haksız fiil/temerrüt esaslarına göre; tazminat talebi SMK m.157 yollamasıyla TBK haksız fiil zamanaşımına (TBK m.72: ıttıladan itibaren 2 yıl ve her hâlde 10 yıl) tabidir.
6. Ara sonuç: Seçilen yöntem, hesap tablosu, faiz ve zamanaşımı durumu net yazılır.

## Çıktı modülleri
- Tazminat hesap tablosu (kalem, yöntem, veri kaynağı, tutar).
- Yöntem seçimi gerekçesi ve katkı payı analizi.
- Faiz başlangıcı ve zamanaşımı kontrol notu.

## Plugin bağlamı

Bu beceri `tasarim-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
