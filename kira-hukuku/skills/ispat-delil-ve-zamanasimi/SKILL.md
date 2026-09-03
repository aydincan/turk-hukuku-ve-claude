---
name: ispat-delil-ve-zamanasimi
description: "Kira uyuşmazlığında hangi delillerin gerekli olduğu, ispat yükünün kimde olduğu, senetle ispat zorunluluğu veya kira alacağı ve diğer taleplerde zamanaşımı süreleri tartışıldığında bu beceriyi kullan."
---

# İspat, Delil ve Zamanaşımı

## Görev
Kira uyuşmazlığında ispat yükünü dağıtmak, gerekli delilleri belirlemek ve uygulanabilir zamanaşımı sürelerini saptamak; delil planını talep türüne göre kurmak.

## Soğuk başlangıç (intake)
- Çekişmeli vakıa ne (ödeme, ihtar, ayıp, ihtiyaç)?
- Elde hangi yazılı belgeler var (sözleşme, makbuz, banka, ihtar)?
- Talep türü ne ve doğum tarihi/dönemi?
- Karşı tarafın savunması/def'ileri biliniyor mu?

## Denetim şeması
1. **İspat yükü (HMK m.190; TMK m.6)**: Bir vakıadan kendi lehine hak çıkaran onu ispatla yükümlüdür. Kiraya veren ihtar/temerrüt/ihtiyaç vakıasını; kiracı ödemeyi, taahhüdün geçersizliğini ispatlar.
2. **Senetle ispat (HMK m.200-201)**: Belirli parasal sınırı aşan hukuki işlemler senetle ispatlanır; senede/yazılı sözleşmeye karşı tanık dinlenemez (istisnalar saklı). Ödeme banka kaydı/makbuzla; ihtar noter belgesiyle ispatlanır.
3. **Delil türleri**: Yazılı sözleşme, kira ve aidat ödeme kayıtları, noter ihtarnameleri, tahliye taahhüdü, keşif-bilirkişi (ayıp/emsal kira), tanık (sınırlar dahilinde).
4. **Zamanaşımı**: Kira bedeli alacağı **beş yıllık** zamanaşımına tabidir (TBK m.147/1 — kira bedelleri). Diğer sözleşme kaynaklı tazminat/iade talepleri kural olarak **on yıl** (TBK m.146); haksız fiil benzeri talepler için ayrı süreler. Tahliye davaları zamanaşımına değil, ilgili **hak düşürücü** dava sürelerine (m.351, m.353) tabidir.
5. **Ara sonuç**: Çekişmeli vakıa-ispat yükü-delil eşleştirmesi + uygulanabilir zamanaşımı/hak düşürücü süre.

## Çıktı modülleri
- Delil matrisi (vakıa / yük / delil / durum).
- Zamanaşımı-hak düşürücü süre tablosu.
- Delil toplama/sunma eylem listesi.

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
