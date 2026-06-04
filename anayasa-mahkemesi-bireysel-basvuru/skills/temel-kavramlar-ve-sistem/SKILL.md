---
name: temel-kavramlar-ve-sistem
description: "Bireysel başvurunun ne olduğu, ikincil (sübsidiyer) niteliği, norm denetiminden farkı, kapsam ve genel mimari sorulduğunda; başvurunun hangi yola oturduğunu konumlandırmak için kullanılır."
---

# Temel Kavramlar ve Sistematik

## Görev
Olayın bireysel başvuru yoluna uygun olup olmadığını, başvurunun ikincil niteliğini ve diğer denetim yollarından (norm denetimi, AİHM, idari/adli yargı) farkını netleştirmek; başvurucuya doğru yolu göstermek.

## Soğuk başlangıç (intake)
- Şikâyet edilen nedir: bir mahkeme kararı mı, idari işlem mi, kanun hükmü mü, yoksa bir ihmal mi?
- Olağan kanun yolları (istinaf, temyiz, itiraz) tüketildi mi, yoksa hâlâ açık mı?
- Şikâyet, hakkın özüne mi (anayasal) yoksa delil/yorum hatasına mı (kanun yolu) ilişkin?
- Aynı konu AİHM veya başka bir uluslararası mercide derdest mi?

## Denetim şeması
1. Yol tespiti — Anayasa m.148/3 ve 6216 m.45: bireysel başvuru, kamu gücü işlemiyle Anayasa'da ve AİHS'in Türkiye'nin taraf olduğu hükümlerinde ORTAK güvence altına alınan haklara yöneliktir. Kanunun soyut iptali isteniyorsa yol norm denetimidir (m.150 vd.), bireysel başvuru değildir.
2. İkincillik — m.148/3 ve m.45/2: başvuru, ihlali giderebilecek olağan kanun yolları tüketilmeden yapılamaz. AYM bir "süper temyiz" değildir; maddi vakıa ve delil değerlendirmesi kural olarak derece mahkemelerine aittir (kanun yolu şikâyeti yasağı). Ara sonuç: salt yorum/delil itirazı ise başvuru "açıkça dayanaktan yoksun" sayılır (m.48/2).
3. Kapsam süzgeci — yalnızca Anayasa ve AİHS kesişimindeki haklar. Yalnızca Anayasa'da olup AİHS'te karşılığı bulunmayan ya da yalnızca AİHS'te olup Türkiye'nin çekince koyduğu güvenceler kapsam dışı kalabilir.
4. Diğer yollarla ilişki — AYM'ye başvuru iç hukuk yolu sayılır; tüketilmeden AİHM'e gidilemez. AYM kararından sonra AİHS m.34-35 yolu açıktır.
5. Mağdur sıfatı — m.46: ihlalden güncel, kişisel ve doğrudan etkilenme aranır; potansiyel/soyut etki yetmez.

İspat yükü: başvurucu, hangi hakkın hangi kamu gücü işlemiyle ihlal edildiğini ve mağdur sıfatını gösterir.

## Çıktı modülleri
- Yol uygunluk notu (bireysel başvuru mu / norm denetimi mi / kanun yolu mu).
- Kapsam ve ikincillik değerlendirmesi.
- İhlal iddiasının hangi hakka oturduğuna dair ön nitelendirme.
- Sonraki adım önerisi (tüketme, süre, hak analizi becerisine yönlendirme).

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
