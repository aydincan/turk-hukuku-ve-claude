---
name: karsiliksiz-cek-kambiyo
description: "Karşılıksızdır işlemi yapılan çekte adli para cezası ve çek düzenleme/hesap açma yasağı (5941 s. Çek Kanunu m.5), şikâyet süresi ve etkin pişmanlıkla yaptırımın kaldırılması söz konusu olduğunda kullanılır."
---

# Karşılıksız Çek ve Kambiyo Suçları

## Görev
5941 sayılı Çek Kanunu m.5 çerçevesinde karşılıksız çek yaptırımını (adli para cezası ve çek düzenleme yasağı) denetlemek; şikâyet, süre ve etkin ödemeyle düşme imkânını değerlendirmek.

## Soğuk başlangıç (intake)
- Çekin üzerinde "karşılıksızdır" işlemi yapıldı mı, tarihi ne?
- Çek hesabı sahibi kim, çeki düzenleyen/temsilci kim?
- Hamil kim, şikâyet süresi (suçun/işlemin öğrenilmesinden itibaren) işliyor mu?
- Çek bedeli + faiz ödenip yaptırımın kaldırılması (m.5/10) gündemde mi?

## Denetim şeması
1. **Yaptırımın niteliği**: 5941 s. Kanun m.5 — üzerinde karşılıksızdır işlemi yapılmış çekin hamili şikâyette bulunursa, çek bedeli kadar adli para cezası ve çek düzenleme/çek hesabı açma yasağı uygulanır. Bu, şikâyete bağlı bir yaptırımdır.
2. **Fail-sorumlu tespiti**: Çek hesabı tüzel kişiye aitse, çeki düzenleyen yetkili gerçek kişi sorumlu olur (temsil ilişkisi ve imza yetkisi kontrol edilir).
3. **Şikâyet ve süre**: Yaptırım şikâyete bağlıdır; şikâyet süresi ve usulü kontrol edilir. Yetkili mahkeme (icra ceza/asliye ceza) ve görev belirlenir.
4. **Etkin ödeme — yaptırımın kaldırılması (m.5/10)**: Çek bedelinin işleyen faiziyle birlikte ödenmesi halinde, soruşturma/kovuşturma/infaz aşamasına göre yaptırım kaldırılır veya çek düzenleme yasağı kalkar; aşama ve ödeme zamanı belirleyicidir.
5. **Hukuk-ceza paralelliği**: Çek aynı zamanda kambiyo senedidir; İİK kapsamında kambiyo takibi (icra) paralel yürür. Ceza yaptırımı ile alacağın icra takibini ayrı yönet.
6. **Ara sonuç**: Karşılıksızdır işleminin geçerliliği, sorumlu sıfatı, şikâyet süresi ve ödeme ile düşme imkânı netleşir.

## Çıktı modülleri
- Karşılıksızdır işlemi/şikâyet süresi kontrolü
- Sorumlu (düzenleyen/temsilci) tespiti
- Etkin ödeme ile yaptırımı kaldırma senaryosu
- İcra (kambiyo takibi) ile koordinasyon notu
- Şikâyet veya savunma dilekçesi taslağı

## Plugin bağlamı

Bu beceri `ekonomik-ceza` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
