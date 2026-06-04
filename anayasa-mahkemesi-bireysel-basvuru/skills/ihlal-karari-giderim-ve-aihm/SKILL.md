---
name: ihlal-karari-giderim-ve-aihm
description: "İhlal kararının sonuçları, yeniden yargılama, tazminat, kararın icrası ile bireysel başvuru sonrası AİHM yolu ve süresi değerlendirilirken kullanılır."
---

# İhlal Kararı, Giderim ve AİHM İlişkisi

## Görev
6216 m.50 çerçevesinde ihlal kararının doğurduğu sonuçları (yeniden yargılama, tazminat, icra) yönetmek ve gerekiyorsa AİHS m.34-35 yolunu planlamak.

## Soğuk başlangıç (intake)
- AYM ihlal mi, kabul edilemezlik/ret mi, ihlal yok kararı mı verdi?
- Karar yeniden yargılamaya mı gönderdi, yoksa tazminata mı hükmetti?
- İhlali ve sonuçlarını giderecek başka işlem gerekiyor mu?
- AİHM'e gitmek gerekirse süre işliyor mu?

## Denetim şeması
1. Karar türleri — m.49-50: kabul edilemezlik, ihlal yok veya ihlal kararı. İhlal kararında AYM, ihlalin ve sonuçlarının ortadan kaldırılması için yapılması gerekenlere hükmeder.
2. Yeniden yargılama — m.50/2: ihlal bir mahkeme kararından kaynaklanmışsa ve yeniden yargılamada hukuki yarar varsa, dosya ilgili mahkemeye gönderilir; mahkeme ihlali ve sonuçlarını gidermekle yükümlüdür. Yeniden yargılamada ihlal kararı bağlayıcıdır.
3. Tazminat — m.50/2: yeniden yargılamada yarar yoksa veya bu yol mümkün değilse AYM lehe maddi/manevi tazminata hükmedebilir ya da genel mahkemede dava açma yolunu gösterir.
4. İcra ve bağlayıcılık — AYM kararları yasama, yürütme, yargı organlarını ve herkesi bağlar (Anayasa m.153/6 ilkesi bireysel başvuru kararları yönünden de geçerlidir). Kararın gereği gecikmeksizin yerine getirilmelidir.
5. AİHM'e geçiş — AYM bireysel başvurusu etkili iç hukuk yolu sayılır ve tüketilmiş olur. AYM kararının sonucu yetersizse, AİHS m.35 uyarınca nihai iç karardan itibaren süre (güncel dört aylık süre) içinde AİHM'e başvurulabilir; süre ve koşullar resmî kaynaktan teyit edilir.

İspat yükü: giderimde hukuki yararı ve tazminat kalemlerini başvurucu temellendirir.

Ara sonuç: uygulanacak giderim yolu ve gerekiyorsa AİHM takvimi.

## Çıktı modülleri
- Karar türüne göre sonuç haritası.
- Yeniden yargılama / tazminat seçim notu.
- İcra takibi ve gecikme halinde yapılabilecekler.
- AİHM başvuru süresi ve koşul kontrolü [doğrulanacak].

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
