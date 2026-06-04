---
name: kurucu-vesting-esop
description: "Kurucu paylarının hak edilmesi (vesting) ve çalışanlara hisse/opsiyon verme (ESOP) programları kurgulanırken; pay havuzunun oluşturulması, hak ediş ve geri alım mekaniği, AŞ kendi pay iktisabı sınırı ve vergi boyutu denetlenirken kullanılır."
---

# Kurucu Vesting ve Çalışan Hisse Opsiyonu (ESOP)

## Görev
Ekip teşvik yapısını kurmak: kurucu paylarının vesting takvimi ve ayrılışta geri alımı; çalışan opsiyon havuzunun (ESOP) oluşturulması, tahsisi, hak edişi ve vergisel sonuçları.

## Soğuk başlangıç (intake)
1. Kurucu vesting takvimi ne (ör. 4 yıl, 1 yıl cliff) ve ayrılışta pay ne olacak?
2. ESOP havuzu yüzde kaç; turdan önce mi sonra mı açılıyor (kimi sulandırıyor)?
3. Çalışana gerçek pay mı, sanal/fantom pay mı, yoksa pay opsiyonu mu veriliyor?
4. Hak ediş tetikleyicileri ve ayrılma (good/bad leaver) sonuçları belirlendi mi?
5. Şirket AŞ mi; opsiyon karşılığı paylar nereden gelecek (havuz/artırım/kendi pay)?

## Denetim şeması
1. Kurucu vesting: Kurucu payları baştan ihraç edilir; vesting "hak edilmemiş payların ayrılışta geri alınması/zorunlu satışı" olarak kurgulanır. Mekanik: SHA + esas sözleşmesel zorunlu satış/önalım (TTK m.491-493) + cezai şart (TBK m.179). Good/bad leaver ayrımı ve fiyat (nominal mi gerçek değer mi) yazılır.
2. ESOP yapı seçimi: (a) Gerçek pay + vesting; (b) pay opsiyonu (gelecekte pay alma hakkı); (c) sanal/fantom pay (nakdî, pay vermeyen). Türk hukukunda en yaygını sözleşmesel opsiyon + havuz; her biri farklı kurumsal ve vergisel sonuç doğurur.
3. Pay kaynağı: Opsiyon kullanılınca pay ya (i) mevcut ortaktan devir, ya (ii) sermaye artırımı (m.456), ya (iii) sınırlı ölçüde AŞ'nin kendi payını iktisabı (m.379-381: sermayenin %10'u sınırı, fon şartı) ile sağlanır.
4. Sulandırma: Havuzun turdan önce açılması mevcut ortakları, sonra açılması yeni yatırımcıyı da sulandırır; term sheet'te netleştir (cap table beceresiyle modelle).
5. Vergi: Çalışana piyasa değerinin altında pay/opsiyon menfaati kural olarak ücret (GVK ücret hükümleri); gelir vergisi/stopaj doğabilir. Teşvikli istisnaları (TGB/Ar-Ge kapsamı, 4691/5746) ayrıca teyit et.
6. İspat/şekil: Opsiyon planı + bireysel tahsis sözleşmesi yazılı; pay devri m.490 şekli; kurumsal kararlar.

## Çıktı modülleri
- ESOP planı ve bireysel opsiyon/tahsis sözleşmesi taslağı.
- Kurucu vesting + good/bad leaver geri alım mekaniği.
- Pay kaynağı ve vergi/sulandırma uyarı notu.

## Plugin bağlamı

Bu beceri `girisim-startup-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
