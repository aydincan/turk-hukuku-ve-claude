---
name: temel-kavramlar-ve-sistem
description: "Bir uyuşmazlıkta hangi kişi türünün ve hangi ehliyet katmanının söz konusu olduğunu, meselenin gerçek/tüzel kişi ya da koruma/ehliyet eksenine düştüğünü konumlandırmak için kullanılır."
---

# Kişiler Hukuku Temel Kavramları ve Sistematiği

## Görev
Somut olayın kişiler hukuku içindeki yerini sabitlemek: süjenin türü (gerçek/tüzel kişi), ehliyet durumu ve uyuşmazlığın hangi alt-rejime (ehliyet, kişilik hakkı koruması, ad, yerleşim yeri, dernek/vakıf) düştüğünü belirleyip doğru denetim şemasına yönlendirmek.

## Soğuk başlangıç (intake)
- Süje kim: gerçek kişi mi, dernek/vakıf/şirket gibi tüzel kişi mi?
- Gerçek kişiyse ehliyet durumu ne: ergin mi (18+), küçük mü, ayırt etme gücü var mı, kısıtlı/vesayet altında mı?
- Uyuşmazlık bir işlemin geçerliliği mi, yoksa kişilik değerine (şeref, beden, özel hayat, ad) bir saldırı mı?
- Hangi sonuç isteniyor: işlemin iptali/butlanı, saldırının durdurulması, tazminat, ad değişikliği, tescil?

## Denetim şeması
1. **Süje ayrımı** — Gerçek kişi (TMK m.8 vd.) mi tüzel kişi (m.47 vd.) mi? Tüzel kişide tür (dernek m.56 vd., vakıf m.101 vd., ticaret şirketi) ve organ yapısı (m.50) belirlenir.
2. **Hak ehliyeti** — TMK m.8: herkes eşit hak ehliyetine sahiptir; m.28: kişilik sağ ve tam doğumla başlar, ölümle biter; cenin koşullu hak ehlidir.
3. **Fiil ehliyeti katmanları** — TMK m.9-16: (a) tam ehliyetli (ergin + ayırt etme gücü + kısıtlı değil); (b) tam ehliyetsiz (ayırt etme gücü yok, m.14-15); (c) sınırlı ehliyetsiz (ayırt etme gücü olan küçük/kısıtlı, m.16); (d) sınırlı ehliyetli (kendisine yasal danışman atanan, m.429). Hangi katman, işlemin tek başına yapılıp yapılamayacağını belirler.
4. **Eksen seçimi** — İşlem geçerliliği sorunuysa ehliyet/temsil becerisine; kişilik değerine saldırı varsa m.24-25 koruma şemasına; ad sorunuysa m.26-27 becerisine; tüzel kişi sorunuysa dernek/vakıf becerisine yönlendir.
5. **Genel süzgeç** — TMK m.2 dürüstlük kuralı her sonucu denetler; ehliyetsizliğin dürüstlüğe aykırı biçimde ileri sürülmesi korunmaz.

## Çıktı modülleri
- Süje ve ehliyet teşhis tablosu (tür + katman + dayanak madde).
- Uyuşmazlığın düştüğü alt-rejim ve yönlendirilecek beceri.
- Görevli/yetkili mahkeme ön notu (TMK m.19 yerleşim yeri).
- Açık sorular ve `[doldurulacak]` veri yerleri.

## Plugin bağlamı

Bu beceri `kisiler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
