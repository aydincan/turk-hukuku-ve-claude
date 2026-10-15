---
name: calisan-kvkk-uyumu
description: "Özlük dosyası, işe alım verisi, işyeri kamerası, e-posta/log izleme, sağlık raporu gibi çalışan kişisel verisinin işlenmesi tasarlanıyor veya denetlenecekse kullanılır."
---

# Çalışan ve Aday Verilerinde KVKK Uyumu

## Görev
İK süreçlerinde işlenen çalışan/aday kişisel verisini KVKK'ya uygun dayanağa oturtmak; aydınlatma, saklama-imha ve aktarım rejimini kurmak; işyeri izleme (kamera, e-posta, log) uygulamasını hukuka uygun sınırda tasarlamak.

## Soğuk başlangıç (intake)
1. Hangi veri, hangi süreçte işleniyor (işe alım, özlük, performans, izleme)?
2. Özel nitelikli veri var mı (sağlık raporu, engellilik, sendika, adli sicil)?
3. Veri yurt dışına/üçüncü kişiye (bordro, SGK aracısı, grup şirketi) aktarılıyor mu?
4. İşyerinde kamera veya e-posta/internet izleme var mı, çalışan bilgilendirildi mi?

## Denetim şeması
1. **İşleme şartı (KVKK m.5)**: Çalışan verisinde **açık rıza zayıf dayanaktır** (güç asimetrisi); bunun yerine sözleşmenin ifası, hukuki yükümlülük (SGK/iş mevzuatı) veya meşru menfaat dayanağı tercih edilir.
2. **Özel nitelikli veri (m.6)**: Sağlık verisi yalnızca sınırlı şartlarla ve gerekli teknik tedbirlerle işlenir; sağlık raporu işyeri hekimi/yetkili eliyle işlenmeli, dosyada gereksiz tutulmamalı.
3. **Aydınlatma (m.10)**: İşe alımda ve istihdam başında çalışan aydınlatma metni tebliğ edilmeli; izleme yapılıyorsa kapsamı önceden açıkça bildirilmeli (aksi halde izleme delili hukuka aykırı sayılabilir — içtihat, `[doğrulanacak]`).
4. **İzleme ölçülülüğü**: Kamera/e-posta izleme meşru amaç + ölçülülük + önceden bilgilendirme şartına tabi; özel alana (soyunma odası vb.) izleme yasak.
5. **Aktarım (m.8-9)**: Bordro/SGK/grup şirketi aktarımı için uygun şart ve sözleşmesel güvence; yurt dışı aktarımda ek rejim.
6. **Saklama-imha**: Her veri kategorisi için saklama süresi ve imha politikası; iş ilişkisi sonrası zamanaşımı süreleri kadar tutma gerekçesi.
7. **Ara sonuç**: Dayanaksız/aşırı işleme → Kurul yaptırımı ve davada delil değeri kaybı.

## Çıktı modülleri
- Çalışan aydınlatma metni ve izleme bilgilendirmesi taslağı.
- Veri kategori-dayanak-saklama tablosu.
- Aktarım ve imha politikası notu.

## Plugin bağlamı

Bu beceri `ik-insan-kaynaklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
