---
name: temel-kavramlar-ve-sistem
description: "Sebepsiz zenginleşmenin ne olduğunu, hangi borç kaynağına girdiğini ve haksız fiil ile sözleşmeden farkını netleştirmek gerektiğinde; bir uyuşmazlığın gerçekten sebepsiz zenginleşme olup olmadığını ilk anda teşhis etmek için kullanılır."
---

# Temel Kavramlar ve Sistematik

## Görev
Eldeki malvarlığı kaymasının sebepsiz zenginleşme borç ilişkisi (TBK m.77 vd.) doğurup doğurmadığını teşhis etmek; bu kurumu sözleşme, haksız fiil ve vekâletsiz iş görmeden ayırarak doğru hukuki çerçeveyi kurmak. Yanlış çerçeve, ölçüyü (zenginleşme mi, zarar mı), süreyi ve faizi kökünden değiştirir.

## Soğuk başlangıç (intake)
- Bir malvarlığı değeri bir taraftan diğerine mi geçti; ne (para, mal, emek, kullanım yararı)?
- Bu geçişin arkasında geçerli bir sebep (sözleşme, kanun, mahkeme kararı) var mı?
- Taraflar arasında hâlâ ayakta bir sözleşme ilişkisi mevcut mu?
- Kayma kimin fiiliyle oldu (fakirleşenin ödemesi mi, zenginleşenin müdahalesi mi)?

## Denetim şeması
1. **Borç kaynağını ayır.** Sebepsiz zenginleşme, sözleşme ve haksız fiilin yanında üçüncü bağımsız kaynaktır (TBK m.77). Amacı denkleştirici adalet; ceza veya zarar tazmini değil. Ölçü daima "zenginleşme miktarı"dır.
2. **Dört unsuru sına (m.77/1).** (a) Zenginleşme (aktif artışı veya pasif azalması), (b) fakirleşme (malvarlığından veya emeğinden), (c) ikisi arasında illiyet bağı, (d) haklı sebebin yokluğu. Dördü birlikte aranır.
3. **Talep türünü belirle.** Edim sebepsiz zenginleşmesi (fakirleşenin bilinçli kazandırması) ile müdahale (haksız kullanım, başkasının malını harcama) sebepsiz zenginleşmesini ayır; ispat yükü ve kapsam farklılaşır.
4. **Yarışmayı kontrol et (tali nitelik).** Aynî istihkak (TMK m.683), sözleşmenin ifası veya haksız fiil (TBK m.49) talebi mümkünse kural olarak ona öncelik verilir; sebepsiz zenginleşme ikincil/tamamlayıcıdır. Vekâletsiz iş görme (TBK m.526 vd.) varsa onun özel hükümleri uygulanır.
5. **Ara sonuç.** Uygulanacak madde bloğu (m.77-82), talebin tipi ve görevli mahkeme netleşir; ispat yükü genel kural TMK m.6 ile dağıtılır: haklı sebebin yokluğunu iade isteyen ispatlar.

## Çıktı modülleri
- Nitelendirme notu (kaynak + tip + dayanak madde + gerekçe).
- Yarışma analizi (öncelikli talep var mı tablosu).
- Yanlış çerçeve riski uyarısı (zarar/zenginleşme ölçü farkı).

## Plugin bağlamı

Bu beceri `sebepsiz-zenginlesme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
