---
name: sureler-zamanasimi-ve-takip-takvimi
description: "İcra-iflas dosyasındaki tüm hak düşürücü süreleri, takip ve dava zamanaşımlarını ve dosyanın işlemden kalkmaması için kritik tarihleri tek tabloda çıkarmak gerektiğinde kullanılır."
---

# Süreler, Zamanaşımı ve Takip Takvimi

## Görev
Dosyadaki bütün süreleri (itiraz, şikâyet, dava açma, haciz/satış isteme, zamanaşımı) tek bir takvimde toplamak; süre kaçırma ve dosyanın işlemden kalkması riskini önlemek.

## Soğuk başlangıç (intake)
- Takip yolu hangisi (ilamsız/ilamlı/kambiyo)?
- Ödeme/icra emri tebliğ tarihi nedir?
- Hangi aşamadayız (itiraz, haciz, satış, dağıtım)?
- Alacağın maddi hukuk zamanaşımı ne (TBK/TTK)?

## Denetim şeması
1. **İtiraz süreleri**: İlamsızda ödeme emrine itiraz 7 gün (m.62); kambiyoda borca/imzaya itiraz 5 gün (m.168/4-5). Süreler tebliğden işler ve kesindir.
2. **Dava süreleri**: İtirazın iptali 1 yıl (m.67); itirazın kaldırılması 6 ay (m.68); istirdat 1 yıl (m.72); tasarrufun iptali 5 yıllık zamanaşımı (m.284); ihalenin feshi 7 gün (m.134).
3. **Takip işlemleri süreleri**: Haciz isteme 1 yıl (m.78); satış isteme süreleri ve elektronik artırma takvimi; aksi halde haciz/dosya düşer ve yenileme gerekir.
4. **Takip zamanaşımı vs. maddi hukuk zamanaşımı**: İlama dayalı alacakta ilamların zamanaşımı 10 yıl (m.39); ilamsız alacakta dayanağın maddi hukuk zamanaşımı (TBK m.146 genel 10 yıl, m.147 istisnalar 5 yıl; kambiyoda TTK özel süreleri; çekte 5941 s.K.) ayrıca denetlenir.
5. **Sürelerin durması/kesilmesi**: Adli tatil, takip işlemleri ve dava açılmasıyla kesilme; her tarih için dayanağı not edilir.
6. **Ara sonuç**: Kritik tarihlerin renk kodlu takvimi ve uyarı eşikleri oluşturulur.

## Çıktı modülleri
- Tek tablo süre/zamanaşımı takvimi (tarih × işlem × dayanak).
- Yenileme/düşme uyarı listesi.
- Maddi hukuk + takip zamanaşımı çapraz kontrolü.

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
