---
name: ciro-devir-zinciri
description: "Emre yazılı senetlerde ciro türlerini, ciro zincirinin muntazamlığını ve yetkili hamil sıfatını incelemek; hak sahipliği, devir geçerliliği ve hamilin konumunu belirlerken kullanılır."
---

# Ciro ve Devir Zinciri

## Görev
Emre yazılı kambiyo senedinin ciro yoluyla devrini denetlemek, ciro zincirinin muntazamlığını ve hamilin yetkili hamil sıfatını tespit etmek; özel ciro türlerinin (tahsil, rehin, beyaz) sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
- Senedin arkasında kaç ciro var; cirolar tarih sırası ve isim bakımından birbirine bağlanıyor mu?
- Beyaz ciro (imza-only) var mı; son hamil senedi nasıl edinmiş?
- Cirolardan biri tahsil ("bedeli tahsil içindir") veya rehin amaçlı mı?
- Devirler arasında temlik, miras veya başka bir kanuni intikal var mı?

## Denetim şeması
1. Devir biçimi: emre senet ciro + teslimle, hamiline senet teslimle, nama senet alacağın temlikiyle devredilir (TTK m.681, m.654). Emre senede "emre yazılı değildir" kaydı eklenirse nama hükmüne girer ve temlikle devredilir (m.681/2).
2. Ciro türleri: tam ciro (devir), beyaz ciro (m.683 — imza yeter; hamil boşluğu doldurabilir veya teslimle devredebilir), tahsil cirosu (m.688 — hamil sadece temsilci, borçlu lehtara karşı def'ilerini ileri sürebilir), rehin cirosu (m.689 — hamile rehin hakkı).
3. Zincir muntazamlığı: hamil, kesintisiz ciro zinciriyle hakkını ispatlarsa yetkili hamil sayılır; beyaz ciroyu izleyen imza önceki ciroyu yapmış gibi kabul edilir (TTK m.686). Çizilmiş cirolar yok sayılır.
4. İyiniyetli iktisap: senedi kesintisiz ciroyla iyiniyetle edinen hamilden senet geri istenemez (TTK m.687/iktisap); kişisel def'iler iyiniyetli hamile karşı ileri sürülemez (m.687/def'i).
5. Ara sonuç: zincir muntazamsa hamil yetkili hamildir ve takip/ödeme talep edebilir; zincirde kopukluk veya tahsil cirosu varsa hamilin hak ve def'i konumu yeniden tartılır.

## Çıktı modülleri
- Ciro zinciri akış şeması (cirant > ciro türü > hamil).
- Yetkili hamil değerlendirme notu (m.686 dayanaklı).
- Def'i konumu özeti (iyiniyet/tahsil cirosu etkisi).

## Plugin bağlamı

Bu beceri `kiymetli-evrak` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
