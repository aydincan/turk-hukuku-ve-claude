---
name: ictihat-baglayiciligi-ibk-ve-aym
description: "Bir karara dayanılırken onun mahkemeleri ne ölçüde bağladığı tartışıldığında; içtihadı birleştirme kararı, genel kurul, daire ve AYM kararlarının bağlayıcılık hiyerarşisini belirlemek için kullanılır."
---

# İçtihat Bağlayıcılığı (İBK, HGK, AYM)

## Görev
Bir yargı kararının somut uyuşmazlıkta ne kadar ağırlık taşıdığını — bağlayıcı mı yoksa yalnızca ikna edici mi olduğunu — doğru sınıflandırmak ve buna göre güç atfetmek.

## Soğuk başlangıç (intake)
- Karar hangi merciden: İBK, HGK/İDDK/VDDK, daire, BAM/BİM mi?
- Konu AYM norm denetimi veya bireysel başvuru kararına mı dayanıyor?
- Karşı tarafın dayandığı içtihat ile çatışan başka karar var mı?
- Karardan sonra mevzuat veya içtihat değişmiş mi?

## Denetim şeması
1. **AYM kararları** — Anayasa m.153/son: bağlayıcı (herkesi bağlar). Norm denetimi kararı iptal ettiği hükmü ortadan kaldırır; bireysel başvuruda ihlal kararı yeniden yargılama yolu açabilir. En üst değer.
2. **İçtihadı Birleştirme Kararı (İBK)** — Yargıtay Kanunu m.45: benzer hukuki konularda Yargıtay genel kurullarını, dairelerini ve mahkemeleri bağlar. Daireler arası çelişkiyi giderir; daire kararından üstündür.
3. **Genel Kurul (HGK / Ceza GK / İDDK / VDDK)** — Bağlayıcı değil ama daire kararından ağır basan, yön gösterici emsal; direnme kararlarında belirleyici.
4. **Daire kararı** — İkna edici emsal (Anayasa m.138/1: hâkim yalnız hukuka bağlı). "Yerleşik içtihat" demek için birden çok, istikrarlı, güncel karar gerekir.
5. **BAM/BİM (istinaf)** — Bölgesel emsal değeri; ülke çapında bağlayıcılığı yoktur, daireler arasında farklılaşabilir.
6. **Çatışma ve güncellik** — Çelişen kararlarda hiyerarşi (İBK > GK > daire) ve tarih gözetilir; eski karar, sonraki kanun değişikliği veya İBK ile aşılmış olabilir.

## Çıktı modülleri
- Karar → bağlayıcılık sınıfı eşlemesi.
- "Yerleşik içtihat" iddiası için yeterlilik kontrolü.
- Çatışan içtihat varsa öncelik/tarih analizi.
- Güç atfı önerisi (bağlar / güçlü emsal / tek görüş) + `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `atif-turk-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
