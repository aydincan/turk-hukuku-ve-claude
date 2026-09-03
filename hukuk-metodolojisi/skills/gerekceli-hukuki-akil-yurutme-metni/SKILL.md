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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
