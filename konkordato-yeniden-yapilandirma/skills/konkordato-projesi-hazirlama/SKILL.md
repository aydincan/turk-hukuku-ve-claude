---
name: konkordato-projesi-hazirlama
description: "Konkordato ön projesini ve projesini ekonomik olarak gerçekçi, tasdik şartlarını karşılayacak biçimde hazırlamak veya mevcut projeyi denetlemek gerektiğinde kullanılır."
---

# Konkordato Projesi ve Ön Proje Hazırlama

## Görev
İİK m.286'ya uygun konkordato ön projesini ve nihai projeyi hazırlamak veya denetlemek; tenzilat/vade/karma yapısını, kaynak planını ve alacaklı sınıflandırmasını tasdik şartlarına (m.305) uyacak şekilde kurmak.

## Soğuk başlangıç (intake)
- Önerilen yapı: alacaktan indirim mi, vade mi, karma mı? Oran ve süreler?
- Ödeme kaynağı: işletme faaliyeti, sermaye artırımı, varlık satışı, yeni finansman?
- Alacaklı sınıfları: rehinli, imtiyazlı (m.206), adi alacaklılar nasıl dağılıyor?
- Makul güvence veren denetim raporu mevcut mu?

## Denetim şeması
1. **Ön proje içeriği (m.286/a).** Alacaklıların hangi oranda alacağından vazgeçeceği veya vadenin nasıl tanınacağı, ödeme planı; ödemelerin nasıl finanse edileceği açıkça gösterilmeli.
2. **Belge seti (m.286/b-e).** Mal varlığı durumunu gösteren belgeler, finansal tablolar, ara bilanço, alacaklı/alacak listesi, makul güvence veren bağımsız denetim raporu (KGK denetim standartları). İspat: projenin sayısal varsayımları belgeyle desteklenmeli.
3. **Kaynak gerçekçiliği.** Nakit akış projeksiyonu ile ödeme planı tutarlı mı? İmtiyazlı alacakların (m.206) tam ödeneceği güvenceye bağlanmış mı (m.305 şartı)?
4. **Alacaklı eşitliği.** Aynı sınıftaki alacaklılara eşit muamele; farklı sınıflar arasında haklı ayrım gerekçesi. Rehinli alacaklılarla yapılan ayrı düzenleme (m.308/h) ayrıca ele alınır.
5. **Tasdik süzgeci.** Teklifin borçlunun kaynaklarıyla orantılılığı (m.305/1-a), çoğunluk (m.302) ve depo şartları önceden test edilir. Ara sonuç: proje tasdik edilebilir nitelikte mi.

## Çıktı modülleri
- Konkordato ön projesi taslağı (yer tutuculu).
- Ödeme planı ve nakit akış tablosu iskeleti.
- Alacaklı sınıflandırma ve oran tablosu.
- Tasdik şartı uyum kontrol listesi.

## Plugin bağlamı

Bu beceri `konkordato-yeniden-yapilandirma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
