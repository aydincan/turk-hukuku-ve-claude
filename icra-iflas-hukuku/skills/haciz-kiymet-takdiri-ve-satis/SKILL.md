---
name: haciz-kiymet-takdiri-ve-satis
description: "Takip kesinleştikten sonra mal/alacak/maaş haczi yapmak, kıymet takdirine itiraz etmek ve taşınır-taşınmaz satış (açık artırma) sürecini yürütmek gerektiğinde; haciz kapsamı, hacizli malların satışı ve ihale şikâyeti için kullanılır."
---

# Haciz, Kıymet Takdiri ve Satış

## Görev
Kesinleşen takipte borçlunun mal, alacak ve haklarını haczetmek; haczedilemezlik sınırlarını gözetmek; kıymet takdiri ve açık artırma yoluyla satışı yürütmek; ihalenin feshi/şikâyet risklerini yönetmek.

## Soğuk başlangıç (intake)
- Takip kesinleşti mi, haciz isteme süresi (m.78) içinde miyiz?
- Haczedilecek mal taşınır mı, taşınmaz mı, maaş/banka alacağı mı?
- Haczedilmezlik iddiası var mı (m.82, m.83 — maaşta 1/4 sınırı)?
- Kıymet takdiri yapıldı mı, itiraz süresi geçti mi?

## Denetim şeması
1. **Haciz isteme (m.78)**: Kesinleşmeden itibaren 1 yıl içinde haciz istenmezse dosya işlemden kalkar; yenileme gerekir. Haciz mahalde fiilen veya kayden (tapu, trafik, banka) yapılır.
2. **Haczedilmezlik (m.82-83)**: Zorunlu ev eşyası, mesleki araçlar, kısmen maaş (1/4) gibi mallar denetlenir; aşkın/usulsüz haciz şikâyet konusudur (m.16).
3. **Hacze iştirak ve istihkak**: Diğer alacaklıların iştiraki (m.100, m.101) ve üçüncü kişinin istihkak iddiası (m.96-99) ayrıca yönetilir.
4. **Kıymet takdiri (m.87, m.128/a)**: Bilirkişiyle değer biçilir; takdire karşı icra mahkemesine süresinde itiraz edilir (7 gün).
5. **Satış (m.106 vd., m.123 vd.)**: Talep süreleri ve elektronik açık artırma usulü gözetilir; taşınmazda m.126 vd., ihalenin feshi m.134 (7 gün içinde icra mahkemesi, fesih sebepleri: usulsüzlük, zarar, fahiş fiyat farkı).
6. **Ara sonuç**: Satış takvimi, beklenen bedel ve fesih riski belirlenir; paranın paylaştırılmasına (sıra cetveli) geçiş hazırlanır.

## Çıktı modülleri
- Haciz talebi ve haczedilmezlik şikâyeti taslağı.
- Kıymet takdirine itiraz dilekçesi.
- Satış/ihale takvimi ve ihalenin feshi risk notu.

## Plugin bağlamı

Bu beceri `icra-iflas-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
