---
name: ispat-yuku-deliller
description: "Hangi vakıayı kimin, hangi delille ispatlayacağını planlamak; senetle ispat zorunluluğu, kesin/takdiri delil ayrımı, ikrar-yemin-tanık-bilirkişi-keşif rejimini doğru kurmak gerektiğinde başvurulur."
---

# İspat Yükü ve Delil Sistemi

## Görev
Uyuşmazlıktaki çekişmeli vakıaları belirleyip ispat yükünü dağıtmak ve her vakıa için elverişli, hukuken kabul edilebilir delili eşleştirmek.

## Soğuk başlangıç (intake)
- Çekişmeli (ispatı gereken) vakıalar hangileri?
- İşlemin değeri senetle ispat sınırının üstünde mi?
- Elde senet/belge var mı, yoksa tanık/bilirkişiye mi gidilecek?
- Karşı tarafın elindeki belge için ibraz (m.219-222) gerekiyor mu?

## Denetim şeması
1. **İspat yükü** (HMK m.190; TMK m.6): Bir vakıadan kendi lehine hak çıkaran taraf onu ispatla yükümlüdür. Karinelerin (TMK) ispat yükünü yer değiştirdiği hallere dikkat edilir.
2. **İspatın konusu** (m.187): Yalnızca **çekişmeli** ve hukuken önemli vakıalar ispatlanır; ikrar edilen (m.188) veya herkesçe bilinen vakıa ispat gerektirmez.
3. **Senetle ispat zorunluluğu** (m.200): Belirli parasal sınırı aşan hukuki işlemler senetle ispatlanır; bu sınır yıllık tarifeden teyit edilir. **Senede karşı tanıkla ispat** kural olarak yasaktır (m.201); istisna: yazılı delil başlangıcı (m.202) veya delil başlangıcı sayılan haller.
4. **Kesin deliller**: senet (m.199, m.204-206), kesin hükme bağlanan ikrar (m.188), yemin (m.225 vd.). **Takdiri deliller**: tanık (m.240 vd.), bilirkişi (m.266 vd.), keşif (m.288 vd.), uzman görüşü (m.293).
5. **Belge ibrazı**: Karşı taraf veya üçüncü kişi elindeki belge için ibraz istenebilir (m.219-221); ibrazdan kaçınmanın sonuçları (m.220) değerlendirilir.
6. **Delil sunma anı**: Yazılı yargılamada deliller dilekçelerde gösterilir ve ön incelemede bağlanır; basit yargılamada (m.318) dilekçelerle birlikte sunulur — sonradan delil ancak istisnai koşullarla kabul edilir.

Ara sonuç: Her çekişmeli vakıa için "yük kimde + delil türü + kabul edilebilir mi" satırı.

## Çıktı modülleri
- İspat planı tablosu (vakıa / yük / delil / dayanak madde).
- Senetle ispat ve istisna analizi.
- Eksik/elde edilmesi gereken delil listesi (ibraz/keşif talepleri).

## Plugin bağlamı

Bu beceri `hukuk-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
