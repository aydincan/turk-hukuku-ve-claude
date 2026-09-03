---
name: temel-kavramlar-ve-sistem
description: "Kamu ihale hukukunun yapısını 4734 ve 4735 ekseninde kavramak, ihale türü-usul-eşik değer ilişkisini kurmak ve hangi alt rejimin uygulanacağını ayırt etmek için ilk başvurulacak harita beceridir."
---

# Temel Kavramlar ve İhale Sistematiği

## Görev
Somut işin kamu ihale rejimine girip girmediğini, giriyorsa hangi kanun/yönetmelik/usul ve eşik değere tabi olduğunu tespit etmek; sonraki uzman beceriye doğru yönlendirme yapmak.

## Soğuk başlangıç (intake)
1. İdare hangi kurum? (4734 m.2 kapsamı mı, m.3 istisna/kapsam dışı mı?)
2. İşin türü nedir: mal alımı, hizmet alımı, yapım işi, danışmanlık?
3. Yaklaşık maliyet/sözleşme bedeli eşik değerin altında mı üstünde mi (m.8, m.13)?
4. Uygulanan usul: açık, belli istekliler, pazarlık (m.21) yoksa doğrudan temin (m.22) mi?
5. Hangi aşamadasın: ilan öncesi, teklif değerlendirme, sözleşme, yoksa yasaklama mı?

## Denetim şeması
1. **Kapsam testi:** İdare 4734 m.2 kapsamında mı? Kapsamdaysa m.3 istisnaları veya kapsam dışılık var mı? İstisna varsa ilgili istisna usulü uygulanır, KİK denetimi farklılaşır.
2. **Tür tespiti:** Mal/hizmet/yapım ayrımı doğru yapılır; her tür için ayrı Uygulama Yönetmeliği ve tip şartname geçerlidir. Karma işlerde ağırlıklı unsur belirleyicidir.
3. **Eşik değer ve usul:** m.8 eşik değerleri ve m.13 ilan süreleri kontrol edilir; eşik altı/üstü ilan süresini ve ilan mecrasını değiştirir. Açık ihale asıldır; pazarlık (m.21/a-f) ve doğrudan temin (m.22/a-i) yalnızca sayılı hallerde kullanılır — istisnaî usule keyfî kaçış hukuka aykırılıktır.
4. **İlke süzgeci (m.5):** Saydamlık, rekabet, eşit muamele, güvenilirlik ve kaynakların verimli kullanımı her aşamada ölçüt alınır; ihtiyacın bütünlük arz etmesi gerekir, kısmî bölmeyle eşik kaçırma yasaktır.
5. **Ara sonuç:** Tür + usul + eşik + aşama belirlenince, doğru uzman beceriye (yeterlik, aşırı düşük, şikâyet, sözleşme, yasaklama) sevk edilir.

İspat yükü: İdarenin işlemi tesis ederken dayandığı sebep ve dokümanı; isteklinin ise iddiasını teklif dosyası ve doküman üzerinden ortaya koyması beklenir.

## Çıktı modülleri
- İhale künyesi tablosu (idare, tür, usul, eşik, IKN, takvim).
- Uygulanacak kanun/yönetmelik/tip şartname listesi.
- Hangi uzman beceriye yönlendirildiğine dair kısa not.

## Plugin bağlamı

Bu beceri `kamu-ihale-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
