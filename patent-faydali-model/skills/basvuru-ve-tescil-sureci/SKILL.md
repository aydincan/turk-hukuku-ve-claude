---
name: basvuru-ve-tescil-sureci
description: "TPMK nezdinde patent veya faydalı model başvurusu hazırlanırken, inceleme/itiraz aşamaları yönetilirken ve rüçhan/dönüştürme kararları verilirken kullanılır; başvuru stratejisi ve süreç yönetimi için temel beceridir."
---

# Patent/Faydalı Model Başvuru ve Tescil Süreci

## Görev
TPMK başvuru dosyasının unsurlarını (SMK m.90-92) hazırlamak, araştırma-inceleme-itiraz aşamalarını yönetmek, rüçhan ve faydalı modele dönüştürme kararlarını planlamak.

## Soğuk başlangıç (intake)
1. Buluş için patent mi faydalı model mi hedefleniyor; teknik alan ne?
2. Yurt dışı öncelik (rüçhan) var mı; PCT/EPC yolu düşünülüyor mu?
3. Tarifname, istemler, özet ve resimler hazır mı; istem stratejisi belirlendi mi?
4. Kamuya açıklama riski/zaman baskısı var mı (grace period)?

## Denetim şeması
1. **Başvuru unsurları (SMK m.90-92).** Başvuru dilekçesi, tarifname, bir veya birden çok istem, özet, gerektiğinde resimler. Başvuru tarihinin kesinleşmesi için asgari unsurlar (m.90) tamam mı? Buluş bütünlüğü (tek genel buluş düşüncesi) sağlanmış mı?
2. **Rüçhan (SMK m.93-94).** Paris Sözleşmesi rüçhanı ilk başvurudan itibaren 12 ay; rüçhan belgesi süresinde sunulmalı. Tarih, yenilik değerlendirmesinin referansını belirler.
3. **Araştırma ve inceleme (patent).** Araştırma raporu talebi, yayım, üçüncü kişi görüşü, esaslı inceleme; patent verme kararı esaslı incelemeye tabidir (SMK m.96-98). Süreleri ve ücretleri takip et.
4. **İtiraz (SMK m.99).** Patentin verilmesi kararına karşı yayımdan itibaren altı ay içinde itiraz; YİDD (Yeniden İnceleme ve Değerlendirme Dairesi) kararı, ardından FSHM'de iptal davası.
5. **Faydalı model özellikleri (SMK m.143-144).** Esaslı inceleme zorunlu değildir ama araştırma raporu düzenlenir; buluş basamağı aranmaz. Patent-faydalı model arası dönüştürme imkânını (m.144) süre koşuluyla değerlendir.

## Çıktı modülleri
- Başvuru unsurları kontrol listesi ve eksik uyarısı.
- Rüçhan ve süre takvimi.
- Araştırma-inceleme-itiraz yol haritası.
- Patent/faydalı model ve dönüştürme strateji notu.

## Plugin bağlamı

Bu beceri `patent-faydali-model` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
