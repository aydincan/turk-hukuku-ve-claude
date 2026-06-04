---
name: mulkiyet-ve-kamulastirma
description: "Mülkiyet hakkına (m.35) yönelik bir müdahalenin, kamulaştırmanın veya fiili el atmanın anayasaya uygunluğunu ve giderim boyutunu değerlendirmek; kamu yararı, kanunilik ve adil denge analizinin gerektiği hallerde kullanılır."
---

# Mülkiyet Hakkı ve Kamulaştırma

## Görev
Mülkiyet hakkına (Anayasa m.35, AİHS Ek 1 No.lu Protokol m.1) yönelik müdahaleleri — kamulaştırma (m.46), idari kısıtlama, fiili/hukuki el atma — anayasal çerçevede denetlemek ve giderim/tazminat boyutunu değerlendirmek.

## Soğuk başlangıç (intake)
1. Mülkiyet konusu ne (taşınmaz, taşınır, ekonomik değer/alacak) ve müdahale türü hangisi?
2. Usulüne uygun bir kamulaştırma işlemi mi, yoksa fiili/hukuki el atma mı söz konusu?
3. Müdahalenin dayandığı kamu yararı kararı ve kanuni dayanak var mı?
4. Bedel/tazminat ödendi mi, ödenecekse hangi usulle belirleniyor?

## Denetim şeması
1. **Mülk kavramı.** Mevcut mal, meşru beklenti ve ekonomik değer taşıyan alacaklar koruma alanındadır. Ara sonuç: koruma alanında mıyız?
2. **Müdahale türünü ayır.** (a) Mülkiyetten yoksun bırakma (kamulaştırma), (b) kullanımın düzenlenmesi (imar kısıtı vb.), (c) genel müdahale. Tür, denetim yoğunluğunu belirler.
3. **Kanunilik.** Müdahale erişilebilir ve öngörülebilir bir kanuna dayanmalı (m.13, m.35). Kamulaştırmada 2942 sayılı Kamulaştırma Kanunu usulüne uygunluk aranır.
4. **Kamu yararı.** Müdahale gerçek ve meşru bir kamu yararına dayanmalı; m.46 kamulaştırmada kamu yararı kararı şarttır.
5. **Adil denge / ölçülülük.** Bireysel yük ile kamu yararı arasında orantı kurulmalı; m.46 gerçek karşılığın (bedelin) peşin ve nakden ödenmesini öngörür. Karşılıksız ya da fahiş düşük bedelle el atma adil dengeyi bozar.
6. **Fiili/hukuki el atma.** İdarenin kamulaştırmasız el atması hukuka aykırıdır; bedel davası ve el atmanın önlenmesi yolları gündeme gelir. İmar kısıtlamasının süresiz/karşılıksız sürmesi (hukuki el atma) ayrı denetlenir.
İspat: müdahaleyi malik, kamu yararı ve usule uygunluğu idare gösterir. AYM/AİHM mülkiyet içtihadına ilke düzeyinde atıf yapın; künyeyi `[doğrulanacak]` işaretleyin.

## Çıktı modülleri
- Müdahale türü nitelendirmesi ve uygulanacak denetim yoğunluğu.
- Kanunilik-kamu yararı-adil denge değerlendirme tablosu.
- Bedel/giderim yolu ve dava türü (idari/adli) önerisi.

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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
