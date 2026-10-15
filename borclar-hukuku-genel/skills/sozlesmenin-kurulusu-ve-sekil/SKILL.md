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
