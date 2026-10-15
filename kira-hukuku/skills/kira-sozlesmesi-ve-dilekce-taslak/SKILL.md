---
name: kira-sozlesmesi-ve-dilekce-taslak
description: "Yeni bir kira sözleşmesi, tahliye/temerrüt ihtarnamesi, dava veya cevap dilekçesi ya da kira tespiti talebi taslağı hazırlanması gerektiğinde bu beceriyi kullan."
---

# Kira Sözleşmesi, İhtarname ve Dilekçe Taslağı

## Görev
Kira hukukuna özgü belgeleri emredici hükümlere uygun, eksiksiz ve uygulanabilir şekilde taslaklamak: kira sözleşmesi, noter ihtarnamesi, dava/cevap dilekçesi, kira tespiti ve tahliye taleplerini üretmek.

## Soğuk başlangıç (intake)
- Hangi belge isteniyor (sözleşme, ihtar, dilekçe)?
- Taraf ve taşınmaz bilgileri net mi; bilinmeyen alanlar?
- Belgenin amacı/dayanağı hangi madde (m.315, m.350-352, m.344-345)?
- Süre/şekil kısıtı var mı (noter, taahhütlü tebliğ)?

## Denetim şeması
1. **Sözleşme taslağı**: Taraf-taşınmaz-bedel-süre-teslim; emredici sınırlara uyum — güvence en çok üç aylık kira (m.342), gecikme cezası/muacceliyet kaydı **konulamaz** (m.346), artış kaydı TÜFE on iki aylık ortalama tavanına bağlanır (m.344). Bağlantılı edim eklenmez (m.340).
2. **İhtarname**: Temerrüt ihtarında en az otuz günlük süre ve fesih uyarısı (m.315); içerik kesin ve belirli; noterden/iadeli taahhütlü gönderim; tebliğ tarihi delillendirilir.
3. **Dava dilekçesi (HMK m.119)**: Mahkeme, taraflar, konu, vakıalar, hukuki sebepler (ilgili TBK/İİK maddeleri), deliller ve **talep sonucu**; basit yargılama gereği delillerin dilekçeyle sunulması; arabuluculuk son tutanağının eklenmesi.
4. **Kira tespiti talebi**: Süre penceresi (m.345), emsal ve oran dayanağı, yeni bedel talebi ve karar etkisinin dönem başına bağlanması.
5. **Yer tutucu disiplini**: Bilinmeyen her veri `[doldurulacak]` ile işaretlenir; tarih, tutar, ada/parsel uydurulmaz.
6. **Ara sonuç**: Belge + dayanak maddeler + eksik veri listesi.

## Çıktı modülleri
- İstenen belgenin tam taslağı (yer tutuculu).
- Dayanak madde listesi.
- Gönderim/sunum talimatı (noter, harç, ek belgeler).

## Plugin bağlamı

Bu beceri `kira-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
