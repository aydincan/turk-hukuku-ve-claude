---
name: hakaret-ozel-hayat-suclari
description: "Hakaret, isnadın ispatı, haksız fiile karşı işlenen hakaret, özel hayatın gizliliği, verileri hukuka aykırı kaydetme ve haberleşmenin gizliliği gündeme geldiğinde kullanılır."
---

# Şerefe ve Özel Hayata Karşı Suçlar

## Görev
Hakaret ve özel hayata karşı suçlarda tipiklik, ifade özgürlüğü sınırı, isnadın ispatı ve cezayı kaldıran/azaltan halleri madde metniyle değerlendirmek.

## Soğuk başlangıç (intake)
- Söylenen/yazılan ifade somut olarak nedir; somut bir fiil isnadı mı, sövme/değer yargısı mı?
- İfade mağdurun yüzüne mi, gıyabında mı (ihtilat şartı), yoksa basın/sosyal medya yoluyla mı?
- Karşı tarafın önceki bir haksız fiili veya karşılıklı hakaret var mı?
- Bir görüntü/ses kaydı alındı, yayıldı veya haberleşme içeriği ele geçirildi mi?

## Denetim şeması
1. Hakaret (TCK m.125): Somut bir fiil/olgu isnadı ya da sövme yoluyla onur-şeref-saygınlığa saldırı + kast. Gıyapta hakarette en az üç kişiyle ihtilat şartı (m.125/1). Huzurda işlenmesiyle eşdeğer sayılan haller (m.125/2: mektup, telefon, mesaj).
2. Nitelikli haller (TCK m.125/3): kamu görevlisine görevinden dolayı, dinî-siyasî değerleri açıklama, alenen işlenmesi (m.125/4) cezayı artırır. Kamu görevlisine karşı görev nedeniyle işlenenlerde resen kovuşturma.
3. İfade özgürlüğü sınırı ve eleştiri: Değer yargısı niteliğindeki sert eleştiri ile hakaret ayrımını yap; AYM bireysel başvuru içtihadında ifade özgürlüğü dengesi gözetilir (kararlarbilgibankasi.anayasa.gov.tr üzerinden ilkesel atıf, künye `[doğrulanacak]`).
4. İsnadın ispatı (TCK m.127): İsnat edilen fiilin suç oluşturması veya ispatında kamu yararı bulunması halinde ispat hakkı; ispatlanırsa ceza verilmez.
5. Cezayı azaltan/kaldıran haller: Haksız fiile tepki ve karşılıklı hakarette ceza indirimi veya verilmemesi (TCK m.129). Hakaret kural olarak şikâyete bağlı (m.131); kamu görevlisine karşı görevden dolayı işlenen hariç.
6. Özel hayat suçları: Özel hayatın gizliliğini ihlal (m.134), kişisel verileri hukuka aykırı kaydetme/verme-yayma (m.135-136), haberleşmenin gizliliğini ihlal (m.132). Rıza, hukuka uygunluk ve aleniyet unsurlarını ayrıca denetle. Ara sonuç: uygulanacak madde, şikâyet ve resen kovuşturma durumu.

## Çıktı modülleri
- İfade nitelendirme notu (hakaret mi eleştiri mi) ve madde atfı.
- İhtilat/aleniyet ve şikâyet süresi değerlendirmesi.
- İsnadın ispatı ve TCK m.129 indirimi stratejisi.

## Plugin bağlamı

Bu beceri `ceza-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
