---
name: temel-kavramlar-ve-sistem
description: "Marka hukukuna ilk girişte; markanın hukuki niteliği, hak sahipliği, koruma kapsamı ve SMK'nın tescil-koruma-tasarruf ekseninin haritalanması gerektiğinde uyuşmazlığı doğru kanala yerleştirmek için kullanılır."
---

# Temel Kavramlar ve SMK Sistematiği

## Görev
Somut sorunu 6769 sayılı SMK'nın doğru ekseninde (tescil/idari süreç, hükümsüzlük-iptal, tecavüz, sözleşme) konumlandırmak; markanın tanımı (m.4), hakkın doğumu (tescil ilkesi) ve kapsamının (m.7) çerçevesini kurmak. Yanlış kanal seçimi süre ve görev hatasına yol açar; bu yüzden ilk filtre budur.

## Soğuk başlangıç (intake)
- İşaret tescilli mi, başvuru aşamasında mı, tescilsiz kullanım mı?
- Hangi mal/hizmetler (Nice sınıfları) söz konusu?
- Talep ne: tescil/itiraz, hükümsüzlük/iptal, tecavüzün önlenmesi, tazminat, lisans/devir?
- Karşı tarafın hakkı/önceliği var mı, tarih sırası nedir?

## Denetim şeması
1. **Marka olabilirlik (m.4).** İşaret ayırt edici mi ve sicilde açık-kesin gösterilebiliyor mu (kelime, şekil, renk, ses, üç boyutlu). Olamıyorsa hiç tescil edilmemeli.
2. **Hakkın doğumu.** Türk sisteminde marka hakkı kural olarak tescille doğar (m.7/1). Tescilsiz işaret için m.6/3 (eskiye dayalı kullanım) ve haksız rekabet (TTK m.54-55) yolu ayrıca değerlendirilir.
3. **Koruma kapsamı (m.7).** Aynı işaret-aynı mal; benzer işaret-benzer mal + karıştırılma; tanınmış markada farklı sınıf koruması. Yasaklama yetkisinin kapsamı buradan çıkar.
4. **Sınırlar.** Dürüst kullanım (m.7/5), hakkın tüketilmesi (m.152), kullanmama def'i (m.19/2), sessiz kalma (m.25/6) hakkın kullanımını sınırlar.
5. **Ara sonuç.** Uyuşmazlığın türü (idari/adli), görevli merci (TÜRKPATENT/FSHHM) ve uygulanacak ana norm bloğu (m.5-6 / m.25-26 / m.29-150) belirlenir; süre riski işaretlenir.

## Çıktı modülleri
- Uyuşmazlık türü ve doğru kanal haritası.
- İşaret-mal/hizmet (Nice sınıfı) tablosu.
- Uygulanacak ana norm bloğu ve süre uyarı listesi.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
