---
name: aydinlatma-yukumlulugu
description: "Aydınlatma metni hazırlanırken, mevcut metnin KVKK m.10 ve Tebliğ'e uygunluğu denetlenirken veya aydınlatmanın açık rızadan ayrı tutulması gerektiğinde kullanılır."
---

# Aydınlatma Yükümlülüğü ve Metin Tasarımı

## Görev
KVKK m.10 ve Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ uyarınca aydınlatma metni üretmek veya mevcut metni denetlemek; aydınlatmayı açık rızadan ve diğer belgelerden ayrı, doğru zamanlamayla kurmak.

## Soğuk başlangıç (intake)
1. Aydınlatma hangi kanaldan, hangi anda yapılacak (web formu, işe alım, sözleşme imzası, çağrı merkezi)?
2. Hangi veri kategorileri ve işleme amaçları söz konusu?
3. Aktarım var mı; varsa kime ve hangi amaçla?
4. Aynı süreçte açık rıza da alınacak mı (ayrı belge gerekir)?

## Denetim şeması
1. **Zorunlu içerik — m.10/1**: (a) veri sorumlusunun ve varsa temsilcisinin kimliği, (b) işleme amacı, (c) aktarılabileceği alıcı/alıcı grupları ve amacı, (ç) toplama yöntemi ve hukuki sebebi, (d) m.11'deki haklar. Tebliğ bunların somut ve açık biçimde sayılmasını ister; "vb.", "gerektiğinde" gibi muğlak ifadeler eksiklik sayılır.
2. **Zamanlama**: Aydınlatma, verinin elde edilmesi sırasında yapılır; sonradan yapılan aydınlatma yükümlülüğü ihlal eder.
3. **Açık rızadan ayrılık**: Tebliğ m.5 gereği aydınlatma ile açık rıza tek metinde/tek onayda birleştirilemez; aydınlatma rıza şartına bağlanamaz (aydınlatma her hâlde zorunludur, rıza ise koşullu).
4. **Hukuki sebebin doğru gösterimi**: Metinde m.5/m.6'daki sebep, genel "açık rıza" ifadesiyle değil, işleme bazında gösterilmelidir.
5. **Ara sonuç**: Eksik veya geç aydınlatma m.18/1-a kapsamında idari para cezası riskidir; metin her işleme amacına göre güncellenmelidir.

İspat yükü: Aydınlatmanın usulüne uygun ve zamanında yapıldığını veri sorumlusu ispatlar; bu nedenle kayıt/onay logu tutulmalıdır.

## Çıktı modülleri
- m.10 unsurlarına göre yapılandırılmış aydınlatma metni taslağı ([doldurulacak] yer tutucularıyla).
- Aydınlatma-açık rıza ayrımı kontrol listesi.
- Kanal bazlı aydınlatma matrisi (web, işe alım, müşteri, ziyaretçi).

## Plugin bağlamı

Bu beceri `kvkk-veri-koruma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
