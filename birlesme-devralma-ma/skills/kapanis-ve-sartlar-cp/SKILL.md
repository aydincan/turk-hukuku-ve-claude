---
name: kapanis-ve-sartlar-cp
description: "İmza ile kapanış arası dönemin yönetimi, kapanış ön şartlarının (conditions precedent) listelenmesi, kapanışta teslim edilecek belgelerin ve eş zamanlı işlemlerin kurgulanması için kullanılır."
---

# Kapanış Şartları (CP) ve Kapanış Yönetimi

## Görev
İmza-kapanış arası dönemi düzenlemek, kapanış ön şartlarını ve kapanış belgelerini eksiksiz kurgulamak; eksik/gecikmeli kapanış sonuçlarını hükme bağlamak.

## Soğuk başlangıç (intake)
- İmza ve kapanış eş zamanlı mı, ayrık mı (signing/closing split)?
- Hangi izinler kapanış şartı (rekabet, sektörel, üçüncü kişi onayı)?
- Kapanış için uzun stop (long-stop date) tarihi belirlendi mi?
- Kapanışta hangi belgeler eş zamanlı teslim edilecek?

## Denetim şeması
1. **CP kataloğu**: Rekabet Kurulu izni, sektörel ön izin (BDDK/EPDK vb.), üçüncü kişi onayları (change-of-control), kurumsal kararlar, beyanların kapanışta doğru olması (bring-down).
2. **Ara dönem taahhütleri**: TBK m.2 dürüstlük kuralı çerçevesinde olağan işletme yürütümü; satıcının değer düşürücü işlem yapmama taahhüdü.
3. **Kapanış belgeleri (deliverables)**: Pay devir ciroları, pay defteri kaydı (TTK m.499), istifa/atama kararları, banka talimatları, disclosure güncellemesi.
4. **Eş zamanlılık**: Kapanış işlemlerinin tek seansta ve birbirine bağlı (interdependent) yapılması; aksi halde geri alma (unwind) mekanizması.
5. **Eksik kapanış**: Long-stop tarihine kadar CP sağlanmazsa fesih hakkı; kusurlu tarafın temerrüt sorumluluğu (TBK m.117 vd.).
6. **İspat/dayanak**: CP'nin sağlandığı belge (izin yazısı, onay kararı) ile kanıtlanır.
7. **Ara sonuç**: Kapanış protokolü (closing memorandum) ile tüm adımlar teyit edilir.

## Çıktı modülleri
- CP kontrol listesi (sorumlu taraf ve durum sütunlu)
- Kapanış belgeleri (deliverables) dizini
- Closing memorandum / kapanış protokolü iskeleti
- Long-stop ve fesih klozu lafzı

## Plugin bağlamı

Bu beceri `birlesme-devralma-ma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
