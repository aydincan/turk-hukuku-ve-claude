---
name: koruma-kararlari-6284
description: "Aile içi şiddet, taciz, tehdit veya ısrarlı takip hallerinde 6284 sayılı Kanun kapsamında koruyucu ve önleyici tedbir başvurusu hazırlamak, tedbir türünü ve mercii seçmek gerektiğinde kullanılır."
---

# 6284 Koruma Kararları ve Aile İçi Şiddet

## Görev
Şiddet veya şiddet tehlikesi altındaki kişi için 6284 sayılı Kanun çerçevesinde doğru tedbiri (koruyucu/önleyici) ve mercii (hâkim/mülki amir/kolluk) belirleyip başvuruyu hızla hazırlamak.

## Soğuk başlangıç (intake)
1. Şiddetin türü nedir: fiziksel, cinsel, psikolojik, ekonomik, ısrarlı takip?
2. Mağdur ve şiddet uygulayan kim; aralarında evlilik/akrabalık/birliktelik var mı?
3. Acil tehlike var mı (gecikmesinde sakınca bulunan hal)?
4. Mağdurun barınma, uzaklaştırma, iletişimin engellenmesi gibi öncelikli ihtiyacı nedir?

## Denetim şeması
1. **Kapsam.** 6284 sK. şiddete uğrayan veya uğrama tehlikesi bulunan kadın, çocuk, aile bireyleri ve tek taraflı ısrarlı takip mağdurlarını korur (m.1). Şiddet delili veya raporu **şart değildir**; beyan esas alınarak tedbir verilebilir.
2. **Önleyici tedbirler — hâkim (m.5).** Şiddet uygulayana yönelik: konuta/işyerine/okula yaklaşmama, iletişim kurmama, mağduru rahatsız etmeme, silah teslimi, alkol/madde kullanmama, sağlık kuruluşuna başvurma; gerekirse elektronik kelepçe (teknik takip).
3. **Koruyucu tedbirler (m.3, m.4).** Mağdura yönelik: uygun barınma yeri/sığınmaevi, geçici maddi yardım, kreş, kimlik/adres gizliliği, geçici koruma.
4. **Mercii ve hız.** Tedbirlere kural olarak aile mahkemesi hâkimi karar verir; **gecikmesinde sakınca bulunan hallerde** mülki amir koruyucu tedbire, kolluk amiri ise belirli önleyici tedbirlere (uzaklaştırma vb.) karar verir ve 24 saat içinde hâkim onayına sunar (m.8). Karar genellikle ilk başta en çok altı aya kadar verilir, uzatılabilir (m.8/3).
5. **İhlal yaptırımı.** Tedbir kararına aykırılıkta zorlama hapsi: her ihlal için 3-10 gün, tekrarında 15-30 güne kadar (m.13). Başvuru **harçtan muaftır**.
6. **Ara sonuç.** Tedbir listesi + mercii + süre + ihlal yaptırımı uyarısı raporlanır.

## Çıktı modülleri
- Talep edilecek tedbirlerin maddeye dayalı listesi.
- Aciliyet ve mercii (hâkim/mülki amir/kolluk) kararı.
- 6284 başvuru dilekçesi taslağı ve ihlal halinde izlenecek yol notu.

## Plugin bağlamı

Bu beceri `aile-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
