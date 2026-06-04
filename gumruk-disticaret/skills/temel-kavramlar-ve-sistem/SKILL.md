---
name: temel-kavramlar-ve-sistem
description: "Gümrük rejimleri, gümrük yükümlülüğü, kıymet-menşe-tarife üçlüsü ve gümrük işleminin temel akışını çözmek gerektiğinde; bir gümrük uyuşmazlığını doğru çerçeveye oturtmadan önce sistematiği kurmak için kullanılır."
---

# Temel Kavramlar ve Gümrük Sistematiği

## Görev
Bir gümrük olayını doğru kavramsal çerçeveye oturtmak: eşyanın hangi rejime tabi olduğunu, gümrük yükümlülüğünün ne zaman doğduğunu, matrahı oluşturan kıymet-menşe-tarife üçlüsünü ve işlem akışını netleştirmek.

## Soğuk başlangıç (intake)
- Eşya nedir, GTİP biliniyor mu, hangi gümrük idaresinden işlem gördü?
- Hangi rejim uygulandı (serbest dolaşıma giriş, antrepo, dahilde işleme, transit, geçici ithalat)?
- Beyan edilen kıymet, menşe ülke ve menşe ispat belgesi (EUR.1, A.TR, menşe şahadetnamesi) var mı?
- İşlem tamamlandı mı, yoksa sonradan kontrol/inceleme mi söz konusu?

## Denetim şeması
1. Rejim tespiti: Eşya 4458 m.46-49 uyarınca gümrükçe onaylanmış işlem/kullanıma tabi mi? Serbest dolaşıma giriş (m.74) ile şartlı muafiyet/ekonomik etkili rejimler (antrepo, dahilde işleme, geçici ithalat) ayrımını yap. Şartlı rejimlerde yükümlülük askıdadır.
2. Gümrük yükümlülüğünün doğması: İthalatta yükümlülük kural olarak beyannamenin tescili anında doğar (4458 m.181). Usulsüz giriş, izinsiz çıkarma veya şartlara aykırılık halinde m.182-184 uygulanır. Doğum anı oran/kur ve zamanaşımı için kritiktir.
3. Matrah üçlüsü:
   - Kıymet: kural satış bedeli yöntemi (m.24); yurt dışı navlun, sigorta, royalti gibi ilaveler (m.27) ve indirilebilir kalemler (m.28) kontrol edilir.
   - Menşe: tercihsiz menşe (m.18-21) ve tercihli menşe (anlaşmalar) ayrılır; menşe ispat belgesi varsa indirimli/sıfır oran uygulanır.
   - Tarife/sınıflandırma: GTİP doğru mu; Tarife Cetveli ve İzahname ile teyit; tereddütte BTB başvurusu.
4. İspat yükü ve belge: Beyanın doğruluğunu kural olarak yükümlü ispatlar; idare aksini ortaya koyarken somut tespit ve karşı delil sunmalıdır. Beyanname ekleri, fatura, taşıma/sigorta belgeleri, ekspertiz/laboratuvar raporları dosyalanır.
5. Ara sonuç: Olayın rejimi, yükümlülüğün doğum anı ve matrah parametreleri saptanır; uyuşmazlığın kıymet/menşe/sınıflandırma/oran eksenlerinden hangisinde olduğu belirlenir.

## Çıktı modülleri
- Eşya-rejim-matrah künyesi (GTİP, kıymet kalemleri, menşe, oran)
- Uyuşmazlık eksen tespiti ve açık nokta listesi
- Eksik belge ve ek araştırma önerileri

## Plugin bağlamı

Bu beceri `gumruk-disticaret` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
