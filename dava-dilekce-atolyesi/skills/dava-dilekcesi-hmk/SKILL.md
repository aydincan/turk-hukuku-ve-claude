---
name: dava-dilekcesi-hmk
description: "Medeni yargıda HMK m.119 unsurlarına uygun dava dilekçesi taslağı hazırlamak; eda, tespit veya inşai talepleri doğru kurmak gerektiğinde kullanılır."
---

# Dava Dilekçesi (HMK)

## Görev
HMK m.119'un zorunlu unsurlarını eksiksiz taşıyan, vakıa-altlama-talep omurgası sağlam bir dava dilekçesi taslağı üretmek. Eksik unsur, kesin süreli tamamlama veya dava şartı yokluğu riskine yol açar.

## Soğuk başlangıç (intake)
- Talep eda mı (para/teslim), tespit mi, inşai mi (boşanma, iptal)?
- Taraf bilgileri ve TC/vergi numaraları tam mı?
- Zorunlu arabuluculuk tutanağı/dava şartı eki var mı?
- Faiz başlangıcı ve türü (yasal/avans/ticari) ne olacak?

## Denetim şeması
1. Zorunlu unsurlar (HMK m.119/1): a) mahkeme, b) davacı-davalı ad/TC-vergi no/adres, c) varsa vekil, ç) konu (değer), d) vakıalar (numaralı), e) deliller (her vakıa hangi delille), f) hukuki sebepler, g) açık talep sonucu, ğ) imza. Eksiklikte m.119/2: bir haftalık kesin süre.
2. Talep sonucu netliği: İnfaz edilebilir biçimde yazın; alacakta ana para + faiz (başlangıç tarihi ve oranı TBK m.88/120 veya 3095 s.K.) + yargılama gideri + vekâlet ücreti. Belirsiz alacak davası ise HMK m.107 dayanağını ve fazlaya ilişkin hakkı belirtin.
3. Harç ve gider: Nispi/maktu harç değere göre; eksik harç dava şartı niteliğinde tamamlanır.
4. Delil bağlama: HMK m.194 somutlaştırma yükü; her delili ilgili vakıaya bağlayın. Senetle ispat sınırı (m.200) aşılıyorsa tanık caiz değildir, dikkat edin.
5. Dava şartları kontrolü (m.114): arabuluculuk, görev, yetki, hukuki yarar. Ara sonuç: unsurlar tamsa taslak, avukatın son incelemesine ve imzasına hazırdır; değilse `[doldurulacak]` yer tutucuları ve eksik listesi.

## Çıktı modülleri
- Tam dava dilekçesi taslağı (m.119 başlıklı)
- Talep sonucu bloğu (faiz/gider/ücret dâhil)
- Delil listesi ve dava şartı ekleri kontrol listesi
- Eksik bilgi ve yer tutucu raporu

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
