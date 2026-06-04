---
name: genel-hukumlerin-kiyasen-uygulanmasi-tmk-5
description: "Bir özel hukuk ilişkisinde doğrudan hüküm bulunmadığında, TMK ve TBK genel hükümlerinin bu ilişkiye kıyasen uygulanıp uygulanamayacağı tartışıldığında TMK m.5 köprüsünü kurmak için kullanılır."
---

# Genel Hükümlerin Kıyasen Uygulanması (TMK m.5)

## Görev
TMK ve TBK'nın genel nitelikli hükümlerinin, başka bir özel hukuk ilişkisine (aile, miras, eşya, ticaret, fikrî haklar) "uygun düştüğü ölçüde" kıyasen uygulanıp uygulanamayacağını belirlemek.

## Soğuk başlangıç (intake)
- Eldeki ilişkiyi düzenleyen özel hüküm gerçekten yok mu (önce o aranır)?
- Taşınmak istenen hüküm "genel nitelikli" mi, yoksa kendi alanına özgü istisnai bir hüküm mü?
- Hükmün amacı (ratio) eldeki ilişkiye uygun düşüyor mu, yoksa niteliği engelliyor mu?
- İlişki TBK genel hükümlerine zaten tabi mi (ör. borç ilişkisiyse doğrudan uygulanır, kıyasa gerek yok)?

## Denetim şeması
1. **Köprü hükmü** — TMK m.5: TMK ve TBK'nın genel nitelikli hükümleri, *uygun düştükleri ölçüde* tüm özel hukuk ilişkilerine uygulanır. Bu, doğrudan uygulama değil, kıyasen (analojik) uygulamadır.
2. **Önce boşluk kontrolü** — İlişkiyi düzenleyen özel norm varsa m.5 devreye girmez. Boşluk gerçek mi (kural yok) yoksa bilinçli susma mı (a contrario) ayrılır.
3. **"Genel nitelik" testi** — Taşınacak hüküm, yalnızca borç ilişkilerine özgü teknik bir kural değil, tüm özel hukuka yayılabilecek genel bir ilke içermeli (ör. temsil, ehliyet, irade sakatlığı, ifa, temerrüt ilkeleri). İstisnai/özel amaçlı hükümler kural olarak taşınmaz.
4. **"Uygun düşme" testi** — Hükmün amacı eldeki ilişkinin niteliğiyle bağdaşmalı; aile/miras gibi kişiye sıkı bağlı alanlarda borçlar hukuku mantığı her zaman taşınmaz (ör. irade sakatlığı hükümleri evlenme/vasiyette kendi özel rejimine tabidir).
5. **Sonuç** — Şartlar sağlanırsa genel hükmün sonucu, gerekli uyarlamayla eldeki ilişkiye uygulanır; sağlanmazsa TMK m.1 sırasına (örf-âdet, hâkimin hukuk yaratması) geçilir.

## Çıktı modülleri
- Boşluk tespiti (özel norm var/yok).
- Taşınacak hükmün "genel nitelik" ve "uygun düşme" analizi.
- Kıyasen uygulama sonucu + gerekli uyarlama.
- Uygulanamazsa m.1 yönlendirmesi + ilkesel içtihat `[doğrulanacak]`.

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
