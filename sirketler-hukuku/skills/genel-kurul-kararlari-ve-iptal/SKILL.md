---
name: genel-kurul-kararlari-ve-iptal
description: "Anonim veya limited şirkette genel kurul çağrısı, gündem, nisaplar, kararların butlanı (TTK m.447) ve iptali (m.445-446) ile azlık haklarının kullanımı gündeme geldiğinde; karar sakatlığını teşhis ve dava stratejisi için kullanılır."
---

# Genel Kurul Kararları ve İptal/Butlan

## Görev
Genel kurul kararının geçerliliğini denetlemek; sakatsa butlan mı iptal mi olduğunu, kimin, hangi sürede dava açabileceğini saptamak ve azlık haklarını işletmek.

## Soğuk başlangıç (intake)
1. Karar tarihi, gündem maddesi ve alınan kararın özü ne?
2. Çağrı usulü ve nisaplar tutturuldu mu; bakanlık temsilcisi gerekiyorsa hazır mıydı?
3. İtiraz eden pay sahibi toplantıya katıldı mı, muhalefetini tutanağa geçirdi mi?
4. Karar emredici hükme/temel pay sahipliği haklarına mı aykırı (butlan emaresi)?
5. Karar tarihinden bu yana ne kadar süre geçti?

## Denetim şeması
1. Çağrı ve gündem: AŞ m.410-414 (çağrı yetkisi, ilan, gündem); gündemde olmayan konu görüşülemez (m.413), istisnalar (azlık/genel kurulun yetkili olduğu hâller). Çağrısız genel kurul m.416 (tüm payların temsili + itirazsızlık).
2. Nisaplar: Olağan toplantı/karar nisapları m.418; ağırlaştırılmış nisaplar m.421 (esas sözleşme değişikliği türlerine göre).
3. Butlan: m.447 — vazgeçilemez pay sahipliği haklarını sınırlayan, anonim şirketin temel yapısına/sermayenin korunmasına aykırı kararlar batıl; süreye bağlı değil, tespit davası niteliğinde.
4. İptal: m.445 — kanuna, esas sözleşmeye veya dürüstlük kuralına aykırı kararlar; iptal davası açma hakkı m.446 (toplantıda muhalefet şerhi veren/katılması engellenen pay sahibi, çağrı/gündem usulsüzlüğü, yönetim kurulu, kişisel sorumluluk doğacaksa üye). Süre: karar tarihinden itibaren üç ay (m.445).
5. Görev/yetki: Asliye ticaret mahkemesi, şirket merkezi (m.445/2). Teminat ve yürütmenin geri bırakılması m.448-449.
6. Azlık hakları: özel denetçi atanması talebi (m.438-439), finansal tabloların müzakeresinin ertelenmesi (m.420), genel kurulu toplantıya çağırma (m.411-412).
7. İspat: Çağrı/nisap usulsüzlüğünü ve muhalefet şerhini davacı, kararın yerindeliğini şirket ortaya koyar.

## Çıktı modülleri
- Karar sakatlık teşhisi (butlan/iptal ayrımı, madde atıflı).
- İptal davası dilekçesi iskeleti (süre, taraf, talep sonucu, [doldurulacak]).
- Azlık hakkı başvuru/ihtar taslağı.

## Plugin bağlamı

Bu beceri `sirketler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
