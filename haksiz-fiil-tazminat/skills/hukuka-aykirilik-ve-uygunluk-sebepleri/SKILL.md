---
name: hukuka-aykirilik-ve-uygunluk-sebepleri
description: "Fiilin hukuka aykırı sayılıp sayılmayacağı tartışmalıysa veya karşı taraf meşru savunma, rıza, zorda kalma ya da hakkın kullanılması savunması ileri sürdüğünde; aykırılık ve uygunluk dengesini denetlemek için kullanılır."
---

# Hukuka Aykırılık ve Hukuka Uygunluk Sebepleri

## Görev
Fiilin hukuka aykırılığını (mutlak hak ihlali / koruma normu ihlali / ahlaka aykırı kasıtlı zarar) tespit etmek ve TBK m.63'teki hukuka uygunluk sebeplerinden birinin aykırılığı ortadan kaldırıp kaldırmadığını denetlemek. Uygunluk sebebi varsa sorumluluk doğmaz; sınırı aşılırsa kısmî sorumluluk gündeme gelir.

## Soğuk başlangıç (intake)
- Hangi hak/menfaat zarar gördü (mutlak hak mı, salt malvarlığı mı)?
- Salt malvarlığı zararıysa ihlal edilen bir koruma normu var mı?
- Karşı taraf hangi haklılık sebebine dayanıyor (rıza, savunma, iztırar, hakkın kullanımı, kamu gücü)?
- Savunma/zorunluluk hâlinde ölçü aşıldı mı?

## Denetim şeması
1. **Aykırılık tipini belirle.** Mutlak hak (yaşam, beden, sağlık, kişilik, mülkiyet) ihlali kural olarak doğrudan hukuka aykırıdır. Salt malvarlığı zararında ihlal edilen davranış/koruma normu ya da m.49/2 (ahlaka aykırı + kast) aranır.
2. **Rıza (m.63/1).** Zarar görenin geçerli, aydınlatılmış ve hukuken korunan rızası aykırılığı kaldırır; kişilik haklarından kesin/sürekli vazgeçme geçersizdir (TMK m.23).
3. **Üstün özel/kamu yararı (m.63/1).** Korunan menfaat ihlal edilen menfaatten üstünse aykırılık kalkar; orantılılık aranır.
4. **Meşru savunma ve iztırar (m.63/2 ve m.64).** Saldırıya karşı orantılı savunma hukuka uygundur. Zorda kalan, başkasının malına verdiği zararda hâkimin takdiriyle tazminata hükmedilebilir (m.64).
5. **Hakkın kullanılması ve kamu gücü (m.63/1).** Yetkili merciin hukuka uygun emrini/yetkisini kullanma aykırılığı kaldırır; sınır aşılırsa kalan kısım için sorumluluk sürer.
6. **Ara sonuç ve ispat.** Aykırılığı (ve hak ihlalini) zarar gören; hukuka uygunluk sebebini ileri süren ve ölçüye uyduğunu ispatlar (TMK m.6). Sebebin sınırı aşılmışsa indirim (m.52) ya da kısmî sorumluluk değerlendirilir.

## Çıktı modülleri
- Aykırılık nitelendirme notu (hak tipi + dayanak).
- Uygunluk sebebi kontrol listesi (sebep + şart + ölçü).
- Sınır aşımı/kısmî sorumluluk değerlendirmesi.

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
