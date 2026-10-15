---
name: surel-zamanasimi-ve-takvim
description: "Sermaye piyasası uyuşmazlıklarında dava açma süreleri, idari yaptırım ve suçlarda zamanaşımı, izahname/kamuyu aydınlatma sorumluluğunda zamanaşımı ve hak düşürücü sürelerin hesaplanması gerektiğinde kullanılır."
---

# Süreler, Zamanaşımı ve Takvim

## Görev
Dosyadaki tüm süreleri (dava açma, zamanaşımı, hak düşürücü) ilgili norma göre hesaplamak; başlangıç anı, durma/kesilme ve son günü belgelemek.

## Soğuk başlangıç (intake)
- Talep türü nedir: idari yaptırıma iptal, tazminat, cezai sorumluluk mu?
- Tetikleyici olay ve öğrenme/tebliğ tarihi nedir?
- Süreyi durduran/kesen işlem (başvuru, dava, Kurul kararı) var mı?
- Birden çok eksen (idari + adli) varsa her biri için ayrı takvim gerekiyor mu?

## Denetim şeması
1. **Eksen ayrımı:** İdari yaptırıma iptal süresi İYUK'a; izahname/kamuyu aydınlatma tazminatı SPK m.10/m.32 ve TBK'ya; piyasa suçlarında dava zamanaşımı TCK'ya tabidir. Her eksen ayrı hesaplanır.
2. **İptal davası süresi:** İYUK m.7 uyarınca kararın tebliğinden itibaren işleyen dava açma süresi; üst makama/Kurul'a başvuru (İYUK m.11) süreyi durdurabilir. Hak düşürücüdür, re'sen dikkate alınır.
3. **Tazminat zamanaşımı:** İzahname/kamuyu aydınlatma sorumluluğunda SPK özel hükmü ile TBK m.72 (haksız fiilde öğrenmeden 2, her hâlde 10 yıl) birlikte değerlendirilir; sözleşmesel sorumlulukta TBK m.146 (10 yıl) esas alınır.
4. **Ceza zamanaşımı:** Piyasa suçlarında (SPK m.106-107) dava zamanaşımı, suçun cezası üzerinden TCK m.66'ya göre belirlenir; Kurul mütalaası şartı (m.115) süreçle birlikte not edilir.
5. **Takvim kurma:** Başlangıç anı, durma/kesilme sebepleri ve son gün tarih olarak yazılır; ara sonuç olarak en yakın kritik tarih öne çıkarılır. Tatil/adli tatil etkisi kontrol edilir.

## Çıktı modülleri
- Eksen bazlı süre tablosu (başlangıç-durma-son gün)
- Kritik tarih uyarı listesi
- Zamanaşımı/hak düşürücü ayrımı notu
- Sonraki adım ve hatırlatma planı

## Plugin bağlamı

Bu beceri `sermaye-piyasasi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
