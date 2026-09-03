---
name: kdv-ve-dolayli-vergiler
description: "Katma değer vergisinde vergiyi doğuran olay, indirim, iade, tevkifat ve sahte belge kaynaklı KDV reddi sorunlarını çözmek; KDV ve dolaylı vergi uyuşmazlıklarında kullanılır."
---

# KDV ve Dolaylı Vergiler

## Görev
Katma değer vergisi ve diğer dolaylı vergilerde (ÖTV, damga) verginin doğumu, indirim hakkı, iade süreci ve özellikle SMİYB kaynaklı indirim reddi uyuşmazlıklarını çözmek.

## Soğuk başlangıç (intake)
1. İhtilaf indirim reddi mi, iade reddi mi, tevkifat mı?
2. Sahte/yanıltıcı belge (SMİYB) iddiası var mı; karşıt inceleme yapılmış mı?
3. İade türü nedir (ihracat istisnası, indirimli oran, tevkifat iadesi)?
4. Vergiyi doğuran olayın gerçekleştiği dönem ve teslim/hizmet anı nedir?
5. KDV beyannameleri ve YMM raporu/teminat durumu nedir?

## Denetim şeması
1. **Vergiyi doğuran olay:** KDVK m.10 — teslim, hizmetin yapılması, fatura düzenlenmesi veya kısmi teslim anı. Doğru dönemi tespit et; erken/geç beyan ceza riskidir.
2. **Verginin konusu ve mükellef:** KDVK m.1 (ticari/sınai/zirai/serbest meslek faaliyeti, ithalat), m.8 mükellef, m.9 tevkifat ve sorumlu sıfatı.
3. **İndirim hakkı:** KDVK m.29 — yüklenilen KDV'nin indirimi; m.34 indirimin belgeye ve kayda bağlılığı; m.30 indirilemeyecek KDV (özellikle m.30/d — Gelir/Kurumlar yönünden gider kabul edilmeyen harcamalara ait KDV).
4. **SMİYB kaynaklı ret:** İndirim reddinde idare belgenin sahteliğini somut tespitle (VTR, karşıt inceleme) ortaya koymalı; mükellef gerçek mal/hizmet hareketini (ödeme, sevkiyat, stok) ispatla çürütebilir. VUK m.3/B ekonomik yaklaşım ve VUK m.359 sahte belge ilişkisini ayır.
5. **İstisna ve iade:** KDVK m.11-12 (ihracat istisnası), m.32 (istisna işlemlerde yüklenilen verginin iadesi), indirimli oran iadesi m.29/2. İade için aranan belge ve YMM tasdik şartını kontrol et. Ara sonuç: indirim/iade reddi haklı mı, hangi delille çürütülür?
6. **ÖTV ve damga:** ÖTV'de listeye giren mal ve doğuran olay (ÖTVK 4760); damga vergisinde kâğıt ve nispi/maktu oran (488 sayılı Kanun). İlgili özel vergi için ayrı denetim.

## Çıktı modülleri
- KDV doğum-indirim-iade akış tablosu (dönem bazında).
- SMİYB savunma dosyası (gerçeklik delilleri listesi: ödeme, irsaliye, stok, kapasite).
- İade hak ediş ve eksik belge listesi.
- İhtilaf dilekçesi argüman iskeleti.

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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
