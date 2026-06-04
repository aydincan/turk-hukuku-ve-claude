---
name: risk-degerlendirmesi
description: "İşyerinde risk değerlendirmesinin yapılıp yapılmadığını, kapsam ve güncelliğini değerlendirmek ve 6331 m.5 önleme hiyerarşisine uygun tedbir tasarlamak için kullanılır."
---

# Risk Değerlendirmesi ve Önleme Hiyerarşisi

## Görev
6331 m.10 ve Risk Değerlendirmesi Yönetmeliği çerçevesinde risk değerlendirmesinin varlığı, kapsamı, yöntemi ve güncelliğini denetlemek; m.5 önleme hiyerarşisine göre tedbir önerilerini sıralamak. Hem uyum hem de kaza dosyasında kusur tartışmasının çekirdeğidir.

## Soğuk başlangıç (intake)
- Risk değerlendirmesi yapılmış mı; tarihi ve kullanılan yöntem (ör. matris/L tipi) nedir?
- Tehlike sınıfı nedir (değerlendirmenin yenileme periyodunu belirler)?
- İşyerinde değişiklik (yeni makine, süreç, kaza, ramak kala) sonrası güncelleme yapıldı mı?
- Değerlendirmeye çalışan temsilcisi ve İSG profesyonelleri katıldı mı?

## Denetim şeması
1. **Varlık ve zaman (m.10):** Risk değerlendirmesi yapılmamışsa bu başlı başına yükümlülük ihlalidir; kaza sonrası kusur değerlendirmesinde belirleyici olur.
2. **Kapsam:** Tüm tehlikeler (mekanik, kimyasal, ergonomik, psikososyal, biyolojik) ve etkilenebilecek çalışanlar (genç, gebe, engelli, alt işveren çalışanı) kapsanmış mı?
3. **Yöntem ve güncellik:** Tehlike sınıfına göre yenileme süresi (genelde çok tehlikeli 2, tehlikeli 4, az tehlikeli 6 yıl) ile değişiklik/kaza halinde derhal güncelleme yükümlülüğü.
4. **Önleme hiyerarşisi (m.5):** Önerilen tedbirler sırasıyla: riski ortadan kaldırma → kaynağında önleme → ikame → mühendislik/toplu koruma → idari önlem → kişisel koruyucu donanım. KKD daima son sırada; sadece KKD verilmiş olması yetersizdir.
5. **İspat ve illiyet:** Gerçekleşen kazadaki tehlikenin değerlendirmede öngörülüp öngörülmediği, öngörüldüyse tedbirin uygulanıp uygulanmadığı kusur oranını doğrudan etkiler. **Ara sonuç:** Öngörülmüş + tedbir alınmamış = ağır kusur karinesi.

## Çıktı modülleri
- Risk değerlendirmesi yeterlilik kontrol listesi.
- Tehlike-tedbir-hiyerarşi eşleştirme tablosu.
- Kaza dosyası için "öngörülebilirlik" değerlendirme notu.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
