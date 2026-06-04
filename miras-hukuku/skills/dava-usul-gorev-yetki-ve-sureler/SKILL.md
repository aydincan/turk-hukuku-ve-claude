---
name: dava-usul-gorev-yetki-ve-sureler
description: "Miras davasını doğru mahkemede ve süresinde açmak; çekişmeli-çekişmesiz iş ayrımı, görevli mahkeme, yetki, harç ve hak düşürücü süre/zamanaşımı haritası çıkarmak gerektiğinde kullanılır."
---

# Dava Usulü, Görev-Yetki ve Süreler

## Görev
Her miras talebini doğru yargı yoluna oturtmak: çekişmeli/çekişmesiz ayrımı, görevli ve yetkili mahkeme, harç-gider ve süre disiplinini HMK ve TMK normlarıyla kurmak.

## Soğuk başlangıç (intake)
- Talep ne? (mirasçılık belgesi, ret, tenkis, muvazaa, istihkak, paylaşma)
- Mirasbırakanın son yerleşim yeri neresi? Taşınmaz nerede?
- Ölüm ve öğrenme tarihleri? Süreler işliyor mu?
- Taraflar kim, mirasçı sayısı? (zorunlu dava arkadaşlığı)
- Önceden açılmış derdest dava/karar var mı?

## Denetim şeması
1. **Çekişmesiz işler — sulh hukuk (HMK m.382, m.4):** Mirasçılık belgesi (m.598), mirasın reddinin tescili (m.609), defter tutma, terekenin tespiti/yönetimi, vasiyetnamenin açılması (m.595-597), ortaklığın giderilmesi.
2. **Çekişmeli davalar — asliye hukuk (HMK m.2):** Tenkis, muris muvazaası (tapu iptali-tescil), miras sebebiyle istihkak, denkleştirme, vasiyetnamenin/miras sözleşmesinin iptali, mirasçılık belgesinin iptali.
3. **Yetki:** Mirasbırakanın son yerleşim yeri mahkemesi (TMK m.576; HMK m.11). Taşınmaza ilişkin tapu iptali-tescilde taşınmazın bulunduğu yer kesin yetkisi (HMK m.12) gündeme gelir.
4. **Taraf — zorunlu dava arkadaşlığı:** Elbirliği mülkiyetini ilgilendiren davalarda (paylaşma, muvazaa) tüm mirasçıların davada yer alması gerekir; aksi halde dava şartı eksikliği.
5. **Süre haritası:** Mirasın reddi 3 ay (m.606); tenkis 1 yıl / 10 yıl (m.571); vasiyet iptali 1 / 10 / 20 yıl (m.559); miras sebebiyle istihkak 10 / 20 yıl (m.639). Muris muvazaası ve ortaklığın giderilmesi süreye tabi değildir.
6. **Ara sonuç:** dava türü + mahkeme + yetki + süre durumu + harç (nispi/maktu). Dilekçe HMK m.119 unsurlarıyla kurulur.

## Çıktı modülleri
- Görev-yetki-süre karar tablosu
- Süre takvimi (hak düşürücü/zamanaşımı, kalan gün)
- Taraf ve zorunlu dava arkadaşlığı listesi
- Dilekçe başlığı ve harç türü notu

## Plugin bağlamı

Bu beceri `miras-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
