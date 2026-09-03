---
name: ise-alim-ve-is-sozlesmesi
description: "Yeni işe alım, sözleşme türü seçimi, deneme süresi, belirli/belirsiz süreli ayrımı, rekabet yasağı ve gizlilik kayıtları ile iş sözleşmesi taslağı gerektiğinde kullanılır."
---

# İşe Alım ve İş Sözleşmesi Tasarımı

## Görev
İşverenin yeni çalışan istihdamında doğru sözleşme türünü seçmesini, emredici hükümlere uygun ve dava riski düşük bir iş sözleşmesi kurmasını sağlamak. Aşırı koruyucu ama geçersiz kayıtlar yerine ayakta kalacak, dengeli metin üretmek.

## Soğuk başlangıç (intake)
1. Pozisyon, görev tanımı ve aylık ücret (brüt/net, prim/yan haklar) nedir?
2. İhtiyaç süreklilik arz ediyor mu, yoksa proje/sezon bazlı objektif neden var mı (belirli süreli için şart)?
3. Çalışan gizli bilgiye/müşteri portföyüne erişecek mi (rekabet yasağı/gizlilik gereği)?
4. Deneme süresi öngörülüyor mu, uzaktan/hibrit mi?

## Denetim şeması
1. **Süre tipi (4857 m.11)**: Belirli süreli sözleşme ancak işin niteliği veya objektif neden varsa kurulabilir; aksi halde baştan **belirsiz süreli** sayılır ve zincirleme yenileme belirsiz süreliye döner. Objektif neden yoksa belirsiz süreli tasarla.
2. **Şekil (m.8)**: Bir yıl ve üzeri süreli sözleşme yazılı yapılır; yazılı olmasa bile işveren 2 ay içinde çalışma koşullarını gösteren belge vermek zorundadır.
3. **Deneme süresi (m.15)**: En çok 2 ay (TİS ile 4 aya çıkarılabilir); bu sürede iki taraf da bildirimsiz fesih yapabilir, ancak kıdem korunur.
4. **Rekabet yasağı (TBK m.444-447)**: Geçerlilik için işçinin müşteri çevresi/üretim sırlarına vakıf olması, **yer-zaman-konu** bakımından sınırlama ve hakkaniyet şarttır; süre kural olarak 2 yılı aşamaz (m.445). Aşırı kayıt hâkim tarafından sınırlanır → ölçülü yaz.
5. **Cezai şart**: Tek taraflı (yalnız işçi aleyhine) ve fahiş cezai şart geçersiz/indirilebilir (TBK m.182). Karşılıklı dengele.
6. **KVKK**: Aday ve çalışan verisi için işleme şartı (m.5) ve aydınlatma (m.10); sağlık/adli sicil özel nitelikli veri olup işleme sınırlıdır. İspat yükü: sözleşmenin yapıldığını ve içeriğini işveren ispatlar.

## Çıktı modülleri
- İş sözleşmesi taslağı (tür gerekçesi + esas kayıtlar + [doldurulacak] alanlar).
- Görev tanımı ve çalışma koşulları eki.
- Gizlilik/rekabet yasağı ve KVKK aydınlatma + ek protokol seti.

## Plugin bağlamı

Bu beceri `ik-insan-kaynaklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
