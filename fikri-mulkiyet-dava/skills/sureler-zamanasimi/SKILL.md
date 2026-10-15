---
name: sureler-zamanasimi
description: "Fikri-sınai uyuşmazlıkta TÜRKPATENT itiraz süreleri, hükümsüzlük/iptal, tazminat zamanaşımı, ihtiyati tedbir sonrası dava süresi ve sessiz kalma yoluyla hak kaybını hesaplamak gerektiğinde kullanılır."
---

# Süreler ve Zamanaşımı

## Görev
Davaya etki eden tüm süreleri (idari itiraz, dava, tedbir, zamanaşımı, hak düşürücü) doğru hesaplayıp takvime bağlamak; hak kaybını önlemek.

## Soğuk başlangıç (intake)
- Bir TÜRKPATENT/YİDK kararı var mı ve tebliğ tarihi nedir?
- Tecavüz ne zaman öğrenildi, ne zaman gerçekleşti, devam ediyor mu?
- İhtiyati tedbir dava açılmadan mı alındı?
- Marka kaç yıldır biliniyor/kullanılıyor (sessiz kalma riski)?

## Denetim şeması
1. İdari süreçler: Marka yayımına itiraz ve karara itiraz süreleri SMK m.18-20 çerçevesinde (yayımdan itibaren itiraz; YİDK kararına karşı dava süresi tebliğden 2 ay — SMK m.21 ilgili hükmü). Süre kaçırılırsa idari karar kesinleşir.
2. Tazminat zamanaşımı: Tecavüz haksız fiildir; TBK m.72 — zararı ve faili öğrenmeden itibaren 2 yıl, her hâlde 10 yıl. Fiil aynı zamanda suç ise daha uzun ceza zamanaşımı uygulanabilir (TBK m.72/1 son cümle).
3. Süregelen tecavüz: İhlal devam ediyorsa zamanaşımı her gün yeniden işlemeye başlar; geçmişe dönük talepte 2 yıllık kesit korunur.
4. Tedbir sonrası dava: Dava açılmadan alınan ihtiyati tedbirde 2 hafta içinde esas dava açılmazsa tedbir kendiliğinden kalkar (HMK m.397/1). Delil tespitinde benzer disiplin.
5. Sessiz kalma: Marka hükümsüzlüğünde 5 yıl boyunca sonraki markaya sessiz kalma hak kaybı doğurur; kötüniyet istisnadır (SMK m.25/6).
6. Hak düşürücü-zamanaşımı ayrımı: Hükümsüzlük davaları kural olarak süreye tabi değildir (kullanmama/sessiz kalma istisnaları hariç). Ara sonuç: her süre kaynağı (idari, adli, tedbir) ayrı izlenir.

## Çıktı modülleri
- Süre takvimi tablosu (kaynak / başlangıç / bitiş / dayanak madde).
- Zamanaşımı risk notu (süregelen ihlal vurgusuyla).
- Tedbir/delil tespiti dava açma süresi uyarısı.

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
