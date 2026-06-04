---
name: durustluk-kurali-tmk-2-1
description: "Bir sözleşmesel veya yasal ilişkide tarafların hak kullanımı ve borç ifasının dürüstlük ölçüsüne uyup uymadığı, yan yükümlülükler veya sözleşme boşluğu tartışıldığında TMK m.2/1 süzgecini uygulamak için kullanılır."
---

# Dürüstlük Kuralı (TMK m.2/1)

## Görev
Bir hakkın kullanımının ve bir borcun ifasının TMK m.2/1 dürüstlük kuralına (objektif iyiniyet) uygun olup olmadığını denetlemek; yan yükümlülükleri ve sözleşme boşluğunun dürüstlükle doldurulmasını gerekçelendirmek.

## Soğuk başlangıç (intake)
- Hangi hak kullanılıyor / hangi borç ifa ediliyor ve dürüstlüğe aykırı görülen davranış nedir?
- İlişki sözleşmesel mi, yasal mı; sözleşmede açık hüküm var mı yoksa boşluk mu var?
- İddia edilen ihlal bir asıl edim mi, yoksa sadakat/özen/koruma/bilgilendirme gibi yan yükümlülük mü?
- Taraflar tacir mi (özen ölçütü ağırlaşır), tüketici mi?

## Denetim şeması
1. **Objektif ölçüt** — TMK m.2/1: herkes haklarını kullanırken ve borçlarını yerine getirirken dürüstlük kuralına uymak zorundadır. Ölçüt, aynı durumdaki dürüst ve makul kişinin davranışıdır (objektif), kişinin niyeti değil.
2. **Yan yükümlülükler** — Asıl edim yanında sadakat, özen, koruma, bilgilendirme ve sır saklama yükümlülükleri dürüstlük kuralından doğar; ihlali sözleşmeye aykırılık sayılır (TBK m.112 ile bağ).
3. **Sözleşme boşluğunun doldurulması** — Tarafların düzenlemediği nokta önce yedek hukuk kuralıyla, yoksa dürüstlük kuralıyla varsayımsal taraf iradesine göre tamamlanır (TBK m.19 yorumuyla birlikte).
4. **Edimler arası denge** — İfa tarzı, zamanı ve yeri dürüstlükle belirlenir; aşırı katı lafzî ifa talebi dürüstlüğe aykırı olabilir.
5. **İspat** — Dürüstlüğe aykırılığı iddia eden, dayandığı vakıaları TMK m.6 / HMK m.190 uyarınca ispatlar; hâkim açık aykırılığı re'sen gözetebilir.
6. **Sınır** — m.2/1 bağımsız talep kaynağı değildir; mevcut bir ilişkinin içinde çalışır. Hakkın *açıkça kötüye* kullanılması ise m.2/2 ile ayrıca denetlenir (ayrı beceri).

## Çıktı modülleri
- İlişki ve tartışılan davranışın tespiti.
- Yan yükümlülük / boşluk doldurma analizi.
- Objektif dürüstlük ölçütüne göre değerlendirme.
- İspat yükü + ilkesel içtihat `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `medeni-hukuk-baslangic` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
