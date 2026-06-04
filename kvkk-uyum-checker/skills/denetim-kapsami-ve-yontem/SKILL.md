---
name: denetim-kapsami-ve-yontem
description: "Bir KVKK uyum taraması başlatılırken kapsamın, denetlenecek birim ve sistemlerin, rol tespitinin ve denetim yönteminin sabitlenmesi gerektiğinde kullanılır."
---

# Denetim Kapsamı ve Yöntem Belirleme

## Görev
KVKK uyum taramasının iskeletini kurmak: neyin, hangi rol bakımından, hangi kanıtlarla ve hangi skorlama mantığıyla denetleneceğini yazılı olarak sabitlemek. Kapsamı tanımlanmamış denetim, bulgu üretmez.

## Soğuk başlangıç (intake)
1. Denetlenen kuruluşun sektörü, çalışan sayısı ve işlediği başlıca veri kategorileri nedir?
2. Tarama tüm kuruluşu mu, yoksa belirli birim/süreçleri (İK, pazarlama, müşteri hizmetleri) mi kapsıyor?
3. Kuruluş bu süreçlerde veri sorumlusu mu, veri işleyen mi?
4. Daha önce denetim yapıldı mı, açık bulgu var mı, hangi belgeler hazır?

## Denetim şeması
1. **Rol tespiti (KVKK m.3)**: Kapsamdaki her faaliyet için veri sorumlusu/veri işleyen sıfatı belirlenir; yükümlülükler asıl olarak sorumluya düşer, işleyene m.12 sözleşmesiyle aktarılan kısımlar ayrı izlenir.
2. **Kapsam matrisi**: Birim × süreç × sistem (CRM, İK yazılımı, web sitesi, çağrı merkezi, bulut/SaaS) tablosu çıkarılır; her hücre denetim kalemine dönüşür.
3. **Kanıt kuralı**: Her kontrol maddesi için beyan değil belge istenir (politika, ekran görüntüsü, log, sözleşme). Belge yoksa bulgu "Uygunsuz" kabul edilir; hesap verebilirlik ispat yükü veri sorumlusundadır (m.4 — accountability).
4. **Skorlama tanımı**: Her madde "Uygun / Kısmen / Uygunsuz / Kapsam dışı"; risk = olasılık × etki (yaptırım m.18 + itibar + ilgili kişi zararı).
5. **Ara sonuç**: Kapsam, rol ve skorlama mantığı yazıya dökülmeden kanıt toplamaya geçilmez; aksi halde bulgular karşılaştırılamaz.

İspat yükü: Uyumu belgelerle ispat yükümlülüğü veri sorumlusundadır; denetçi yokluk halinde uygunsuzluk lehine karine kurar.

## Çıktı modülleri
- Denetim kapsam ve rol tanımı belgesi.
- Birim/süreç/sistem kapsam matrisi.
- Skorlama ve kanıt kuralı tanım sayfası.

## Plugin bağlamı

Bu beceri `kvkk-uyum-checker` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
