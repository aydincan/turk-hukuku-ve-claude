---
name: eczaci-meslek-disiplin-sorumluluk
description: "Eczacının hatalı ilaç verme, danışmanlık, sır saklama ve oda disiplin sorumluluğu ile hastaya karşı tazminat sorumluluğu konularında kullanılır."
---

# Eczacının Meslek, Disiplin ve Tazminat Sorumluluğu

## Görev
Eczacının mesleki kusurundan (yanlış ilaç/doz, danışmanlık eksikliği, reçeteye aykırı verme) doğan disiplin, hukuki ve cezai sorumluluğunu değerlendirmek.

## Soğuk başlangıç (intake)
- İddia: yanlış ilaç/doz verme, muadil değişimi, reçeteye aykırılık, danışmanlık eksikliği, sır ihlali mi?
- Hastada zarar doğdu mu; nedensellik kuruluyor mu?
- Süreç: hasta şikâyeti, eczacı odası disiplin, savcılık, tazminat davası?
- Reçete ve teslim kaydı (varsa kamera/İTS) mevcut mu?

## Denetim şeması
1. **Sorumluluk türleri.** Disiplin (eczacı odası/Türk Eczacıları Birliği mevzuatı), hukuki tazminat (TBK m.49 vd. haksız fiil veya hasta-eczane ilişkisinde sözleşmesel sorumluluk), cezai (taksirle yaralama TCK m.89 / öldürme m.85).
2. **Kusur ve özen.** Eczacının uzman özen yükümlülüğü: reçeteyi kontrol, etkileşim uyarısı, doğru ürün/doz teslimi, muadil kuralları. Ara sonuç: özen yükümlülüğü ihlal edildi mi (objektif özen ölçütü)?
3. **Nedensellik ve zarar.** Hatalı teslim ile zarar arasında uygun illiyet; hastanın kendi kusuru/araya giren etken müterafık kusur (TBK m.52) doğurabilir. İspat: kusuru/zararı davacı; özenli davranışı eczacı belgelemeye çalışır.
4. **Sır saklama ve veri.** Hasta sağlık verisi özel nitelikli kişisel veridir (KVKK m.6); ifşa hem disiplin hem tazminat hem ceza (TCK m.136) sorumluluğu doğurabilir.
5. **Süre.** Haksız fiilde TBK m.72 zamanaşımı; ceza zamanaşımı uzunsa o uygulanır.

## Çıktı modülleri
- Sorumluluk türü ve görevli mercilere göre ayrıştırma.
- Kusur-nedensellik-zarar altlama notu.
- Disiplin savunması / tazminat dava değerlendirmesi [doldurulacak].

## Plugin bağlamı

Bu beceri `eczacilik-ilac` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
