---
name: zorunlu-trafik-sigortasi
description: "Trafik kazası nedeniyle zarar görenin sigortacıya doğrudan başvurması, teminat sınırları, kusur dağılımı ve zarar kalemleri tartışıldığında kullanılır; zorunlu mali sorumluluk sigortası kaynaklı uyuşmazlıkların temel becerisidir."
---

# Zorunlu Trafik Sigortası ve Üçüncü Kişinin Doğrudan Hakkı

## Görev
Trafik kazasında zarar görenin Zorunlu Mali Sorumluluk (trafik) sigortacısına doğrudan başvuru hakkını, teminat sınırlarını, kusur dağılımına göre sorumluluğu ve karşılanacak zarar kalemlerini belirlemek.

## Soğuk başlangıç (intake)
1. Kaza tarihi, taraflar ve araçların trafik sigortası poliçeleri ne?
2. Zarar bedeni mi (yaralanma/ölüm/destekten yoksunluk) maddi mi (araç hasarı)?
3. Kaza tespit tutanağı ve kusur durumu nedir?
4. Sigortacıya yazılı başvuru yapıldı mı; teminat limiti aşılıyor mu?

## Denetim şeması
1. **Doğrudan dava hakkı.** KTK m.97 ve m.91: zarar gören üçüncü kişi, doğrudan sigortacıya başvurabilir ve dava açabilir. Dava şartı: önce sigortacıya yazılı başvuru ve 15 günlük cevap süresi (KTK m.97).
2. **Teminat ve sorumluluk.** Sigortacı, işletenin sorumlu olduğu zararı poliçe teminat limitiyle sınırlı karşılar (KTK m.85, m.91; her yıl belirlenen teminat tutarları). Limit üstü kalan, işleten/sürücüye kalır.
3. **Zarar kalemleri.** Bedeni zararlarda tedavi giderleri, geçici/sürekli iş göremezlik, destekten yoksun kalma tazminatı (TBK m.53-55); maddi zararlarda araç onarım/değer kaybı. Ara sonuç: hangi kalemler teminatta?
4. **Kusur ve indirim.** Zarar görenin müterafik kusuru oranında indirim (TBK m.52). Genel şart istisnaları (örn. mücbir sebep, üçüncü kişinin ağır kusuru) sigortacı lehine sınır oluşturabilir.
5. **Zamanaşımı.** KTK m.109: kural iki yıl ve her halde sekiz yıl; fiil aynı zamanda suç oluşturup TCK'da daha uzun zamanaşımı öngörülmüşse o süre (uzamış ceza zamanaşımı) uygulanır. İspat: zararı ve kusuru zarar gören, teminat dışılığı sigortacı.

## Çıktı modülleri
- Doğrudan başvuru ve dava şartı kontrolü (KTK m.97).
- Teminat limiti ve karşılanan/karşılanmayan zarar ayrımı.
- Kusur dağılımı ve indirim hesabı.
- Zamanaşımı (m.109) değerlendirmesi ve süre uyarısı.

## Plugin bağlamı

Bu beceri `sigorta-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
