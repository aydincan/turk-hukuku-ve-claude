---
name: karar-sonrasi-kanun-yollari-ve-icra
description: "Karar çıktıktan sonra istinaf-temyiz başvurusu yapmak, lehine kararı icraya koymak veya aleyhine kararın icrasını durdurmak isteyen taraf için kullanılır."
---

# Karar Sonrası Kanun Yolları ve İcra

## Görev
Kararı aldıktan sonraki adımları yönetmek: itiraz (istinaf/temyiz) süresini korumak; lehe kararı icra etmek; aleyhe kararda zarar görmemek.

## Soğuk başlangıç (intake)
- Karar lehinize mi, aleyhinize mi sonuçlandı?
- Gerekçeli karar tebliğ edildi mi, tarihi nedir?
- Karara itiraz mı etmek istiyorsunuz, yoksa icraya mı koyacaksınız?
- Uyuşmazlık değeri istinaf/temyiz sınırının üstünde mi?
- Karşı taraf ödeme yapmaya yanaşıyor mu?

## Denetim şeması
1. **İstinaf (HMK m.341-360):** İlk derece kararına karşı kanun yolu istinaftır. Süre, gerekçeli kararın tebliğinden itibaren **iki haftadır** (m.345). Miktar/değer belli bir parasal sınırın altındaysa karar kesindir, istinafa gidilemez — sınır yıllık güncellenir, **[doğrulanacak]**. İstinaf dilekçesinde sebepler açıkça gösterilir (m.342).
2. **Temyiz (HMK m.361 vd.):** İstinaf kararına karşı, kanunda öngörülen parasal sınırın üzerindeki uyuşmazlıklarda temyiz yolu açıktır; süre tebliğden iki haftadır. Bazı kararlar kesindir (m.362).
3. **İcranın durması:** İstinaf/temyiz başvurusu kural olarak icrayı kendiliğinden durdurmaz; kararı veren para/teslim ilamı icra edilebilir. Aleyhine karar olan taraf, teminat göstererek icranın geri bırakılmasını (tehir-i icra) talep edebilir (İİK m.36).
4. **Lehe kararın icrası (2004 sayılı İİK):** Kesinleşmesi gerekmeyen para ilamları için ilamlı icra takibi başlatılır (İİK m.24 vd.); icra dairesine başvurularak icra emri çıkarılır.
5. **Ara sonuç:** Süre korunur (itiraz edilecekse) veya icra takibi açılır; aleyhe kararda tehir-i icra değerlendirilir.

## Çıktı modülleri
- İstinaf/temyiz dilekçesi iskeleti (sebepler bölümüyle) ve süre uyarısı.
- İlamlı icra takip yol haritası (lehe karar).
- Tehir-i icra/teminat seçeneği notu (aleyhe karar).

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
