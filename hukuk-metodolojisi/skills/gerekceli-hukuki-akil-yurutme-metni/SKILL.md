---
name: gerekceli-hukuki-akil-yurutme-metni
description: "Bir hukuki analizi okunaklı, izlenebilir ve gerekçeli bir metne dökmek gerektiğinde; mütalaa, layiha gerekçesi ya da hukuki görüşün argüman mimarisini kurmak için kullanılır."
---

# Gerekçeli Hukuki Akıl Yürütme Metni (IRAC/Altlama Üslubu)

## Görev
Yapılmış bir hukuki analizi; sorunu, kuralı, uygulamayı ve sonucu açıkça birbirinden ayıran, atıf disiplinli ve karşı argümanı karşılayan gerekçeli bir metne dönüştürmek.

## Soğuk başlangıç (intake)
- Metin kim için: mahkeme (layiha), müvekkil (mütalaa), iç değerlendirme mi?
- Çözülecek hukuki soru tek mi, çok başlıklı mı?
- Lehe ve aleyhe argümanlar hazır mı; tartışmalı içtihat var mı?
- İstenen ton: kesin görüş mü, seçenekli risk analizi mi?

## Denetim şeması
1. **Olay (Facts)** — Hukuken önemli vakıalar yansız ve kronolojik verilir; nitelendirme bu aşamada yapılmaz, çekişmeli vakıa işaretlenir.
2. **Sorun (Issue)** — Çözülecek hukuki soru(lar) tek cümlelik, cevaplanabilir biçimde çerçevelenir; birden çok sorun ayrı başlıklara bölünür.
3. **Kural (Rule)** — Uygulanacak norm madde/fıkra/bent ile; yorum gerekiyorsa yöntem belirtilir; içtihat yalnızca doğrulanabilir künye veya `[doğrulanacak]` ile, ilke vurgusuyla anılır. Yürürlükteki kural ile doktrin görüşü ayrılır.
4. **Uygulama (Application)** — Altlama: her norm unsuru eldeki vakıaya bağlanır; ispat yükü (TMK m.6/HMK m.190) gösterilir; karşı argüman açıkça ele alınıp çürütülür ("ileri sürülebilirse de...").
5. **Sonuç (Conclusion)** — Net cevap; belirsizlik varsa olasılık dürüstçe ("kuvvetle muhtemel / tartışmalı") nitelenir, abartılı kesinlikten kaçınılır.
6. **Risk ve öneri** — Mütalaada eylem önerisi, alternatif strateji ve `[doldurulacak]` yer tutucularıyla eksik bilgi açıkça işaretlenir.

## Çıktı modülleri
- Başlıklı IRAC iskeleti (Olay/Sorun/Kural/Uygulama/Sonuç).
- Atıf listesi (mevzuat madde + içtihat `[doğrulanacak]`).
- Karşı argüman/çürütme bloğu.
- Risk haritası ve öneri (mütalaa ise).

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
