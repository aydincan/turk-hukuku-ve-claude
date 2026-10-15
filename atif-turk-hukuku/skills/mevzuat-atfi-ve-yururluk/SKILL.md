---
name: mevzuat-atfi-ve-yururluk
description: "Bir kanun, kararname veya yönetmelik hükmüne atıf yapılırken; madde-fıkra-bent doğruluğunu, hükmün güncel/mülga/değişik olup olmadığını ve yürürlük tarihini denetlemek için kullanılır."
---

# Mevzuat Atfı ve Yürürlük Kontrolü

## Görev
Bir mevzuat hükmüne, doğru madde/fıkra/bent ile ve yürürlük durumu teyit edilmiş biçimde atıf yapmak; mülga veya değişmiş hükme dayanarak hatalı sonuç üretmeyi önlemek.

## Soğuk başlangıç (intake)
- Hangi kanun/kararname/yönetmelik, hangi madde-fıkra-bent?
- Hüküm güncel mi, yoksa değişmiş/yürürlükten kalkmış olabilir mi?
- Olayın tarihi ile hükmün yürürlük tarihi uyumlu mu (zaman bakımından uygulama)?
- Bu bir özel kanun mu, genel kanun mu (lex specialis ilişkisi var mı)?

## Denetim şeması
1. **Tam atıf** — Kanun adı veya numarası + madde + fıkra + bent: "TBK m.49/1", "HMK m.119/1-(e)", "İİK m.67/1". Kısaltma standardı tutarlı kullanılır (TMK 4721, TBK 6098, TTK 6102, TCK 5237, CMK 5271, HMK 6100, İYUK 2577, İİK 2004).
2. **Yürürlük/değişiklik** — mevzuat.gov.tr karşılaştırmalı/güncel metni esas alınır; "Mülga" veya "(Değişik: …)" ibaresi kontrol edilir. Eski metne dayanılıyorsa açıkça belirtilir.
3. **Zaman bakımından uygulama** — Olay tarihi ile hüküm tarihi çatışıyorsa hangi kanunun uygulanacağı (geçmişe etkisizlik, derhal uygulama, geçiş hükmü; ceza için lehe kanun, TCK m.7) ayrıca değerlendirilir.
4. **Hiyerarşi ve yetki** — Yönetmelik/tebliğ kanuna aykırı olamaz (Anayasa m.124); alt düzenleme kanunsuz hak/yük getiremez. Atıfta üst normla uyum denetlenir.
5. **Yollama zinciri** — Madde başka maddeye yolluyorsa (örn. "… hükümleri kıyasen uygulanır") zincir izlenir; atıf, asıl uygulanacak hükme yapılır.
6. **Yanlış numara riski** — Madde numarası benzer kanunlarla (örn. eski-yeni TBK/BK) karışabilir; numara daima güncel kanuna göre teyit edilir.

## Çıktı modülleri
- Tam mevzuat atfı (madde/fıkra/bent).
- Yürürlük durumu: güncel / değişik / mülga + tarih.
- Zaman bakımından uygulama notu (gerekirse).
- Hiyerarşi/yollama uyarısı.

## Plugin bağlamı

Bu beceri `atif-turk-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
