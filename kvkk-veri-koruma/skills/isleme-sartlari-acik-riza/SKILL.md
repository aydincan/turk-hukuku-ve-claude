---
name: isleme-sartlari-acik-riza
description: "Bir veri işleme faaliyetinin hangi hukuki sebebe dayandığını belirlemek, açık rıza yerine m.5/m.6 istisnalarının uygulanıp uygulanmayacağını değerlendirmek gerektiğinde kullanılır."
---

# İşleme Şartları ve Açık Rıza Denetimi

## Görev
Somut bir işleme faaliyetinin KVKK m.5 (genel veri) veya m.6 (özel nitelikli veri) çerçevesinde hangi hukuki sebebe oturduğunu saptamak; açık rıza refleksinin tuzaklarından kaçınıp daha sağlam istisnaları tercih etmek.

## Soğuk başlangıç (intake)
1. İşlemenin somut amacı nedir, hangi faaliyetin parçasıdır?
2. Veri genel mi, özel nitelikli mi?
3. Bir kanun, sözleşme ya da hukuki yükümlülük bu işlemeyi zaten gerektiriyor mu?
4. Şu an dayanılan sebep açık rıza mı; rıza geri alınırsa faaliyet durur mu?

## Denetim şeması
1. **Genel veri — m.5**: Önce açık rıza dışı şartları sırayla dene: (a) kanunlarda açıkça öngörülme, (b) ilgili kişinin fiili imkânsızlık nedeniyle rıza veremediği hal, (c) sözleşmenin kurulması/ifası için zorunluluk, (ç) veri sorumlusunun hukuki yükümlülüğünü yerine getirmesi, (d) ilgili kişinin kendisi tarafından alenileştirme, (e) bir hakkın tesisi/kullanılması/korunması için zorunluluk, (f) meşru menfaat (ilgili kişinin temel hak ve özgürlüklerine zarar vermemek kaydıyla, denge testiyle).
2. **Meşru menfaat dengesi**: m.5/2-f en esnek ama en tartışmalı sebeptir; menfaatin meşruluğu, işlemenin gerekliliği ve ilgili kişi üzerindeki etkisi tartılarak yazılı denge testi (LIA) belgelenmelidir.
3. **Özel nitelikli veri — m.6** (7499 ile 01.06.2024'ten itibaren): açık rıza ya da m.6/3'te sayılan haller (kanunda öngörülme, fiili imkânsızlık, alenileştirme, hakkın tesisi, sağlık/cinsel hayat verisinin sır saklama yükümlüsünce kamu sağlığı vb. amaçla işlenmesi, istihdam ve sosyal güvenlik yükümlülükleri, vakıf-dernek-sendika faaliyetleri). Eski "sağlık dışı/sağlık" ayrımına dayalı ezberi kullanma; güncel metni esas al.
4. **Ara sonuç**: Açık rıza yalnızca başka şart bulunmadığında seçilir; rızaya dayanan işlemede rızanın her an geri alınabileceği (m.11) unutulmamalıdır.

İspat yükü: Geçerli işleme şartının varlığı veri sorumlusundadır; açık rızanın özgür/bilgilendirilmiş/belirli olduğunu da o ispatlar.

## Çıktı modülleri
- İşleme faaliyeti — hukuki sebep eşleştirme tablosu.
- Meşru menfaat denge testi (LIA) taslağı.
- Açık rıza yerine geçecek alternatif sebep önerisi notu.

## Plugin bağlamı

Bu beceri `kvkk-veri-koruma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
