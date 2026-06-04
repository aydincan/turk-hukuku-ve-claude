---
name: temel-kavramlar-ve-koruma-turleri
description: "Tescilli/tescilsiz tasarım, FSEK ve marka kümülasyonu ayrımının yapılması, koruma türünün ve uygulanacak rejimin belirlenmesi; bir görünümün hangi sınai mülkiyet hakkıyla korunacağını netleştirmek gerektiğinde kullanılır."
---

# Temel Kavramlar ve Koruma Türleri

## Görev
Önündeki uyuşmazlık veya danışma için doğru koruma rejimini belirlemek: tescilli tasarım, tescilsiz tasarım, FSEK eser koruması ve marka korumasından hangisinin (veya hangilerinin birlikte) devreye girdiğini tespit etmek.

## Soğuk başlangıç (intake)
1. Korunması istenen şey bir ürünün veya parçanın görünümü mü, teknik bir işlevi mi, yoksa bir ayırt edici işaret mi?
2. Tasarım TÜRKPATENT'te tescilli mi; tescilliyse başvuru/tescil tarihi nedir?
3. Tasarım ilk kez kamuya ne zaman ve nasıl sunuldu (fuar, satış, katalog, internet)?
4. Görünüm özgün bir sanatsal/estetik yaratım mı (FSEK eseri ihtimali)?
5. Olay 10/01/2017 öncesi mi sonrası mı (554 KHK / 6769 SMK ayrımı)?

## Denetim şeması
1. Konu tanımı (SMK m.55): "Tasarım" ürünün tümü veya bir parçasının görünümüdür; "ürün" geniş tanımlıdır (bileşik ürün parçaları, ambalaj, grafik semboller dâhil). Görünüm değil işlev korunuyorsa tasarım yolu kapanır, patent/faydalı model'e yönelin.
2. Koruma türü ayrımı:
   - Tescilli (SMK m.55/4, m.69): TÜRKPATENT tescili ile doğar, 5'er yıllık yenilemeyle azami 25 yıl. Yenilik ve ayırt edicilik için aynı ölçütler aranır ama korumanın kapsamı geniştir (kötü niyet/kopyalama aranmaz).
   - Tescilsiz (SMK m.55/4, m.57/2): Kamuya ilk sunmadan itibaren 3 yıl; yalnızca taklit/kopyalamaya karşı koruma.
3. Kümülasyon kontrolü: Görünüm aynı zamanda özgün eserse FSEK m.1/B-4 (güzel sanat eseri) kümülatif korunabilir (SMK m.58/5'in kümülasyona engel olmadığı). Ürün şekli ayırt edici işaret işlevi görüyorsa 6769 marka hükümleri (m.4-5) ayrıca incelenir.
4. Zaman bakımından uygulama: Koruma 10/01/2017 öncesi doğmuşsa 554 KHK'nın ilgili hükümleri esas alınır; ara sonuç olarak hangi metnin uygulanacağı net yazılır.
5. Ara sonuç: Korunan değer (görünüm), koruma türü, süre ve uygulanacak metin tek cümlede sabitlenir.

## Çıktı modülleri
- Koruma türü karar tablosu (tescilli/tescilsiz/FSEK/marka) ve gerekçe.
- Tarih hattı (kamuya sunma, başvuru, rüçhan, koruma bitişi).
- Uygulanacak mevzuat ve madde listesi; eksik bilgi için [doldurulacak] notları.

## Plugin bağlamı

Bu beceri `tasarim-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
