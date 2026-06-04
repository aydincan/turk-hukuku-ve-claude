---
name: patentlenebilirlik-denetimi
description: "Bir buluşun yenilik, buluş basamağı ve sanayiye uygulanabilirlik şartlarını taşıyıp taşımadığı; patentlenebilir konu olup olmadığı tartışıldığında kullanılır; başvuru stratejisi ve hükümsüzlük analizinin temel beceridir."
---

# Patentlenebilirlik Denetim Şeması

## Görev
Buluşun SMK m.82-83 patentlenebilirlik şartlarını (yenilik, buluş basamağı, sanayiye uygulanabilirlik) ve konu istisnalarını adım adım denetleyerek belge alabilirlik/ayakta kalabilirlik değerlendirmesi yapmak.

## Soğuk başlangıç (intake)
1. Buluşun çözdüğü teknik sorun ve teknik çözüm (istemler) nedir?
2. Başvuru/rüçhan tarihi ne; bu tarihten önce kamuya açıklama (sergi, yayın, satış, sunum) oldu mu?
3. En yakın bilinen teknik (prior art) ve fark nedir; araştırma raporu var mı?
4. Konu yazılım, iş yöntemi, tedavi usulü gibi istisnaya girer mi?

## Denetim şeması
1. **Konu denetimi.** SMK m.82/2-3: keşif, teori, matematiksel yöntem, estetik yaratma, iş yöntemi, bilgisayar programı "bu unsurlara ilişkin olduğu ölçüde" patentlenemez; m.82/3 kamu düzeni/ahlak, bitki-hayvan çeşitleri, insan/hayvan tedavi ve teşhis usulleri. Teknik katkı varsa istisna aşılabilir. Ara sonuç: konu patentlenebilir mi?
2. **Yenilik (SMK m.83/1-2).** Tekniğin bilinen durumu, başvuru/rüçhan tarihinden önce dünyada yazılı/sözlü/kullanım yoluyla erişilebilir kılınan her şeydir. Tek bir önceki belge istemin tüm özelliklerini içeriyorsa yenilik yok. Buluş sahibinin önceki açıklaması için m.84 grace period (12 ay) kontrol et.
3. **Buluş basamağı (SMK m.83/4).** İlgili alanda uzman kişiye göre tekniğin bilinen durumundan aşikâr çıkarılamama. Problem-çözüm yaklaşımı: en yakın teknik → objektif teknik problem → çözüm aşikâr mı? Faydalı modelde bu şart aranmaz.
4. **Sanayiye uygulanabilirlik (SMK m.83/6).** Tarım dahil sanayide üretilebilir/kullanılabilir olma.
5. **Yeterli açıklama (SMK m.92/4).** Tarifname, uzmanın buluşu uygulayabileceği açıklıkta olmalı; aksi halde belge alınsa da hükümsüzlük sebebi (m.138/1-b).

## Çıktı modülleri
- Şart şart patentlenebilirlik değerlendirmesi (geçti/geçmedi gerekçeli).
- Prior art - istem eşleştirme tablosu (yenilik/buluş basamağı için).
- Konu istisnası ve grace period notu.
- Belge alabilirlik / hükümsüzlük riski skoru.

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
