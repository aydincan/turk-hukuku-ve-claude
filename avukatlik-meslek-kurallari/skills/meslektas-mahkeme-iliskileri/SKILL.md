---
name: meslektas-mahkeme-iliskileri
description: "Avukatın meslektaşlarına, karşı taraf vekiline, mahkemeye ve adli mercilere karşı davranış kuralları, mektuplaşma gizliliği ve dürüstlük yükümü söz konusu olduğunda kullanılır."
---

# Meslektaşlar Arası İlişkiler ve Mahkemeyle İletişim

## Görev
Avukatın meslektaşları, karşı taraf ve yargı mercileriyle ilişkilerinde uyması gereken
nezaket, dürüstlük ve gizlilik kurallarını somut olaya uygulamak.

## Soğuk başlangıç (intake)
1. Uyuşmazlık meslektaşla mı (karşı vekil, devir alınan dosya) yoksa mahkemeyle mi?
2. Karşı vekille yapılan sulh görüşmesi/yazışması gizli kaydıyla mı yürütüldü?
3. Mahkemeye/karşı tarafa yönelik bir beyan dürüstlük/saygı sınırında mı?
4. Devralınan dosyada önceki meslektaşın ücreti çözüldü mü?

## Denetim şeması
1. **Meslektaşa saygı ve dürüstlük.** Avukatlar birbirine ve mesleğe karşı dürüst ve saygılı
   davranmakla yükümlüdür (Av. K. m.34; TBB Meslek Kuralları m.5, m.11 vd.). Meslektaşı
   küçük düşüren beyan disiplin suçudur. Ara sonuç: beyan eleştiri mi, kişisel saldırı mı?
2. **Sulh görüşmesi gizliliği.** "Gizli/sulh amaçlı" kaydıyla yapılan yazışma ve görüşmeler,
   karşı tarafın muvafakati olmadan mahkemeye delil olarak sunulamaz (TBB Meslek Kuralları
   m.27). Bu kural müzakere serbestisini korur.
3. **Dosya devri ve önceki vekilin hakkı.** Bir işi başka avukattan devralan avukat, önceki
   meslektaşın ücret hakkı ve durumu konusunda meslek kurallarını gözetir (TBB Meslek
   Kuralları m.38); devir öncesi bilgilendirme beklenir.
4. **Mahkemeye karşı yükümlülük.** Avukat mahkemeye saygı gösterir, yanıltıcı beyandan
   kaçınır; usule uygun, doğru ve özenli savunma yapar (Av. K. m.34; HMK m.29 dürüstlük ve
   doğruyu söyleme yükümü). Duruşma düzenine ve hâkime saygı esastır.
5. **Yaptırım.** İhlaller disiplin sorumluluğu (m.135) doğurur; mahkemeye karşı taşkınlık
   ayrıca duruşma düzeni ve ilgili usul yaptırımlarını gündeme getirir.

## Çıktı modülleri
- Davranışın kural uygunluğu değerlendirmesi (meslektaş/mahkeme ekseninde).
- "Gizli/sulh amaçlı" yazışma şerhi şablonu.
- Dosya devir bilgilendirme yazısı taslağı.

## Plugin bağlamı

Bu beceri `avukatlik-meslek-kurallari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
