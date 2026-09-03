---
name: stajyer-ve-yetkilendirme
description: "Stajyer avukat veya yardımcı personele görev verirken, yetki sınırlarını ve sorumluluk-gizlilik çerçevesini belirlerken ve süpervizyon kurarken kullanılır."
---

# Stajyer Yönetimi ve Görev Yetkilendirmesi

## Görev
Stajyer avukat ve yardımcı personele verilecek görevleri meslek hukuku sınırları içinde tanımlamak; gizlilik ve süpervizyon çerçevesini kurmak; büronun sorumluluğunu yönetmek.

## Soğuk başlangıç (intake)
1. Görev kime verilecek (stajyer avukat / sekreter / paralegal) ve niteliği ne?
2. Görev bağımsız temsil mi gerektiriyor yoksa hazırlık/araştırma işi mi?
3. Stajyerin yetki belgesi/durumu ve gözetimi sağlayacak avukat kim?
4. Görevde gizli müvekkil bilgisi ve çıkar çatışması riski var mı?

## Denetim şeması
1. **Yetki sınırı (1136 m.23-26 staj rejimi)**: Stajyer avukatın yetkileri kanunla sınırlıdır; belirli işler yanında bulunduğu avukatın gözetiminde yürütülür, bağımsız ve sınırsız temsil söz konusu değildir. Görev bu sınıra göre tanımlanır.
2. **Süpervizyon**: Her görev için sorumlu/gözeten avukat atanır; çıktı kalite kontrolünden geçer (özen — TBK m.506).
3. **Gizlilik (1136 m.36)**: Stajyer ve personel sır saklama yükümlülüğü kapsamındadır; yazılı gizlilik taahhüdü ve erişim sınırlaması (KVKK m.12) uygulanır.
4. **Çıkar çatışması**: Görevlendirme öncesi ilgili kişinin o dosyada çatışması olmadığı teyit edilir (1136 m.38).
5. **Sorumluluk**: Stajyer/personel hatasının büroyu bağladığı bilinciyle, riskli işlerde çift kontrol konur.
6. **Ara sonuç**: Yetkiye uygun görev + atanmış süpervizör + gizlilik + çatışma teyidi sağlanınca görev verilebilir.

## Çıktı modülleri
- Görev tanım ve yetki sınırı notu.
- Gizlilik/veri erişim taahhüdü taslağı.
- Süpervizyon ve kontrol akışı.

## Plugin bağlamı

Bu beceri `hukuk-burosu-yonetimi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
