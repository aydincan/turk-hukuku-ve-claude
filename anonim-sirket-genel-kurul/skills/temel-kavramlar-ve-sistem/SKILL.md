---
name: temel-kavramlar-ve-sistem
description: "Anonim sirket genel kurulunun organ yapisi, gorev-yetki dagilimi, toplanti turleri ve karar gecersizligi rejiminin haritasini cikarmak gerektiginde; kullanicinin sorununu dogru alt-konuya yonlendirmek icin kullanilir."
---

# Temel Kavramlar ve Sistematik

## Görev
Anonim şirket genel kurulu (GK) hukukunun temel kavramlarını ve sistematiğini ortaya koymak; somut soruyu doğru alt-rejime (çağrı, nisap, temsil, iptal/butlan, azlık) yerleştirerek çalışma planı çıkarmak.

## Soğuk başlangıç (intake)
1. Şirket kapalı AŞ mi, halka açık/borsada işlem gören mi (SPK rejimi devreye girer mi)?
2. Sorun toplantı öncesi (çağrı/gündem), toplantı anı (nisap/temsil/oy) yoksa toplantı sonrası (karar geçersizliği) aşamasında mı?
3. Müvekkil pay sahibi mi, yönetim kurulu üyesi mi, azlık mı, şirket tüzel kişiliği mi?
4. Pay oranı ve imtiyaz var mı; oydan yoksunluk doğuran ilişki var mı?

## Denetim şeması
1. **Organ ve yetki:** GK'nin devredilemez görevleri TTK m.408'de sayılır (esas sözleşme değişikliği, organ seçimi/ibrası, finansal tabloların onayı, kâr dağıtımı, fesih vb.). Bir kararın hangi organa ait olduğu, yetki aşımının yaptırımını belirler; GK yetkisindeki bir işin YK'ce yapılması yokluk/butlan sorununa gider.
2. **Toplantı türü:** Olağan GK her faaliyet dönemi sonundan itibaren üç ay içinde (m.409/1); olağanüstü GK gerektikçe yapılır. Süreye uyulmaması başlı başına kararı sakatlamaz ama sorumluluk doğurabilir.
3. **Geçersizlik kademesi (ara sonuç):** Sakatlığı önce **yokluk** (hiç toplantı/çağrı yokluğu, irade yokluğu), sonra **butlan** (m.447 — vazgeçilemez pay sahipliği haklarına aykırılık, AŞ'nin temel yapısına/sermayenin korunmasına aykırılık), en sonra **iptal edilebilirlik** (m.445 — kanuna, esas sözleşmeye, dürüstlük kuralına aykırılık) sırasıyla test et. Butlan/yokluk süresiz ve herkesçe ileri sürülür; iptal üç aylık hak düşürücü süreye ve sınırlı davacı çevresine tabidir.
4. **İspat yükü:** Usulsüzlüğü ileri süren taraf vakıayı (örn. çağrı ilanının yapılmadığı) ispatla yükümlüdür; şirket usule uygunluğu tutanak, hazır bulunanlar listesi ve ilan belgeleriyle karşılar (TMK m.6).

## Çıktı modülleri
- Sorunun aşama haritası (öncesi/anı/sonrası) ve uygulanacak madde listesi.
- Geçersizlik kademesi tablosu (yokluk/butlan/iptal + süre + davacı).
- İlgili alt-beceriye yönlendirme ve eksik bilgi listesi.

## Plugin bağlamı

Bu beceri `anonim-sirket-genel-kurul` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
