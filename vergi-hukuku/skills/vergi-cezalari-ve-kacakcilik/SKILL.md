---
name: vergi-cezalari-ve-kacakcilik
description: "Vergi ziyaı, usulsüzlük ve özel usulsüzlük cezaları ile VUK m.359 kaçakçılık suçunu değerlendirmek; ceza ihbarnamesi geldiğinde veya ceza riski sorulduğunda kullanılır."
---

# Vergi Cezaları ve Kaçakçılık Suçu

## Görev
Kesilen idari vergi cezasının türünü ve tutarını denetlemek, kaçakçılık suçu (VUK m.359) riskini değerlendirmek ve ceza indirimi/kaldırma yollarını planlamak.

## Soğuk başlangıç (intake)
1. Ceza türü nedir (vergi ziyaı / usulsüzlük / özel usulsüzlük)?
2. Vergi ziyaı cezası bir kat mı, üç kat mı kesilmiş?
3. Sahte/muhteviyatı itibarıyla yanıltıcı belge (SMİYB) iddiası var mı?
4. Aynı fiilden vergi suçu raporu düzenlenip Cumhuriyet savcılığına bildirim yapıldı mı?
5. Pişmanlık, uzlaşma veya cezada indirim talep edildi mi?

## Denetim şeması
1. **Vergi ziyaı:** VUK m.341 — verginin zamanında tahakkuk etmemesi/eksik tahakkuku. Ceza VUK m.344 uyarınca ziyaa uğratılan verginin bir katı; fiil m.359'daki kaçakçılık fiiliyle işlenmişse üç katı. Kat hesabını doğrula.
2. **Usulsüzlük:** VUK m.351-352 — kanuni ödevlerin biçimsel ihlali; derecelere göre maktu. Re'sen takdiri gerektiren usulsüzlüklerde ağırlaştırma kontrolü.
3. **Özel usulsüzlük:** VUK m.353, mük.355 — belge düzenine aykırılık (fatura vermeme/almama), bilgi verme ödevinin ihlali; tutar ve üst sınır denetimi.
4. **Tek fiil-çok ceza:** VUK m.336 — bir fiil hem usulsüzlük hem vergi ziyaına yol açıyorsa ağır olan kesilir; içtima kuralını uygula.
5. **Kaçakçılık suçu:** VUK m.359 — defter/belgede hile, sahte belge düzenleme/kullanma, defter gizleme. Bu hapis cezasını gerektiren suç olup vergi mahkemesinin değil ceza mahkemesinin görev alanındadır; idari ceza ile bağımsızdır (non bis in idem tartışması ayrı değerlendirilir). m.359/son: etkin pişmanlık ve ödeme ile indirim imkânı.
6. **İndirim/kaldırma yolları:** VUK m.376 (cezada indirim — süresinde ödeme ve dava açmama şartı), uzlaşma (Ek m.1, m.11), pişmanlık (m.371 — ziyaı cezası kesilmez), düzeltme (m.116 vd.). Ara sonuç: hangi yol süreyi ve tutarı en çok lehe çevirir?

## Çıktı modülleri
- Ceza türü-tutar doğrulama tablosu (madde / oran / hesap).
- Kaçakçılık riski değerlendirme notu (m.359 unsur analizi, ceza yargısı uyarısı).
- İndirim/uzlaşma/pişmanlık karşılaştırma matrisi (süre, tutar, dava hakkı etkisi).
- Savunma dilekçesi argüman iskeleti.

## Plugin bağlamı

Bu beceri `vergi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
