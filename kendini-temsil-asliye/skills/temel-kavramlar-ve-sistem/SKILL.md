---
name: temel-kavramlar-ve-sistem
description: "Davasını avukatsız takip etmek isteyen kişi temel kavramları (asil, dava ehliyeti, görev, dava şartı arabuluculuk) öğrenmek istediğinde ve uyuşmazlığını doğru kategoriye yerleştirmek istediğinde kullanılır."
---

# Temel Kavramlar ve Kendini Temsil Sistemi

## Görev
Davasını avukatla değil bizzat takip edecek kişiye sistemin haritasını çıkarmak: kim, hangi mahkemede, hangi ön koşulla, nasıl dava açabilir veya başvuru yapabilir.

## Soğuk başlangıç (intake)
- Uyuşmazlık ne hakkında (alacak, kira, tüketici, zilyetlik, mülkiyet, tazminat)?
- Karşı taraf gerçek kişi mi, şirket mi, kamu kurumu mu?
- Talep ettiğiniz tutar veya konunun değeri yaklaşık nedir?
- Daha önce başvuru, ihtar veya arabuluculuk yapıldı mı?
- Tarafsınız mı yoksa başkası adına mı hareket ediyorsunuz (vekâlet/veli/vasi)?

## Denetim şeması
1. **Dava ehliyeti ve takip yetkisi (HMK m.50-52, 71):** Taraf tam fiil ehliyetine sahipse davasını kendisi açıp takip edebilir; avukat zorunlu değildir. Kısıtlı/küçük ise yasal temsilci (veli-vasi) gerekir. Tüzel kişi adına ancak yetkili organ/temsilci hareket eder.
2. **Görev (dava şartı, HMK m.114/1-c, m.1):** Görev kanunla belirlenir, taraflar değiştiremez, re'sen incelenir. Sulh hukukun görev alanı HMK m.4'te sayılıdır (kira, paydaşlığın giderilmesi, zilyetlik). Aksi belirtilmedikçe genel görevli asliye hukuktur (m.2). Tüketici işlemi varsa tüketici hakem heyeti/tüketici mahkemesi (6502 sayılı Kanun).
3. **Zorunlu ön başvuru:** Dava şartı arabuluculuk; ticari, tüketici, kira, ortaklığın giderilmesi gibi uyuşmazlıklarda dava açmadan önce zorunludur (7036/6325 sayılı düzenlemeler) — atlanırsa dava usulden reddedilir. Tüketici uyuşmazlığında parasal sınır altı işlerde önce hakem heyeti zorunludur.
4. **Yargılama usulü:** Sulh hukuk ve kanunda sayılan işler basit yargılamaya tabidir (HMK m.316). Basit yargılamada dilekçe teatisi kısadır ve cevaba cevap/ikinci cevap yoktur.
5. **Ara sonuç:** Doğru forum + zorunlu ön koşul + ehliyet tamamsa dava/başvuru yoluna geçilir; eksikse önce o giderilir.

## Çıktı modülleri
- Uyuşmazlık sınıflandırma kartı (forum + usul + ön koşul).
- Yapılması gerekenler kontrol listesi (sırasıyla).
- Atlanması durumunda risk uyarıları.

## Plugin bağlamı

Bu beceri `kendini-temsil-asliye` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
