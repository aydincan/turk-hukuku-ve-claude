---
name: dava-usul-gorev-yetki
description: "Patent uyuşmazlığı mahkemeye taşınırken görevli/yetkili mahkeme, dava türü, ihtiyati tedbir ve delil tespiti planlanırken kullanılır; usul iskeleti ve yargı yolu seçimi için temel beceridir."
---

# Dava, Usul ve Görev-Yetki

## Görev
Patent/faydalı model uyuşmazlığında görevli ve yetkili mahkemeyi, dava türünü, ihtiyati tedbir ve delil tespiti yollarını SMK ve HMK çerçevesinde belirleyip usul iskeletini kurmak.

## Soğuk başlangıç (intake)
1. Talep ne: tecavüzün tespiti/men/ref, tazminat, hükümsüzlük, gasp, lisans/devir uyuşmazlığı?
2. Taraflar nerede; tecavüz fiili nerede işleniyor?
3. Acil koruma ihtiyacı var mı (ürünün piyasaya çıkması, delilin kaybı)?
4. İdari süreç (YİDD kararı) tüketildi mi; iptal davası mı söz konusu?

## Denetim şeması
1. **Görevli mahkeme (SMK m.156).** Sınai mülkiyet hukukundan doğan dava ve işlerde görevli mahkeme **Fikri ve Sınai Haklar Hukuk Mahkemesi** (FSHM); kurulmamış yerlerde Asliye Hukuk Mahkemesi bu sıfatla bakar. Ceza yönü için Fikri ve Sınai Haklar Ceza Mahkemesi (not: patent tecavüzünde ceza yaptırımı marka kadar geniş değildir; konuyu hukuk davası ekseninde değerlendir).
2. **Yetki (SMK m.156/3).** Hak sahibi tarafından açılacak davada davacının yerleşim yeri, hukuki işlemin yapıldığı veya tecavüz fiilinin gerçekleştiği yer mahkemesi yetkilidir; bu, HMK genel yetki kurallarına ek seçenekler sunar.
3. **Dava türü ayrımı.** Tecavüz davaları (m.149) hak sahibi/lisans alan tarafından; hükümsüzlük davası (m.138) menfaati olanlarca; YİDD kararının iptali davası ise TPMK'ye karşı kararın bildiriminden itibaren süresinde FSHM'de açılır.
4. **İhtiyati tedbir ve delil tespiti (SMK m.159, HMK m.389 vd., m.400 vd.).** Tecavüzün durdurulması, ürünlere el konulması, gümrükte durdurma gibi tedbirler; teminat ve yaklaşık ispat. Delil tespiti ile fiili/teknik durum kayıt altına alınır.
5. **İspat ve bilirkişi.** Teknik değerlendirme bilirkişiye dayanır; istem-tekniğin bilinen durumu eşleştirmesi raporda denetlenir. İspat yükü: tecavüzü/kapsamı davacı, savunma/def'i ve istisnayı davalı.

## Çıktı modülleri
- Görev-yetki tespiti ve yargı yolu haritası.
- Dava türü ve taraf sıfatı tablosu.
- İhtiyati tedbir / delil tespiti talep iskeleti.
- İspat yükü dağılımı ve bilirkişi soru listesi taslağı.

## Plugin bağlamı

Bu beceri `patent-faydali-model` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
