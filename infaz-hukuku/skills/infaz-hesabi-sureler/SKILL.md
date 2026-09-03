---
name: infaz-hesabi-sureler
description: "Hapis cezasının koşullu salıverilme, denetimli serbestlik, açığa ayrılma ve bihakkın tahliye tarihlerini hesaplamak, gözaltı/tutukluluk mahsubunu çıkarmak gerektiğinde kullanılır."
---

# İnfaz Hesabı, Mahsup ve Süreler

## Görev
Verilen hapis cezası için açığa ayrılma, denetimli serbestlik, koşullu salıverilme ve bihakkın (kesin) tahliye tarihlerini, mahsuplar dahil olmak üzere doğru biçimde hesaplamak.

## Soğuk başlangıç (intake)
- Toplam hapis cezası ne kadar; birden fazla ilam varsa içtima yapıldı mı?
- Suç tarihi ve suç tipi nedir (oran bu ikisine bağlı)?
- Gözaltı/tutukluluk süresi var mı (mahsup için)?
- Hükümlünün infaza başlama tarihi nedir; firar/ara verme oldu mu?

## Denetim şeması
1. Mahsup: gözaltı ve tutuklulukta geçen süre cezadan düşülür (TCK m.63). Aynı ilam nedeniyle uygulanan adli kontrol/elektronik kelepçe de değerlendirilir. Ara sonuç: net çekilecek ceza.
2. Koşullu salıverilme oranı: kural 5275 m.107 uyarınca uygulanır; suç tarihine göre TCK geçici m.6 ve 7242 sayılı Kanun değişiklikleri lehe hüküm (TCK m.7) süzgecinden geçirilir. İstisnai suç tipleri (kasten öldürme, cinsel dokunulmazlığa karşı suçlar, terör, uyuşturucu ticareti) için ağırlaştırılmış oranlar ayrıca kontrol edilir.
3. Denetimli serbestlik: 5275 m.105/A uyarınca koşullu salıverilmeye belirli süre kala (genel kural ve geçici düzenlemeler farklı olabilir) açık kurumdan denetimli serbestliğe ayrılma hesaplanır.
4. Açığa ayrılma: 5275 m.14 ve Açık Ceza İnfaz Kurumlarına Ayrılma Yönetmeliği kıstasları.
5. İspat/doğrulama: çıkan sonuç UYAP infaz hesabı ve Cumhuriyet Başsavcılığı infaz bürosu hesabıyla karşılaştırılır; tutarsızlık infaz hâkimliğine şikâyet konusu yapılır (4675 sayılı Kanun).
6. Ara sonuç: dört kritik tarih (açığa ayrılma, denetimli serbestlik, koşullu salıverilme, bihakkın tahliye) tablo halinde.

## Çıktı modülleri
- Tarih hesabı tablosu (oran, mahsup, sonuç tarihleri).
- Lehe kanun karşılaştırması (suç tarihi vs. yürürlük).
- Hesap hatası varsa infaz hâkimliğine itiraz taslağı tetiği.

## Plugin bağlamı

Bu beceri `infaz-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
