---
name: tahsilat-odeme-emri-haciz
description: "6183 sayılı Kanun kapsamında ödeme emri, haciz, teminat, tecil-taksitlendirme ve ihtiyati haciz işlemlerine karşı korunma ve dava yollarını planlamak için kullanılır."
---

# Tahsilat, Ödeme Emri ve Haciz (AATUHK)

## Görev
Kesinleşmiş ya da kesinleşmemiş kamu alacağının cebri tahsili aşamasında (ödeme emri, haciz, teminat, ihtiyati haciz) mükellefin korunma yollarını ve dava stratejisini kurmak.

## Soğuk başlangıç (intake)
1. Elde ödeme emri mi, haciz/ihtiyati haciz mi, teminat istemi mi var?
2. Asıl borç kesinleşti mi (dava açıldı/sonuçlandı mı)?
3. Ödeme emri hangi tarihte tebliğ edildi?
4. İtiraz sebebi "borcum yok / kısmen ödedim / zamanaşımına uğradı" mı?
5. Tecil-taksitlendirme veya yapılandırma talebi düşünülüyor mu?

## Denetim şeması
1. **Ödeme emri ve süre:** AATUHK m.55 ödeme emri tebliğ edilir; m.58 — ödeme emrine karşı 15 gün içinde vergi mahkemesinde dava açılır. İtiraz sebepleri sınırlıdır: "böyle bir borç yoktur, kısmen ödedim veya zamanaşımına uğradı".
2. **Tahsil zamanaşımı:** AATUHK m.102 — vadeyi izleyen takvim yılı başından itibaren 5 yıl; m.103 zamanaşımını kesen haller (ödeme, haciz, cebren tahsil, mal bildirimi vb.). Zamanaşımı ödeme emrine karşı temel savunmadır.
3. **Teminat ve ihtiyati haciz:** AATUHK m.9, m.13 — teminat istenmesi ve ihtiyati haciz şartları (henüz tahakkuk etmemiş ya da kesinleşmemiş alacakta), m.15 ihtiyati hacze itiraz 7 gün içinde.
4. **Haciz:** AATUHK m.62 vd.; haczedilemeyecek mallar (m.70), haczin kaldırılması, paraya çevirme. Usulsüz haciz ve hacze yetki sınırları denetlenir.
5. **Tecil-taksitlendirme:** AATUHK m.48 — çok zor durum şartıyla tecil; teminat ve tecil faizi. Yapılandırma kanunları (varsa yürürlükteki af/yapılandırma) ayrıca değerlendirilir.
6. **Sorumluluk genişlemesi:** Kanuni temsilci (VUK m.10), limited şirket ortağı (AATUHK m.35) ve yöneticilerin (AATUHK mük.35) ikincil sorumluluğu; takibin muhatabı doğru mu? Ara sonuç: hangi işleme, hangi sürede, hangi sebeple itiraz/dava açılır.

## Çıktı modülleri
- Ödeme emri itiraz sebebi tablosu (üç sınırlı sebep ile eşleştirme).
- Tahsil zamanaşımı hesap çizelgesi (vade, kesen haller, dolum tarihi).
- Tecil/teminat/ihtiyati haciz seçenek notu.
- İtiraz/dava dilekçesi iskeleti.

## Plugin bağlamı

Bu beceri `vergi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
