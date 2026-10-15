---
name: muhlet-ve-tasdik-semasi
description: "Geçici mühletten kesin mühlete, oradan tasdike kadar konkordato sürecinin her aşamasını madde madde denetlemek, şartların ve sürelerin sağlanıp sağlanmadığını kontrol etmek gerektiğinde kullanılır."
---

# Mühlet ve Tasdik Denetim Şeması

## Görev
Konkordato sürecini talep-geçici mühlet-kesin mühlet-tasdik ekseninde adım adım denetlemek; her aşamada İİK'nın aradığı şartların, sürelerin ve çoğunlukların sağlanıp sağlanmadığını belirlemek.

## Soğuk başlangıç (intake)
- Süreç hangi aşamada: talep mi verildi, geçici mühlet mi var, tasdik aşaması mı?
- Talep belgeleri (İİK m.286) tam mı?
- Komiser atandı mı, alacaklılar kurulu kuruldu mu?
- Kabul için gerekli çoğunluk (m.302) sağlanıyor mu?

## Denetim şeması
1. **Talep ve belgeler (m.285-286).** Konkordato ön projesi, mal varlığı belgeleri, finansal tablolar, makul güvence veren denetim raporu (KGK standartlarına göre), alacaklı/alacak listesi eksiksiz mi? Eksik belge tamamlattırılır.
2. **Geçici mühlet (m.287).** Mahkeme belgeler tamamsa derhal geçici mühlet (kural üç ay; m.287/4 ile bir ay uzatma) verir ve geçici komiser atar. Geçici mühlet kesin mühletin sonuçlarını doğurur (m.288).
3. **Kesin mühlet (m.289).** Komiserin raporu ve borçlu/alacaklı dinlendikten sonra konkordatonun başarı ihtimali varsa bir yıllık kesin mühlet; güçlük halinde altı aya kadar uzatma. İspat yükü: borçlu, projenin başarı ihtimalini ortaya koymalıdır.
4. **Mühletin sonuçları (m.294-297).** Takip yasağı (rehinli alacaklılar bakımından istisna), faiz, sözleşmeler ve borçlunun tasarruf yetkisinin sınırlanması (m.297) denetlenir.
5. **Alacaklılar toplantısı ve çoğunluk (m.299-302).** Kaydedilmiş alacaklıların ve alacak miktarının yarısını ya da kaydedilmiş alacaklıların dörtte birini ve alacakların üçte ikisini aşan çoğunluk şartı (m.302/3) kontrol edilir.
6. **Tasdik şartları (m.305).** Teklifin borçlunun kaynaklarıyla orantılı olması, imtiyazlı alacakların tam ödenmesinin güvenceye bağlanması, yargılama gideri ve komiser ücretinin depo edilmesi. Ara sonuç: tasdik edilebilir mi, reddedilir mi (m.308) belirlenir.

## Çıktı modülleri
- Aşama bazlı kontrol listesi (yapıldı/eksik).
- Çoğunluk hesabı tablosu.
- Tasdik şartları denetim raporu.
- Eksik/risk listesi ve süre uyarıları.

## Plugin bağlamı

Bu beceri `konkordato-yeniden-yapilandirma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
