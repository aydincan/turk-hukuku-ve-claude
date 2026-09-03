---
name: risk-strateji-iscilik-davasi
description: "Bir işçilik dosyasında kazanç ihtimali, alacak büyüklüğü, işe iade ile alacak davası arasında seçim ve müzakere/sulh stratejisi belirlenmesi gerektiğinde; işçi veya işveren tarafında risk haritası ve karar önerisi üretmek için kullan."
---

# Risk ve Strateji — İşçilik Davası Değerlendirmesi

## Görev
Dosyayı uçtan uca tartarak kazanç olasılığı, beklenen alacak/maruz kalınan risk ve en uygun yol haritasını (dava/sulh/işe iade) belirlemek.

## Soğuk başlangıç (intake)
1. Tarafını temsil ettiğin kim (işçi mi işveren mi) ve önceliği nedir?
2. Fesih nitelendirmesinde zayıf/güçlü noktalar neler?
3. Belgesel delil durumu lehte mi aleyhte mi?
4. İşçi tekrar çalışmak istiyor mu, yoksa tazminat odaklı mı?

## Denetim şeması
1. **Fesih zemini riski:** Fesih haklı/geçerli/usulsüz ekseninde nerede? İşveren m.19 usulüne uymamışsa geçerli sebep dahi zayıflar; m.26 süresini kaçırdıysa haklı fesih düşer.
2. **İşe iade vs. alacak tercihi:** Güvence kapsamı varsa: işe iade kazanılırsa boşta geçen (≤4 ay) + başlatmama (4-8 ay) tazminatı doğar, ancak kıdem/ihbar mahsubu ve işe başlatma riski hesaplanmalı. Alacak davası daha kesin nakit sonuç verir ama güvence tazminatlarını içermez. İkisi birlikte/sırayla kurgulanabilir.
3. **Alacak büyüklüğü tahmini:** Kıdem + ihbar + fazla çalışma + tatil + izin kalemlerinin kaba aralığı; takdiri indirim ve zamanaşımı süzgeci uygulanır.
4. **İspat riski:** Tanığa bağlı kalemler (fazla çalışma) belirsizlik taşır; belgeyle desteklenmeyen iddialarda indirim beklenmeli. İşveren tarafında ibraz edilmeyen kayıt riski not edilir.
5. **Sulh/müzakere analizi:** Arabuluculuk aşaması zorunlu olduğundan, beklenen yargılama maliyeti, faiz ve süresi karşısında erken sulh aralığı hesaplanır. İşveren için itibar ve emsal etkisi; işçi için nakit-zaman dengesi tartılır.
6. **Ara sonuç:** Lehe/aleyhe faktör matrisi ve önerilen yol.

## Çıktı modülleri
- Güçlü/zayıf yön (SWOT benzeri) matrisi.
- Beklenen sonuç aralığı (alacak / tazminat tahmini).
- İşe iade-alacak-sulh karar önerisi ve gerekçesi.
- Müzakere taban-tavan aralığı ve sonraki adım listesi.

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
