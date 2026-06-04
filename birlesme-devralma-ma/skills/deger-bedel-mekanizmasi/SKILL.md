---
name: deger-bedel-mekanizmasi
description: "İşlem bedelinin yapılandırılması, kapanış bilançosu düzeltmesi, locked-box, earn-out ve escrow mekanizmalarının hukuki olarak tasarlanması ve uyuşmazlık riskinin azaltılması için kullanılır."
---

# Değerleme, Bedel ve Earn-Out Mekaniği

## Görev
İşlem bedelinin hukuki yapısını kurmak; düzeltme, earn-out ve teminat mekanizmalarını uyuşmazlığa dayanıklı biçimde tasarlamak.

## Soğuk başlangıç (intake)
- Bedel sabit mi, kapanış hesaplarına göre düzeltmeli mi?
- Locked-box mu, completion accounts mu tercih ediliyor?
- Earn-out hangi metriğe (ciro, FAVÖK) bağlanacak ve süresi ne?
- Bedelin bir kısmı escrow/teminatta tutulacak mı?

## Denetim şeması
1. **Bedel yapısı**: Satış bedeli TBK m.207 anlamında belirli veya belirlenebilir olmalıdır; belirlenebilir bedelde objektif formül şarttır, aksi halde geçersizlik/uyuşmazlık riski.
2. **Locked-box**: Referans bilanço tarihinden sonra değer kaçışına (leakage) karşı satıcı taahhüdü ve tazminatı.
3. **Completion accounts**: Kapanış sonrası net borç/işletme sermayesi düzeltmesi; uzman/bağımsız denetçi başvurma mekanizması (expert determination).
4. **Earn-out**: Metrik tanımı, ölçüm dönemi, alıcının işletmeyi olağan yürütme taahhüdü; manipülasyon riskine karşı iyiniyet (TMK m.2) ve özel koruyucu klozlar.
5. **Escrow**: Beyan-tekeffül ihlali tazminatına teminat; serbest bırakma takvimi ve şartları.
6. **Vergi etkisi**: Bedel yapısının değer artış kazancı/KDV/damga açısından sonuçları gözetilir.
7. **İspat yükü**: Düzeltme/earn-out talebini ileri süren taraf metriğin gerçekleştiğini ispatlar.

## Çıktı modülleri
- Bedel mekaniği şeması ve formül lafzı
- Earn-out koruyucu klozları
- Escrow sözleşmesi ana hatları
- Vergi etkisi notu

## Plugin bağlamı

Bu beceri `birlesme-devralma-ma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
