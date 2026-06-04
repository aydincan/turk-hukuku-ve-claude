---
name: disiplin-ve-savunma-sureci
description: "Çalışan kusuru, devamsızlık, talimata aykırılık gibi olaylarda tutanak, savunma istem ve disiplin cezası süreci kurulacaksa ya da mevcut disiplin işlemi denetlenecekse kullanılır."
---

# Disiplin ve Savunma Süreci Yönetimi

## Görev
Çalışan kusurlu davranışını, ileride haklı/geçerli feshe dayanak olacak biçimde usulüne uygun belgelemek; orantılı disiplin yaptırımını uygulamak ve savunma hakkını hukuka uygun kullandırmak.

## Soğuk başlangıç (intake)
1. Somut olay nedir, tarihi ve tanıkları kim (devamsızlık, talimata aykırılık, kavga, gizlilik ihlali)?
2. İşyerinde disiplin yönetmeliği/ceza skalası var mı?
3. Çalışanın sicilinde benzer önceki ihtar/ceza var mı (tekerrür-orantılılık)?
4. Olay kaç gün önce gerçekleşti?

## Denetim şeması
1. **Tespit ve tutanak**: Olay anında, en az iki tanık imzasıyla, somut yer-zaman-davranış içeren tutanak düzenle. Belirsiz ifadeler ("saygısızdı") değil, fiil tarif et.
2. **Savunma istemi (4857 m.19/2)**: Çalışana yazılı, makul süreli (uygulamada genelde 2-3 işgünü) savunma daveti tebliğ et; sorulan davranış açıkça belirtilsin. Savunma vermezse bunu da tutanağa bağla.
3. **Devamsızlıkta özel rejim (m.25/II-g)**: İzinsiz/mazeretsiz ardı ardına **2 işgünü**, bir ayda iki kez tatil sonrası işgünü ya da bir ayda **3 işgünü** devamsızlık haklı fesih sebebidir; her gün ayrı tutanakla ve tercihen ihtarla belgelenmeli.
4. **Orantılılık ve eşit davranma (m.5)**: Yaptırım fiil ağırlığıyla orantılı; benzer olayda farklı çalışana farklı muamele eşitlik ihlali doğurur.
5. **Süre (m.26)**: Haklı fesih sebebi olacaksa öğrenmeden itibaren 6 işgünü içinde harekete geç.
6. **İspat**: Disiplin sürecinin tüm adımları (tutanak, tebliğ, savunma) yazılı delille kanıtlanmalı; ispat yükü işverende.
7. **Ara sonuç**: Savunma alınmadan/orantısız ceza → fesihte usulsüzlük ve eşitsiz muamele riski.

## Çıktı modülleri
- Olay tutanağı taslağı (tanık imza alanlı).
- Savunma istem (tebliğ) yazısı taslağı.
- Disiplin kurulu kararı / yazılı ihtar taslağı ve orantılılık notu.

## Plugin bağlamı

Bu beceri `ik-insan-kaynaklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
