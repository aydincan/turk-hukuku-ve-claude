---
name: rekabet-izni-ve-birlesme-kontrolu
description: "Bir devralma işleminin 4054 sayılı Kanun m.7 kapsamında Rekabet Kurulu iznine tabi olup olmadığını ciro eşiklerine göre değerlendirmek, bildirim hazırlamak ve gun-jumping riskini yönetmek için kullanılır."
---

# Rekabet İzni ve Birleşme Kontrolü

## Görev
İşlemin 4054 sayılı Kanun m.7 ve 2010/4 sayılı Tebliğ uyarınca bildirime/izne tabi olup olmadığını saptamak, bildirimi kurgulamak ve izin alınmadan kapanış (gun-jumping) riskini bertaraf etmek.

## Soğuk başlangıç (intake)
- Tarafların Türkiye ve dünya ciroları nedir (son mali yıl)?
- İşlem kontrol değişikliği yaratıyor mu (tek/ortak kontrol)?
- Taraflar aynı pazarda yatay/dikey örtüşüyor mu?
- Kapanış için izin kapanış şartı (CP) olarak kurgulandı mı?

## Denetim şeması
1. **Kontrol testi**: 4054 m.7 — bir teşebbüsün kontrolünde kalıcı değişiklik yaratan devralma/birleşme. Azınlık pay alımı tek başına kontrol vermiyorsa kural olarak bildirime tabi değildir.
2. **Eşik testi**: 2010/4 sayılı Tebliğ m.7'deki ciro eşikleri aşılıyorsa bildirim **zorunludur**. Eşikler periyodik güncellendiği için yürürlükteki güncel tutarlar rekabet.gov.tr'den teyit edilir `[doğrulanacak]`.
3. **Teknoloji teşebbüsü istisnası**: Tebliğde teknoloji teşebbüslerinin devralınmasında yerel eşik aranmaması düzenlemesi gözetilir (güncel metinden teyit).
4. **Bildirim ve askı**: İzin alınmadan işlem hukuken **geçerlilik kazanmaz** (m.7) ve gun-jumping idari para cezası (4054 m.16) doğurur. Kapanış izne bağlanır.
5. **Esasa ilişkin değerlendirme**: Etkilenen pazarlarda hâkim durum yaratma/güçlendirme analizi; gerekirse taahhüt (remedy) önerisi.
6. **İspat/dayanak**: Ciro hesabı bağlı teşebbüsler dahil yapılır; bildirim formu belgeyle desteklenir.
7. **Ara sonuç**: Bildirim gerekli/gereksiz kararı ve izin takvimi (yaklaşık süre) belirlenir.

## Çıktı modülleri
- Bildirim gerekliliği değerlendirme notu (eşik hesabı)
- Rekabet Kurulu bildirim formu taslağı kontrol listesi
- Gun-jumping risk uyarısı ve closing condition lafzı
- İzin takvimi

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
