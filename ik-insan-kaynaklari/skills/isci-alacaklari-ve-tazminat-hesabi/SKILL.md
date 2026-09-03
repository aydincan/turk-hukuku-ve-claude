---
name: isci-alacaklari-ve-tazminat-hesabi
description: "Kıdem, ihbar, yıllık izin, fazla mesai, UBGT ve diğer işçilik alacaklarının hesabı, fesih sonrası yükümlülüklerin belirlenmesi veya karşı hesap çıkarılması gerektiğinde kullanılır."
---

# İşçilik Alacakları ve Tazminat Hesap Şeması

## Görev
Fesih sonrası işverenin ödeyeceği (veya dava edilebilecek) işçilik alacaklarını kalem kalem hesaplamak, hak ediş/zamanaşımı süzgecinden geçirmek ve bordro/SGK kayıtlarıyla tutarlı bir karşı hesap üretmek.

## Soğuk başlangıç (intake)
1. İşe giriş-çıkış tarihleri, son giydirilmiş brüt ücret ve yan haklar (yol, yemek, prim) nedir?
2. Fesih kim tarafından, hangi sebeple yapıldı (kıdem/ihbar hak ediş belirler)?
3. Kullandırılmayan yıllık izin, fazla mesai ve UBGT iddiası var mı, kayıt var mı?
4. Daha önce ödeme/ibraname/avans verildi mi?

## Denetim şeması
1. **Kıdem tazminatı (1475 m.14, yürürlükte)**: 1 yıl+ kıdem ve hak kazandıran fesih (işveren m.25/II hariç fesih, işçinin haklı feshi vb.) şartı; her tam yıl için 30 günlük **giydirilmiş brüt** ücret, kıdem tavanı sınırıyla. m.25/II ile fesihte kıdem yok.
2. **İhbar tazminatı (4857 m.17)**: Bildirim sürelerine (2-8 hafta, kıdeme göre) uymadan fesihte; haklı fesihte (m.25) işveren ihbar ödemez.
3. **Yıllık izin ücreti (m.59)**: Kullandırılmayan izin, fesihte **son ücret** üzerinden ödenir; zamanaşımı fesihten işler.
4. **Fazla çalışma (m.41)**: Haftalık 45 saati aşan süre %50 zamlı; ispatı kural olarak işçide, ancak işyeri kayıt tutmuşsa kayda bakılır. Yıllık 270 saat sınırı.
5. **UBGT/hafta tatili (m.44, 46-47)**: Çalışılan genel tatil ve hafta tatili ücreti zamlı.
6. **Zamanaşımı**: Kıdem, ihbar, yıllık izin alacaklarında **5 yıl** (m.32/8 ve geçiş hükümleri); fazla mesai/UBGT gibi ücret alacaklarında 5 yıl.
7. **İndirim/mahsup**: İbraname (TBK m.420 — yazılı, fesihten 1 ay sonra, banka ödemesi), avans ve önceki ödemeler düşülür. Ara sonuç: net işveren yükü.

## Çıktı modülleri
- Kalem kalem alacak hesap tablosu (hak ediş + zamanaşımı + mahsup).
- Bordro/SGK ile çelişki notu.
- Karşı hesap / sulh teklifi taslağı.

## Plugin bağlamı

Bu beceri `ik-insan-kaynaklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
