---
name: prim-temerrut
description: "Primin ödenmemesi nedeniyle teminatın askıya alınması, sözleşmenin feshi veya rizikonun primsiz dönemde gerçekleşmesi tartışıldığında kullanılır; prim temerrüdünün sigortacının sorumluluğuna etkisini denetler."
---

# Prim Ödeme Borcu ve Temerrüt

## Görev
Primin (ilk veya takip eden taksit) zamanında ödenip ödenmediğini, ödenmemenin teminata ve sigortacının sorumluluğuna etkisini, fesih ve askı sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
1. Hangi prim ödenmedi: ilk prim mi, takip eden taksit mi?
2. Ödeme tarihi ve vadesi ne; kısmi ödeme var mı?
3. Sigortacı ihtar/uyarı gönderdi mi, fesih iradesi açıklandı mı?
4. Riziko hangi tarihte gerçekleşti — prim borcu var iken mi?

## Denetim şeması
1. **Borcun niteliği.** TTK m.1430: prim, sözleşmede kararlaştırılan tutar ve vadede ödenir; götürülecek borçtur. Ara sonuç: hangi prim, hangi vade?
2. **İlk primde temerrüt.** TTK m.1430/3 ve genel şartlar: ilk taksit/peşin prim ödenmeden sigortacının sorumluluğu başlamaz; bu dönemde gerçekleşen riziko karşılanmaz.
3. **Takip eden primde temerrüt.** TTK m.1434: sigortacı, ödememe halinde sigorta ettirene noter aracılığıyla ya da iadeli taahhütlü mektupla on günlük süre vererek borcun ödenmesini ister. Süre sonunda ödeme yapılmazsa sözleşme feshedilmiş sayılır; ihtarda bu sonuç belirtilmelidir.
4. **Askı/sorumluluk boşluğu.** İhtar süresince ve fesihten sonra gerçekleşen rizikoda sigortacının sorumluluğu doğmaz. İstisna: usulüne uygun ihtar çekilmemişse fesih sonucu doğmaz; teminat devam eder.
5. **İspat.** Ödemeyi sigorta ettiren, usulüne uygun ihtarı ve feshi sigortacı ispatlar.

## Çıktı modülleri
- Prim ödeme/temerrüt zaman çizelgesi.
- İhtar usulü uygunluk kontrolü (m.1434).
- Riziko anında teminat durumu (var/askıda/fesihli).
- Sigortalı veya sigortacı için argüman seti.

## Plugin bağlamı

Bu beceri `sigorta-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
