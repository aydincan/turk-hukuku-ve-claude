---
name: dernekler-hukuku
description: "Bir derneğin kurulması, tüzük ve organ işlemleri, üyelik uyuşmazlıkları, genel kurul kararlarının iptali ya da sona erme/fesih konuları gündeme geldiğinde kullanılır."
---

# Dernekler Hukuku (Kuruluş, Organlar, Sona Erme)

## Görev
Bir derneğin kuruluşunu, organ yapısını ve işleyişini TMK m.56-100 ve 5253 sayılı Dernekler Kanunu çerçevesinde denetlemek; üyelik, genel kurul kararı ve sona erme uyuşmazlıklarında doğru talep yolunu kurmak.

## Soğuk başlangıç (intake)
- Sorun kuruluş aşaması mı, işleyiş (genel kurul/yönetim) mi, üyelik mi, sona erme mi?
- Tüzük elimizde mi; zorunlu kayıtları (amaç, organlar, üyelik şartları) içeriyor mu?
- Genel kurul kararı tartışmalıysa: çağrı, gündem, nisap, içerik hangi yönden sakat?
- Talep: tescil, üyelikten çıkarma iptali, genel kurul kararının iptali, fesih mi?

## Denetim şeması
1. **Kuruluş** — TMK m.56-58: en az yedi gerçek/tüzel kişi, kanunun açıkça yasaklamadığı bir amaçla dernek kurabilir; kuruluş bildirimi ve tüzükle tüzel kişilik **kuruluş anında** kazanılır (m.59); ilgili idari makama kuruluş bildirimi verilir.
2. **Tüzük** — TMK m.58: derneğin adı, amacı, gelir kaynakları, üyelik koşulları, organları ve örgütü tüzükte gösterilir; tüzük kanunun emredici hükümlerine aykırı olamaz.
3. **Organlar** — TMK m.72 vd.: zorunlu organlar genel kurul (en yetkili organ), yönetim kurulu ve denetim kuruludur. Genel kurul çağrısı, gündem ve toplantı/karar nisapları tüzük ve TMK m.74-81'e tabidir.
4. **Üyelik** — TMK m.64-67: üyelik kişiye bağlıdır; üye her zaman çıkma hakkına sahiptir (m.66). Üyelikten çıkarma tüzükte gösterilen sebeplerle olur; haksız çıkarmaya karşı üye dava açabilir.
5. **Karar denetimi** — Genel kurulun kanuna, tüzüğe veya dürüstlük kuralına aykırı kararlarına karşı, toplantıda bulunmayıp karara katılmayan veya muhalif kalan her üye, karar tarihinden başlayarak bir ay (öğrenme/tescil ölçütleriyle) içinde iptal davası açabilir (TMK m.83 atfı; TTK genel kurul rejimiyle paralel mantık).
6. **Sona erme** — TMK m.87-89: kendiliğinden sona erme (amaç gerçekleşmesi/imkânsızlaşması, aciz, ilk genel kurulun yapılamaması), genel kurul kararıyla fesih ve mahkeme kararıyla fesih (kanuna/ahlaka aykırı amaç).

## Çıktı modülleri
- Aşama teşhisi (kuruluş/işleyiş/üyelik/sona erme) + dayanak.
- Tüzük/zorunlu içerik kontrol listesi.
- İlgili dava türü ve süre uyarısı (özellikle karar iptalinde).
- Dilekçe/başvuru iskeleti + `[doldurulacak]` veri yerleri.

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
