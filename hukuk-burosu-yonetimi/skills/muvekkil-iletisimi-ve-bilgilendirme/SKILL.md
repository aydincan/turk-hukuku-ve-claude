---
name: muvekkil-iletisimi-ve-bilgilendirme
description: "Müvekkili dosyanın seyri, riskleri ve seçenekleri hakkında bilgilendirme yazısı veya teklif/kapsam mektubu (engagement letter) hazırlanırken ve beklenti yönetimi gerektiğinde kullanılır."
---

# Müvekkil İletişimi ve Bilgilendirme

## Görev
Müvekkili dosyanın durumu, hukuki riskler, olası sonuçlar, süreler ve maliyetler hakkında sade ve doğru biçimde bilgilendirmek; beklentiyi yönetmek ve önemli kararları yazılı onaya bağlamak.

## Soğuk başlangıç (intake)
1. Bilgilendirmenin konusu ne (yeni iş teklifi, gelişme bildirimi, strateji kararı, olumsuz haber)?
2. Müvekkilin hukuki bilgi düzeyi ve tercih ettiği dil/ton nedir?
3. Müvekkilden bir karar/onay isteniyor mu (örn. sulh teklifi, kanun yoluna başvurma)?
4. Aktarılacak risk veya maliyet kalemleri neler?

## Denetim şeması
1. **Özen ve sadakat (TBK m.506; 1136 özen yükümü)**: Müvekkile dürüst, gerçekçi ve zamanında bilgi verilir; başarı garantisi verilmez, riskler gizlenmez.
2. **Kapsam netliği**: Engagement/kapsam mektubunda işin sınırı, dahil olmayan işler ve varsayımlar yazılır.
3. **Risk ve seçenek sunumu**: Her seçenek için olası sonuç, süre, maliyet ve risk dengeli biçimde aktarılır; karar müvekkilindir.
4. **Karar onayı**: Kritik kararlar (sulh, davadan feragat, kanun yolundan vazgeçme) yazılı talimata bağlanır (talimata uyma — TBK m.505); bu hem müvekkili korur hem de avukatın sorumluluğunu sınırlar.
5. **Sır ve gizlilik (1136 m.36)**: İletişim kanalı ve içeriği sır kapsamında; üçüncü kişilere paylaşım yapılmaz.
6. **Ara sonuç**: Doğru bilgi + dengeli risk + gereken yerde yazılı onay sağlanmışsa bilgilendirme tamamdır.

## Çıktı modülleri
- Müvekkil bilgilendirme/gelişme yazısı (sade dil).
- Kapsam/teklif mektubu (engagement letter) taslağı.
- Karar onay formu ([doldurulacak] seçenek ve sonuçları ile).

## Plugin bağlamı

Bu beceri `hukuk-burosu-yonetimi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
