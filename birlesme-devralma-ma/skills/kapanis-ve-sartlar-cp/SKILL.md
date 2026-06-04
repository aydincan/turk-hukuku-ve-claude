---
name: kapanis-ve-sartlar-cp
description: "İmza ile kapanış arası dönemin yönetimi, kapanış ön şartlarının (conditions precedent) listelenmesi, kapanışta teslim edilecek belgelerin ve eş zamanlı işlemlerin kurgulanması için kullanılır."
---

# Kapanış Şartları (CP) ve Kapanış Yönetimi

## Görev
İmza-kapanış arası dönemi düzenlemek, kapanış ön şartlarını ve kapanış belgelerini eksiksiz kurgulamak; eksik/gecikmeli kapanış sonuçlarını hükme bağlamak.

## Soğuk başlangıç (intake)
- İmza ve kapanış eş zamanlı mı, ayrık mı (signing/closing split)?
- Hangi izinler kapanış şartı (rekabet, sektörel, üçüncü kişi onayı)?
- Kapanış için uzun stop (long-stop date) tarihi belirlendi mi?
- Kapanışta hangi belgeler eş zamanlı teslim edilecek?

## Denetim şeması
1. **CP kataloğu**: Rekabet Kurulu izni, sektörel ön izin (BDDK/EPDK vb.), üçüncü kişi onayları (change-of-control), kurumsal kararlar, beyanların kapanışta doğru olması (bring-down).
2. **Ara dönem taahhütleri**: TBK m.2 dürüstlük kuralı çerçevesinde olağan işletme yürütümü; satıcının değer düşürücü işlem yapmama taahhüdü.
3. **Kapanış belgeleri (deliverables)**: Pay devir ciroları, pay defteri kaydı (TTK m.499), istifa/atama kararları, banka talimatları, disclosure güncellemesi.
4. **Eş zamanlılık**: Kapanış işlemlerinin tek seansta ve birbirine bağlı (interdependent) yapılması; aksi halde geri alma (unwind) mekanizması.
5. **Eksik kapanış**: Long-stop tarihine kadar CP sağlanmazsa fesih hakkı; kusurlu tarafın temerrüt sorumluluğu (TBK m.117 vd.).
6. **İspat/dayanak**: CP'nin sağlandığı belge (izin yazısı, onay kararı) ile kanıtlanır.
7. **Ara sonuç**: Kapanış protokolü (closing memorandum) ile tüm adımlar teyit edilir.

## Çıktı modülleri
- CP kontrol listesi (sorumlu taraf ve durum sütunlu)
- Kapanış belgeleri (deliverables) dizini
- Closing memorandum / kapanış protokolü iskeleti
- Long-stop ve fesih klozu lafzı

## Plugin bağlamı

Bu beceri `birlesme-devralma-ma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
