---
name: belge-taslak-ihtar-fesih-sozlesme
description: "İş ilişkisinde ihtarname, haklı/geçerli fesih bildirimi, savunma istem yazısı, iş sözleşmesi veya ibraname taslağı hazırlanması gerektiğinde; usule uygun, gerekçeli ve yer tutuculu taslak metin üretmek için kullan."
---

# Belge ve Taslak Üretimi — İhtar, Fesih, Sözleşme, Savunma

## Görev
İş ilişkisinde usule uygun belge taslakları üretmek: fesih bildirimi, savunma istem yazısı, ihtarname, iş sözleşmesi, ibraname. Yer tutucu disipliniyle, eksik bilgiyi [doldurulacak] olarak işaretleyerek.

## Soğuk başlangıç (intake)
1. Hangi belge isteniyor; taraf hangisi (işçi/işveren)?
2. Belgenin hukuki amacı ve dayandığı sebep nedir (örn. m.25/II fesih)?
3. Tarih, ücret, sicil gibi değişken veriler elde var mı?
4. Tebligat usulü nasıl yapılacak (noter/iadeli taahhütlü/KEP)?

## Denetim şeması
1. **Fesih bildirimi (m.19):** Yazılı olmalı, fesih sebebi açık ve kesin gösterilmeli, m.25/II hariç davranış/verimsizlikte önceden savunma alınmalı. Bildirimde dayanılan vakıa, tarih, hukuki sebep (m.25/II-... vb.) ve ekler belirtilir. Sonradan başka sebep eklenemeyeceği için sebep tam yazılır.
2. **Savunma istem yazısı:** İşçiye isnat edilen somut olay, yer-zaman, makul savunma süresi ve cevap usulü açıkça belirtilir; aksi halde fesih usulsüz olur.
3. **İhtarname (işçi tarafı):** Ödenmeyen ücret/fazla çalışma için temerrüde düşürme; muacceliyet, talep edilen tutar/dönem, ödeme süresi ve aksi halde m.24/II haklı fesih ihtarı içerir. Faiz başlangıcı için önemlidir.
4. **İş sözleşmesi taslağı:** Taraflar, işin tanımı, ücret ve ekler, süre/tür, deneme süresi (m.15), çalışma süresi, rekabet yasağı (TBK m.444 sınırları — süre/yer/konu) ve gizlilik; emredici hükümlere aykırı (örn. fazla çalışma ücretini tamamen dışlayan) lafızdan kaçınılır.
5. **İbraname taslağı (TBK m.420):** Fesihten 1 ay sonrasına tarihli, kalem ve miktar açık, ödeme banka üzerinden; aksi halde geçersizlik/makbuz riski not düşülür.
6. **Tebligat:** İspat değeri için noter veya KEP önerilir.

## Çıktı modülleri
- İstenen belgenin tam taslağı (başlık, gövde, talep, ekler, imza bloğu).
- Kullanılan madde dayanakları listesi.
- [doldurulacak] yer tutucu envanteri.
- Tebligat ve saklama önerisi.

## Plugin bağlamı

Bu beceri `is-hukuku-bireysel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
