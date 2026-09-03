---
name: temel-kavramlar-ve-sistem
description: "Bilirkişi delilinin niteliği, ne zaman caiz olduğu, hâkim-bilirkişi görev ayrımı ve denetim mantığının çerçevesini kurmak istendiğinde; rapora ilk bakışta hangi gözle yaklaşılacağını belirlemek için kullanılır."
---

# Bilirkişilik Temel Kavramları ve Sistematik

## Görev
Bilirkişi raporunu denetlemeye başlamadan önce zihinsel çerçeveyi kurmak: raporun bir **takdiri delil** olduğunu, hâkimi bağlamadığını (HMK m.282), yalnızca özel/teknik bilgi gerektiren konularda caiz olduğunu (HMK m.266) ve hukuki nitelendirmenin hâkime ait kaldığını netleştirmek.

## Soğuk başlangıç (intake)
- Rapor hangi yargı kolundan (hukuk/ceza/idari) ve hangi dava türünden geliyor?
- Bilirkişi hangi uzmanlık alanından; rapor o alanla mı sınırlı kalmış?
- Görevlendirme kararını gördünüz mü; bilirkişiye sorulan sorular elinizde mi?
- Rapor size ne zaman tebliğ edildi (iki haftalık itiraz süresi için)?

## Denetim şeması
1. **Caizlik süzgeci (HMK m.266):** Konu hâkimlik mesleğinin genel/hukuki bilgisiyle çözülebilecek nitelikteyse bilirkişiye gidilmesi başlı başına hukuka aykırıdır. Örn. "sözleşme geçerli midir", "fesih haklı mıdır" gibi salt hukuki sorular bilirkişiye havale edilemez. Ara sonuç: konu teknik mi, hukuki mi?
2. **Görev ayrımı (HMK m.279/son):** Bilirkişi hukuki nitelendirme ve değerlendirme yapamaz; yalnızca teknik kanaat bildirir. Rapor "davalı kusurludur, tazminata hükmedilmelidir" diyorsa görev sınırını aşmıştır.
3. **Delil değeri (HMK m.282):** Rapor hâkimi bağlamaz; serbestçe takdir edilir. Bu, rapora karşı somut, gerekçeli karşı argüman üretmenin meşru zeminidir. İspat yükü esas davadaki dağılıma göre kalır; rapor ispat yükünü değiştirmez.
4. **Bizzat ifa (HMK m.277):** Bilirkişi görevini devredemez; raporu fiilen başkası hazırlamışsa itiraz konusudur.
5. **Ara sonuç:** Rapor caiz bir konuda mı, görev sınırı içinde mi, gerekçeli mi? Bu üç soruya verilecek yanıt, sonraki ayrıntılı denetimin yönünü belirler.

## Çıktı modülleri
- Raporun bir cümlelik konumlandırması (yargı kolu, dava türü, bilirkişi alanı).
- Caizlik ve görev sınırı ön değerlendirmesi (uygun / şüpheli / aykırı).
- Denetimin odaklanacağı eksenlerin listesi (usul / metodoloji / hesap / çelişki).
- İtiraz süresinin son günü ve takvim uyarısı.

## Plugin bağlamı

Bu beceri `bilirkisi-rapor-inceleme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
