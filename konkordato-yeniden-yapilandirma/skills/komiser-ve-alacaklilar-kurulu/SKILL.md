---
name: komiser-ve-alacaklilar-kurulu
description: "Konkordato komiserinin görev ve yetkilerini, alacaklılar kurulunun oluşumunu ve işleyişini, organların kararlarına karşı başvuru yollarını ele almak gerektiğinde kullanılır."
---

# Konkordato Komiseri ve Alacaklılar Kurulu

## Görev
Sürecin organlarını yönetmek: komiserin görevlendirilmesi, görev ve yetkilerinin (İİK m.290) denetimi, alacaklılar kurulunun oluşturulması (m.289/3) ve işleyişi, organların işlem ve raporlarına karşı denetim/şikâyet yollarının kullanımı.

## Soğuk başlangıç (intake)
- Komiser atandı mı, sayısı ve nitelikleri uygun mu (komiserlik yönetmeliği)?
- Alacaklılar kurulu kuruldu mu, kaç üyeli, hangi alacaklı gruplarını temsil ediyor?
- Komiserin/kurulun bir işlemine itiraz mı var?
- Komiser ücreti ve depo durumu nedir?

## Denetim şeması
1. **Komiser görevlendirme.** Mahkeme, geçici mühletle birlikte bir veya birden fazla geçici komiser atar; nitelikler Adalet Bakanlığı konkordato komiserliği yönetmeliği ile belirlenir. Bilirkişilik/komiserlik listesine kayıt şartı denetlenir.
2. **Komiserin görevleri (m.290).** Projenin tamamlanmasına katkı, defter ve belgelerin incelenmesi, malların korunması, alacaklılar kurulunca verilen görevler, mahkemeye dönemsel rapor. İspat: komiser raporunun gerekçeli ve belgeye dayalı olması aranır.
3. **Alacaklılar kurulu (m.289/3, m.290).** Mahkeme, alacaklı sayısı/alacak miktarı ve niteliği gözetilerek bir alacaklılar kurulu oluşturabilir; farklı alacaklı sınıflarının (rehinli, imtiyazlı, adi) temsili sağlanır. Kurul komiserin işlemlerini denetler, görüş bildirir.
4. **Organların kararlarına karşı (m.290/son, m.297).** Komiserin tasarruf onayı, kurulun kararları ve raporlar; ilgililer mahkemeye şikâyet/itiraz edebilir. Süre ve usul denetlenir.
5. **Komiser ücreti.** Adalet Bakanlığı ücret tarifesi esas alınır; tasdik şartı olarak depo (m.305) gözetilir. Ara sonuç: organ yapısı usule uygun mu, müdahale gerekir mi.

## Çıktı modülleri
- Komiser/alacaklılar kurulu görev-yetki tablosu.
- Komiser raporu değerlendirme notu.
- Organ kararına itiraz/şikâyet dilekçesi taslağı (yer tutuculu).
- Ücret ve depo kontrol listesi.

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
