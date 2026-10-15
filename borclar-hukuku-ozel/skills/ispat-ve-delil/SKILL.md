---
name: ispat-ve-delil
description: "Sözleşmenin varlığı, içeriği, ifa, ayıp veya ödeme gibi vakıaların nasıl ispatlanacağını, ispat yükünün kimde olduğunu ve hangi delillerin kabul edileceğini belirlemek gerektiğinde kullanılır."
---

# İsimli Sözleşmelerde İspat ve Delil

## Görev
Sözleşme uyuşmazlığında ispat yükünü TMK m.6 ve tipe özgü kurallara göre dağıtmak, senetle ispat zorunluluğu ve istisnalarını (HMK m.200-203) uygulamak, delil planı kurmak.

## Soğuk başlangıç (intake)
- İspatı gereken vakıa ne (kuruluş, içerik, ifa, ayıp, ödeme)?
- Yazılı sözleşme/senet var mı; bedel miktarı senet sınırını aşıyor mu?
- Eldeki deliller (fatura, e-posta, WhatsApp, tanık, banka kaydı, keşif/bilirkişi konusu)?
- Ticari defter tutan taraf var mı?

## Denetim şeması
1. **İspat yükü (TMK m.6).** Bir vakıadan lehine hak çıkaran onu ispatla yükümlü. Sözleşmenin kurulduğunu iddia eden kuruluşu; ifayı/ödemeyi iddia eden ifayı; ayıbı iddia eden ayıbı ve süresinde ihbarı ispatlar.
2. **Senetle ispat zorunluluğu (HMK m.200).** Dava konusu değeri 2025 için belirlenen parasal sınırı (her yıl güncellenen tutar; `[doğrulanacak]`) aşan hukuki işlemler senetle ispatlanır; senede karşı tanık kural olarak dinlenmez (m.201).
3. **İstisnalar (m.203).** Altsoy-üstsoy, eşler, kardeşler arası işlemler; hukuki işlemin yapıldığı sırada senet alınamaması (yangın/yakın ilişki gibi haklı sebep); delil başlangıcı (m.202) varsa tanık tamamlayıcı delil olur.
4. **Belirli vakıa-delil eşlemesi.** Ödeme → makbuz/banka dekontu/ibra; ayıp → bilirkişi-keşif; teslim → tutanak/irsaliye; kira ödemesi → m.347 ihtara karşı dekont. Ticari defterler HMK m.222 ile sahibi lehine/aleyhine delil.
5. **Elektronik deliller.** Güvenli elektronik imzalı belge senet hükmünde (HMK m.205); imzasız e-posta/mesajlar delil başlangıcı veya takdiri delil olarak değerlendirilir, içerik ve aidiyet tartışılır.
6. **Resmî şekil.** Taşınmaz satışı resmî senetle (TMK m.706, TBK m.237) geçerli; şekil eksikliği geçerlilik sorunu olup ispattan önce gelir. Ara sonuç: vakıa-yük-delil matrisi ve eksik delil listesi.

## Çıktı modülleri
- İspat yükü ve delil planı tablosu.
- Senetle ispat/istisna değerlendirme notu.
- Delil tespiti veya bilirkişi talebi taslağı.

## Plugin bağlamı

Bu beceri `borclar-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
