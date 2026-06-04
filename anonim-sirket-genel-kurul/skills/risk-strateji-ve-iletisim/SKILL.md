---
name: risk-strateji-ve-iletisim
description: "Genel kurul uyusmazligi oncesi/sonrasi risk haritasi cikarilacak, dava acma-uzlasma karari, karsi tarafa cevap veya muvekkile bilgilendirme yazisi hazirlanacaksa ve butun adimlari birlestiren strateji gerektiginde kullanilir."
---

# Risk, Strateji ve Taraf İletişimi

## Görev
Genel kurul uyuşmazlığında bütüncül risk haritası kurmak; dava/uzlaşma stratejisini belirlemek ve hem müvekkile hem karşı tarafa uygun iletişim metinlerini hazırlamak.

## Soğuk başlangıç (intake)
1. Müvekkil hangi konumda: azlık/çoğunluk pay sahibi, YK, şirket tüzel kişiliği?
2. Hedef nedir: kararı iptal ettirmek, kararı savunmak, müzakere etmek, çıkış (m.531) mı?
3. Karar tescil/icra edildi mi; geri dönülemez işlemler yapıldı mı?
4. Tarafların gücü ve ilişki süreklilik arz ediyor mu (ortaklığın devamı isteniyor mu)?

## Denetim şeması
1. **Konum ve menfaat haritası:** Tarafın hukuki konumunu ve gerçek menfaatini (kontrol, kâr payı, çıkış, itibar) ayır. İptal davası ortaklık ilişkisini gerebilir; bazen m.531 (haklı sebeple fesih/çıkış) veya pay devri daha rasyonel sonuçtur.
2. **Sebep gücü ve olasılık:** Sakatlığın hangi kademede (yokluk/butlan/iptal) olduğunu ve ispat gücünü değerlendir. Salt usul aykırılığı iptal getirir ama karar yeniden alınabilir; bu, davanın pratik değerini düşürür. Esasa ilişkin/vazgeçilmez hak ihlali daha güçlüdür.
3. **Süre/eşik riski:** Üç aylık hak düşürücü süre (m.445) ve azlık eşiği (1/10) kaçırılmışsa strateji butlan/yokluk veya sorumluluk davasına kayar. Teminat riski (m.448) maliyet hesabına katılır.
4. **Yan yollar:** Karar iptaliyle birlikte YK üyelerine karşı sorumluluk davası (TTK m.553) veya özel denetim (m.438) paralel değerlendirilir.
5. **İletişim:** Müvekkile sade dille seçenek-sonuç-maliyet tablosu sunulur; karşı tarafa gönderilecek ihtar/uzlaşma yazısı, hukuki dayanağı net ama müzakereye kapı bırakan üslupta yazılır. Avukatlık sır ve çıkar çatışması kuralları (1136 sayılı Kanun) gözetilir.
6. **İspat/ara sonuç:** Strateji, eldeki belgelerin (tutanak, ilan, hazır bulunanlar listesi) ispat gücüyle sınanır; zayıf delil varsa önce delil tespiti/özel denetim düşünülür.

## Çıktı modülleri
- Risk haritası (sebep gücü, olasılık, süre, maliyet, ilişki etkisi).
- Strateji önerisi (dava/uzlaşma/çıkış) ve gerekçe.
- Müvekkil bilgilendirme yazısı ve karşı tarafa ihtar/uzlaşma metni taslağı.

## Plugin bağlamı

Bu beceri `anonim-sirket-genel-kurul` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
