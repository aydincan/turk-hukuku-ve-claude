---
name: kat-karsiligi-insaat-ve-imar
description: "Arsa payı karşılığı (kat karşılığı) inşaat sözleşmesi ile imar süreçleri kesiştiğinde; ruhsat-iskân yükümlülükleri, ayıplı/eksik ifa, gecikme ve sözleşmenin imar engeline takılması gündeme geldiğinde kullanılır."
---

# Kat Karşılığı İnşaat ve İmar Kesişimi

## Görev
Kat karşılığı inşaat sözleşmesinin imar boyutuyla (ruhsat, iskân, projeye uygunluk) kesişen yükümlülüklerini analiz etmek ve ihtilafta tarafların pozisyonunu kurmak.

## Soğuk başlangıç (intake)
- Sözleşme tarihi, paylaşım oranı ve teslim süresi ne?
- Ruhsat alındı mı, inşaat ruhsata/projeye uygun mu, iskân var mı?
- Gecikme, eksik veya ayıplı ifa ya da imar engeli (plan değişikliği, durdurma) var mı?
- Tapu/arsa payı devri ve kat irtifakı kuruldu mu?

## Denetim şeması
1. **Sözleşmenin niteliği ve şekli**: Kat karşılığı inşaat, eser ve gayrimenkul satış vaadi unsurlarını birleştiren karma sözleşmedir; taşınmaz devri içerdiğinden **resmî şekilde (düzenleme şeklinde, noterde)** yapılması gerekir (TBK m.237, TMK tapu şekli). Şekil eksikliği ve ifa ilişkisi (TMK m.2) tartışılır.
2. **Yüklenicinin imar yükümü**: Yüklenici, **ruhsata ve onaylı projeye uygun** yapı yapmak, iskân almakla yükümlüdür; ruhsatsız/projeye aykırı imalat hem idari yaptırım (3194 m.32, m.42) hem sözleşmesel ayıp/eksik ifa doğurur (TBK m.474 vd. eser hükümleri).
3. **İmar engeli ve imkânsızlık**: Sözleşme sonrası plan değişikliği, emsal düşüşü veya inşaat durdurma yükümün ifasını etkilerse, kusur ve **uyarlama/imkânsızlık** (TBK m.136, m.138) çerçevesinde risk dağıtımı yapılır.
4. **Gecikme ve gecikme tazminatı**: Teslim süresinin geçmesi temerrüt doğurur; cezai şart, kira kaybı/gecikme tazminatı ve arsa sahibinin seçimlik hakları (aynen ifa, dönme) değerlendirilir.
5. **Yargı kolu ve ispat**: Sözleşme uyuşmazlığı **adli yargıda (asliye hukuk)**; imar işlemleri (ruhsat/yıkım/ceza) idari yargıda. Ruhsat, iskân, hakediş, bilirkişi (inşaat mühendisi) ve fiziki tespit delildir. Eksik/ayıbı arsa sahibi, ifa engelini ileri sürerse yüklenici ispatlar.
6. **Ara sonuç**: İmar boyutu (ruhsat/iskân) ile sözleşmesel ifa birlikte değerlendirilip, ifa/dönme/tazminat seçenekleri ve idari risk müvekkile sunulur. Yargıtay 15./23. HD ilkesel atıfları `[doğrulanacak]`.

## Çıktı modülleri
- Sözleşme-imar yükümlülük haritası.
- Ruhsat/iskân ve projeye uygunluk denetim notu.
- İmar engeli/uyarlama risk değerlendirmesi.
- İfa/dönme/tazminat seçenek tablosu ve ihtar/dava taslağı.

## Plugin bağlamı

Bu beceri `imar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
