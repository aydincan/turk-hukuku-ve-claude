---
name: sozlesme-anatomisi-ve-tip-tespiti
description: "Bir sözleşme taslağını ilk kez ele alırken metnin türünü, taraf konumunu, uygulanacak hukuku ve emredici rejimi saptamak, inceleme planını kurmak gerektiğinde kullanılır."
---

# Sözleşme Anatomisi ve Tip Tespiti

## Görev
Önündeki metnin sözleşme tipini (isimli/isimsiz/karma), tarafların hukuki sıfatını, müvekkilin konumunu ve uygulanacak emredici rejimi belirleyerek tüm inceleme stratejisinin iskeletini kurmak.

## Soğuk başlangıç (intake)
- Müvekkil hangi taraf ve taslağı kim hazırladı (lehe kurgu beklenir)?
- Taraflar tacir mi, tüketici mi, işçi/işveren mi, kamu tüzel kişisi mi?
- Sözleşme tek seferlik mi (satış) yoksa sürekli/yenilenen mi (kira, hizmet, distribütörlük)?
- Uygulanacak hukuk ve dil kararlaştırılmış mı; yabancılık unsuru var mı?

## Denetim şeması
1. **Tip tespiti**: TBK İkinci Kısım isimli sözleşmelere (satış m.207, kira m.299, eser m.470, vekâlet m.502, kefalet m.581) köprü kur; karma/atipik ise TBK genel hükümler ve kıyas. Tip, hangi emredici/tamamlayıcı kuralın boşlukları dolduracağını belirler.
2. **Taraf sıfatı süzgeci**: Tüketici işlemi ise TKHK m.5 (haksız şart) ve cayma/koruma hükümleri; iş sözleşmesi ise İş K. emredici asgari haklar; iki tacir arası ise TTK m.18-22 (basiretli tacir, m.22 cezai şart/fahiş şart sınırı) ve yetki sözleşmesi serbestisi (HMK m.17).
3. **Serbesti-emredici sınırı**: TBK m.26 serbesti, m.27 sınır. Hangi maddeler pazarlık alanında, hangileri emredici koruma altında ayrıştırılır.
4. **Şekil**: Geçerlilik şekline tabi mi (taşınmaz satış vaadi resmî şekil, kefalet TBK m.583 el yazısı miktar/tarih, tüketici kredisi yazılı)? Şekil eksikliği kesin hükümsüzlük doğurur.
5. **İspat/dil**: İmza, nüsha, ek-metin ve çeviri çatışması riski; çelişki hâlinde hangi metin esas (m.23 aleyhe yorum hatırlanır).
6. **Ara sonuç**: Sözleşme haritası ve hangi alt-becerilerin (risk dağılımı, sorumluluk, fesih, uyuşmazlık) önceliklendirileceği.

## Çıktı modülleri
- Sözleşme künyesi (tip, taraf sıfatı, uygulanacak hukuk, emredici rejim).
- Madde-bölüm haritası ve eksik standart madde listesi.
- İnceleme yol haritası ve öncelikli risk alanları.

## Plugin bağlamı

Bu beceri `sozlesme-inceleme-redline` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
