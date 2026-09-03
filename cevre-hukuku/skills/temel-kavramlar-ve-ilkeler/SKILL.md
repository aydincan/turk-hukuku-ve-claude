---
name: temel-kavramlar-ve-ilkeler
description: "Çevre hukukunun sistematiğini, kirleten öder ve ihtiyat ilkelerini, idari/özel/ceza eksenlerinin ayrımını ve uygulanacak normlar piramidini kurmak gerektiğinde; bir çevre uyuşmazlığını ilk kez çerçevelerken kullan."
---

# Temel Kavramlar ve İlkeler

## Görev
Çevresel bir olguyu doğru hukuki eksene oturtmak, uygulanacak normlar bütününü ve yol haritasını belirlemek; idari, özel hukuk ve ceza katmanlarını ayırt etmek.

## Soğuk başlangıç (intake)
1. Müvekkil hangi konumda: yatırımcı/işletme, idare, yoksa kirliliğe maruz kalan/itiraz eden mi?
2. Ortada somut bir idari işlem (ÇED kararı, izin, yaptırım) var mı; varsa tarihi ve tebliği nedir?
3. Talep ne: işlem iptali, tazminat, faaliyetin durdurulması, yoksa ceza riskini yönetmek mi?
4. Faaliyet hangi sektör/tesis; hangi çevresel unsur (hava, su, atık, gürültü) etkileniyor?

## Denetim şeması
1. **İlkeleri uygula**: 2872 sayılı Çevre Kanunu m.3 — önleme, ihtiyat, kirleten/bozan öder, işbirliği ve katılım ilkeleri yorum ölçütüdür. Anayasa m.56 sağlıklı ve dengeli çevrede yaşama hakkını güvence altına alır.
2. **Ekseni belirle**: İzin/ÇED/yaptırım işlemleri → idari eksen (2577 sayılı İYUK). Kirlilikten doğan zarar → özel hukuk ekseni (TBK m.49 vd.; el atma için TMK m.683). Kasten/taksirle kirletme → ceza ekseni (TCK m.181-182).
3. **Sorumluluk türünü tespit et**: 2872 m.28 uyarınca kirletenin sorumluluğu kusura bağlı değildir; birden çok kirleten varsa müteselsil sorumluluk gündeme gelir. İdari yaptırımlarda ise m.20-23 cetveli ve 5326 sayılı Kanun genel rejimi uygulanır.
4. **Norm hiyerarşisini kur**: Kanun (2872, 3194) → yönetmelik (ÇED, Çevre İzin ve Lisans, alan yönetmelikleri) → genelge/kılavuz. Yönetmelik kanuna, genelge yönetmeliğe aykırı olamaz; aykırılık iptal sebebidir.
5. **Ara sonuç**: İlgili norm, yargı yolu, süre durumu ve ispat ihtiyacı tek paragrafta sabitlenir.

## Çıktı modülleri
- Eksen ve yargı yolu haritası (idari/özel/ceza)
- Uygulanacak normlar listesi (madde + yürürlükteki yönetmelik sürümü)
- İlkesel değerlendirme ve ilk risk notu
- Sonraki adım önerisi (hangi beceriye geçilecek)

## Plugin bağlamı

Bu beceri `cevre-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
