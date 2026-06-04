---
name: durustluk-risk-strateji
description: "Bir talebin veya savunmanın yalnızca TMK m.2/m.3 gibi esnek başlangıç hükümlerine dayandığı hâllerde; bu argümanın gücünü, başarı olasılığını ve alternatif dayanakları tartmak için kullanılır."
---

# Başlangıç Hükümleri Temelli Risk ve Strateji Değerlendirmesi

## Görev
Dürüstlük kuralı, hakkın kötüye kullanılması veya iyiniyet gibi esnek/takdire açık başlangıç hükümlerine dayanan bir argümanın gerçekçi başarı şansını değerlendirmek; daha sağlam alternatif dayanakları ve ispat risklerini ortaya koymak.

## Soğuk başlangıç (intake)
- Argüman *yalnızca* başlangıç hükmüne mi dayanıyor, yoksa daha güçlü bir özel norm da var mı?
- Başlangıç hükmünün şartları (özellikle m.2/2 "açıklık" eşiği) somut olayda gerçekten karşılanıyor mu?
- İspat yükü (m.6) bizde mi; ispat araçları yeterli mi?
- Hâkimin takdiri (m.4) ne yöne meyledebilir; emsal eğilim nedir?

## Denetim şeması
1. **Önce sağlam dayanak ara** — Esnek başlangıç hükmü, mümkünse asıl dayanak değil destek olmalıdır. Somut bir özel norm (sözleşme ihlali, ayıp, geçersizlik, mülkiyet) varsa o öne çıkarılır; m.2/m.3 ikincil savunma katmanı tutulur.
2. **"Açıklık" riski** — TMK m.2/2 yalnızca *açık* kötüye kullanmada korur; eşik yüksektir. Sıradan menfaat çatışmasını kötüye kullanma diye sunmak zayıf argümandır ve güven kaybı yaratır.
3. **Takdir belirsizliği — m.4** — Hakkaniyet/takdir alanı sonucu öngörülemez kılar; bu belirsizlik dürüstçe müvekkile aktarılır. Sonuç "tartışmalı / hâkimin takdirine bağlı" diye nitelenir, abartılı kesinlik verilmez.
4. **İspat zafiyeti — m.6** — Çelişkili davranış, güven, kötüniyet gibi vakıaların ispatı güçtür; yazılı delil, yazışma, tanık ve karine durumu envanterlenir. İspatlanamayan vakıa "gerçekleşmemiş" sayılır.
5. **Senaryo ve alternatif** — En iyi/orta/en kötü senaryo; başlangıç hükmü tutmazsa devreye girecek yedek dayanak; sulh/uzlaşma penceresi. İçtihat eğilimi tek cümlede dürüstçe (lehe karar seçip aleyhe gizlemeden) özetlenir.
6. **Etik sınır** — Zayıf bir m.2 argümanını "kesin" diye sunmak meslek kurallarına ve dürüst danışmanlığa aykırıdır; risk açıkça paylaşılır.

## Çıktı modülleri
- Dayanak haritası (asıl norm + başlangıç hükmü katmanı).
- Şart/eşik ve ispat riski değerlendirmesi.
- Senaryo tablosu (iyi/orta/kötü) + olasılık nitelemesi.
- Yedek strateji + sulh penceresi + ilkesel içtihat eğilimi `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `medeni-hukuk-baslangic` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
