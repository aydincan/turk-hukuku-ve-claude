---
name: dilekce-ve-belge-taslaklari
description: "Genel kurul cevresinde gerekli olan cagri metni, gundem, vekaletname, tutanak, muhalefet serhi, iptal dava dilekcesi ve ihtarname gibi belgelerin yer tutucu disipliniyle taslaklari uretilecekse kullanilir."
---

# Dilekçe ve Belge Taslakları

## Görev
Genel kurul sürecinin tüm belge ihtiyaçlarını — çağrı, gündem, vekâletname, tutanak, muhalefet şerhi, iptal/butlan dilekçesi, ihtarname — usule uygun ve `[doldurulacak]` yer tutucu disipliniyle üretmek.

## Soğuk başlangıç (intake)
1. Hangi belge isteniyor (toplantı öncesi/anı/sonrası)?
2. Şirket ve taraf bilgileri (unvan, MERSİS, merkez, pay oranları) elde mevcut mu?
3. Görevli/yetkili mahkeme ve süre durumu nedir (dava belgeleri için)?
4. Elektronik genel kurul/Bakanlık temsilcisi gibi özel gereklilik var mı?

## Denetim şeması
1. **Belge-norm eşleştirmesi:** Her belgeyi dayandığı maddeyle bağla — çağrı/gündem (m.413-414), vekâletname (m.425), hazır bulunanlar listesi (m.415), tutanak (m.422), muhalefet şerhi (m.446/1-b), iptal dilekçesi (m.445-448), azlık ihtarı (m.411).
2. **Dava dilekçesi mimarisi:** İptal/butlan dilekçesinde HMK m.119 zorunlu unsurları eksiksiz olmalı: taraflar, dava konusu, vakıalar (toplantı kronolojisi), hukuki sebepler (TTK m.445/447), deliller (tutanak, hazır bulunanlar listesi, TTSG ilanı), talep sonucu (kararın iptali/butlanın tespiti). Görevli mahkeme: asliye ticaret (TTK m.5); yetkili: şirket merkezi (m.448).
3. **Yer tutucu disiplini:** Doğrulanamayan her veri köşeli parantezle işaretlenir: `[karar tarihi]`, `[pay oranı]`, `[muhalefet şerhi metni]`. Uydurma tarih/oran/künye yazılmaz.
4. **İçtihat hijyeni:** Dilekçede ilkesel atıf yapılır; Yargıtay 11. HD kararları için künye `[doğrulanacak]` bırakılır ve karararama.yargitay.gov.tr kaynağı anılır. Sahte esas/karar numarası asla yazılmaz.
5. **İspat/delil bağlama:** Her vakıa, dilekçede onu ispatlayan belgeyle (tutanak madde no, ilan tarihi) eşleştirilir; ispat yükü TMK m.6 ve HMK çerçevesinde dağıtılır.
6. **Ara sonuç:** Belge teslimden önce süre (üç ay), davacı sıfatı (muhalefet şerhi) ve görev-yetki yeniden kontrol edilir.

## Çıktı modülleri
- İstenen belgenin tam taslağı (başlık-imza blokları dahil).
- Eksik bilgi listesi (`[doldurulacak]` envanteri).
- Sonraki adım ve süre uyarısı.

## Plugin bağlamı

Bu beceri `anonim-sirket-genel-kurul` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
