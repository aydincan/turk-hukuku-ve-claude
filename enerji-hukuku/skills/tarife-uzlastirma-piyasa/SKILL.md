---
name: tarife-uzlastirma-piyasa
description: "Tarife uygulaması, dağıtım/sistem kullanım bedelleri, son kaynak tedarik tarifesi, dengeleme ve uzlaştırma (DUY) alacak-borç uyuşmazlıkları ele alındığında kullanılır."
---

# Tarifeler, Dengeleme ve Uzlaştırma

## Görev
Tarife ve uzlaştırma kaynaklı bedel/alacak uyuşmazlıklarını çözmek; EPDK tarife metodolojisi ile EPİAŞ uzlaştırma verisini birlikte değerlendirerek doğru tutarı ve itiraz yolunu belirlemek.

## Soğuk başlangıç (intake)
1. Hangi bedel tartışmalı: dağıtım, iletim, sistem kullanım, son kaynak, dengeleme?
2. Müvekkil üretici mi, tedarikçi mi, serbest/serbest olmayan tüketici mi?
3. Tartışmalı fatura/uzlaştırma dönemi ve tutar nedir?
4. EPİAŞ/EPDK nezdinde itiraz/düzeltme başvurusu yapıldı mı?

## Denetim şeması
1. **Tarife dayanağı**: 6446 m.17 ve ilgili Tarifeler Yönetmelikleri — tarife türleri (bağlantı, iletim, dağıtım, perakende satış, son kaynak) ve Kurul onaylı tarifelerin bağlayıcılığı. Ara sonuç: uygulanan bedel onaylı tarifeye uygun mu.
2. **Son kaynak tedarik tarifesi**: 6446'da 6719 sayılı Kanun değişikliği sonrası rejim; belirli tüketim eşiği üstü tüketicilere uygulanan SKTT esasları doğru tüketici grubuna uygulanmış mı.
3. **Dengeleme ve uzlaştırma**: Dengeleme ve Uzlaştırma Yönetmeliği (DUY) — gün öncesi/dengeleme güç piyasası, dengesizlik tutarları, uzlaştırma hesapları. Tutar EPİAŞ verisiyle ve bilirkişi hesabıyla doğrulanır.
4. **İspat ve veri**: Sayaç/ölçüm verisi, uzlaştırmaya esas veri ve EPİAŞ bildirimleri esas delildir; ispat yükü bedeli talep/itiraz eden taraftadır.
5. **İtiraz yolu**: Önce EPİAŞ/ilgili tüzel kişiye düzeltme/itiraz; EPDK işlemi söz konusuysa İYUK m.7 süresinde idari dava; salt özel hukuk alacağı ise adli yargı/tahkim ayrımı yapılır.

## Çıktı modülleri
- Tarife/uzlaştırma uygunluk ve fark hesabı.
- İtiraz/düzeltme başvuru taslağı.
- Dava/ tahkim için tutar ve delil dizini.

## Plugin bağlamı

Bu beceri `enerji-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
