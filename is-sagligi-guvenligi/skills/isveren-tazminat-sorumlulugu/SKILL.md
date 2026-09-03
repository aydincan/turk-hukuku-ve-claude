---
name: isveren-tazminat-sorumlulugu
description: "İş kazası veya meslek hastalığı nedeniyle işverenin maddi-manevi tazminat sorumluluğunun kurulması, kusur ve illiyetin değerlendirilmesi ile zararın hesaplanması için kullanılır."
---

# İşverenin Tazminat Sorumluluğu (İş Kazası)

## Görev
İş kazası/meslek hastalığı nedeniyle işverenin işçiye veya hak sahiplerine karşı maddi ve manevi tazminat sorumluluğunu kurmak; gözetme borcuna aykırılığı, illiyeti, kusuru ve zararı altlamak.

## Soğuk başlangıç (intake)
- Kaza nitelendirildi mi; kusur/bilirkişi raporu var mı, kusur oranı dağılımı ne?
- Sürekli iş göremezlik oranı (maluliyet) belirlendi mi; SGK gelir bağladı mı?
- Talep maddi mi, manevi mi, destekten yoksun kalma mı; talep eden işçi mi, hak sahipleri mi?
- Müterafik kusur, üçüncü kişi kusuru veya beklenmeyen hal iddiası var mı?

## Denetim şeması
1. **Hukuki temel:** İşverenin işçiyi gözetme borcu sözleşmeseldir (TBK m.417/2); ancak ölüm ve bedensel zararların tazmini haksız fiil hükümlerine tabidir (TBK m.417/3, m.49, m.54-56). Bu nedenle hem sözleşmesel hem haksız fiil esasları birlikte uygulanır.
2. **Sorumluluğun unsurları:** (a) işverenin somut bir İSG yükümlülüğünü ihlali (hangi 6331 maddesi/yönetmelik), (b) zarar (maluliyet/ölüm), (c) illiyet bağı, (d) kusur. İşveren önlemleri eksiksiz aldığını ispatlayamazsa sorumlu olur; ispat yükü işverendedir.
3. **Kusur ve illiyet:** Kusur oranı dosyaya özgü bilirkişi/İSG uzman raporuyla belirlenir; soyut oran verilmez. İşçinin kusuru müterafik kusur (TBK m.52) olarak indirim sebebidir, illiyeti kesen ağır kusur ise sorumluluğu tümüyle kaldırabilir.
4. **Zararın hesabı:** Maddi tazminatta bilinen-bilinmeyen dönem, maluliyet oranı, TRH-2010 vb. yaşam tablosu, %X iskonto, SGK gelirinin rücua konu kısmının düşülmesi (peşin sermaye değeri). Manevi tazminatta TBK m.56 ölçütleri. Destekten yoksun kalma için TBK m.53.
5. **İndirim/savunma:** Müterafik kusur, hatır ilişkisi, üçüncü kişi/mücbir sebep. **Ara sonuç:** Sorumluluk kurulduktan sonra kalem kalem hesap iskeleti çıkar.

## Çıktı modülleri
- Sorumluluk unsurları altlama tablosu.
- Maddi/manevi/destek tazminat hesap iskeleti.
- Savunma ve indirim argümanları listesi.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
