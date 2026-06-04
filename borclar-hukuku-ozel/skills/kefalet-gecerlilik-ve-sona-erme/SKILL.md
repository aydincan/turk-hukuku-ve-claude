---
name: kefalet-gecerlilik-ve-sona-erme
description: "Kefalet sözleşmesinin geçerli kurulup kurulmadığı, eşin rızası, sorumluluk üst sınırı veya kefilin sorumluluktan kurtulması söz konusu olduğunda; kefaletin sıkı şekil ve koruma rejimini denetlemek için kullanılır."
---

# Kefalet — Geçerlilik Şekli, Eş Rızası ve Sona Erme

## Görev
Kefaletin TBK m.581-603 kapsamındaki sıkı geçerlilik şartlarını, kefilin sorumluluk sınırını ve sona erme/düşme hallerini denetlemek; çoğu uyuşmazlığın şekil eksikliğinde düğümlendiğini gözeterek geçerlilik testini önce yapmak.

## Soğuk başlangıç (intake)
- Kefalet yazılı mı; el yazısıyla azami miktar ve tarih var mı?
- Kefilin eşi var mı, rızası alınmış mı (istisnalar var mı)?
- Kefalet türü (adi/müteselsil); süreli mi süresiz mi?
- Asıl borcun durumu (muaccel mi, takip yapıldı mı)?

## Denetim şeması
1. **Şekil (m.583).** Kefalet yazılı olmalı; **kefilin el yazısıyla** sorumlu olduğu azami miktar, kefalet tarihi ve müteselsil kefalette bu sıfat belirtilmeli. Eksiklik kesin hükümsüzlük doğurur — ilk kontrol budur.
2. **Eş rızası (m.584).** Evli kişinin kefaletinde, kefalet anında veya en geç sözleşme kurulurken eşin yazılı rızası şart; sonradan değişiklik ağırlaştırıyorsa yeniden rıza. İstisnalar (ticaret siciline kayıtlı tacirin işi, mesleki faaliyet vb.) dar yorumlanır.
3. **Tür ve başvuru.** Adi kefalette önce asıl borçluya başvurma (tartma def'i, m.585); müteselsil kefilde alacaklı doğrudan kefile gidebilir (m.586). Kefil, asıl borçlunun def'ilerini ileri sürebilir (m.591).
4. **Sorumluluk kapsamı (m.589).** Azami miktarla sınırlı; faiz, takip giderleri belirli koşullarla eklenir.
5. **Sona erme/düşme (m.598-600).** Gerçek kişi kefaletinde süre kararlaştırılmasa da 10 yılın sonunda kendiliğinden sona erer (m.598/3). Süreli kefalette sürenin sonunda alacaklı bir ay içinde takip/dava yapmazsa kefil kurtulur (m.600). Alacaklının kefili gözetme yükümü ve teminatları koruma (m.592).
6. **İspat.** Geçerli kefaleti (şekil + eş rızası) alacaklı; düşme/sona erme şartlarını kefil ispatlar. Ara sonuç: geçerlilik + sorumluluk tavanı + güncel durum.

## Çıktı modülleri
- Geçerlilik kontrol listesi (şekil + eş rızası).
- Kefile karşı/ kefil lehine savunma stratejisi notu.
- Sona erme/düşme savunması dilekçe iskeleti.

## Plugin bağlamı

Bu beceri `borclar-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
