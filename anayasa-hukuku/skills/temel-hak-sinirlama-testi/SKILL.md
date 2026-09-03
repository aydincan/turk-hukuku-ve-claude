---
name: temel-hak-sinirlama-testi
description: "Bir kanun, kararname veya idari işlemin bir temel hakka müdahalesinin Anayasa m.13 ölçütlerine uygun olup olmadığını adım adım test etmek; kanunilik, meşru amaç, demokratik gereklilik ve ölçülülük analizi gerektiğinde kullanılır."
---

# Temel Hak Sınırlama Testi (m.13)

## Görev
Bir devlet tasarrufunun temel hakka müdahalesini Anayasa m.13'ün beş ölçütüyle (kanunilik, sınırlama sebebine bağlılık, demokratik toplum düzeninin gerekleri, ölçülülük, hakkın özü) sistematik biçimde denetlemek ve sonucu gerekçeli bir değerlendirmeye bağlamak.

## Soğuk başlangıç (intake)
1. Hangi temel hak müdahaleye uğradı (ör. ifade m.26, mülkiyet m.35, toplantı m.34)?
2. Müdahale hangi tasarrufla yapıldı — kanun, CB kararnamesi, yönetmelik, idari işlem?
3. Müdahalenin dayandığı amaç/sebep (kamu düzeni, başkalarının hakları, milli güvenlik vb.) ne?
4. Daha hafif bir önlemle aynı amaca ulaşmak mümkün müydü?

## Denetim şeması
1. **Koruma alanı ve müdahale.** Önce hakkın kapsamını ve müdahalenin varlığını saptayın. Müdahale yoksa test sona erer.
2. **Kanunilik.** Müdahale erişilebilir, belirli ve öngörülebilir bir **kanunla** öngörülmüş mü? (m.13). Yönetmelikle hak sınırlaması kural olarak yetersizdir. Ara sonuç: kanuni dayanak var mı?
3. **Meşru amaç / sınırlama sebebine bağlılık.** İlgili hakkın kendi maddesindeki özel sınırlama sebebine dayanıyor mu? (ör. m.26/2'deki sebepler). Genel sınırlama yasağı: sebep dışına çıkılamaz.
4. **Demokratik toplum düzeninin gerekleri.** Müdahale zorlayıcı bir toplumsal ihtiyaca karşılık geliyor mu? AİHS m.8-11 ve m.90/son üzerinden AİHM ölçütleriyle besleyin.
5. **Ölçülülük.** Üç alt ilke: (a) elverişlilik — önlem amaca ulaştırıyor mu; (b) gereklilik — daha az sınırlayıcı bir araç var mı; (c) orantılılık — yarar/zarar dengesi. Ara sonuç: en az birinde elenirse müdahale ölçüsüzdür.
6. **Hakkın özü.** Sınırlama hakkı kullanılamaz hale getiriyor mu? Öze dokunma tek başına aykırılık sebebidir.
İspat: müdahalenin varlığını başvurucu, meşruiyetini ve gerekliliğini kamu makamı ortaya koyar. İlke düzeyinde AYM ölçülülük içtihadına atıf yapın ve künyeyi `[doğrulanacak]` işaretleyin (kararlarbilgibankasi.anayasa.gov.tr).

## Çıktı modülleri
- Adım adım m.13 test tablosu (her ölçüt: karşılandı/karşılanmadı + gerekçe).
- Zayıf halka tespiti ve aykırılık/ihlal sonucu.
- Norm denetimi veya bireysel başvuru dilekçesine taşınacak gerekçe paragrafları.

## Plugin bağlamı

Bu beceri `anayasa-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
