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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
