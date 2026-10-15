---
name: borca-aykirilik-tazminat
description: "Borçlunun borcunu hiç veya gereği gibi ifa etmemesinden doğan tazminat sorumluluğunun unsurları, kusur karinesi ve zarar hesabı tartışıldığında kullanılır."
---

# Borca Aykırılık ve Tazminat Sorumluluğu

## Görev
Borçlunun borca aykırı davranışından doğan tazminat sorumluluğunu (TBK m.112 vd.) unsurları, kusur karinesi, illiyet ve zarar hesabı yönünden değerlendirmek.

## Soğuk başlangıç (intake)
- Borç hiç mi ifa edilmedi, geç mi, yoksa kötü mü ifa edildi?
- Alacaklının uğradığı zarar nedir; doğrudan/dolaylı, fiili zarar/yoksun kalınan kâr?
- Borçlunun yardımcı kişileri (ifa yardımcısı) devrede miydi?
- Sorumsuzluk anlaşması veya sınırlandırma var mı?

## Denetim şeması
1. Temel norm: TBK m.112 — borç hiç veya gereği gibi ifa edilmezse borçlu, kendisine bir kusur yüklenemeyeceğini ispat etmedikçe zararı gidermekle yükümlüdür. Burada kusur karinesi vardır; ispat yükü borçludadır (haksız fiilden farkı).
2. Unsurlar: (a) borca aykırı davranış, (b) zarar, (c) illiyet bağı, (d) kusur (karine ile var sayılır). Kusursuzluk ispatı veya uygun illiyetin kesilmesi sorumluluğu kaldırır.
3. İfa yardımcısının fiili: m.116 — borçlu, yardımcı kişilerin verdiği zarardan kendi fiili gibi sorumludur; bu sorumluluk sözleşmeyle sınırlandırılabilir (m.115 sınırları içinde).
4. Sorumsuzluk anlaşması: m.115 — ağır kusur (kasıt/ağır ihmal) için önceden yapılan sorumsuzluk anlaşması kesin hükümsüzdür; uzmanlık gerektiren faaliyet/izinli işlerde hafif kusur için bile geçersizdir.
5. Zararın belirlenmesi ve indirim: m.114 atfıyla haksız fiil hükümleri (m.51-52) kıyasen; müterafik kusur ve hâkimin takdiri (m.52), öngörülebilirlik.
6. Zamanaşımı: Kural 10 yıl (m.146); kanunda özel süre varsa o uygulanır.
7. İspat yükü: Aykırılığı ve zararı alacaklı; kusursuzluğunu borçlu ispatlar.

## Çıktı modülleri
- Sorumluluk unsurları kontrol listesi (kusur karinesi vurgulu).
- Zarar kalemleri ve indirim sebepleri tablosu.
- Sorumsuzluk/sınırlama maddelerinin geçerlilik denetimi.

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
