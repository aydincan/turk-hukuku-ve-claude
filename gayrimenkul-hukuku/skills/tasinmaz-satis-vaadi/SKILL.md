---
name: tasinmaz-satis-vaadi
description: "Bir taşınmazın ileride devredileceğine dair noter sözleşmesi yapıldığında veya satıcı devirden kaçındığında; vaadin geçerliliği, şerhi, ifası ve tapu iptali-tescil yoluyla zorla tescil için kullanılır."
---

# Taşınmaz Satış Vaadi Sözleşmesi

## Görev
Taşınmaz satış vaadini kurmak, geçerliliğini denetlemek ve ifasını sağlamak: vaad borçlusu devirden kaçınırsa vaad alacaklısının tapu iptali ve tescil yoluyla mülkiyeti zorla edinmesini değerlendirmek; şerhin üçüncü kişilere karşı koruyucu etkisini işletmek.

## Soğuk başlangıç (intake)
- Vaad noterde resmî şekilde mi düzenlendi/tasdik mi edildi; tarih ve taraflar net mi?
- Satış vaadi tapuya şerh edildi mi (TMK m.1009); şerh tarihi ne?
- Alıcı bedeli (kısmen/tamamen) ödedi mi, taşınmaz fiilen teslim edildi mi?
- Taşınmaz bu arada üçüncü bir kişiye devredildi mi; o kişi iyiniyetli mi?

## Denetim şeması
1. **Geçerlilik şekli**: Taşınmaz satış vaadi resmî şekle tabidir; noterde düzenleme şeklinde yapılır (TBK m.29; Noterlik K. 1512 m.60/3, m.89). Adi yazılı vaad kural olarak geçersizdir (TBK m.27).
2. **Şerh ve üçüncü kişiye etki**: Satış vaadi tapu kütüğüne şerh edilebilir (TMK m.1009; TST). Şerhle, vaad sonraki maliklere karşı ileri sürülebilir hâle gelir; şerh yoksa üçüncü iyiniyetli kazananın hakkı korunur (m.1023) ve alacaklı tazminata yönelir.
3. **İfa talebi (tapu iptali ve tescil)**: Vaad borçlusu devirden kaçınırsa alacaklı, aynen ifa olarak tapu iptali ve tescil davası açar; mahkeme kararı tescili sağlar (TMK m.705/2 çerçevesinde). Karşılıklı edimlerde alıcının bedeli ifaya hazır olması (ödeme/depo) aranır.
4. **Zamanaşımı**: Satış vaadinden doğan ifa talebi genel zamanaşımına (10 yıl, TBK m.146) tabidir; sürenin başlangıcı sözleşmede kararlaştırılan ifa anına bağlanır. Taşınmazın teslim edilip kullanılması zamanaşımı savunmasını dürüstlük süzgecinden geçirir (TMK m.2) [ilkeler için karararama.yargitay.gov.tr].
5. **Kat karşılığı ile ilişki**: Arsa sahibi-yüklenici ilişkisinde, yükleniciden bağımsız bölüm satın alan üçüncü kişi de satış vaadi/temlik zincirine dayanarak doğrudan arsa sahibine karşı tescil isteyebilir (yüklenicinin edimini ifa etmiş olması kaydıyla) [doğrulanacak — karararama.yargitay.gov.tr].
6. **Ara sonuç**: Geçerli + (varsa) şerhli vaadde ifaya hazır alacaklı tescili icbar eder; aksi hâlde tazminat.

## Çıktı modülleri
- Satış vaadi sözleşmesi taslağı (taraflar, taşınmaz, bedel, ifa tarihi, şerh kaydı) [doldurulacak] yer tutucularıyla.
- Tapu iptali ve tescil dava dilekçesi iskeleti (vaad, ödeme, talep sonucu).
- Şerh/ihtiyati tedbir ve zamanaşımı uyarı notu.

## Plugin bağlamı

Bu beceri `gayrimenkul-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
