---
name: risk-strateji-ve-portfoy
description: "Tescil öncesi clearance, dava açma/açmama kararı, sulh ihtimali veya marka portföyü yönetimi gerekiyorsa; uyuşmazlık ve tescil risklerini tartıp strateji kurmak için kullanılır."
---

# Risk Değerlendirme, Strateji ve Marka Portföyü

## Görev
Müvekkilin marka kararlarını risk-fayda ekseninde yönlendirmek: tescil öncesi clearance (önaraştırma), itiraz/dava açma-açmama, sulh, portföy genişletme ve sınıf stratejisi. Hukuki teşhisi ticari sonuçla birleştirip uygulanabilir bir yol haritası vermek.

## Soğuk başlangıç (intake)
- Hedef nedir: yeni marka tescili, mevcut hakkın savunması, rakibe karşı saldırı?
- Bütçe, zaman baskısı ve markanın ticari önceliği ne?
- Karşı tarafın gücü, tescil durumu ve uzlaşma eğilimi nedir?
- Coğrafi kapsam (yalnız Türkiye mi, yurt dışı/Madrid Protokolü mü)?

## Denetim şeması
1. **Clearance (önaraştırma).** Sicil ve piyasa taraması; aynı/benzer önceki marka, tanınmış marka, alan adı/ticaret unvanı çakışması. m.5-6 ret riski erken ölçülür.
2. **Dava/itiraz olasılık analizi.** Karıştırılma ihtimali, kullanmama def'i ihtimali (m.19/2), tanınmışlık, kötüniyet delili — kazanma ihtimali ve maliyet karşılaştırılır.
3. **Süre ve usul riski.** İtiraz 2 ay, YİDK dava 2 ay, kullanmama 5 yıl, tazminat zamanaşımı 2/10 yıl — kaçan süre stratejiyi sınırlar.
4. **Alternatif yollar.** İhtarname, sulh/koexistence (birlikte var olma) sözleşmesi, sınıf/coğrafya daraltma, marka değiştirme (rebrand) maliyeti tartılır.
5. **Portföy ve genişleme.** Çekirdek markaların hangi sınıflarda tescil edileceği; savunma tescilleri; yurt dışı için Madrid Protokolü; yenileme takvimi (10 yıllık koruma, m.23) ve kullanmama riskinin yönetimi.
6. **Karar.** Beklenen değer + ticari öncelik + zaman ekseninde net tavsiye (aç/açma/sulh ol/rebrand) ve gerekçesi.

## Çıktı modülleri
- Clearance risk skor tablosu (sınıf bazlı çakışma).
- Senaryo karşılaştırması (dava / sulh / rebrand — maliyet, süre, sonuç).
- Portföy ve yenileme takvimi; tavsiye ve gerekçe notu.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
