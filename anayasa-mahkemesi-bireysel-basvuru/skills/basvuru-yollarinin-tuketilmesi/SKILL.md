---
name: basvuru-yollarinin-tuketilmesi
description: "Bireysel başvurudan önce hangi olağan kanun yolunun etkili ve erişilebilir olduğu, istinaf/temyiz/itirazın tüketilip tüketilmediği, olağanüstü yolların gerekip gerekmediği sorulduğunda kullanılır."
---

# Başvuru Yollarının Tüketilmesi

## Görev
İhlali giderebilecek etkili ve erişilebilir olağan kanun yollarının doğru tespiti ve usulüne uygun tüketildiğinin doğrulanması; erken veya geç başvuru riskini önlemek.

## Soğuk başlangıç (intake)
- Şikâyet edilen işlem adli yargıdan mı, idari yargıdan mı, yoksa idari bir işlemden mi kaynaklanıyor?
- Hangi kanun yolları işletildi (istinaf, temyiz, itiraz, karar düzeltme niteliğinde yollar)?
- İşletilen yolda esasa ilişkin şikâyetler açıkça dile getirildi mi?
- Hâlâ açık ve etkili bir kanun yolu kaldı mı?

## Denetim şeması
1. Kural — Anayasa m.148/3 ve 6216 m.45/2: ihlal iddiasına ilişkin olarak kanunda öngörülmüş idari ve yargısal başvuru yolları tüketilmeden bireysel başvuru yapılamaz.
2. Etkili/erişilebilir yol testi — yalnızca teorik değil, ihlali giderebilecek nitelikte, ulaşılabilir ve makul başarı şansı olan yollar tüketilir. Etkisiz/belirsiz bir yola başvurmamak başvuruyu süresiz hale getirmez.
3. Şikâyetin tüketme sırasında ileri sürülmesi — başvurucu, AYM önüne taşıdığı esas şikâyetleri (örneğin gerekçeli karar hakkı, mülkiyet) derece mahkemelerinde de "özü itibarıyla" ileri sürmüş olmalıdır; aksi halde o şikâyet bakımından tüketme eksikliğinden ret riski doğar.
4. Olağanüstü yollar — yargılamanın yenilenmesi, kanun yararına bozma gibi olağanüstü yollar kural olarak tüketilmesi gereken yol değildir; bunların işletilmesi süreyi yeniden başlatmaz.
5. İstisna — yolların açıkça etkisiz veya fiilen ulaşılamaz olduğu hallerde tüketme şartı esnetilebilir; bu durum gerekçelendirilmelidir.

İspat yükü: tüketmenin tamamlandığını başvurucu gösterir; etkisizlik iddiasını da temellendirir.

Ara sonuç: "tüketildi / eksik / yanlış yol" tespiti ve gerekirse derdest yolun beklenmesi önerisi.

## Çıktı modülleri
- Tüketilen ve kalan kanun yolları haritası.
- Etkili yol değerlendirmesi.
- Şikâyetin tüketme sırasında ileri sürülüp sürülmediğine dair kontrol.
- Erken/geç başvuru riski uyarısı.

## Plugin bağlamı

Bu beceri `anayasa-mahkemesi-bireysel-basvuru` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
