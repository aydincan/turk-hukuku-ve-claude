---
name: gecerlilik-ve-hukumsuzluk
description: "Sözleşmenin içeriğinin emredici hükümlere, ahlaka veya kamu düzenine aykırı olup olmadığı, kesin hükümsüzlük veya gabin iddiası bulunduğunda kullanılır."
---

# Geçerlilik, Hükümsüzlük ve Aşırı Yararlanma

## Görev
Sözleşmenin içerik yönünden geçerliliğini denetlemek; kesin hükümsüzlük, kısmi hükümsüzlük ve aşırı yararlanma (gabin) hâllerini ve sonuçlarını ortaya koymak.

## Soğuk başlangıç (intake)
- Sözleşmenin konusu hukuken mümkün ve belirli mi?
- İçerik emredici bir kurala, ahlaka veya kamu düzenine aykırı mı?
- Taraflardan biri zor durum, deneyimsizlik veya düşüncesizlik içinde miydi; edimler arasında açık oransızlık var mı?
- Sakatlık tüm sözleşmeyi mi yoksa tek bir maddeyi mi etkiliyor?

## Denetim şeması
1. Kesin hükümsüzlük: TBK m.27/f.1 — kanunun emredici hükümlerine, ahlaka, kamu düzenine, kişilik haklarına aykırılık veya başlangıçtaki objektif imkânsızlık. Hâkim resen dikkate alır, herkes ileri sürebilir, sonradan icazetle geçerli hâle gelmez.
2. Kısmi hükümsüzlük: m.27/f.2 — sakatlık yalnız bazı hükümlerde ise sözleşme kalanıyla ayakta kalır; tarafların bu hükümler olmaksızın sözleşmeyi yapmayacağı anlaşılmadıkça. Değiştirilmiş kısmi butlan/lehe yorum imkânı.
3. Aşırı yararlanma (gabin): m.28 — objektif unsur (edimler arası açık oransızlık) + sübjektif unsur (zor durum, deneyimsizlik, düşüncesizlikten yararlanma). Sonuç: oransızlığın giderilmesi veya sözleşmeden dönme; süre bir yıl/beş yıl (m.28/f.2).
4. İmkânsızlık ayrımı: Başlangıçtaki imkânsızlık m.27 (hükümsüzlük); sonraki imkânsızlık m.136 (borçtan kurtulma). Karıştırılmamalı.
5. İspat yükü: Hükümsüzlük iddiasını ileri süren, aykırılık veya gabin unsurlarını ispatla yükümlüdür.
6. Ara sonuç: Sözleşme tümüyle mi, kısmen mi geçersiz; iade ve tazminat sonuçları (sebepsiz zenginleşme, culpa in contrahendo).

## Çıktı modülleri
- Geçerlilik denetim raporu (madde madde).
- Hükümsüzlük türü ve kapsamı değerlendirmesi.
- Gabin hâlinde uyarlama/dönme talep taslağı iskeleti.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
