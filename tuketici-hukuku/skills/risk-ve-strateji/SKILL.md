---
name: risk-ve-strateji
description: "Tüketici dosyasında çözüm yolları arasında seçim yapmak, kazanma şansı ve maliyet-fayda dengesi kurmak, müvekkile gerçekçi beklenti ve eylem planı sunmak gerektiğinde kullanılır."
---

# Risk Değerlendirmesi ve Strateji

## Görev
Tüketici dosyasında alternatif yolların (uzlaşma, hakem heyeti, dava) güçlü/zayıf yönlerini tartmak, başarı olasılığı ve maliyet-fayda dengesini kurmak, müvekkile gerçekçi beklenti ve adım adım eylem planı sunmak.

## Soğuk başlangıç (intake)
- Talebin değeri ve müvekkilin önceliği (hız, para, ilişki sürdürme) ne?
- Delil durumu güçlü mü, karineler lehe mi?
- Karşı taraf kim (banka, büyük satıcı, küçük işletme) ve ödeme/uzlaşma kapasitesi?
- Süre baskısı veya zamanaşımı riski var mı?

## Denetim şeması
1. **Yol haritası seçimi:** Parasal sınır hakem heyetini zorunlu kılıyor mu, yoksa mahkeme yolu mu? Hakem heyeti hızlı ve ücretsizdir; karara itiraz riski hesaba katılır. Mahkemede tüketici harç/gider muafiyetinden yararlanır (TKHK m.73/2).
2. **Esas başarı analizi:** Çekirdek talep (ayıp, haksız şart, iade) için ispat yükü ve karineler lehe mi? Zayıf halkayı (örneğin süre, delil eksikliği) belirle.
3. **Maliyet-fayda:** Vekâlet ücreti, bilirkişi, süre ve tahsilat riski ile beklenen kazanç karşılaştırılır; küçük tutarlı taleplerde hakem heyeti çoğu zaman en rasyonel yoldur.
4. **Tahsil edilebilirlik:** Lehte karar çıksa bile karşı taraftan tahsil mümkün mü? İcra aşaması ve teminat değerlendirilir.
5. **Uzlaşma penceresi:** Erken ihtar/müzakere ile çözüm masrafsız ve hızlıysa öncelik verilir; müvekkilin ilişkiyi sürdürme isteği tartılır.
6. **Süre riski:** Zamanaşımı/itiraz süresi yaklaşıyorsa, en hızlı koruyucu adım (başvuru/dava) öne çekilir.
7. **Ara sonuç:** Önerilen yol, gerekçesi, başarı tahmini aralığı ve birincil/ikincil plan.

## Çıktı modülleri
- Yol karşılaştırma tablosu (hakem heyeti/mahkeme/uzlaşma).
- Güçlü-zayıf yön (SWOT) özeti.
- Maliyet-fayda ve tahsilat değerlendirmesi.
- Adım adım eylem planı ve müvekkile gerçekçi beklenti notu.

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
