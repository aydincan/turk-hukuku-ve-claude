---
name: sureler-zamanasimi-usul
description: "Cevap, istinaf, temyiz, ıslah, görevsizlik gönderme gibi usul sürelerini ve maddi hukuk zamanaşımı/hak düşürücü sürelerini doğru hesaplamak; adli tatil, tebligat ve tatil günü etkisini dikkate almak için."
---

# Usul Süreleri, Hak Düşürücü Süreler ve Zamanaşımı

## Görev
Dosyadaki tüm süreleri (usuli + maddi hukuk) tarihleriyle hesaplamak; tebligat, adli tatil ve son günün tatile gelmesi etkilerini katarak hak kaybını önlemek.

## Soğuk başlangıç (intake)
- Hangi belge ne zaman tebliğ edildi (UYAP/tebliğ tarihi)?
- Süre hangi olaya bağlı (tebliğ, öğrenme, hak doğumu)?
- Süre adli tatile (20 Temmuz-31 Ağustos) denk geliyor mu?
- Maddi hukuk talebinde zamanaşımı/hak düşürücü süre durumu ne?

## Denetim şeması
1. **Sürenin başlangıcı** (HMK m.91-92): Süreler tebliğ veya kanunun belirttiği olayla işlemeye başlar; başladığı gün sayılmaz.
2. **Sürenin sonu** (m.92-93): Süre son günün tatil gününe rastlaması halinde ilk iş gününe uzar (m.93).
3. **Adli tatil** (m.102-104): 20 Temmuz-31 Ağustos arası; adli tatilde görülecek işler (m.103) dışındaki sürelerin bitimi tatili izleyen tarihten itibaren bir hafta uzar (m.104).
4. **Tipik usul süreleri**: cevap iki hafta (m.127); istinaf iki hafta, gerekçeli kararın tebliğinden (m.345); temyiz iki hafta (m.361); görevsizlik/yetkisizlik sonrası gönderme talebi iki hafta (m.20); ıslah tahkikat sonuna kadar bir kez (m.176-177). Süreler kanunla belirlenmişse hâkim değiştiremez (m.90).
5. **Eski hâle getirme** (m.95-101): Kusursuz olarak süre kaçırılmışsa, engelin kalkmasından itibaren iki hafta içinde talep edilebilir.
6. **Maddi hukuk süreleri**: Zamanaşımı **def'i** olarak ileri sürülür (cevapta), hak düşürücü süre re'sen gözetilir. İlgili kanundaki süre (ör. TBK genel zamanaşımı m.146; haksız fiil m.72) ayrıca kontrol edilir.

Ara sonuç: Tarihli süre takvimi ve "son gün" listesi.

## Çıktı modülleri
- Süre takvimi (olay → başlangıç → son gün, adli tatil düzeltmeli).
- Kaçırılan süre varsa eski hâle getirme değerlendirmesi.
- Zamanaşımı/hak düşürücü süre uyarısı (def'i ileri sürme hatırlatması).

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
