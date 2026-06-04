---
name: marka-tecavuzu-denetimi
description: "Bir markanın izinsiz kullanımı, taklit ürün, karıştırılma ihtimali veya tanınmış markadan haksız yararlanma iddiasında tecavüzün varlığını SMK m.7 ve m.29 çerçevesinde adım adım değerlendirmek gerektiğinde kullanılır."
---

# Marka Hakkına Tecavüz Denetimi

## Görev
Tescilli marka hakkına tecavüz iddiasını SMK m.7 (hakkın kapsamı) ve m.29 (tecavüz sayılan fiiller) çerçevesinde denetlemek; karıştırılma ihtimalini ve tanınmışlık korumasını altlamak.

## Soğuk başlangıç (intake)
- Markanın tescil numarası, sınıfı (Nice) ve tescilli işaret nedir?
- İhlal iddia edilen işaret/ürün hangi mal-hizmette, hangi biçimde kullanılıyor?
- Markalar/işaretler aynı mı, benzer mi; mallar/hizmetler aynı mı, benzer mi?
- Marka tanınmış mı; kullanmama def'i (m.19/2) gündeme gelir mi?

## Denetim şeması
1. Hakkın kapsamı: Tescilli marka sahibi izinsiz kullanımı önleme hakkına sahiptir (SMK m.7/2). Aynı işaret + aynı mal/hizmet halinde karıştırılma aranmaz (m.7/2-a).
2. Karıştırılma ihtimali: İşaret benzer ve mal/hizmet benzer ise halk nezdinde karıştırılma ihtimali (ilişkilendirme dahil) değerlendirilir (m.7/2-b). Bütünsel izlenim, ortalama tüketici, ayırt edicilik düzeyi ölçütleri uygulanır.
3. Tanınmış marka: Farklı mal/hizmette dahi haksız yarar, itibara/ayırt ediciliğe zarar varsa koruma genişler (m.7/2-c). Tanınmışlık davacıya ispat yükü.
4. Tecavüz fiilleri: Taklit, iltibas yaratacak kullanım, ambalaj/etiket, ticari belge ve internet kullanımı SMK m.29'da sayılıdır. Marka olarak kullanım şartı ve dürüst kullanım istisnaları (m.7/5) tartılır.
5. Savunmalar: Kullanmama def'i (m.19/2 — son 5 yıl ciddi kullanım), önceki hak, hakkın kötüye kullanılması; süre yönünden sessiz kalma (m.25/6).
6. Ara sonuç: Tecavüz sabitse SMK m.149 talepleri (tespit, durdurma, giderme, tazminat, el koyma, imha) açılır.

## Çıktı modülleri
- İşaret/mal-hizmet karşılaştırma tablosu.
- Karıştırılma ihtimali altlama notu.
- Talep listesi (SMK m.149 atıflı) ve savunma haritası.

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
