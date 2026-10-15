---
name: icerik-erisim-engelleme-5651
description: "İnternet içeriğine erişimin engellenmesi veya içeriğin yayından çıkarılması talepleri, katalog suçlar, gecikmesinde sakınca bulunan haller ve hangi mercie nasıl başvurulacağı söz konusu olduğunda kullanılır."
---

# 5651 Erişim Engelleme ve İçerik Çıkarma Şeması

## Görev
Bir internet içeriği hakkında erişimin engellenmesi veya içeriğin yayından çıkarılması talebinde doğru hukuki sebebi (madde), doğru mercii ve usulü tespit etmek; talep ya da bu tedbire karşı savunma stratejisini kurmak.

## Soğuk başlangıç (intake)
1. Şikâyet konusu içerik nedir ve hangi URL/hesapta yer alıyor?
2. Hukuki dayanak hangisi: katalog suç (m.8), gecikmesinde sakınca (m.8/A), kişilik hakkı ihlali (m.9), özel hayatın gizliliği (m.9/A) mi?
3. Müvekkil talep eden (mağdur) mi, yoksa içerik/yer/erişim sağlayıcı veya içerik sahibi mi?
4. Daha önce yer/erişim sağlayıcıya uyar-kaldır başvurusu yapıldı mı, sonuç ne oldu?

## Denetim şeması
1. **Hukuki sebep tespiti**: 5651 m.8 — sınırlı sayıda katalog suç (ör. çocukların cinsel istismarı, fuhuş, kumar, intihara yönlendirme vb.) için içeriğe/erişime engelleme; m.8/A — millî güvenlik, kamu düzeni, yaşam hakkı gibi gecikmesinde sakınca bulunan hallerde idari (BTK Başkanı) tedbir; m.9 — kişilik hakkı ihlalinde; m.9/A — özel hayatın gizliliği ihlalinde. Ara sonuç: hangi madde/usul.
2. **Merci**: Kural olarak **sulh ceza hâkimliği** karar verir; m.8/A'da BTK Başkanı'nın resen verip 24 saat içinde hâkim onayına sunduğu idari tedbir; m.9/A'da BTK Başkanlığına başvuru ve 4 saat içinde sonuçlandırma rejimi geçerlidir. Yanlış mercie başvuru sürdürülemez.
3. **Ölçülülük ve kapsam**: Tedbir kural olarak içeriğe (URL bazlı) yönelik olmalı; tüm siteye erişim engelleme ancak teknik zorunlulukta ölçülü kabul edilir (ifade özgürlüğü dengesi, Anayasa m.13 ve m.26-28). Ara sonuç: talep edilen kapsam ölçülü mü.
4. **İspat ve süre**: İhlalin somut, içerik bazlı gösterilmesi; m.9'da kişilik hakkı sahibinin başvurusu ve hâkimin 24 saat içinde karar vermesi rejimi; kararın yerine getirilme süresi (kural olarak 4 saat içinde erişim sağlayıcı/BTK marifetiyle) izlenir.
5. **İtiraz/savunma**: Karara karşı CMK m.267 vd. itiraz ilgili sulh ceza hâkimliğine; içerik/site sahibi açısından aşırı geniş ya da dayanaksız engellemeye karşı ölçülülük ve usul itirazı kurulur.

İlkesel içtihat ve ifade özgürlüğü dengesi için kararlarbilgibankasi.anayasa.gov.tr (bireysel başvuru) ve karararama.yargitay.gov.tr taranır; künye [doğrulanacak] işaretlenir, esas/karar no uydurulmaz.

## Çıktı modülleri
- Hukuki sebep + merci + usul tespit notu.
- Erişim engelleme/içerik çıkarma talebi veya itiraz dilekçesi taslağı.
- Ölçülülük ve kapsam değerlendirmesi.

## Plugin bağlamı

Bu beceri `telekomunikasyon-bilisim` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
