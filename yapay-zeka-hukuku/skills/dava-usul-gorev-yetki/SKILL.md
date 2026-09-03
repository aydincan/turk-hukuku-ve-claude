---
name: dava-usul-gorev-yetki
description: "Yapay zekâ kaynaklı bir uyuşmazlık yargıya veya Kurula taşınırken görevli merci, yetkili mahkeme, başvuru yolu, dava türü, ihtiyati tedbir ve süreler belirlendiğinde ve usul yol haritası çıkarıldığında kullanılır."
---

# Yapay Zekâ Uyuşmazlıklarında Dava, Usul ve Görev-Yetki

## Görev
Yapay zekâ kaynaklı uyuşmazlıkta doğru merci, dava türü, yetkili mahkeme ve süreyi tespit ederek usul yol haritası ve gerekirse ihtiyati tedbir stratejisi çıkarmak.

## Soğuk başlangıç (intake)
1. Uyuşmazlığın özü: KVKK ihlali, sözleşmeye aykırılık, haksız fiil/tazminat, fikri hak, kamu işlemi?
2. Taraflar tacir/tüketici mi; aralarında tahkim veya yetki sözleşmesi var mı?
3. Bir Kurul/idare işlemi mi tebliğ edildi, tebliğ tarihi nedir?
4. Acil koruma (içerik kaldırma, delil tespiti, yürütmenin durdurulması) gerekiyor mu?

## Denetim şeması
1. **Yol ayrımı**: KVKK ihlalinde önce m.13 veri sorumlusuna başvuru, ardından m.14 Kurula şikâyet; Kurul kararına karşı idari yargı (İYUK m.7, kural 60 gün). Tazminat talebi için adli yargıda dava (TBK temelli). Ara sonuç: idari mi adli mi.
2. **Görev-yetki (adli)**: Sözleşme/haksız fiilde HMK genel hükümleri (m.5 vd.); ticari işte ticaret mahkemesi (TTK m.4, m.5/A dava şartı arabuluculuk); tüketici işleminde tüketici mahkemesi/hakem heyeti (6502); fikri hakta FSHM; kişilik hakkında asliye hukuk.
3. **Dava türü ve talep**: Tespit, eda (tazminat), men/ref (kişilik hakkı TMK m.25, FSEK m.66-67) veya iptal (kamu işlemi). Talep sonucu net ve HMK m.119 unsurlarıyla kurulur.
4. **İhtiyati koruma**: HMK m.389 vd. ihtiyati tedbir (içerik/erişim), m.400 vd. delil tespiti (model çıktısı/log), kamu işleminde İYUK m.27 yürütmenin durdurulması.
5. **İspat ve bilirkişi**: YZ uyuşmazlıkları teknik bilirkişi gerektirir (HMK m.266); log, model dokümanı ve çıktı kayıtları erkenden güvenceye alınmalı.

İçtihat ve görev tartışmaları için karararama portalları; künyeyi [doğrulanacak] işaretle, esas/karar numarası uydurma.

## Çıktı modülleri
- Merci/dava türü/süre yol haritası.
- İhtiyati tedbir-delil tespiti stratejisi.
- Görev-yetki ve arabuluculuk kontrol notu.

## Plugin bağlamı

Bu beceri `yapay-zeka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
