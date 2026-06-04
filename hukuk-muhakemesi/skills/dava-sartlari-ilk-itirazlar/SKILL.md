---
name: dava-sartlari-ilk-itirazlar
description: "Bir davanın esastan görülmeden usulden reddedilip reddedilemeyeceğini, dava şartı eksikliği mi yoksa ilk itiraz mı söz konusu olduğunu tespit etmek; husumet, hukuki yarar, derdestlik, kesin hüküm, yetki itirazı gibi başlıkları taramak için."
---

# Dava Şartları ve İlk İtirazlar Denetimi

## Görev
Davanın esasa geçmeden önce aşması gereken eşikleri taramak; dava şartı (re'sen, her aşamada) ile ilk itiraz (süresinde ve ön incelemede) ayrımını net kurmak.

## Soğuk başlangıç (intake)
- Davalı/davacı taraf sıfatı (husumet) doğru mu?
- Aynı dava başka mahkemede derdest mi, kesin hüküm var mı?
- Yetki/tahkim itirazı geç kalmamış mı (cevap süresi içinde mi)?
- Dava şartı arabuluculuk gerekiyorsa son tutanak dosyada mı?

## Denetim şeması
1. **Dava şartları** (HMK m.114): yargı yolu, görev, taraf ve dava ehliyeti, davayı takip yetkisi, hukuki yarar (m.114/1-h), derdestlik (m.114/1-ı), kesin hüküm (m.114/1-i), gider avansı (m.114/1-g, m.120). Bunlar **re'sen** ve yargılamanın **her aşamasında** gözetilir (m.115). Eksiklik giderilebilir nitelikteyse süre verilir (m.115/2); değilse dava usulden reddedilir.
2. **İlk itirazlar** (m.116): kesin yetki dışındaki yetki itirazı, tahkim itirazı, iş bölümü (görev kalıntısı) itirazları. Bunlar **yalnızca cevap dilekçesinde** ve hepsi birlikte ileri sürülür (m.117); ön incelemede karara bağlanır. Süresinde ileri sürülmezse dinlenmez.
3. **Husumet (sıfat)**: Maddi hukuka ilişkin taraf sıfatı eksikliği dava şartı değil, esastan ret sebebidir; ancak ön incelemede erken teşhis hak kaybını önler.
4. **Hukuki yarar**: Eda davası açılabilecekken tespit davası açılması, muaccel olmayan alacak gibi hallerde yarar yokluğu usulden redde götürür.
5. **Dava şartı arabuluculuk**: Ticari (TTK m.5/A), iş, tüketici ve genişleyen kapsamda son tutanak yoksa dava usulden reddedilir; kapsam mevzuattan teyit edilir.

Ara sonuç: Her bir başlık için "var / yok / giderilebilir / itiraz süresi geçti" etiketi çıkar.

## Çıktı modülleri
- Dava şartı kontrol listesi (madde atıflı, durum etiketli).
- İlk itiraz değerlendirmesi (süre tutmuş mu, hangileri birlikte ileri sürülmüş).
- Usulden ret riski ve giderme yolu önerisi.

## Plugin bağlamı

Bu beceri `hukuk-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
