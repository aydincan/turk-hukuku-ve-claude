---
name: sureler-ve-zamanasimi
description: "Sebepsiz zenginleşme alacağında iki yıllık ve on yıllık zamanaşımı sürelerinin başlangıcını, kesilme ve durmasını belirlemek; talebin zamanaşımına uğrayıp uğramadığını test etmek gerektiğinde kullanılır."
---

# Süreler ve Zamanaşımı

## Görev
Sebepsiz zenginleşme alacağının özel zamanaşımı rejimini (TBK m.82) uygulamak: iki yıllık (öğrenmeden) ve on yıllık (zenginleşmeden) sürelerin başlangıcını doğru saptamak, kesilme/durmayı işletmek. Bu kurumun süresi genel on yıldan farklı olduğu için ayrı denetim gerektirir.

## Soğuk başlangıç (intake)
- İade hakkı sahibi, hakkını (zenginleşmeyi ve iade isteyebileceğini) ne zaman öğrendi?
- Zenginleşme (kayma) fiilen ne zaman gerçekleşti?
- Bu süreler içinde dava, takip, ihtar veya ikrar gibi kesen bir işlem oldu mu?
- Yarışan bir talep (istihkak/sözleşme) farklı süreye mi tâbi?

## Denetim şeması
1. **İki yıllık süre (m.82/1).** İade alacaklısı, iade hakkını **öğrendiği** tarihten itibaren iki yıl içinde talep etmelidir. Öğrenme; hem zenginleşmeyi hem de sebepsizliği (iade isteyebileceğini) kapsar. Başlangıç anı titizlikle belirlenir.
2. **On yıllık üst süre (m.82/1).** Öğrenme ne zaman olursa olsun, zenginleşmenin gerçekleştiği tarihten itibaren on yıl geçmekle alacak her hâlde zamanaşımına uğrar. İki süreden hangisi önce dolarsa o esastır.
3. **Süre niteliği.** Bu süreler zamanaşımıdır (hak düşürücü değil); def'i olarak ileri sürülmedikçe hâkim resen dikkate almaz (TBK m.161). Borçlu süresinde def'i ileri sürmelidir.
4. **Kesilme (m.154-157).** Dava açılması, icra takibi, borçlunun ikrarı veya hakeme başvuru zamanaşımını keser; kesilince yeni iki yıllık süre işlemeye başlar. Durma halleri m.153'le sınırlıdır.
5. **Yarışan taleple fark.** İstihkak (TMK m.683) kural olarak zamanaşımına tâbi değildir; sözleşmesel iade genel sürelere (TBK m.146, 10 yıl) tâbi olabilir. Talep seçimi süre bakımından kritik avantaj/dezavantaj yaratır.
6. **Ara sonuç.** Her iki süre için somut başlangıç tarihi ve son gün hesaplanır; kesen işlem varsa yeni son gün belirlenir. Yakın dolan süre için acil aksiyon (ihtar/dava) işaretlenir.

## Çıktı modülleri
- İki yıl / on yıl başlangıç ve son gün hesap tablosu.
- Zamanaşımı def'i veya def'e karşı (kesilme) notu.
- Yakın süre acil aksiyon uyarısı.

## Plugin bağlamı

Bu beceri `sebepsiz-zenginlesme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
