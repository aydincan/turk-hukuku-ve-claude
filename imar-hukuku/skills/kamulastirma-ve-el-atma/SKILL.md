---
name: kamulastirma-ve-el-atma
description: "Kamulaştırma bedel tespiti, acele kamulaştırma ya da idarenin hukuki/fiili kamulaştırmasız el atması nedeniyle bedel/tazminat talebi gündeme geldiğinde; yargı kolu, bedel hesabı ve mülkiyet hakkı boyutu sorulduğunda kullanılır."
---

# Kamulaştırma ve Kamulaştırmasız El Atma

## Görev
Taşınmaza idarenin müdahalesinin hukuki niteliğini (kamulaştırma / hukuki el atma / fiili el atma) belirlemek ve doğru bedel/tazminat yolunu kurmak.

## Soğuk başlangıç (intake)
- İdare usulüne uygun kamulaştırma yaptı mı, yoksa el atma mı var?
- El atma fiili (fiilen kullanma/yol-park yapımı) mı, hukuki (planda kamusal alanda bırakıp uygulamama) mı?
- Taşınmazın imar durumu ve plandaki fonksiyonu ne?
- İdari işlem (kamulaştırma kararı, acele kamulaştırma) tebliğ edildi mi?

## Denetim şeması
1. **Nitelik tespiti**: Usulüne uygun kamulaştırma → 2942 m.10 bedel tespiti ve tescil davası (idare açar). İdarenin **fiilen** el atması → kamulaştırmasız el atma bedeli (adli yargı, 2942 geçici m.6). Planda kamusal alana ayrılıp makul sürede kamulaştırılmayan taşınmaz → **hukuki el atma** (Uyuşmazlık Mahkemesi içtihadıyla idari yargıda tam yargı davası).
2. **Yargı kolu**: Fiili el atma adli yargıda (asliye hukuk), hukuki el atma idari yargıda (tam yargı) görülür; doğru kol seçimi görev retini önler. Acele kamulaştırma (m.27) ve kamulaştırma işleminin iptali ayrı denetlenir.
3. **Bedel tespiti (2942 m.11)**: Taşınmazın cinsi, yüzölçümü, imar durumu, emsal satışlar, gelir metodu (arazide), yapı bedeli; **dava tarihindeki** değer esas alınır, kıymet takdiri bilirkişi kuruluyla yapılır.
4. **Mülkiyet hakkı boyutu (Anayasa m.35, m.46)**: Kamulaştırmada **gerçek karşılık ve peşin/nakden ödeme** ilkesi; el atmada mülkiyetin özüne dokunma ve ölçüsüzlük AYM bireysel başvuru konusu olabilir (kararlarbilgibankasi.anayasa.gov.tr).
5. **İspat ve süre**: Tapu, imar durum belgesi, emsal satış kayıtları, keşif ve bilirkişi raporu. Acele kamulaştırma ve kamulaştırma işleminin iptalinde İYUK süreleri; el atma bedelinde zamanaşımı/faiz başlangıcı ayrıca kurulur.
6. **Ara sonuç**: Müdahalenin niteliğine göre doğru dava (bedel tespiti itirazı / kamulaştırmasız el atma bedeli / hukuki el atma tam yargı) ve yetkili mahkeme belirlenir; bilirkişi bedeline itiraz stratejisi hazırlanır. Yargıtay/Danıştay künyeleri `[doğrulanacak]`.

## Çıktı modülleri
- El atma niteliği ve yargı kolu tespit notu.
- Bedel hesabı parametre listesi (emsal/imar durumu/yapı).
- Mülkiyet hakkı (Anayasa m.35) değerlendirme notu.
- İlgili dava türüne göre dilekçe iskeleti.

## Plugin bağlamı

Bu beceri `imar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
