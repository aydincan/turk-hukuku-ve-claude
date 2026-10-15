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
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
