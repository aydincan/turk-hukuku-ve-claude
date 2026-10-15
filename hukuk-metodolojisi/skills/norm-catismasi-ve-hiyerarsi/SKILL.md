---
name: norm-catismasi-ve-hiyerarsi
description: "Aynı olaya birden fazla kural uygulanabiliyor ve bunlar farklı sonuçlar veriyorsa; özel-genel, önceki-sonraki, üst-alt norm çatışmasını ve Anayasa/AİHS üstünlüğünü çözmek için kullanılır."
---

# Norm Çatışması ve Hiyerarşi Çözümü

## Görev
Bir olaya uygulanabilir görünen rakip normlar arasında geçerli/öncelikli olanı, normlar hiyerarşisi ve çatışma kuralları aracılığıyla belirlemek.

## Soğuk başlangıç (intake)
- Çatışan normlar hangileri (kanun-kanun, kanun-tüzük/yönetmelik, kanun-Anayasa, kanun-AİHS)?
- Normlardan biri diğerine göre daha özel mi, daha yeni mi, daha üst mü?
- Konu temel hak alanına giriyor mu (AİHS m.90/5 devreye girer mi)?
- Çatışma görünüşte mi (yorumla giderilebilir) yoksa gerçek mi?

## Denetim şeması
1. **Önce yorumla uzlaştır** — Görünüşteki çatışmalar çoğu kez sistematik/amaçsal yorumla giderilir; iki norm farklı kapsamları düzenliyor olabilir. Gerçek çatışma ancak uzlaştırma imkânsızsa kabul edilir.
2. **Hiyerarşi (lex superior derogat inferiori)** — Anayasa (m.11: bağlayıcı ve üstün) > kanun > Cumhurbaşkanlığı kararnamesi (alanına göre) > yönetmelik. Alt norm üst norma aykırıysa uygulanmaz; idari düzenleme için idari yargıda iptal/itiraz yolu açıktır.
3. **Anayasaya uygun yorum** — Kanun birden çok okumaya açıksa Anayasa'ya uygun olanı seçilir; kanunun Anayasa'ya aykırılığı ciddi ise itiraz yoluyla AYM'ye başvuru (Anayasa m.152) düşünülür. AYM kararları bağlayıcıdır (m.153).
4. **Milletlerarası sözleşme üstünlüğü** — Anayasa m.90/5: usulüne göre yürürlüğe konmuş temel hak ve özgürlüklere ilişkin milletlerarası sözleşmeler (özellikle AİHS) ile kanunlar çatışırsa sözleşme esas alınır.
5. **Özel-genel (lex specialis derogat generali)** — Özel hüküm, genel hükmü kendi alanında bertaraf eder; genel hüküm boşlukta tamamlayıcı kalır.
6. **Önceki-sonraki (lex posterior derogat priori)** — Aynı düzeydeki normlarda sonraki, önceki ile çatıştığı ölçüde onu zımnen ilga eder; ancak sonraki genel, önceki özeli kural olarak ilga etmez.

## Çıktı modülleri
- Çatışan normların ve sonuçların tablosu.
- Uygulanan çatışma kuralı zinciri.
- Anayasa/AİHS denetimi gerekiyorsa yol önerisi.
- Sonuç + `[doğrulanacak]` AYM/Yargıtay künyesi.

## Plugin bağlamı

Bu beceri `hukuk-metodolojisi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
