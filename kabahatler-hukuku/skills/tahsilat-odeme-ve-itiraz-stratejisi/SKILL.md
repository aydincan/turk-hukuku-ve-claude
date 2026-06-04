---
name: tahsilat-odeme-ve-itiraz-stratejisi
description: "İdari para cezasının kesinleşmesi, 6183 sayılı Kanuna göre tahsili, ödeme emri, peşin ödeme indirimi ve başvuru-ödeme arasındaki tercih stratejisini kurmak gerektiğinde kullanılır."
---

# Tahsilat, Ödeme ve İtiraz Stratejisi

## Görev
Cezanın kesinleşme ve tahsil sürecini yönetmek; peşin ödeme indirimi ile başvuru arasında maliyet-risk dengesi kurmak ve tahsilata karşı hukuki yolları belirlemek.

## Soğuk başlangıç (intake)
- Ceza kesinleşti mi, ödeme emri tebliğ edildi mi?
- Peşin ödeme süresi (5326 m.17/6) hâlâ açık mı?
- Tahsilat 6183 sayılı Kanuna göre mi yürütülüyor (haciz, ödeme emri)?
- Başvuru yapıldı mı, sonucu bekleniyor mu?

## Denetim şeması
1. **Tahsil rejimi (5326 m.17):** İdari para cezaları 6183 sayılı Amme Alacaklarının Tahsil Usulü Hakkında Kanuna göre tahsil edilir. Kesinleşmeden cebri tahsil yapılamaz.
2. **Peşin ödeme indirimi (5326 m.17/6):** Tebliğden itibaren süresinde ödenirse cezanın 1/4'ü indirilir. Bu hak, başvuru yapma hakkını ortadan kaldırmaz; ancak ödeme ile başvuru ilişkisini somut olayda doğru kur (ödenen kısmın iadesi/talep stratejisi).
3. **Başvuru-ödeme tercihi:** Başvuruda esaslı şans varsa ve tutar yüksekse başvuru; sübut güçlü ve tutar düşükse indirimli ödeme öne çıkar. Risk haritasıyla karar ver.
4. **Ödeme emrine karşı (6183 m.58):** Ödeme emrinin esasına (borcun yokluğu, zamanaşımı, ödenmiş olma) karşı görevli yargı yolunda dava; idari para cezalarında genel başvuru yolu (5326 m.27) ile ödeme emrine itiraz yolunu ayırt et.
5. **Yerine getirme zamanaşımı (5326 m.21):** Tahsil süresi geçmişse cezanın infaz edilemeyeceğini ileri sür.
6. **Ara sonuç:** Ödeme yapılacaksa indirim süresini koru; itiraz yolu seçilecekse cebri tahsil riskini ve teminat/tedbir ihtimalini değerlendir.

## Çıktı modülleri
- Ödeme vs. başvuru maliyet-risk matrisi.
- Tahsilata karşı hukuki yol notu (6183 m.58 / 5326 m.27 ayrımı).
- Zamanaşımı ve indirim süresi uyarı kartı.

## Plugin bağlamı

Bu beceri `kabahatler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
