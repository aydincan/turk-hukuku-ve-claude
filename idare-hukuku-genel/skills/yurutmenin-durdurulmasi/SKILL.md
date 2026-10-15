---
name: yurutmenin-durdurulmasi
description: "İdari işlemin uygulanması ağır zarar doğuracaksa dava süresince işlemin durdurulması için İYUK m.27 koşullarını değerlendirmek ve güçlü bir YD talebi kurmak amacıyla kullanılır."
---

# Yürütmenin Durdurulması Talebi

## Görev
Dava sonuçlanana kadar işlemin uygulanmasını durdurmak için İYUK m.27 koşullarını (telafisi güç zarar + açık hukuka aykırılık) somut ve ikna edici biçimde gerekçelendirmek.

## Soğuk başlangıç (intake)
1. İşlem uygulanırsa ortaya çıkacak somut zarar nedir; sonradan giderilebilir mi?
2. İşlemin açık hukuka aykırılığını gösteren en güçlü dayanak hangisi?
3. İşlem icra edilmeye başlandı mı; zaman baskısı var mı?
4. Teminat istenmesi muhtemel mi (m.27/6 istisnaları)?

## Denetim şeması
1. **Çifte koşul.** İYUK m.27/2: (a) işlemin uygulanması halinde **telafisi güç veya imkânsız zararlar** doğması **ve** (b) işlemin **açıkça hukuka aykırı** olması. İkisi birlikte aranır; yalnız biri yetmez.
2. **Telafisi güç zarar.** Parayla tam giderilemeyecek, geri dönülemez sonuçlar (yıkım, ruhsat iptali, görevden uzaklaştırma, sınır dışı vb.). Zararı soyut değil somut/ölçülebilir anlat.
3. **Açık hukuka aykırılık.** Beş unsur denetiminden çıkan en kuvvetli, ilk bakışta görülebilir aykırılığı öne çıkar; tartışmalı yorumlar yerine net dayanaklar.
4. **Gerekçe zorunluluğu.** YD kararı gerekçeli olmak zorundadır (m.27); talebini de aynı titizlikle gerekçelendir.
5. **Teminat.** Kural olarak teminat karşılığında verilir; ancak idareden ve adli yardımdan yararlananlardan teminat alınmayabilir (m.27/6). İstisnaları değerlendir.
6. **İtiraz yolu.** YD talebinin reddi/kabulüne karşı bir defaya mahsus itiraz (m.27/7) ve süresi.
7. **Ara sonuç.** Koşullar karşılanıyorsa güçlü YD gerekçesi; karşılanmıyorsa zararı/aykırılığı güçlendirecek ek delil stratejisi.

## Çıktı modülleri
- m.27 çifte koşul değerlendirme tablosu.
- Telafisi güç zarar anlatımı (somut örneklerle).
- Açık hukuka aykırılık özeti.
- Teminat ve itiraz yolu notu.

## Plugin bağlamı

Bu beceri `idare-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
