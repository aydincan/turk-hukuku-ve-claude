---
name: uyum-programi-tasarimi
description: "Bir şirket için sıfırdan KVKK uyum programı kurulurken ya da mevcut uyumda boşluk analizi yapılırken; envanter, politika seti, sözleşme zinciri ve rol yapısı bütüncül tasarlanırken kullanılır."
---

# Kurumsal KVKK Uyum Programı Tasarımı

## Görev
Veri sorumlusu kuruluş için uçtan uca KVKK uyum programını tasarlamak: kişisel veri envanterinden politika setine, sözleşme zincirinden eğitim ve denetime kadar bütünsel uyum mimarisi kurmak.

## Soğuk başlangıç (intake)
1. Kuruluşun sektörü, ölçeği ve işlediği başlıca veri kategorileri nedir?
2. Mevcutta hangi belgeler var (aydınlatma, rıza, politika, VERBİS)?
3. Veri işleyen/alt yüklenici zinciri ve yurt dışı aktarım var mı?
4. İç organizasyon nasıl — irtibat kişisi, komite, sorumluluk dağılımı var mı?

## Denetim şeması
1. **Envanter — temel taş**: Kişisel veri işleme envanteri çıkarılır (faaliyet, veri kategorisi, amaç, hukuki sebep m.5/m.6, alıcı, aktarım, saklama süresi). Tüm diğer belgeler envanterle tutarlı olmak zorundadır.
2. **Hukuki sebep haritalama (m.4-5-6)**: Her işleme bir geçerli şarta bağlanır; açık rızaya gereksiz bağımlılık azaltılır, meşru menfaat için denge testleri belgelenir.
3. **Belge seti**: Aydınlatma metinleri (m.10), gerektiğinde açık rıza beyanları, Saklama ve İmha Politikası, Kişisel Veri İşleme ve Koruma Politikası, ilgili kişi başvuru prosedürü, veri ihlali müdahale planı (m.12).
4. **Sözleşme zinciri**: Veri işleyenlerle m.12 sözleşmeleri; yurt dışı aktarımda m.9 standart sözleşme/güvenceler; çalışan ve tedarikçi taahhütleri.
5. **VERBİS ve organizasyon**: m.16 kayıt yükümlülüğü kontrolü, irtibat kişisi atanması, iç rol ve yetki matrisi, periyodik eğitim ve denetim döngüsü.
6. **Ara sonuç**: Boşluk analizi her başlık için "var/eksik/güncelleme gerekli" olarak skorlanır ve önceliklendirilmiş eylem planına bağlanır.

İspat yükü (hesap verebilirlik): Veri sorumlusu, m.4 ilkelerine ve tüm yükümlülüklere uyumu belgelerle ispatlayabilmelidir; uyum, kâğıt değil işleyen süreç olarak kurulur.

## Çıktı modülleri
- Boşluk analizi (gap analysis) skor tablosu ve eylem planı.
- Politika ve belge seti yapılandırma listesi.
- Sözleşme zinciri ve aktarım haritası.

## Plugin bağlamı

Bu beceri `kvkk-veri-koruma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
