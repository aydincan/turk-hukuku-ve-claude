---
name: temel-kavramlar-ve-sistem
description: "Anayasa hukukunun temel kavramlarını, normlar hiyerarşisini ve 1982 Anayasası sistematiğini netleştirmek; bir uyuşmazlığın hangi anayasal başlığa ve denetim yoluna oturduğunu konumlandırmak gerektiğinde kullanılır."
---

# Temel Kavramlar ve Anayasal Sistematik

## Görev
Kullanıcının önündeki sorunu anayasal sistematiğe oturtmak: normlar hiyerarşisini, anayasanın üstünlüğünü (m.11), temel hak rejimini (m.12-74) ve organ yapısını (yasama-yürütme-yargı) doğru çerçeveye yerleştirip uygun denetim yoluna yönlendirmek.

## Soğuk başlangıç (intake)
1. Sorun bir norma mı (kanun, CB kararnamesi, yönetmelik) yoksa bireysel bir işleme/yargı kararına mı dayanıyor?
2. Hangi temel hak veya anayasal ilke (eşitlik, ifade, mülkiyet, adil yargılanma) zedeleniyor?
3. Taraf kim — birey mi, kamu organı mı, organlar arası yetki sorunu mu?
4. Hedef ne: norm denetimi, bireysel başvuru, yoksa danışma niteliğinde değerlendirme mi?

## Denetim şeması
1. **Normun yerini belirle.** Anayasa (m.11 üstünlük) > kanun/CB kararnamesi (m.104) > yönetmelik (m.124) > bireysel işlem. CB kararnamesi ile kanun çatışmasında kanun esas alınır (m.104/17).
2. **Hak/ilke katmanı.** İlgili Anayasa maddesini tespit et; m.90/son uyarınca AİHS'teki karşılığını köprüle. Ara sonuç: koruma alanı içinde miyiz?
3. **Sınırlama rejimi.** Bir hakka müdahale varsa m.13 süzgeci devreye girer (kanunilik, meşru amaç, demokratik toplumda gereklilik, ölçülülük, hakkın özü). Eşitlik iddiasında m.10: karşılaştırılabilir durum + farklı muamele + haklı sebep yokluğu.
4. **Yetki/usul katmanı.** Organlar arası ilişkide görev, şekil ve yöntem (yasama m.87-89, yürütme m.104-105, yargı bağımsızlığı m.138-140) ayrıca denetlenir.
5. **Denetim yolunu seç.** Soyut/somut norm denetimi (m.150-152), bireysel başvuru (m.148/3, 6216), idari yargı (m.125) ya da olağan yargı. İspat yükü, hak iddiası ileri süren tarafta; müdahalenin meşruiyetini ise müdahale eden kamu makamı temellendirir.

## Çıktı modülleri
- Sorunun anayasal nitelendirmesi ve uygulanacak madde haritası.
- Uygun denetim yolu ve ön koşulların (süre, sıfat, başvuru yolu tüketme) kısa kontrol listesi.
- Bir sonraki uzman beceriye yönlendirme (ör. sınırlama testi, eşitlik, bireysel başvuru).

## Plugin bağlamı

Bu beceri `anayasa-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
