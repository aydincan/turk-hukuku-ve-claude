---
name: tecavuz-davasi-talepleri
description: "Tecavüzün tespiti, durdurulması, giderilmesi, ürünlere el konulması, imha ve kararın ilanı taleplerini SMK m.149 ve FSEK m.66-70 çerçevesinde doğru ve eksiksiz kurgulamak gerektiğinde kullanılır."
---

# Tecavüz Davası ve Talep Mimarisi

## Görev
Tecavüz davasının talep sonucunu eksiksiz, infaza elverişli ve madde dayanaklı biçimde kurmak; sınai (SMK) ve telif (FSEK) rejimine göre talep paketini ayarlamak.

## Soğuk başlangıç (intake)
- Hangi hak ihlal edildi ve ihlal devam ediyor mu?
- Talep sadece durdurma mı, tazminat da var mı, imha/ilan isteniyor mu?
- Karşı tarafın elinde tecavüz ürünü/üretim aracı var mı?
- Manevi tazminat (itibar zedelenmesi) gündemde mi?

## Denetim şeması
1. Tespit ve durdurma: Tecavüzün tespiti, durdurulması ve giderilmesi (SMK m.149/1-a,b,c; FSEK m.66 ref', m.69 men'). Talep, fiili ve sonuçlarını kapsayacak şekilde somutlaştırılır.
2. El koyma ve imha: Tecavüz oluşturan ürünlere, bunların üretiminde münhasıran kullanılan araç/cihazlara el konulması ve imhası (SMK m.149/1-ç,d; m.149/1-e mülkiyetin tanınması). Ölçülülük gözetilir.
3. Tazminat: Maddi tazminat (yoksun kalınan kazanç) ve istenirse itibar tazminatı (SMK m.150) ile manevi tazminat (TBK m.58 atfıyla). FSEK'te m.68 (bedelin üç katına kadar) ve m.70 (maddi-manevi) seçenekleri.
4. Hesaplama yöntemi: SMK m.151 — davacının seçimine göre (a) lisans verseydi elde edeceği gelir, (b) tecavüz edenin elde ettiği kazanç, (c) sözleşme yapılsaydı ödenecek lisans bedeli. Seçim bilinçli yapılır; defter-kayıt ibrazı talep edilir.
5. İlan: Masrafı tecavüz edene ait olmak üzere hükmün ilanı (SMK m.149/1-f). Haklı menfaat şartı.
6. İspat yükü: Tecavüz ve zarar davacıda; tecavüz edenin kazancı için defterlerin sunulması ve bilirkişi. Ara sonuç: tedbir + esas + tazminat birlikte ama ayrı ayrı gerekçelendirilir.

## Çıktı modülleri
- Talep sonucu (numaralı, infaza elverişli) taslağı.
- Tazminat seçeneği ve hesap yöntemi notu (SMK m.151).
- Manevi tazminat ve ilan gerekçesi.

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
