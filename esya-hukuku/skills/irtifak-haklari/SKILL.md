---
name: irtifak-haklari
description: "Bir taşınmaz üzerinde başkası lehine kullanım/yararlanma hakkı kurulması, kullanılması veya sona erdirilmesi söz konusu olduğunda; intifa, oturma, üst hakkı ve geçit/mecra gibi irtifakların tesisi, içeriği ve terkini için kullanılır."
---

# İrtifak Hakları (İntifa, Geçit, Üst Hakkı)

## Görev
İrtifak haklarının kurulması, içeriğinin belirlenmesi ve sona erdirilmesi: eşyaya bağlı ve kişiye bağlı irtifakları ayırmak, intifa/oturma/üst hakkı ve zorunlu geçit gibi tipik irtifakların şartlarını denetlemek.

## Soğuk başlangıç (intake)
- İrtifak bir taşınmaz lehine mi (eşyaya bağlı, örn. geçit) yoksa bir kişi lehine mi (intifa, oturma) kurulacak/kuruldu?
- Hak tapuya tescil edildi mi; süresi/koşulu var mı?
- Uyuşmazlık irtifakın kurulması mı, içeriği/kapsamı mı, yoksa terkini mi?
- Üst hakkı söz konusuysa süre (bağımsız-sürekli olarak ayrı kayıt) ve bedel düzenlenmiş mi?

## Denetim şeması
1. **Tür ayrımı**: Eşyaya bağlı irtifaklar (m.779 vd.) yararlanan taşınmaza bağlıdır; mülkiyetle birlikte geçer. İrtifaklar tescille doğar (m.780).
2. **İntifa hakkı (m.794 vd.)**: Sahibine eşyadan tam yararlanma yetkisi verir; devredilemez ama kullanımı bırakılabilir. İntifa sahibi olağan bakım ve masraflardan sorumludur (m.813). En geç hak sahibinin ölümüyle (tüzel kişide 100 yıl) sona erer (m.797).
3. **Oturma hakkı (m.823 vd.)**: Bir binada/bölümde oturma yetkisi; kişiye bağlı, devredilmez ve mirasla geçmez.
4. **Üst hakkı (m.826 vd.)**: Başkasının arazisinde/altında yapı sahibi olma hakkı; bağımsız ve sürekli nitelikteyse ayrı taşınmaz olarak tapuya kaydedilebilir (m.826/3, m.704).
5. **Zorunlu geçit ve mecra (m.747, m.744)**: Genel yola çıkışı olmayan taşınmaz maliki, tam bedel karşılığında komşudan geçit isteyebilir; mecra (su, enerji hattı) için de benzer kurallar uygulanır. Bu talepler dava yoluyla kurulur.
6. **Sona erme/terkin**: İrtifak, sürenin dolması, hakkın yararsız hâle gelmesi (m.785) veya terkinle sona erer; yararlanan taşınmaz için her türlü yarar kalmamışsa yüklü taşınmaz maliki terkin isteyebilir.
7. **Ara sonuç**: İrtifakın geçerli kuruluşu (tescil), kapsamı ve sona erme şartlarının tespiti.

## Çıktı modülleri
- İrtifak (intifa/geçit/üst hakkı) tesis veya terkin talebi iskeleti.
- Geçit/mecra davasında bedel ve güzergâh değerlendirmesi.
- Tescil/şerh kontrol listesi ve süre/sona erme uyarısı.

## Plugin bağlamı

Bu beceri `esya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
