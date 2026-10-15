---
name: usul-gorev-yetki-dava-sarti
description: "Ekonomik suç dosyasında soruşturma-kovuşturma akışı, görevli-yetkili mahkeme, iddianame denetimi (CMK m.170, m.174) ve vergi/SPK suçlarına özgü mütalaa-şikâyet ön şartlarının kontrolü gerektiğinde kullanılır."
---

# Usul, Görev-Yetki ve Mütalaa/Dava Şartları

## Görev
Ekonomik suç dosyasının ceza muhakemesi iskeletini kurmak: evre, görev-yetki, iddianame denetimi ve alana özgü dava/mütalaa ön şartlarını sıraya koymak.

## Soğuk başlangıç (intake)
- Dosya hangi evrede? (soruşturma, iddianame, kovuşturma, kanun yolu)
- Suç tipi ne ve buna bağlı görevli mahkeme (asliye ceza / ağır ceza) hangisi?
- Ön şart gerektiren bir suç mu (vergi VUK m.367, SPK m.115)?
- İddianamede vakıa-delil-suç vasfı uyumu var mı?

## Denetim şeması
1. **Evre tespiti**: Soruşturma (CMK m.160 vd. — savcılık, kolluk, koruma tedbirleri) ile kovuşturma (iddianamenin kabulüyle başlar) ayrılır; her evrenin imkân ve süreleri farklıdır.
2. **Ön şart taraması**: Vergi kaçakçılığında mütalaa (VUK m.367), SPK suçlarında SPK başvurusu/mütalaası (m.115), karşılıksız çekte şikâyet (5941 m.5) gibi ön şartlar — yoksa kovuşturma usulden sakat, durma/düşme gündeme gelir.
3. **Görev**: Suçun cezasının üst sınırına göre ağır ceza (kural olarak 10 yıl ve üzeri ağırlıkta) / asliye ceza ayrımı; örneğin nitelikli zimmet, irtikâp gibi ağır cezalı suçlar ağır ceza mahkemesinde görülür. Suç tipine göre kontrol edilir.
4. **Yetki (CMK m.12 vd.)**: Suçun işlendiği yer mahkemesi kural; teşebbüs/zincirleme/çok failli ekonomik suçlarda yetki çatışmalarına dikkat.
5. **İddianame denetimi (CMK m.170 ve m.174)**: İddianamede yüklenen suç, olaylar, deliller ve hangi maddeye dayanıldığı gösterilmeli; eksiklik halinde iade (m.174) talep edilir.
6. **Zamanaşımı (TCK m.66, m.68)**: Dava ve ceza zamanaşımı suçun üst sınırına göre hesaplanır; teselsül eden fiillerde başlangıç notu alınır.
7. **Ara sonuç**: Evre, ön şart, görev-yetki, iddianame uygunluğu ve zamanaşımı tek tabloda toplanır.

## Çıktı modülleri
- Evre ve süre haritası
- Mütalaa/şikâyet ön şartı kontrol listesi
- Görev-yetki belirleme notu
- İddianame iade gerekçesi taslağı (varsa)
- Zamanaşımı hesabı

## Plugin bağlamı

Bu beceri `ekonomik-ceza` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
