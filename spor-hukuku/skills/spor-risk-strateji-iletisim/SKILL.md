---
name: spor-risk-strateji-iletisim
description: "Spor uyuşmazlığında kazanç-kayıp ihtimalini değerlendirmek, sportif/mali/itibari riskleri tartmak, çözüm seçeneklerini sıralamak ve müvekkili (sporcu, kulüp, federasyon) bilgilendirmek gerektiğinde kullanın."
---

# Risk Değerlendirmesi, Strateji ve Müvekkil İletişimi

## Görev
Spor uyuşmazlığında olası sonuçları, sportif-mali-itibari riskleri ve çözüm seçeneklerini (mücadele, uzlaşma, geri çekilme) tartmak; müvekkile sade ve dürüst bir risk-strateji bilgilendirmesi sunmaktır.

## Soğuk başlangıç (intake)
1. Müvekkil kim ve nihai hedefi ne (cezanın kalkması, transfer, alacak, itibar koruması)?
2. Uyuşmazlığın bulunduğu aşama ve eldeki güçlü/zayıf yönler?
3. Zaman baskısı var mı (müsabaka takvimi, transfer dönemi, lisans tarihi)?
4. Mali ve itibari hassasiyetler neler?
5. Uzlaşma/sulh seçeneği masada mı?

## Denetim şeması
1. **Olasılık değerlendirmesi**: Hukuki argümanların gücüne ve emsal uygulamaya göre kazanma/hafifletme ihtimali gerçekçi biçimde belirlenir; kesin sonuç vaadi verilmez.
2. **Çok boyutlu risk**: Hukuki sonucun yanında sportif (men, puan silme, transfer yasağı), mali (para cezası, tazminat, bonservis kaybı) ve itibari (kamuoyu, sponsor) etkiler birlikte tartılır.
3. **Zaman ve takvim baskısı**: Müsabaka/transfer/lisans takvimi, tedbir talebi gerekliliği ve sürelerle çakışma değerlendirilir; acil tedbir seçeneği öne çekilir.
4. **Seçenek sıralaması**: Tam mücadele, kısmi itiraz, uzlaşma/sulh, geri çekilme seçenekleri maliyet-fayda ve süreyle birlikte sıralanır.
5. **İletişim ilkesi**: Müvekkile sade dille, en kötü-en iyi-olası senaryo üçlüsüyle ve net karar noktalarıyla bilgi verilir; karar müvekkilindir, kararın temeli yazılı bırakılır.
6. **Ara sonuç**: Önerilen strateji, gerekçesi ve müvekkilden istenen kararlar listelenir.

## Çıktı modülleri
- Risk haritası (hukuki/sportif/mali/itibari)
- Senaryo tablosu (en iyi/olası/en kötü)
- Strateji önerisi ve gerekçe
- Müvekkil bilgilendirme notu (sade dil)

## Plugin bağlamı

Bu beceri `spor-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
