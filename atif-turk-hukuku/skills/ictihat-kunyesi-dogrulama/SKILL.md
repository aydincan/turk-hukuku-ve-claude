---
name: ictihat-kunyesi-dogrulama
description: "Bir karara atıf yapılacağında ya da metinde geçen bir karar künyesinin gerçekliği şüpheliyse; mahkeme-daire-esas-karar-tarih bilgisini doğru biçimde kurmak ve resmî kaynaktan doğrulamak için kullanılır."
---

# İçtihat Künyesi ve Doğrulama

## Görev
Bir yargı kararına usulüne uygun, eksiksiz ve doğrulanmış bir künye ile atıf yapmak; doğrulanamayan künyeyi uydurmak yerine açıkça işaretlemek.

## Soğuk başlangıç (intake)
- Hangi mahkeme/daire/kurul (Yargıtay HGK mı, 11. HD mi, Danıştay mı, AYM mi)?
- Elimizde karar metni var mı, yoksa yalnızca ikinci el bir atıf mı?
- Karar tarihi ve E./K. numaraları tam mı, eksik mi?
- Bu karar lehe mi, yoksa karşı tarafın dayanağı mı?

## Denetim şeması
1. **Tam künye şablonu** — Yargıtay: "Yargıtay [Daire/HGK/İBK], E. …/…, K. …/…, T. gg.aa.yyyy". Danıştay: "Danıştay [Daire/İDDK/VDDK], E. …, K. …, T. …". AYM: norm denetimi "AYM, E. …/…, K. …/…, T. …"; bireysel başvuru "AYM, B. No: …/…, T. …". AİHM: "Taraflar/Türkiye, B. No: …, T. …".
2. **Doğrulama zorunluluğu** — Künye yalnızca karar metni görüldüğünde veya resmî bankadan teyit edildiğinde yazılır: karararama.yargitay.gov.tr, karararama.danistay.gov.tr, kararlarbilgibankasi.anayasa.gov.tr, hudoc.echr.coe.int. **E./K. numarası, daire ve tarih model hafızasından ASLA üretilmez.**
3. **Eksik/şüpheli künye** — Numaranın bir kısmı eksikse veya teyit edilemiyorsa, sayı uydurulmaz; künye `[doğrulanacak]` ile, varsa yalnızca ilke özeti yazılır: "Yargıtay'ın yerleşik içtihadına göre … [künye doğrulanacak]".
4. **İkinci el atıf uyarısı** — Bir dilekçe/makaledeki künye doğrudan kopyalanmaz; asıl metne inilir, çünkü ikinci el atıflarda numara/tarih hatası sıktır.
5. **Künye-içerik tutarlılığı** — Atfedilen ilke, kararın gerçekten kurduğu ilke mi? Vakıası benzer mi? Uyuşmuyorsa karar emsal gösterilmez.

## Çıktı modülleri
- Doldurulmuş künye şablonu (mahkeme türüne göre).
- Doğrulama durumu: teyit edildi / `[doğrulanacak]`.
- Arama sorgusu önerisi (banka adı + anahtar kelime).
- İçerik-künye tutarlılık notu.

## Plugin bağlamı

Bu beceri `atif-turk-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
