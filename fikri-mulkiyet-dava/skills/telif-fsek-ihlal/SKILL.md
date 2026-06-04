---
name: telif-fsek-ihlal
description: "Eser, işleme, çoğaltma, umuma iletim, intihal veya yazılım kopyalama iddialarında FSEK çerçevesinde eser niteliği, mali-manevi hak ihlali ve ihlal eden fiilin tespiti gerektiğinde kullanılır."
---

# Telif Hakkı İhlali Denetimi (FSEK)

## Görev
Bir fikir ve sanat eseri üzerindeki mali veya manevi hakkın ihlal edilip edilmediğini FSEK çerçevesinde belirlemek ve ref'/men/tazminat taleplerini hazırlamak.

## Soğuk başlangıç (intake)
- İhlale konu yapıt nedir (yazı, müzik, yazılım, görsel, sinema eseri)?
- Yapıt FSEK m.1/B-2 anlamında "sahibinin hususiyetini taşıyan" eser mi; hangi türe girer (m.2-6)?
- Eser sahibi/hak sahibi kim; devir-lisans var mı; çalışan eseri (m.18/2) mi?
- İhlal çoğaltma, yayma, umuma iletim, işleme yoksa manevi hak (ad belirtme, bütünlük) ihlali mi?

## Denetim şeması
1. Eser niteliği: Yapıtın eser sayılması için fikrî çaba ve hususiyet aranır (FSEK m.1/B, m.2-6). Fikir değil ifade korunur; sıradan/teknik zorunluluk taşıyan unsurlar dışlanır.
2. Hak sahipliği: Eser sahibi onu meydana getirendir (m.8); çalışanın eseri işverene (m.18/2), sipariş üzerine eserlerde sözleşme belirleyici. Bağlantılı haklar (icracı, yapımcı, yayın) m.80.
3. İhlal edilen hak: Mali haklar — işleme (m.21), çoğaltma (m.22), yayma (m.23), temsil (m.24), umuma iletim/işaret-ses-görüntü nakli (m.25). Manevi haklar — umuma arz, adın belirtilmesi, eserde değişiklik yasağı (m.14-16).
4. İhlal fiili ve benzerlik: İntihal/kopyalamada esaslı benzerlik ve erişim ölçütü; yazılımda kaynak kod kopyalama veya yetkisiz çoğaltma. İstisnalar (iktibas m.35, kişisel kullanım m.38) denetlenir.
5. İspat yükü: Eser sahipliği ve ihlal davacıda; lisans/izin savunması davalıda. Tarih/öncelik için delil tespiti (HMK m.400) ve noter onayı.
6. Ara sonuç: İhlal sabitse tecavüzün ref'i (m.66-68), men'i (m.69) ve tazminat (m.68 üç kata kadar bedel; m.70 maddi-manevi) kurgulanır.

## Çıktı modülleri
- Eser niteliği ve hak sahipliği değerlendirmesi.
- İhlal edilen mali/manevi hak listesi (FSEK madde atıflı).
- Talep ve tazminat seçeneği notu (m.68/m.70).

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
