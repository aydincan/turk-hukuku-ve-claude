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
