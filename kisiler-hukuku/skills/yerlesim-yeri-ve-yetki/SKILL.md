---
name: yerlesim-yeri-ve-yetki
description: "Bir kişinin yerleşim yerinin tespiti, dava yetkisinin ve tebligat adresinin belirlenmesi ya da hısımlık derecesi gibi statü sorunları ortaya çıktığında kullanılır."
---

# Yerleşim Yeri, Hısımlık ve Yetki Sonuçları

## Görev
Bir kişinin yerleşim yerini TMK m.19-21 uyarınca belirleyip bunun yetki, tebligat ve statü sonuçlarını çıkarmak; gerektiğinde kan/kayın hısımlığı derecesini hesaplayarak ilgili hükümlere etkisini saptamak.

## Soğuk başlangıç (intake)
- Kişinin sürekli kalma niyetiyle oturduğu yer neresi; birden çok adresi mi var?
- Küçük/kısıtlı mı (yasal yerleşim yeri sorunu), bir kurumda mı kalıyor?
- Sorun bir davanın yetkili mahkemesini mi, tebligatı mı, yoksa statüyü mü ilgilendiriyor?
- Hısımlık sorusu varsa: taraflar arasındaki bağ kan hısımlığı mı, kayın hısımlığı mı; hangi hükme etkisi soruluyor?

## Denetim şeması
1. **Yerleşim yeri kavramı** — TMK m.19: yerleşim yeri, sürekli kalma niyetiyle oturulan yerdir; bir kimsenin aynı zamanda birden çok yerleşim yeri olamaz (teklik ilkesi). Önceki yerleşim yeri belli değilse oturulan yer (m.20) yerleşim yeri sayılır.
2. **Yasal yerleşim yeri** — TMK m.21: velayet altındaki çocuğun yerleşim yeri ana-babanın, ana-baba ortak yerleşim yerine sahip değilse çocuğun kendisine bırakıldığı tarafın yerleşim yeridir; vesayet altındakinin yerleşim yeri bağlı olduğu vesayet makamının bulunduğu yerdir.
3. **Yetki sonucu** — Genel yetkili mahkeme davalının yerleşim yeri mahkemesidir (HMK m.6); tebligat öncelikle yerleşim yeri/bilinen adrese yapılır. Kişiler hukuku taleplerinde (ad değişikliği, kısıtlama) çoğu kez talep edenin yerleşim yeri yetkilidir.
4. **Hısımlık** — TMK m.17: kan hısımlığının derecesi, hısımları birbirine bağlayan doğum sayısıyla belirlenir; üstsoy-altsoy düz hat, ortak kökten gelenler yan hat hısımıdır. TMK m.18: eşlerden biriyle diğer eşin kan hısımları, aynı tür ve dereceden kayın hısımıdır; kayın hısımlığı, onu doğuran evliliğin sona ermesiyle ortadan kalkmaz.
5. **Bağlantı kontrolü** — Hısımlık derecesi; evlenme engelleri, mirasta zümre, tanıklıktan/hâkimlikten çekinme, vesayet gibi kurumlara doğrudan etki eder; ilgili özel hükme taşınır.

## Çıktı modülleri
- Yerleşim yeri tespiti + dayanak (gerçek/yasal/kurumsal).
- Yetkili mahkeme ve tebligat adresi sonucu.
- Hısımlık derece şeması (gerekiyorsa) ve etkilediği hüküm.
- Açık veri eksikleri için `[doldurulacak]` notu.

## Plugin bağlamı

Bu beceri `kisiler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
