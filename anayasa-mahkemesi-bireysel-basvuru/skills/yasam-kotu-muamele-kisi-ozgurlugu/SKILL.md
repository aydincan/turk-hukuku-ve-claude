---
name: yasam-kotu-muamele-kisi-ozgurlugu
description: "Yaşam hakkı, işkence/kötü muamele yasağı ile kişi hürriyeti ve güvenliği (gözaltı, tutukluluk, uzun tutukluluk) bağlamında negatif ve pozitif yükümlülük ihlalleri iddia edildiğinde kullanılır."
---

# Yaşam, Kötü Muamele ve Kişi Özgürlüğü

## Görev
m.17 (yaşam, maddi-manevi varlık, kötü muamele yasağı) ve m.19 (kişi hürriyeti ve güvenliği) kapsamında Devletin negatif ve pozitif (koruma + etkili soruşturma) yükümlülüklerinin ihlalini değerlendirmek.

## Soğuk başlangıç (intake)
- Olay nedir (ölüm/yaralanma, gözaltı/tutuklama, kötü muamele iddiası)?
- Devlet görevlisi mi sorumlu, yoksa Devletin koruma/önleme/soruşturma ihmali mi var?
- Özgürlükten yoksun bırakma hangi sebebe ve hangi karara dayanıyor?
- Tutukluluk ne kadar sürdü; etkili bir başvuru/itiraz imkânı tanındı mı?

## Denetim şeması
1. Yaşam hakkı (m.17) — negatif yükümlülük: Devletin kasten veya orantısız güç kullanımıyla ölüme yol açmaması. Pozitif yükümlülük: yaşamı koruma ve ölümü/ağır yaralanmayı aydınlatan ETKİLİ, bağımsız, ivedi soruşturma.
2. Kötü muamele yasağı — eşik: muamelenin asgari ağırlık eşiğini aşması. Maddi boyut (muamelenin kendisi) ve usuli boyut (etkili soruşturma) ayrı incelenir; ispat "makul şüphenin ötesinde", gözetim altındaki kişide ispat yükü Devlete kayar.
3. Kişi özgürlüğü (m.19) — yoksun bırakma yalnızca m.19/2-3'teki sınırlı sebeplerle ve kanunda gösterilen usulle mümkündür.
4. Tutuklama denetimi — makul suç şüphesi (somut delil), tutuklama nedenlerinin (kaçma, delil karartma) varlığı, ölçülülük ve adli kontrolün yetersizliği; tutukluluğun makul süreyi aşması (m.19/7) ihlaldir.
5. Usuli güvenceler — yakalanma sebebinin bildirilmesi, hâkim önüne çıkarılma, tutukluluğa etkili itiraz ve tazminat hakkı (m.19/8-9).

İspat yükü: gözaltı/tutukluluk koşullarında ve resmî gözetimde Devlete; aksi halde başvurucuya ağırlıklı olarak düşer.

Ara sonuç: ihlalin maddi mi usuli mi olduğu ve dayanak.

## Çıktı modülleri
- Negatif/pozitif yükümlülük ayrımı.
- Soruşturmanın etkililiği değerlendirmesi.
- Tutukluluk için makul şüphe–neden–süre denetimi.
- İlke kararlarına atıf [doğrulanacak].

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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
