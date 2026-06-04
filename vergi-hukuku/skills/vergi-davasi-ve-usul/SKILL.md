---
name: vergi-davasi-ve-usul
description: "Vergi/ceza ihbarnamesi veya ödeme emrine karşı açılacak davada görevli-yetkili mahkemeyi, süreyi, dava şartlarını ve yürütmenin durdurulmasını belirlemek için kullanılır."
---

# Vergi Davası, Görev-Yetki ve Süreler

## Görev
Vergi uyuşmazlığını yargıya taşırken doğru mahkemeyi, doğru süreyi, dava türünü ve yürütmenin durması/durdurulması rejimini belirleyerek dava açılabilirliğini güvenceye almak.

## Soğuk başlangıç (intake)
1. Dava konusu işlem nedir (vergi/ceza ihbarnamesi, ödeme emri, düzeltme reddi, ihtirazi kayıtla beyan)?
2. İşlem hangi tarihte tebliğ edildi?
3. Daha önce uzlaşma/düzeltme talep edildi mi (süre durması var mı)?
4. İşlemi tesis eden idare (vergi dairesi) hangi yer?
5. Talep iptal mi, tahsilatın durdurulması mı?

## Denetim şeması
1. **Görev:** Vergi mahkemeleri 2576 sayılı Kanun ve İYUK kapsamında genel vergi/ceza uyuşmazlıklarına bakar; kaçakçılık suçu (VUK m.359) ceza mahkemesindedir. İdari işlem niteliği taşımayan özel hukuk ilişkisi değilse idari yargı yolu açıktır.
2. **Yetki:** İYUK m.37 — vergi uyuşmazlıklarında yetkili mahkeme, tarhiyatı/işlemi yapan vergi dairesinin bulunduğu yer vergi mahkemesidir.
3. **Süre:** İYUK m.7 genel kural 30 gün (tebliğden itibaren); ödeme emrine karşı AATUHK m.58 uyarınca 15 gün. Süreler hak düşürücüdür; uzlaşma talebi varsa VUK Ek m.7 ile durma hesabını uygula.
4. **Dava şartları:** Ehliyet ve menfaat (İYUK m.2), kesin/yürütülebilir işlem şartı, idari merci tecavüzü kontrolü (İYUK m.14-15). Dilekçe unsurları İYUK m.3 (taraflar, konu, sebepler, dayandığı deliller, tebliğ tarihi).
5. **Yürütmenin durması/durdurulması:** İYUK m.27/4 — vergi mahkemesinde dava açılması, tarh edilen vergi/ceza ve gecikme faizinin tahsilini kendiliğinden durdurur; ancak ihtirazi kayıtla beyan üzerine açılan dava ile ödeme emrine karşı açılan davada otomatik durma yoktur, ayrıca yürütmenin durdurulması (İYUK m.27/2 — açıkça hukuka aykırılık + telafisi güç zarar) talep edilir.
6. **Kanun yolları:** İstinaf (BİM) ve temyiz (Danıştay) parasal sınır ve İYUK m.45-46 çerçevesinde. Ara sonuç: dava açılabilir mi, hangi sürede, hangi mahkemede, durma rejimi nedir?

## Çıktı modülleri
- Görev-yetki-süre tespit kartı.
- Yürütmenin durması/durdurulması analiz notu (otomatik mi, talep mi?).
- Dava dilekçesi iskeleti (İYUK m.3 unsurlarıyla).
- Kanun yolu ve parasal sınır takvimi.

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
