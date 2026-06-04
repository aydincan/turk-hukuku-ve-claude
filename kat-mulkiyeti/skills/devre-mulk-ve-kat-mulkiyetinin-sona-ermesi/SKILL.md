---
name: devre-mulk-ve-kat-mulkiyetinin-sona-ermesi
description: "Bağımsız bölüm üzerinde dönem dönem (devre mülk) yararlanma hakkının kurulması/kullanılması ya da kat mülkiyetinin sona erdirilmesi (anayapının yok olması, kamulaştırma, terk veya maliklerin istemiyle) gündeme geldiğinde kullanılır."
---

# Devre Mülk ve Kat Mülkiyetinin Sona Ermesi

## Görev
İki ayrı özel kurumu yönetmek: (1) bir mesken nitelikli bağımsız bölümde dönemsel yararlanma sağlayan devre mülk hakkının kuruluş ve kullanım rejimi (KMK m.57-65); (2) kat mülkiyetinin/kat irtifakının sona ermesi hâlleri ve sonuçları (KMK m.46-54).

## Soğuk başlangıç (intake)
- Devre mülk mü kuruluyor/kullanılıyor, yoksa mevcut kat mülkiyetinin sona ermesi mi söz konusu?
- Devre mülkte: hak müşterek mülkiyet payına bağlı dönem hakkı olarak resmî senetle mi kuruldu?
- Sona ermede sebep ne: anayapının tamamen yok olması, kamulaştırma, malik istemi, yoksa kat irtifakının terkini mi?
- Anayapı kısmen mi tamamen mi harap; sigorta/yeniden yapım gündemde mi?

## Denetim şeması
1. **Devre mülk niteliği (KMK m.57-58)**: Devre mülk hakkı, mesken olarak kullanılmaya elverişli bir yapı veya bağımsız bölümün **ortak mülkiyet payına bağlı** olarak yılın belli dönemlerinde yararlanma hakkı sağlayan bir **irtifak hakkıdır** (m.57). Devre mülk hakkı ancak **mesken** nitelikli yerlerde kurulabilir (m.58).
2. **Kuruluş ve sözleşme (m.59-61)**: Hak, tapuda resmî senetle ve dönem tahsisini gösterir biçimde kurulur; dönemler bölünemez ve devir/miras yoluyla geçebilir. Yönetim ve kullanım için ayrı bir devre mülk sözleşmesi/planı düzenlenir.
3. **Kat mülkiyetinin sona ermesi (KMK m.46-47)**: Kat mülkiyeti, kütükteki kaydın silinmesiyle (maliklerin istemi/oybirliğiyle, m.46) veya **anayapının tamamen yok olması ya da harap olması** (m.47) hâlinde sona erer. Anayapı kısmen harap olur ve bağımsız bölümlerin yarısı kullanılmaz hâle gelirse özel rejim işler (m.47/2-3).
4. **Kamulaştırma (m.48, m.46)**: Bağımsız bölümün veya ortak yerin kamulaştırılması hâlinde arsa payı ve değer esasına göre paylaştırma yapılır.
5. **Sona ermenin sonuçları (m.49-50)**: Kat mülkiyeti sona erince anagayrimenkul, kat maliklerinin **arsa payları oranında paylı mülkiyetine** döner; tasfiye ve paylaşma TMK paylı mülkiyet hükümlerine göre yapılır.
6. **Yenileme/onarım yükümü (m.19, m.47)**: Tamamen yok olmamış yapıda onarım kurul kararına ve gider rejimine tabidir; harabiyet iddiası keşif-bilirkişi ile saptanır.
7. **Ara sonuç**: Devre mülkte geçerli kuruluş + dönem tahsisi; sona ermede sebep tespiti + paylı mülkiyete dönüş ve tasfiye.

## Çıktı modülleri
- Devre mülk kuruluş/sözleşme kontrol listesi (mesken şartı, dönem tahsisi).
- Sona erme sebebi tespit notu (m.46-48) ve paylaşma çerçevesi.
- Harabiyet/yeniden yapım için keşif-bilirkişi talebi notu.

## Plugin bağlamı

Bu beceri `kat-mulkiyeti` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
