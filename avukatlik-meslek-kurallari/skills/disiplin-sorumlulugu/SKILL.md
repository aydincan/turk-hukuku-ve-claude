---
name: disiplin-sorumlulugu
description: "Avukat hakkında disiplin şikâyeti, soruşturma ve kovuşturma, disiplin cezaları ve bunlara itiraz/iptal yolları söz konusu olduğunda; disiplin riskini değerlendirmek için kullanılır."
---

# Avukatın Disiplin Sorumluluğu ve Baro Süreçleri

## Görev
Bir davranışın disiplin suçu oluşturup oluşturmadığını, uygulanacak ceza türünü ve sürecin
aşamaları ile kanun yollarını belirlemek.

## Soğuk başlangıç (intake)
1. İsnat edilen davranış nedir (özensizlik, sır ihlali, güveni kötüye kullanma, ücret/emanet
   para sorunu, meslektaşa karşı tavır)?
2. Süreç hangi aşamada (şikâyet, disiplin soruşturması, disiplin kovuşturması, ceza, itiraz)?
3. Daha önce verilmiş disiplin cezası / tekerrür var mı?
4. Aynı fiil hakkında ceza yargılaması da var mı?

## Denetim şeması
1. **Disiplin suçunun çerçevesi.** Avukatlık onuruna, meslek düzenine, meslek kurallarına
   aykırı eylem ve davranışlar disiplin suçudur (Av. K. m.34, m.134; TBB Meslek Kuralları).
   Tip, çoğu zaman somut maddeyle değil genel davranış normuyla kurulur; bu yüzden eylemin
   meslek onuruyla bağı gerekçelendirilir.
2. **Ceza türleri ve ölçek.** Av. K. m.135: uyarma, kınama, para cezası, işten çıkarma
   (geçici olarak mesleki faaliyetten alıkoyma) ve meslekten çıkarma. Ceza, fiilin ağırlığı,
   tekerrür ve kusur derecesine göre belirlenir (orantılılık). Ara sonuç: eylem hangi
   kademeye karşılık gelir?
3. **Süreç.** Baro yönetim kurulu disiplin soruşturması açar; gerekirse baro disiplin kurulu
   kovuşturma yürütür (Av. K. m.136 vd.). Savunma hakkı ve usul güvenceleri esastır; eksik
   tebligat/savunma alınmaması iptal sebebidir.
4. **Kanun yolu.** Baro disiplin kurulu kararına karşı TBB Disiplin Kurulu'na itiraz edilir;
   TBB kararları idari işlem niteliğinde olup idari yargı (Danıştay) denetimine tabidir.
   Süreleri kaçırma hak kaybı doğurur.
5. **Zamanaşımı.** Disiplin kovuşturmasında Av. K. m.157'deki süreler işler; fiilin
   öğrenilmesinden ve işlenmesinden itibaren süreler ayrı ayrı kontrol edilir.
6. **Ceza yargısı ile ilişki.** Disiplin ve ceza sorumluluğu bağımsızdır; beraat tek başına
   disiplin cezasını kaldırmaz, ancak maddi olgu tespitleri dikkate alınır.

İçtihat gerektiğinde TBB Disiplin Kurulu kararları (barobirlik.org.tr) ve Danıştay kararları
ilkesel düzeyde anılır; künye `[doğrulanacak]` işaretlenir.

## Çıktı modülleri
- Davranış-suç-ceza eşleştirmesi ve olası ceza kademesi.
- Süreç ve süre takvimi (soruşturma → kovuşturma → itiraz → idari dava).
- Savunma dilekçesi/itiraz iskeleti ([doldurulacak] yer tutucularla).

## Plugin bağlamı

Bu beceri `avukatlik-meslek-kurallari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
