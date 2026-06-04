---
name: zimmet-rusvet-gorev-suclari
description: "Kamu görevlisinin veya banka mensubunun malı zimmetine geçirmesi (TCK m.247, Bankacılık K. m.160), rüşvet (TCK m.252), irtikâp (m.250) ve görevi kötüye kullanma (m.257) iddiaları; etkin pişmanlık ve görevlinin sıfatı tartışıldığında kullanılır."
---

# Zimmet, Rüşvet ve Görevle Bağlantılı Suçlar

## Görev
Kamu görevlisi/banka mensubu sıfatına bağlı zimmet, rüşvet, irtikâp ve görevi kötüye kullanma suçlarını ayrıştırmak, doğru tipe yerleştirmek ve etkin pişmanlık imkânını değerlendirmek.

## Soğuk başlangıç (intake)
- Failin sıfatı: kamu görevlisi mi (TCK m.6), banka mensubu mu, özel hukuk kişisi mi?
- Fiil: kendisine tevdi edilen malı mı mal edindi (zimmet), menfaat mi sağladı/aldı (rüşvet/irtikâp), yoksa görevin gereklerine mi aykırı davrandı (m.257)?
- Menfaat-iş ilişkisi: belirli bir iş için mi, genel mi?
- Etkin pişmanlık aşamasında mı (soruşturma öncesi/sonrası)?

## Denetim şeması
1. **Sıfat tespiti**: Zimmet/rüşvet kamu görevlisine özgüdür (TCK m.6 tanımı). Banka görevlisinin bankaya ait malı mal edinmesi 5411 s. Bankacılık Kanunu m.160 (banka zimmeti) kapsamındadır — bu özel norm TCK m.247'ye göre uygulanır.
2. **Zimmet (TCK m.247)**: Görevi sebebiyle zilyetliği devredilen/koruma-gözetimiyle yükümlü olunan malın mal edinilmesi. Basit/nitelikli (hileli fiillerle gizleme — m.247/2) ayrımı yapılır. Kullanma zimmeti (m.247/3) ayrı düzenlenmiştir.
3. **Rüşvet (TCK m.252)**: Görevin yapılması/yapılmaması için anlaşma çerçevesinde menfaat. Rüşvet, iki taraflı anlaşma suçudur; rüşvet veren ve alan ayrı ayrı cezalandırılır. İrtikâptan (m.250) farkı: irtikâpta görevlinin nüfuzunu kötüye kullanarak mağduru menfaate icbar/ikna etmesi vardır.
4. **Görevi kötüye kullanma (m.257)**: Tali norm; zimmet/rüşvet/irtikâp oluşmuyorsa, görevin gereklerine aykırılıkla kişilerin mağduriyeti/kamu zararı/haksız menfaat aranır.
5. **Etkin pişmanlık**: Zimmette TCK m.248 (soruşturma başlamadan iade ile ciddi indirim), rüşvette m.254 — şartları ve zaman dilimleri suç tipine göre ayrı ayrı kontrol edilir.
6. **Ara sonuç**: Fail sıfatı, doğru suç tipi (özel norm/genel norm), nitelikli hal ve etkin pişmanlık penceresi netleşir.

## Çıktı modülleri
- Fail sıfatı ve özel/genel norm seçimi
- Zimmet/rüşvet/irtikâp/m.257 ayrım tablosu
- Nitelikli hal değerlendirmesi
- Etkin pişmanlık zaman çizelgesi
- Savunma/iade stratejisi notu

## Plugin bağlamı

Bu beceri `ekonomik-ceza` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
