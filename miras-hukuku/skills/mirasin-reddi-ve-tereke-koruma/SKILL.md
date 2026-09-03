---
name: mirasin-reddi-ve-tereke-koruma
description: "Tereke borca batık ya da belirsizken mirasçının sorumluluktan korunması için ret, defter tutma veya resmi tasfiye seçeneklerini değerlendirmek; üç aylık süre, hükmen ret ve mirasçıların borçtan sorumluluğu söz konusu olduğunda kullanılır."
---

# Mirasın Reddi, Defter Tutma ve Tereke Koruma

## Görev
Mirasçıyı külli halefiyetin getirdiği borç sorumluluğundan korumak; ret (gerçek/hükmen), tutulan defterle kabul ve resmi tasfiye yollarını TMK m.589-636 çerçevesinde değerlendirmek.

## Soğuk başlangıç (intake)
- Mirasbırakan ne zaman öldü? Mirasçı ölümü/sıfatını ne zaman öğrendi?
- Terekenin aktif/pasif durumu biliniyor mu? Borca batık mı?
- Mirasçı terekeye karıştı, tereke malını sahiplendi mi (m.610)?
- Daha önce mirasçılardan reddeden oldu mu? (sıra ve sonuç)
- Mirasçı küçük/kısıtlı mı? (yasal temsilci ve izin)

## Denetim şeması
1. **Süreyi sabitle (m.606):** Ret, mirasın açıldığını/mirasçılık sıfatını öğrenmeden itibaren üç ay içinde sulh hukuk mahkemesine sözlü/yazılı beyanla yapılır. Süre hak düşürücüdür.
2. **Hükmen reddi değerlendir (m.605/2):** Ölümü anında mirasbırakanın ödemeden aczi açıkça belli veya resmen tespit edilmişse, miras reddedilmiş sayılır; bu, alacaklıya karşı tespit/menfi tespit davasıyla ileri sürülür ve üç aylık süreye tabi değildir.
3. **Ret hakkının düşmesi (m.610):** Süre içinde reddetmeyen, tereke işlerine olağan dışı karışan, malları gizleyen/sahiplenen mirasçı reddedemez.
4. **Ret sonuçları (m.611-613):** Reddeden, miras açılmadan önce ölmüş gibi; payı diğer mirasçılara/sonraki zümreye geçer. En yakın mirasçıların tamamı reddederse tereke iflas hükümlerine göre tasfiye edilir (m.612).
5. **Defter tutma (m.619-631):** İstemle tereke yazımı; deftere geçmeyen borçtan sorumluluk sınırlanır (m.629). Resmi tasfiye (m.632-636) borçtan kişisel sorumluluğu kaldırır.
6. **Ara sonuç:** uygun koruma yolu + süre durumu + dilekçe/başvuru türü. İspat: ölüm/öğrenme tarihi, borca batıklık delili (m.6).

## Çıktı modülleri
- Mirasın reddi beyan dilekçesi (sulh hukuk) taslağı
- Hükmen ret (mirasçı olmadığının tespiti) dava taslağı
- Defter tutma/resmi tasfiye talep dilekçesi
- Süre takvimi ve sorumluluk riski notu

## Plugin bağlamı

Bu beceri `miras-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
