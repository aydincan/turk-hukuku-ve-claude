---
name: sureler-ve-zamanasimi
description: "Kullanıcı dava açma, itiraz, cevap, istinaf gibi sürelerin ne zaman dolacağını veya alacağının zamanaşımına uğrayıp uğramadığını hesaplamak istediğinde kullanılır."
---

# Süreler ve Zamanaşımı Takibi

## Görev
Hak düşürücü süreleri, usul sürelerini ve zamanaşımını tespit edip takvimlemek; süre kaçırmaktan doğan hak kaybını önlemek.

## Soğuk başlangıç (intake)
- Hakkınız/alacağınız hangi tarihte doğdu?
- Bir tebligat aldıysanız tebliğ tarihi nedir?
- Daha önce dava, icra takibi veya ihtar yaptınız mı (kesilme/durma)?
- Uyuşmazlık sözleşmeden mi, haksız fiilden mi doğuyor?
- Bir karar/heyet kararı tebliğ edildiyse itiraz süresini mi soruyorsunuz?

## Denetim şeması
1. **Zamanaşımı türü:** Genel sözleşme alacaklarında on yıl (TBK m.146); kira bedeli, faiz, ücret gibi dönemsel edimlerde beş yıl (TBK m.147). Haksız fiilde fiil ve failin öğrenilmesinden iki yıl, her halde on yıl (TBK m.72).
2. **Kesilme/durma:** Zamanaşımı; dava açma, icra takibi, alacağın ikrarı gibi sebeplerle kesilir (TBK m.154) ve kesilmeden sonra yeniden işler (m.156). Durma halleri m.153.
3. **Usul süreleri:** Cevap dilekçesi iki hafta (HMK m.127); istinaf süresi kural olarak kararın tebliğinden iki hafta (m.345); temyiz süresi iki hafta (m.361). Sürelerin hesabı HMK m.92-94'e göre yapılır; tebliğ günü sayılmaz, son gün tatile gelirse ertesi iş gününe uzar.
4. **Hak düşürücü süreler:** Bazı haklarda (örn. bazı tüketici/ayıp ihbarı, iptal davaları) süre hak düşürücüdür; re'sen dikkate alınır, kesilmez/durmaz.
5. **Zamanaşımı def'i (TBK m.161):** Hâkim re'sen uygulamaz; davalı açıkça ileri sürmelidir. Bu nedenle davalı için kritik bir savunmadır.
6. **Ara sonuç:** Tür + başlangıç + kesilme/durma + son gün hesabı yapılırsa süre güvenli takvimlenir.

## Çıktı modülleri
- Süre takvimi (her işlem için son tarih ve dayanak madde).
- Zamanaşımı durumu değerlendirmesi (dolmuş/dolmamış, kesildi mi).
- Kritik süre uyarıları ve hatırlatma listesi.

## Plugin bağlamı

Bu beceri `kendini-temsil-asliye` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
