---
name: hukuka-uygunluk-sebepleri
description: "Meşru savunma, ilgilinin rızası, hak kullanma, kanun hükmü ve amirin emri gibi hukuka uygunluk sebeplerini ve sınırın aşılmasını değerlendirmek gerektiğinde kullanılır."
---

# Hukuka Uygunluk Sebepleri

## Görev
Tipik bir fiilin hukuka aykırılığını ortadan kaldıran sebeplerin (TCK m.24-27) bulunup bulunmadığını ve sınırın aşılması hâlinin etkisini değerlendirmek.

## Soğuk başlangıç (intake)
- Fiil hangi hak/değer için ve hangi saldırıya karşı yapıldı?
- Saldırı haksız, mevcut/yakın ve devam ediyor muydu?
- Savunma ile saldırı arasında orantı var mıydı; başka çıkış yolu var mıydı?
- Rıza söz konusuysa, konu üzerinde tasarruf edilebilir miydi?

## Denetim şeması
1. **Kanun hükmü ve amirin emri (m.24):** Fiil kanunun verdiği yetki ya da bağlayıcı emrin yerine getirilmesiyle mi işlendi? Konusu suç olan emir yerine getirilemez; getirilse de sorumluluk doğar (m.24/3).
2. **Meşru savunma (m.25/1):** Şartlar — (a) haksız bir saldırı, (b) saldırının hâlen var/başlamak üzere/devam ediyor olması, (c) kendine veya başkasına yönelmesi, (d) savunmanın saldırı ile orantılı olması. Tümü varsa fiil hukuka uygundur.
3. **Zorunluluk hâli (m.25/2):** Ağır ve muhakkak tehlikeden korunmak için orantılı kaçınma; bu bir kusurluluğu kaldıran sebep olarak da tartışılır.
4. **Hakkın kullanılması ve rıza (m.26):** Hakkını kullanan kişi (örn. avukatın savunma dokunulmazlığı), üzerinde mutlak surette tasarruf edilebilen bir hakka ilişkin geçerli ve önceden açıklanmış rıza. Yaşam ve vücut bütünlüğünde rızanın sınırlarına dikkat.
5. **Sınırın aşılması (m.27):** Sınır kast olmaksızın (taksirle) aşılmışsa ve fiil taksirle de cezalandırılıyorsa indirimli ceza; meşru savunmada mazur görülebilecek heyecan/korku/telaşla aşılması cezasızlık sonucunu doğurabilir. Ara sonuç: aşma kasıtlı mı, mazur görülebilir mi?
6. **Ara sonuç:** Bir sebep tam ise fiil suç değildir; eksikse kusurluluk katmanına geçilir.

## Çıktı modülleri
- Sebep bazlı şart kontrol listesi (madde atıflı).
- Orantılılık ve başka çıkış yolu değerlendirmesi.
- Sınırın aşılması senaryosu ve sonuç (cezasızlık/indirim).
- Savunma stratejisi notu ve `[doğrulanacak]` içtihat ihtiyacı.

## Plugin bağlamı

Bu beceri `ceza-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
