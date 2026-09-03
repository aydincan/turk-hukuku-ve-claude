---
name: baslangic-hukumleri-sistematigi
description: "Bir medeni hukuk uyuşmazlığında TMK başlangıç hükümlerinden hangisinin (m.1-m.7) devreye gireceği belirsiz olduğunda; süzgeç katmanlarını ayırt edip doğru hükmü ve onun işlevini seçmek için kullanılır."
---

# Başlangıç Hükümleri Sistematiği ve Doğru Hükmü Seçme

## Görev
Eldeki uyuşmazlıkta TMK m.1-m.7 arasındaki hangi başlangıç hükmünün, hangi işlevle (yorum, ispat, takdir, düzeltme) devreye gireceğini doğru teşhis etmek; başlangıç hükmünü esas özel normla karıştırmamak.

## Soğuk başlangıç (intake)
- Uyuşmazlığa doğrudan uygulanan özel norm hangisi (kira, mülkiyet, nafaka, sözleşme...)?
- Sorun bir hakkın kullanım tarzında mı (m.2), bir hakkın kazanılmasında bilgisizlikte mi (m.3), hâkimin takdirinde mi (m.4), kimin ispatlayacağında mı (m.6)?
- Olayda resmî sicil/senet (tapu, nüfus, resmî senet) var mı (m.7)?
- Başlangıç hükmü talep kaynağı mı sanılıyor, yoksa mevcut hakka mı eklemleniyor?

## Denetim şeması
1. **Önce özel norm, sonra süzgeç** — Başlangıç hükümleri (TMK m.5 yoluyla tüm özel hukukta) bağımsız talep doğurmaz; mevcut hak/borcu yorumlar, sınırlar veya tamamlar. Önce maddi kural tespit edilir.
2. **İşleve göre ayrım** — m.1: kaynak ve boşluk doldurma (kural yoksa). m.2: dürüstlük + hakkın kötüye kullanılması (kural var ama kullanım tarzı sorunlu). m.3: iyiniyet (bir hakkın doğumu bilgisizliğe bağlıysa). m.4: takdir/hakkaniyet (kanun hâkime alan bırakmışsa). m.6: ispat yükü. m.7: resmî sicil/senet karinesi.
3. **m.2 ile m.3 ayrımı** — m.2 bir *davranış* kuralıdır (hakkı nasıl kullanmalı); m.3 bir *bilgi* durumudur (kazanımda bilgisizliğin korunması). İkisi karıştırılmaz.
4. **m.5'in kapsamı** — Genel nitelikli TMK/TBK hükümleri "uygun düştüğü ölçüde" diğer özel hukuk ilişkilerine kıyasen uygulanır; niteliği elvermeyen hükümler taşınmaz.
5. **Ara sonuç** — Hangi başlangıç hükmü, hangi işlevle, hangi özel normun üzerine konuyor? Tek cümlede formüle edilir.

## Çıktı modülleri
- Özel norm + başlangıç hükmü eşleştirme tablosu (madde + işlev).
- Seçilen hükmün gerekçesi ve reddedilen alternatifler.
- İşlev notu (yorum/ispat/takdir/düzeltme).
- İlkesel içtihat atfı, künye `[doğrulanacak]` (karararama.yargitay.gov.tr).

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
