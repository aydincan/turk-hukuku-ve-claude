---
name: mali-manevi-haklar-haritasi
description: "Eser üzerindeki hangi mali ve manevi hakların söz konusu olduğunu, kapsamını ve sınırlarını çıkarmak gerektiğinde; ihlal iddiasını doğru hak kalemine oturtmak ve devre konu olabilecek hakları ayırmak için kullanılır."
---

# Mali ve Manevi Hakların Haritalanması

## Görev
Somut eser üzerinde mevcut mali ve manevi hakları tek tek çıkarmak, ihlal/talep iddiasını doğru hak kalemine oturtmak ve hangi hakların devredilebilir olduğunu ayırt etmek.

## Soğuk başlangıç (intake)
- Eser ve sahibi netleşti mi; hangi kullanım/eylem tartışmalı?
- Eylem eserin kopyalanması mı, uyarlanması mı, çevrimiçi paylaşımı mı, sahnelenmesi mi?
- Eser sahibinin adı belirtilmiş mi; üzerinde değişiklik yapılmış mı?
- Hak halen sahibinde mi, devredilmiş/lisanslanmış mı?

## Denetim şeması
1. Mali hak tasnifi (m.20): İhlal eyleminin hangi mali hakka girdiğini belirle — işleme/uyarlama (m.21), çoğaltma (m.22, dijital kopya dâhil), yayma (m.23, ilk satışla yayma hakkının tükenmesi m.23/2), temsil/sahneleme (m.24), işaret-ses-görüntü nakline yarayan araçlarla umuma iletim ve erişilebilir kılma/internet (m.25). Her mali hak bağımsızdır; biri için verilen izin diğerini kapsamaz.
2. Manevi hak tasnifi (m.14-17): Umuma arz yetkisi (m.14), adın belirtilmesi/eser sahibi olarak tanıtılma (m.15), eserde değişiklik yapılmasını men (m.16), eser sahibinin malik ve zilyede karşı hakları (m.17). Manevi haklar devredilemez; yalnızca kullanımı yetkilendirilebilir (m.16/son, m.19).
3. Süre süzgeci: Mali haklar koruma süresiyle sınırlıdır (kural: sahibin ölümü + 70 yıl, m.27; m.26-29). Süre dolmuşsa eser kamuya mal olmuştur; manevi menfaatler m.19 kapsamında belirli kişilerce korunabilir.
4. İhlal-hak eşleştirme: Eylemi madde madde hangi hakkı çiğnediğine bağla; birden çok hakkın ihlali (ör. izinsiz uyarlama + ad belirtmeme) ayrı ayrı sayılır.
5. Ara sonuç: İhlal edilen hak(lar), bunların sahibi ve süresi belirlenir; talep türü (ref/men/tazminat) buna göre kurgulanır.

İspat yükü: hakkın kapsamını ve ihlali iddia eden ispatlar; izin/devir savunmasını ileri süren onu ispatlar (HMK m.190).

## Çıktı modülleri
- Hak haritası tablosu (mali/manevi hak kalemi — madde — sahip — süre — ihlal eylemi).
- Devredilebilir/devredilemez ayrımı.
- Talep türüne köprü notu.

## Plugin bağlamı

Bu beceri `telif-haklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
