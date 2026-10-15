---
name: fesih-sona-erme-ve-cikis
description: "Fesih sebepleri, bildirimli/haklı fesih, dönme-fesih ayrımı, otomatik yenileme ve sözleşme sonrası yükümlülükler incelendiğinde kullanılır."
---

# Fesih, Sona Erme ve Çıkış Hükümleri

## Görev
Sözleşmenin nasıl ve hangi sonuçlarla sona ereceğini denetlemek; fesih haklarının dengesini, bildirim usulünü, geçmişe/ileriye etki ayrımını ve çıkış sonrası yükümlülükleri belirlemek.

## Soğuk başlangıç (intake)
- Sözleşme ani edimli mi (dönme) yoksa sürekli mi (ileriye etkili fesih)?
- Fesih hakları kimde, tek taraflı mı; bildirim süresi/şekli ne?
- Haklı sebeple derhal fesih ve sözleşmeden dönme şartları net mi?
- Sona erme sonrası gizlilik, rekabet yasağı, iade, devir yükümlülükleri var mı?

## Denetim şeması
1. **Dönme/fesih ayrımı**: Ani edimli sözleşmede temerrüt hâlinde TBK m.125 — alacaklı ya ifa+gecikme tazminatı, ya ifadan vazgeçip müspet zarar, ya da dönüp menfi zarar isteyebilir. Sürekli borç ilişkisinde sona erme kural olarak **ileriye etkilidir** (fesih), geçmiş tasfiye edilmez.
2. **Haklı sebeple fesih**: Sürekli ilişkilerde dürüstlük kuralı gereği haklı/önemli sebeple derhal fesih hakkı emredici nitelikte kabul edilir; sözleşmeyle tümüyle kaldırılamaz. Tetikleyiciler somut ve ölçülebilir yazılmalı.
3. **Bildirim usulü**: Süre, şekil (yazılı/noter/KEP), ihtar şartı (TBK m.117 temerrüt için, kira/eser özel hükümleri) ve "cure period" (düzeltme süresi) denetlenir.
4. **Otomatik yenileme/erken çıkış**: Sessiz yenileme, asgari taahhüt süresi ve erken fesih cezası (cezai şart denetimine bağlanır) müvekkil aleyhineyse işaretlenir.
5. **Sona erme sonuçları**: İade, hesap kapama, lisans/erişim sonlandırma, geçiş desteği; ayakta kalan hükümler (survival): gizlilik, rekabet yasağı (ölçülülük: süre-yer-konu), sorumluluk, uyuşmazlık.
6. **İspat/usul**: Fesih sebebini ve usulüne uygunluğunu fesheden taraf ispatlar; haksız fesih müspet zarar doğurabilir.

## Çıktı modülleri
- Fesih hakları denge tablosu (kim, hangi sebeple, hangi usulle).
- Bildirim ve düzeltme süresi (cure) lafız önerisi.
- Survival (ayakta kalan hüküm) ve çıkış yükümlülükleri kontrol listesi.

## Plugin bağlamı

Bu beceri `sozlesme-inceleme-redline` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
