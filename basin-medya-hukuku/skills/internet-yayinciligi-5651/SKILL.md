---
name: internet-yayinciligi-5651
description: "İnternette yayımlanan içeriğin kişilik hakkını ihlali nedeniyle içeriğin çıkarılması veya erişimin engellenmesi, içerik/yer/erişim sağlayıcı sorumluluğu ve unutulma hakkı söz konusu olduğunda kullanılır."
---

# İnternet Yayıncılığı ve Erişim Engelleme (5651)

## Görev
5651 sayılı Kanun kapsamında içeriğin çıkarılması ve erişimin engellenmesi yollarını işletmek; içerik/yer/erişim sağlayıcı sorumluluğunu ve unutulma hakkını değerlendirmek.

## Soğuk başlangıç (intake)
1. İhlal eden içeriğin tam URL'si ve yayın tarihi nedir?
2. İçerik sağlayıcıya başvuru yapıldı mı, sonuç ne oldu?
3. İhlal kişilik hakkı mı yoksa özel hayatın gizliliği mi?
4. İçerik güncel haber değeri taşıyor mu (unutulma hakkı analizi)?

## Denetim şeması
1. **Sorumluluk türleri**: İçerik sağlayıcı kendi içeriğinden sorumludur; yer sağlayıcı uyar-kaldır rejimine tabidir; erişim sağlayıcı hâkimlik/Kurum kararını uygular.
2. **Kişilik hakkı yolu (m.9)**: İhlale uğrayan kişi içerik/yer sağlayıcıdan içeriğin çıkarılmasını ister; sonuç alamazsa sulh ceza hâkimliğine başvurur. Hâkim, ihlali oluşturan kısma yönelik (URL bazlı) erişimin engellenmesine karar verir; ölçülülük esastır.
3. **Özel hayat (m.9/A)**: Özel hayatın gizliliği ihlalinde, gecikmesinde sakınca bulunan hâllerde BTK Başkanı re'sen erişimi engelleyebilir; karar sulh ceza hâkimliği onayına sunulur.
4. **Unutulma hakkı**: Eski haberin güncel kamu yararı kalmamışsa, arama sonuçlarından çıkarılması/indekslenmemesi talep edilebilir; kamu yararı ile kişisel menfaat tartımı yapılır [ilkesel; AYM ve Yargıtay HGK içtihadı doğrulanacak].
5. **Ara sonuç**: İhlal sabit, ölçülü ve URL'ye özgülenmiş talepse erişim engelleme/içeriğin çıkarılması kabule değer.

## Çıktı modülleri
- İçerik/yer sağlayıcıya uyar-kaldır bildirimi
- Sulh ceza hâkimliğine m.9 başvuru dilekçesi (URL listeli)
- Unutulma hakkı tartım notu

## Plugin bağlamı

Bu beceri `basin-medya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
