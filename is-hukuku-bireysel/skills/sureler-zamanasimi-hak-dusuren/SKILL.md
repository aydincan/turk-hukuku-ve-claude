---
name: sureler-zamanasimi-hak-dusuren
description: "İş hukukunda zamanaşımı ve hak düşürücü sürelerin (haklı fesih 6 işgünü, işe iade 1 ay/2 hafta, alacaklarda 5 yıl) hesabı gerektiğinde; hangi talebin ne zaman zamanaşımına uğradığını ve kritik süre kayıplarını saptamak için kullan."
---

# Süreler, Zamanaşımı ve Hak Düşürücü Süreler

## Görev
İş uyuşmazlığındaki tüm süreleri (hak düşürücü ve zamanaşımı) doğru kanun atfıyla hesaplamak ve süre riski oluşturan kalemleri işaretlemek.

## Soğuk başlangıç (intake)
1. Fesih ve fiili çalışma sona erme tarihi nedir?
2. Talep edilen kalemler hangileri ve hangi tarihte muaccel oldu?
3. Haklı fesih düşünülüyorsa sebebi öğrenme tarihi nedir?
4. İşe iade gündemde mi, fesih bildirimi ne zaman tebliğ edildi?

## Denetim şeması
1. **Hak düşürücü süreler:**
   - Haklı (derhal) fesih: İş K. m.26 — sebebi öğrenmeden itibaren **6 işgünü** ve her halde fiilin gerçekleşmesinden itibaren **1 yıl**.
   - İşe iade: Arabuluculuğa fesih bildiriminin tebliğinden **1 ay**; arabuluculuk anlaşamama tutanağından **2 hafta** içinde dava (7036 m.11, m.3).
2. **Zamanaşımı (7036 Geç. m.8 ve TBK):**
   - Kıdem tazminatı, ihbar tazminatı, kötüniyet tazminatı, eşit davranma (ayrımcılık) tazminatı ve yıllık izin ücreti: **5 yıl** (7036 ile getirilen özel süre; yürürlük tarihi ayrımı için geçiş hükmü gözetilir).
   - Ücret, fazla çalışma, hafta tatili, UBGT gibi ücret nitelikli alacaklar: **5 yıl** (TBK m.147/1).
3. **Başlangıç:** Kıdem/ihbarda zamanaşımı kural olarak fesih tarihinden; ücret ve fazla çalışma gibi dönemsel alacaklarda her dönem muaccel oldukça işler (her ay ayrı).
4. **Kesilme/durma:** Dava, icra takibi, arabuluculuğa başvuru gibi sebepler zamanaşımını keser/durdurabilir; arabuluculukta sürelerin durması (6325 m.16 atfı) gözetilir.
5. **Ara sonuç:** Süresi geçmiş kalem talep edilemez; kısmi dava/ıslah halinde ek talep edilen kısmın zamanaşımı ıslah/ek talep tarihine göre değerlendirilir.

## Çıktı modülleri
- Süre tablosu (kalem / süre türü / başlangıç / bitiş).
- Riskli/kaybedilmiş kalemler uyarısı.
- Zamanaşımını kesecek/durduracak işlem önerisi.
- Geçiş hükmü ve [doğrulanacak] yürürlük notu.

## Plugin bağlamı

Bu beceri `is-hukuku-bireysel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
