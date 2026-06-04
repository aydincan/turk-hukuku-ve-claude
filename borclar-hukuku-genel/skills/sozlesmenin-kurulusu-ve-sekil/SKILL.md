---
name: sozlesmenin-kurulusu-ve-sekil
description: "Bir sözleşmenin geçerli kurulup kurulmadığı, şekil şartına tabi olup olmadığı veya tek taraflı dayatılan standart maddelerin denetimi söz konusu olduğunda kullanılır."
---

# Sözleşmenin Kurulması, Şekil ve Genel İşlem Koşulları

## Görev
Bir sözleşmenin kurulup kurulmadığını, kuruluş anını, şekle uygunluğunu ve standart/dayatılmış maddelerin geçerliliğini denetlemek.

## Soğuk başlangıç (intake)
- Öneri ve kabul nasıl, ne zaman ve hangi içerikle gerçekleşti?
- Sözleşme bir şekle tabi mi (taşınmaz satışı, kefalet, vekâletten azil)?
- Metin matbu/standart mı; karşı taraf maddeleri müzakere edebildi mi?
- Tarafların esaslı noktalarda tam uyuşması var mı?

## Denetim şeması
1. Öneri-kabul: TBK m.1-2; esaslı noktalarda uyuşma şart, ikincil noktalar boş bırakılırsa hâkim doldurur (m.2/f.2). Süreli/süresiz öneri ve bağlayıcılık (m.3-5).
2. Şekil: Kural serbestî (m.12). Kanunen öngörülen şekil geçerlilik şartıdır; aksi hâlde kesin hükümsüzlük. Taşınmaz satışı resmî şekle (TMK m.706, Tapu K.), kefalet yazılı + el yazısı miktar/tarih (m.583), genel vekâletten azil serbest. İradi şekil kararlaştırılmışsa adi yazılı varsayılır (m.17).
3. Genel işlem koşulları: m.20-25. Yazılmamış sayılma (beklenmeyen/şaşırtıcı kayıt, m.21), yorumda aleyhe yorum, değiştirme yasağı (m.24), dürüstlüğe aykırı içerik denetimi (m.25). Tüketici işlemlerinde 6502 s.K. m.5 ek koruma.
4. Muvazaa: Görünürdeki ve gizli işlem ayrımı (TBK m.19); nispi muvazaada gizli işlem geçerli şekil şartını taşıyorsa ayakta kalır.
5. İspat yükü: Sözleşmenin kurulduğunu iddia eden ispatlar; senede karşı senetle ispat kuralı (HMK m.201) ve şekil şartına tabi işlemlerde tanık sınırı.
6. Ara sonuç: Sözleşme geçerli kuruldu mu, hangi maddeler yazılmamış sayılır?

## Çıktı modülleri
- Kuruluş analizi ve şekil uygunluk tablosu.
- Yazılmamış/geçersiz GİK maddeleri listesi.
- Eksik veya riskli kayıtlar için düzeltme önerisi.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
