---
name: rekabet-uyum-programi
description: "Teşebbüsler için önleyici rekabet uyumu kurmak; fiyatlandırma, dağıtım, bilgi paylaşımı, rakip temasları ve yerinde inceleme hazırlığı gibi alanlarda risk taraması ve iç politika tasarlamak istendiğinde kullanılır."
---

# Rekabet Uyum Programı ve Risk Önleme

## Görev
Bir teşebbüsün rekabet hukuku ihlal riskini ihlal gerçekleşmeden azaltmak; ticari uygulamaları (fiyat, dağıtım, bilgi paylaşımı, ihale, rakip temasları) m.4/m.6 süzgecinden geçirerek iç politika, eğitim ve yerinde inceleme protokolü kurmak.

## Soğuk başlangıç (intake)
- Teşebbüsün pazardaki konumu hâkim/lider mi, yoksa pazar payı düşük mü?
- Rakiplerle temas alanları: dernek/birlik üyeliği, ortak ihaleler, kıyaslama (benchmarking), tedarik?
- Dağıtım modeli: bayilik, tek satıcılık, online satış kısıtları, fiyat tavsiyesi var mı?
- Daha önce soruşturma/şikâyet geçmişi var mı?

## Denetim şeması
1. **Yatay risk taraması (m.4)** — rakiplerle fiyat, kapasite, gelecek strateji, müşteri/bölge bilgisi paylaşımı kırmızı çizgidir; dernek toplantıları, kıyaslama çalışmaları ve ihale işbirlikleri ayrı ayrı taranır. Rekabete duyarlı bilginin akışı sınırlandırılır.
2. **Dikey risk taraması (m.4 + 2002/2 Tebliğ)** — yeniden satış fiyatının belirlenmesi (RSF) ve mutlak bölgesel koruma ağır kısıtlamadır; tavsiye fiyat/azami fiyat ile RSF ayrımı netleştirilir, online satış ve platform kısıtları gözden geçirilir.
3. **Hâkim durum riski (m.6)** — pazar payı yüksekse münhasırlık, sadakat indirimi, fiyat sıkıştırması, ayrımcılık ve bağlama uygulamaları nesnel haklılık ekseninde değerlendirilir; hâkim teşebbüsün özel sorumluluğu vurgulanır.
4. **Birleşme/işbirliği kontrolü (m.7)** — gelecek işlemler için bildirim eşiği erken kontrol; gun-jumping önleme.
5. **Yerinde inceleme (dawn raid) protokolü** — m.15 incelemesinde kapıda davranış, yasal danışmana ulaşma, belgelerin korunması, engelleme yasağı (silme/saklama nispi ceza ve karine riski); çalışan eğitimi.
6. **Pişmanlık refleksi** — ihlal tespit edilirse Pişmanlık Yönetmeliği kapsamında ilk başvuran avantajının iç prosedüre yerleştirilmesi.

## Çıktı modülleri
- Risk ısı haritası (yatay/dikey/hâkim durum/işlem).
- İç politika ve kırmızı-çizgi rehberi taslağı.
- Yerinde inceleme (dawn raid) eylem protokolü.
- Eğitim ve periyodik denetim takvimi önerisi.

## Plugin bağlamı

Bu beceri `rekabet-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
