---
name: kira-bedeli-tespit-ve-artis
description: "Yenilenen dönemde uygulanacak kira artış oranı, sözleşmedeki artış kaydının geçerliliği, beş yılı aşan kiralarda hakkaniyet belirlemesi veya kira tespit davası açma şartları ve hesabı söz konusu olduğunda bu beceriyi kullan."
---

# Kira Bedelinin Belirlenmesi, Artışı ve Kira Tespit Davası

## Görev
Yenilenen kira döneminde geçerli kira bedelini hesaplamak; sözleşmedeki artış kaydını TBK m.344 sınırına göre denetlemek; kira tespit davasının (TBK m.345) şartlarını, süresini ve etkisini ortaya koymak.

## Soğuk başlangıç (intake)
- Sözleşmedeki artış kaydı ne (sabit oran, TÜFE, döviz)?
- Sözleşme kaç yıldır sürüyor; beş yıl doldu mu?
- Talep eden kim, hangi dönem için ne istiyor?
- Emsal kira ve taşınmazın durumu hakkında veri var mı?

## Denetim şeması
1. **Artış sınırı (TBK m.344/1)**: Tarafların yenilenen dönem için anlaştığı artış oranı, bir önceki kira yılında **on iki aylık ortalama TÜFE** oranını geçemez; aşan kısım geçersiz, sınıra çekilir. Bu kural sözleşmede daha yüksek oran kararlaştırılmış olsa da uygulanır.
2. **Anlaşma yoksa (m.344/2)**: Hâkim, TÜFE on iki aylık ortalamasını aşmamak üzere ve kiralananın durumunu gözeterek hakkaniyete göre belirler.
3. **Beş yıldan uzun/beşinci yıl sonrası (m.344/3)**: Beş yıldan uzun süreli veya beş yıldan sonra yenilenen sözleşmelerde, beşinci yılın sonunda hâkim; TÜFE oranı, kiralananın durumu ve **emsal kira bedelleri** ışığında **hakkaniyet** ile yeni bedeli belirler. Sonraki her beş yılda aynı şekilde.
4. **Yabancı para (m.344/4)**: Sözleşme döviz üzerinden ise beş yıl geçmedikçe değişiklik yapılamaz (kambiyo mevzuatı ve aşırı ifa güçlüğü — TBK m.138 saklı).
5. **Kira tespit davası (TBK m.345)**: Her zaman açılabilir; ancak yeni dönem başından önceki son otuz gün içinde açılır veya kiraya veren bu süre içinde yazılı bildirimde bulunmuşsa dava yeni dönem boyunca açılabilir ve karar yeni dönem başından itibaren etkili olur. Görev sulh hukuk mahkemesi.
6. **İspat ve ara sonuç**: Emsal kira, bilirkişi/keşif; hesabın oran + emsal + hakkaniyet üçlüsüyle gerekçelendirilmesi.

## Çıktı modülleri
- Dönem bazlı kira hesap tablosu.
- Artış kaydı geçerlilik notu.
- Kira tespit davası dilekçesi iskeleti (görev, süre, talep).

## Plugin bağlamı

Bu beceri `kira-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
