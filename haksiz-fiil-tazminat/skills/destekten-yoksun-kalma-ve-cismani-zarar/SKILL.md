---
name: destekten-yoksun-kalma-ve-cismani-zarar
description: "Ölüm veya bedensel zarar (yaralanma, sürekli sakatlık) söz konusu olduğunda; tedavi gideri, çalışma gücü kaybı ve destekten yoksun kalma kalemlerini ve hak sahiplerini belirlemek için kullanılır."
---

# Destekten Yoksun Kalma ve Cismani Zarar

## Görev
Ölüm ve bedensel zarar hallerinde TBK m.53-55 kalemlerini tek tek belirlemek: cenaze gideri, tedavi gideri, çalışma gücü kaybı/azalması, ekonomik geleceğin sarsılması ve destekten yoksun kalma tazminatı. Hak sahiplerini ve destek ilişkisini saptamak; hesabı aktüeryal dayanağa oturtmak.

## Soğuk başlangıç (intake)
- Zarar ölümle mi sonuçlandı, yoksa bedensel zarar/sürekli sakatlık mı var?
- Ölende destek veren konum (gelir, yaş, bakmakla yükümlü olunanlar)?
- Yaralanmada iyileşme süresi, maluliyet oranı (rapor var mı)?
- Trafik/iş kazası gibi özel rejim ve sigorta devrede mi?

## Denetim şeması
1. **Ölüm hâli kalemleri (m.53).** Cenaze giderleri; ölüm hemen gerçekleşmemişse tedavi giderleri ve çalışma gücü kaybından doğan kayıplar; destekten yoksun kalma zararı. Bu kalemler ayrı ayrı talep edilir.
2. **Destek kavramı.** Destek, ölenin düzenli ve fiilen yardım ettiği kişidir; salt yasal akrabalık yetmez, fiilî destek ilişkisi aranır. Eş, çocuk, ana-baba tipik destek görenlerdir; destek payı ve süresi belirlenir.
3. **Bedensel zarar kalemleri (m.54).** Tedavi giderleri, kazanç kaybı, çalışma gücünün azalmasından/yitirilmesinden doğan kayıplar ve ekonomik geleceğin sarsılmasından doğan kayıplar.
4. **Belirleme (m.55).** Destek ve bedensel zarar hesabında sosyal güvenlik/sigorta mevzuatındaki sınırlamalarla bağlı kalınmaz; gerçek zarar esas alınır. Maluliyet oranı sağlık kurulu/ATK raporuna, hesap aktüer tablosuna (TRH/PMF) dayandırılır.
5. **Mahsup ve rücu.** SGK gelir/aylık ve sigorta ödemelerinin tazminata etkisi ve rücu ilişkisi (m.62; ilgili sosyal güvenlik mevzuatı) ayrıca incelenir; mükerrer tahsil önlenir.
6. **Ara sonuç.** Kalem-hak sahibi-tutar tablosu kurulur; maluliyet ve aktüer raporu ihtiyacı, destek payı varsayımları ve `[doğrulanacak]` veriler açıkça işaretlenir.

## Çıktı modülleri
- Kalem ve hak sahibi tablosu (ölüm/bedensel ayrımı).
- Bilirkişi/aktüer soru listesi (destek payı, maluliyet, yaşam süresi).
- Talep sonucu taslağı (kalem bazlı tutarlarla).

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
