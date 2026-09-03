---
name: cevap-replik-duplik
description: "Davalı vekili olarak cevap dilekçesi (HMK m.126-129) hazırlarken itiraz, inkâr, def'i ve ilk itirazları doğru kanala koymak; cevaba cevap (replik) ve ikinci cevap (düplik) aşamasında genişletme yasağını yönetmek için."
---

# Cevap, Replik ve Düplik Stratejisi

## Görev
Savunmayı HMK m.126-129 çerçevesinde kurmak; inkâr/itiraz/def'i ayrımını netleştirmek, ilk itirazları süresinde toplu ileri sürmek ve dilekçeler teatisi içinde savunmayı tam serbestlikle tamamlamak.

## Soğuk başlangıç (intake)
- Cevap süresi ne zaman doluyor (yazılıda iki hafta, m.127; basitte iki hafta, m.317)?
- İleri sürülecek bir def'i var mı (zamanaşımı, ödemezlik, takas)?
- Yetki/tahkim gibi ilk itiraz gerekiyor mu?
- Karşı dava (m.132-134) koşulları oluştu mu?

## Denetim şeması
1. **Cevap süresi** (m.127): Dava dilekçesinin tebliğinden itibaren iki hafta; gerektiğinde bir aya kadar ek süre (m.127/2) istenebilir. Basit yargılamada süre iki haftadır (m.317).
2. **Cevap unsurları** (m.129): m.119'a paralel; vakıaların açık reddi veya kabulü, dayanılan deliller, hukuki sebepler, talep sonucu. **Açıkça inkâr edilmeyen vakıa ikrar edilmiş sayılabilir** (m.128) — sessizlik risklidir.
3. **İtiraz / def'i ayrımı**: İtiraz (örn. borç hiç doğmadı, ödendi) re'sen dikkate alınır; **def'i** (zamanaşımı, ödemezlik def'i, takas) yalnızca ileri sürülürse hüküm doğurur ve **zamanaşımı def'i** mutlaka cevapta ileri sürülmelidir.
4. **İlk itirazlar** (m.116-117): Yetki (kesin olmayan), tahkim vb. cevap dilekçesinde **birlikte** ileri sürülür; sonradan ileri sürülemez.
5. **Karşı dava** (m.132): Asıl dava ile bağlantı veya takas/mahsup ilişkisi varsa cevap süresi içinde açılır.
6. **Replik–düplik** (m.136): Cevaba cevap ve ikinci cevap dilekçeleri verilir; **bu aşama bitene kadar** iddia/savunma serbestçe tamamlanabilir, sonrasında genişletme yasağı (m.141) işler.

Ara sonuç: "Savunma tipi + def'iler + ilk itirazlar + karşı dava" haritası.

## Çıktı modülleri
- Cevap dilekçesi iskeleti (m.129 unsurlu).
- Def'i ve ilk itiraz kontrol listesi (süre uyarılı).
- Replik/düplik için açık kalan savunma noktaları.

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
