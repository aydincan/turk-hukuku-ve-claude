---
name: vergi-incelemesi-ve-ispat
description: "Vergi inceleme süreci, vergi tekniği raporu, ispat yükünün dağılımı ve delillerin değerlendirilmesini yönetmek; inceleme başladığında veya rapora dayalı tarhiyatta kullanılır."
---

# Vergi İncelemesi, İspat ve Delil

## Görev
Vergi inceleme sürecinde mükellef haklarını korumak, vergi tekniği/inceleme raporunu denetlemek, ispat yükünün dağılımını doğru kurmak ve delil stratejisini oluşturmak.

## Soğuk başlangıç (intake)
1. İnceleme hangi vergi türü ve dönem için, tam/sınırlı/özel inceleme mi?
2. İnceleme başlama tutanağı düzenlendi mi, defter-belge istendi mi?
3. Vergi tekniği raporu (VTR) veya inceleme raporu elde var mı?
4. İddia SMİYB, randıman, kayıt dışı hasılat mı; somut tespit nedir?
5. Mükellefin karşıt delilleri (ödeme, kapasite, stok, sözleşme) neler?

## Denetim şeması
1. **İnceleme yetkisi ve usulü:** VUK m.135-141 — incelemeye yetkililer, incelemenin yeri ve zamanı, başlama tutanağı (m.140), inceleme süreleri. Usul ihlali (defter-belge isteme yazısı, tutanak imzalama hakkı) savunmaya dayanak olur.
2. **Defter-belge ibrazı:** VUK m.139, m.256 — ibraz ödevi; ibraz edilmemesi re'sen takdir sebebidir (VUK m.30). Mücbir sebep (m.13) varsa ibraz etmeme mazur görülebilir; bu ayrımı kur.
3. **İspat yükünün dağılımı:** VUK m.3/B — vergiyi doğuran olay ve gerçek mahiyetin tespitinde iktisadi, ticari ve teknik icaplara uygunluk esas; iddia eden ispatla yükümlü. Vergiyi doğuran olayın varlığını idare, lehe istisna/indirim/giderin varlığını mükellef ispatlar.
4. **Delil serbestisi ve sınırı:** VUK m.3/B — yemin hariç her türlü delil; ancak vergiyi doğuran olayla ilgisi açık olmayan tanık beyanı ispatlama vasıtası sayılmaz. Karşıt inceleme, banka kayıtları, sevk irsaliyesi, kapasite raporu gibi somut delilleri öne çıkar.
5. **VTR denetimi:** Raporun somut tespite mi yoksa varsayım/oranlamaya mı dayandığını ayır; randıman/karşılaştırmalı yöntemlerin gerçek faaliyete uygunluğunu sorgula. Gerekçesiz rapor iptal sebebidir. Ara sonuç: tarhiyatın delil temeli ne kadar sağlam?
6. **Mükellef hakları:** İzaha davet (VUK m.370) imkânı kullanıldı mı; raporu okuma, tutanağa şerh düşme, görüş bildirme hakları.

## Çıktı modülleri
- İnceleme usulü kontrol listesi (tutanak, süre, ibraz, yetki).
- İspat yükü dağılım tablosu (iddia → ispat yükümlüsü → mevcut delil).
- VTR çürütme notu (somut tespit / varsayım ayrımı, karşı delil eşleştirmesi).
- İzah/savunma dilekçesi argüman iskeleti.

## Plugin bağlamı

Bu beceri `vergi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
