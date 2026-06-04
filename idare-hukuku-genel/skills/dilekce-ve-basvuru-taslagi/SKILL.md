---
name: dilekce-ve-basvuru-taslagi
description: "İdari yargıda iptal/tam yargı dava dilekçesi ile İYUK m.11/m.13 idari başvuru ve dilekçe hakkı başvurularının taslağını üretmek için kullanılır; somut bir metin istendiğinde başvurulur."
---

# Dava Dilekçesi ve İdari Başvuru Taslağı

## Görev
İYUK formatına uygun dava dilekçesi (iptal/tam yargı) ve idari başvuru (m.11/m.13, dilekçe hakkı) metinlerini, yer tutucu disipliniyle üretmek. Dilekçe, önceki becerilerin çıktısını birleştirir.

## Soğuk başlangıç (intake)
1. Hangi metin gerekiyor (iptal dilekçesi, tam yargı dilekçesi, m.11 başvurusu, m.13 başvurusu)?
2. Taraflar, dava konusu işlem ve tebliğ tarihi belli mi?
3. İptal sebepleri ve/veya tazminat kalemleri hazır mı?
4. Yürütmenin durdurulması talep edilecek mi?

## Denetim şeması
1. **Zorunlu unsurlar.** İYUK m.3: davacı/davalı idare, dava konusu işlem ve tebliğ tarihi, olayların özeti, hukuki sebepler, talep sonucu, deliller. Eksik unsur m.15/1-d uyarınca düzeltme/ret sebebidir.
2. **Yapı.** (a) Davalı idare ve dava konusu, (b) tebliğ/öğrenme tarihi ve süre tutar açıklaması, (c) olaylar (kronolojik, tarafsız), (d) hukuki açıklamalar (beş unsur denetiminden gelen sebepler, madde atıflarıyla), (e) yürütmenin durdurulması talebi ve gerekçesi (m.27), (f) deliller, (g) talep sonucu (net ve sayılı).
3. **Talep sonucu disiplini.** İptal davasında "işlemin iptali"; tam yargıda miktar belirterek "… TL maddi/manevi tazminatın … tarihinden işleyecek faiziyle tahsili". Belirsiz alacakta usulü gözet.
4. **İdari başvuru metni.** m.11: işlemin kaldırılması/değiştirilmesi talebi ve sürenin durduğuna dikkat çekme. m.13: eylem ve zararın somutlaştırılması, tazminat talebi.
5. **Yer tutucu disiplini.** Eksik bilgi için `[doldurulacak: …]` kullan; uydurma tarih/sayı/karar künyesi yazma. İçtihat atfını `[doğrulanacak]` ile işaretle.
6. **Ara sonuç.** Eksiksiz, atıfları doğru, talep sonucu net taslak metin.

## Çıktı modülleri
- İptal/tam yargı dava dilekçesi taslağı (İYUK m.3 unsurlarıyla).
- m.11/m.13 idari başvuru dilekçesi taslağı.
- Yürütmenin durdurulması talep paragrafı.
- Doldurulacak alanlar ve eklenecek belgeler listesi.

## Plugin bağlamı

Bu beceri `idare-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
