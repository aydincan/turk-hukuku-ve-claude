---
name: iflas-yollari-ve-masasi
description: "Borçlunun iflasını istemek (takipli/doğrudan iflas), iflas davasını yürütmek, iflasın açılmasının sonuçlarını ve masanın tasfiyesini yönetmek gerektiğinde; tacirin iflası, alacak kaydı ve sıra cetveli için kullanılır."
---

# İflas Yolları ve İflas Masası

## Görev
İflasa tabi borçlu hakkında takipli iflas (m.155 vd.) veya doğrudan doğruya iflas (m.177) yolunu seçmek; iflas davasını ticaret mahkemesinde yürütmek; iflasın açılmasının sonuçlarını ve masanın tasfiyesini (adi/basit) yönetmek.

## Soğuk başlangıç (intake)
- Borçlu İİK m.43 anlamında iflasa tabi mi (tacir/şirket)?
- Takipli iflas için ödeme emrine itiraz/ödeme yapıldı mı; depo süresi işledi mi?
- Doğrudan iflas sebeplerinden biri (m.177) var mı?
- Alacaklı isen alacağını masaya kaydettirme süresi geçti mi?

## Denetim şeması
1. **Takipli iflas (m.155-166)**: İflas yoluyla takip talebi → iflas ödeme emri → itiraz edilmez/ödenmezse alacaklı 1 yıl içinde ticaret mahkemesinde iflas davası açar. Mahkeme depo kararı verir; borç ödenmezse iflasa karar verilir.
2. **Doğrudan iflas (m.177-178)**: Borçlunun yerinin bilinmemesi, taahhütlerden kaçınması, ödemelerin tatili gibi hallerde takip şartı aranmadan iflas istenir; borçlu da kendi iflasını isteyebilir (m.178).
3. **İflasın açılması sonuçları (m.184 vd.)**: Borçlunun malları iflas masasını oluşturur; tasarruf yetkisi kısıtlanır; takipler durur, müflisin alacakları muaccel hale gelir.
4. **Tasfiye usulü**: Masa, adi (m.208 vd.) veya basit tasfiye (m.218) ile tasfiye edilir; iflas idaresi ve alacaklılar toplantısı görev yapar.
5. **Alacak kaydı ve sıra (m.206-207)**: Alacaklılar alacağını kaydettirir; iflas idaresi sıra cetveli düzenler; itiraz icra/ticaret mahkemesi ayrımına göre yürütülür.
6. **Ara sonuç**: İflas kararının ihtimali, tasfiye türü ve alacak tahsil beklentisi belirlenir.

## Çıktı modülleri
- İflas yolu seçim notu ve dava dilekçesi iskeleti.
- Masaya alacak kaydı ve takip durumu tablosu.
- Tasfiye/sıra cetveli akış planı.

## Plugin bağlamı

Bu beceri `icra-iflas-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
