---
name: ihtiyati-tedbir-delil-tespiti
description: "Dava açılmadan veya yargılama sırasında bir hakkın güvence altına alınması (HMK m.389-399) ya da kaybolma riski olan delilin tespiti (m.400-405) gerektiğinde; teminat, itiraz ve tedbirin uygulanması süreçleri için."
---

# İhtiyati Tedbir ve Delil Tespiti

## Görev
Hak veya delili korumak için geçici hukuki koruma talebi kurmak; tedbir şartlarını, teminatı, uygulama ve itiraz sürelerini yönetmek.

## Soğuk başlangıç (intake)
- Korunacak menfaat ne? (mevcut durumun değişme/zarar riski var mı?)
- Tedbir dava açılmadan mı, dava sırasında mı isteniyor?
- Hakkın varlığı yaklaşık olarak ispatlanabilir mi (m.390/3)?
- Kaybolma riski olan delil mi söz konusu (tanık yaşlı/hasta, durum değişecek)?

## Denetim şeması
1. **Tedbir sebebi** (HMK m.389): Mevcut durumda meydana gelebilecek bir değişme nedeniyle hakkın elde edilmesinin önemli ölçüde zorlaşacağı veya tamamen imkânsız hâle geleceği ya da gecikme sebebiyle ciddi zarar doğacağı hallerde tedbir istenir.
2. **Yaklaşık ispat** (m.390/3): Talep eden, davanın esası yönünden kendisinin haklılığını **yaklaşık olarak** ispat etmek zorundadır; kesin ispat aranmaz.
3. **Talep ve karar** (m.390-391): Tedbir, dava açılmadan önce esas hakkında görevli/yetkili mahkemeden; dava sırasında davaya bakan mahkemeden istenir. Karar gerekçeli olur.
4. **Teminat** (m.392): Tedbir kural olarak teminat karşılığı verilir; resmi belgeye/kesin delile dayanan haklarda teminattan vazgeçilebilir.
5. **Uygulama ve dava açma zorunluluğu** (m.393-397): Tedbir kararı **bir hafta** içinde uygulanması istenmezse kendiliğinden kalkar (m.393); **dava açılmadan** alınan tedbirde **iki hafta** içinde esas dava açılmazsa tedbir kendiliğinden kalkar (m.397/1).
6. **İtiraz** (m.394): Aleyhine tedbir kararı verilen, tedbirin uygulanmasından itibaren bir hafta içinde itiraz edebilir.
7. **Delil tespiti** (m.400-405): Henüz inceleme sırası gelmemiş veya ileride elde edilmesi imkânsızlaşacak delil için tespit istenir; hukuki yarar (m.401) gerekir.

Ara sonuç: "Tedbir şartı + teminat + uygulama ve dava açma süreleri" çizelgesi.

## Çıktı modülleri
- Tedbir/delil tespiti talep dilekçesi iskeleti (yaklaşık ispat gerekçeli).
- Süre kontrol listesi (1 hafta uygulama, 2 hafta esas dava, 1 hafta itiraz).
- Teminat değerlendirmesi.

## Plugin bağlamı

Bu beceri `hukuk-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
