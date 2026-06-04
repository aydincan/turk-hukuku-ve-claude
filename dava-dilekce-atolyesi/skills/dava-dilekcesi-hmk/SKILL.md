---
name: dava-dilekcesi-hmk
description: "Medeni yargıda HMK m.119 unsurlarına uygun dava dilekçesi taslağı hazırlamak; eda, tespit veya inşai talepleri doğru kurmak gerektiğinde kullanılır."
---

# Dava Dilekçesi (HMK)

## Görev
HMK m.119'un zorunlu unsurlarını eksiksiz taşıyan, vakıa-altlama-talep omurgası sağlam bir dava dilekçesi taslağı üretmek. Eksik unsur, kesin süreli tamamlama veya dava şartı yokluğu riskine yol açar.

## Soğuk başlangıç (intake)
- Talep eda mı (para/teslim), tespit mi, inşai mi (boşanma, iptal)?
- Taraf bilgileri ve TC/vergi numaraları tam mı?
- Zorunlu arabuluculuk tutanağı/dava şartı eki var mı?
- Faiz başlangıcı ve türü (yasal/avans/ticari) ne olacak?

## Denetim şeması
1. Zorunlu unsurlar (HMK m.119/1): a) mahkeme, b) davacı-davalı ad/TC-vergi no/adres, c) varsa vekil, ç) konu (değer), d) vakıalar (numaralı), e) deliller (her vakıa hangi delille), f) hukuki sebepler, g) açık talep sonucu, ğ) imza. Eksiklikte m.119/2: bir haftalık kesin süre.
2. Talep sonucu netliği: İnfaz edilebilir biçimde yazın; alacakta ana para + faiz (başlangıç tarihi ve oranı TBK m.88/120 veya 3095 s.K.) + yargılama gideri + vekâlet ücreti. Belirsiz alacak davası ise HMK m.107 dayanağını ve fazlaya ilişkin hakkı belirtin.
3. Harç ve gider: Nispi/maktu harç değere göre; eksik harç dava şartı niteliğinde tamamlanır.
4. Delil bağlama: HMK m.194 somutlaştırma yükü; her delili ilgili vakıaya bağlayın. Senetle ispat sınırı (m.200) aşılıyorsa tanık caiz değildir, dikkat edin.
5. Dava şartları kontrolü (m.114): arabuluculuk, görev, yetki, hukuki yarar. Ara sonuç: unsurlar tamsa imzaya hazır; değilse `[doldurulacak]` yer tutucuları ve eksik listesi.

## Çıktı modülleri
- Tam dava dilekçesi taslağı (m.119 başlıklı)
- Talep sonucu bloğu (faiz/gider/ücret dâhil)
- Delil listesi ve dava şartı ekleri kontrol listesi
- Eksik bilgi ve yer tutucu raporu

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
