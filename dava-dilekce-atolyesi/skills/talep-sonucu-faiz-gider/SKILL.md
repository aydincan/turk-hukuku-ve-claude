---
name: talep-sonucu-faiz-gider
description: "Dilekçenin sonuç kısmını infaz edilebilir biçimde yazmak; faiz türü ve başlangıcı, belirsiz alacak, terditli talep, harç ve vekâlet ücretini doğru kurmak gerektiğinde kullanılır."
---

# Talep Sonucu, Faiz ve Yargılama Gideri

## Görev
Layihanın en kritik bölümü olan talep sonucunu, mahkemenin aynen hükmedebileceği ve infaz edilebileceği netlikte yazmak; faiz, gider ve vekâlet ücretini eksiksiz eklemek. Talep edilmeyen şeye hükmedilemez (HMK m.26 — taleple bağlılık).

## Soğuk başlangıç (intake)
- Talep miktarı belirli mi, belirsiz mi (HMK m.107)?
- Faiz türü ne: yasal mı, ticari/avans mı (3095 s.K., TBK m.88/120)?
- Faiz başlangıcı: temerrüt mü, dava/ihtar tarihi mi?
- Terditli/kademeli talep var mı?

## Denetim şeması
1. Talep türü: Eda, tespit, inşai ayrımını netleştirin; eda talebinde miktar ve para birimi açık olmalı.
2. Belirsiz alacak (HMK m.107): Miktar dava açılırken belirlenemiyorsa belirsiz alacak davası; asgari tutar ve fazlaya ilişkin hak saklı tutulur. Aksi halde kısmi dava (m.109) tercih edilir.
3. Faiz: Türünü ve başlangıcını ayrı belirtin. Temerrüt faizi başlangıcı TBK m.117 (temerrüt) ve m.120; oran 3095 s.K. (ticari işlerde avans faizi). Faiz talebi açıkça yazılmazsa hükmedilemez.
4. Yargılama gideri ve vekâlet ücreti (HMK m.323, m.326-330): Gider haksız çıkan tarafa yükletilir; vekâlet ücreti AAÜT'ye göre. Talep sonucuna açıkça ekleyin.
5. Terdit/kademe: Asıl ve yedek talebi (ör. öncelikle aynen ifa, olmazsa tazminat) açık ayırın; harç bu yapıya göre hesaplanır. Ara sonuç: her kalem yazılı ve dayanaklıysa sonuç bloğu kapanır.

## Çıktı modülleri
- Numaralı talep sonucu bloğu
- Faiz tablosu (tür, oran dayanağı, başlangıç)
- Belirsiz alacak/kısmi dava tercih notu
- Gider ve vekâlet ücreti talebi

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
