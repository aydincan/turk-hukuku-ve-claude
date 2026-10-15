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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
