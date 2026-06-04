---
name: ticari-sozlesme-ve-belge-taslagi
description: "Tacirler arasi cerceve/mal alim/hizmet sozlesmesi, cari hesap sozlesmesi, fatura itiraz veya temerrut ihtarnamesi ile ticaret sicili basvurusu gibi belgelerin TTK emredici hukumlerine uygun taslagini uretmek gerektiginde kullanilir."
---

# Ticari Sözleşme, İhtarname ve Başvuru Taslağı

## Görev
Ticari işletme hukuku alanında işleme uygun, TTK emredici hükümlerine ve uygulama gerçeğine uygun belge taslağı üretmek: sözleşme, ihtarname veya sicil başvurusu. Belge, yer tutucu disipliniyle hazırlanır.

## Soğuk başlangıç (intake)
1. Hangi belge isteniyor (sözleşme türü / ihtarname / sicil başvurusu)?
2. Taraflar kim; tacir sıfatları ve unvanları ne?
3. Konu, bedel, vade, faiz ve teminat parametreleri belli mi?
4. Müvekkil hangi tarafta; risk toleransı ve pazarlık gücü ne?

## Denetim şeması
1. **Belge tipini ve zorunlu içeriği belirle:** Sözleşmede taraf kimlikleri (unvan + sicil no), konu, edim, bedel/faiz (TTK m.8 serbestisi), teslim/ifa, ayıp ve temerrüt, fesih, uygulanacak hukuk ve uyuşmazlık çözümü (yetki/tahkim — HMK m.17/tahkim şartı). İhtarnamede: muaccel borç, dayanak, verilen süre, sonuç ihtarı; tebliğ usulü TTK m.18/3'e uygun (noter/iadeli taahhütlü/KEP).
2. **Emredici süzgeç:** TTK ve TBK emredici hükümleri (örn. cezai şart indirimi — tacir m.22 ile indirim isteyemez; bunu sözleşmede aleyhe kullan/lehte koru), genel işlem koşulları denetimi (TBK m.20-25; haksız rekabet m.55/1-f), tüketici işlemiyse TKHK önceliği. Geçersiz/asimetrik şartları işaretle.
3. **Faiz ve süre fıkraları:** Ticari temerrüt faizi/avans faizi (3095 m.2) ve fatura itiraz süresine (TTK m.21: 8 gün) atıf; cari hesapta yazılı şekil (TTK m.89) ve dönem sonu bakiye (m.94) hükümleri.
4. **Yer tutucu disiplini:** Bilinmeyen her veri `[doldurulacak: ...]` olarak bırakılır; varsayım yapılmaz, varsayım yapılmışsa açıkça not düşülür.
5. **Ara sonuç:** Taslak, zorunlu unsurlar + emredici süzgeç + müvekkil lehine dengeli risk dağılımı ile tamamlanır; karşı tarafın değiştirmek isteyeceği maddeler ayrıca işaretlenir.

## Çıktı modülleri
- Belge taslağı (madde başlıkları ve yer tutucularla).
- Riskli/müzakere edilecek madde notları (lehte/aleyhte).
- Tebliğ ve süre takip uyarıları (TTK m.18/3, m.21, zamanaşımı).

## Plugin bağlamı

Bu beceri `ticari-isletme-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
