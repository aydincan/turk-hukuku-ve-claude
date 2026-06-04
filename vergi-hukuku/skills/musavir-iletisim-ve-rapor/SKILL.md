---
name: musavir-iletisim-ve-rapor
description: "Vergi konusundaki teknik analizi mükellefin/karar vericinin anlayacağı dilde sunmak, gerekçeli vergi mütalaası ve bilgilendirme yazısı üretmek için kullanılır."
---

# Müvekkil İletişimi ve Mütalaa Yazımı

## Görev
Vergi hukuku analizini mükellefe, mali müşavire veya şirket yönetimine açık, gerekçeli ve eyleme dönük biçimde aktarmak; hukuki mütalaa, bilgilendirme yazısı veya yönetim notu hazırlamak.

## Soğuk başlangıç (intake)
1. Muhatap kim (bireysel mükellef, şirket yönetimi, mali müşavir, dava karşı tarafı)?
2. Çıktı türü nedir (mütalaa, bilgi notu, dava değerlendirmesi, e-posta özeti)?
3. Karar verici hangi soruya cevap arıyor (öde / dava aç / uzlaş / yapıyı değiştir)?
4. Teknik derinlik ne olmalı (özet mi, gerekçeli mütalaa mı)?
5. Tutar, ceza ve süre baskısı var mı?

## Denetim şeması
1. **Soru çerçeveleme:** Hukuki sorunu tek cümleyle sabitle (ör. "Re'sen tarhiyatın iptali şansı ve uzlaşma alternatifi"). Cevap bu soruya bağlı kalmalı.
2. **Olay tespiti:** Maddi vakıaları tarafsız ve tarihli biçimde özetle; ihtilaflı/belgesiz vakıaları ayrıca işaretle.
3. **Altlama:** İlgili normu (VUK/GVK/KVK/KDVK/İYUK/AATUHK ilgili maddesi) olaya uygula; karşı görüşü ve içtihadı dengeli ver. Doğrulanmamış karar künyesini `[doğrulanacak]` ile işaretle; karararama.danistay.gov.tr kaynağını an.
4. **Sonuç ve gerekçe:** Net bir sonuç ver; tek seçenek dayatma, lehe-aleyhe ihtimalleri ve başarı olasılığını dürüstçe belirt (kesinlik vaadi verme).
5. **Sade dile çevirme:** Teknik terimi (re'sen tarh, ihtirazi kayıt, tevkifat) parantez içi kısa açıklamayla ver; karar vericinin yapması gerekeni madde madde yaz. Ara sonuç: muhatap "ne yapacağını" tereddütsüz anlar.
6. **Risk ve süre uyarısı:** Hak düşürücü süreyi ve sonraki kritik tarihi belgenin başında ve sonunda vurgula.

## Çıktı modülleri
- Yönetici özeti (soru – cevap – kritik tarih, 3-5 satır).
- Gerekçeli mütalaa gövdesi (olay / hukuki değerlendirme / sonuç).
- Aksiyon listesi (kim, neyi, hangi tarihe kadar).
- Sade dil eki ve istenecek belge/teyit listesi.

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
