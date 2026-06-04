---
name: idari-para-cezasi-hesabi
description: "4054 m.16 uyarınca ciro üzerinden idari para cezası riskini hesaplamak, ağırlaştırıcı/hafifletici unsurları belirlemek ve pişmanlık ya da uzlaşma yoluyla indirim stratejisi kurmak istendiğinde kullanılır."
---

# İdari Para Cezası ve Pişmanlık-Uzlaşma

## Görev
Rekabet ihlalinde 4054 m.16 ve Ceza Yönetmeliği çerçevesinde olası para cezasını öngörmek; ağırlaştırıcı/hafifletici sebepleri haritalamak; pişmanlık (kartel) ve uzlaşma yollarıyla cezayı azaltma stratejisi geliştirmek.

## Soğuk başlangıç (intake)
- İhlal türü: kartel mi, diğer m.4 ihlali mi, m.6 kötüye kullanma mı, izinsiz birleşme/yanlış bilgi mi?
- Teşebbüsün ihlal yılına ilişkin yıllık gayri safi geliri (ciro) yaklaşık ne düzeyde?
- İhlal süresi ve tekerrür durumu nedir?
- İşbirliği/pişmanlık başvurusu yapılabilir mi; deliller ne durumda?

## Denetim şeması
1. **Ceza türü (m.16)** — esas para cezası kural olarak teşebbüsün bir önceki yıl gayri safi gelirleri üzerinden orana göre belirlenir (üst sınır kanunda öngörülmüştür). Ayrıca yerinde incelemeyi engelleme, yanlış/yanıltıcı bilgi, izinsiz birleşme gibi durumlarda nispi/özel cezalar gündeme gelir.
2. **Temel oran ve ağırlık** — Ceza Yönetmeliği uyarınca ihlalin türü (kartel daha ağır), süresi, pazar etkisi temel oranı belirler; süre uzadıkça artış uygulanır.
3. **Ağırlaştırıcı sebepler** — tekerrür, soruşturmaya yardımcı olmama, ihlale devam, zorlayıcı/teşvik edici (elebaşı) rol.
4. **Hafifletici sebepler** — soruşturmaya yardım, ihlale son verme, kusurun azlığı, devlet teşvikiyle hareket, ihlalde sınırlı rol.
5. **Pişmanlık (Kartel Yönetmeliği)** — yalnızca kartellerde; ilk başvurana ve delil sunana tam muafiyet, sonrakilere kademeli indirim. Başvuru sırası ve delil kalitesi belirleyicidir.
6. **Uzlaşma (Uzlaşma Yönetmeliği)** — ihlalin kabulü karşılığında belirli oranda indirim ve sürecin kısaltılması; pişmanlıkla birlikte kullanılabilir.
7. **Ara sonuç** — ceza aralığı tahmini, en uygun indirim yolu (pişmanlık/uzlaşma) ve net beklenen yaptırım senaryosu.

## Çıktı modülleri
- Ceza aralığı tahmini (ciro tabanı + ağırlık + süre + sebepler).
- Ağırlaştırıcı/hafifletici sebep envanteri.
- Pişmanlık vs. uzlaşma karar matrisi ve zamanlama uyarısı.
- Özel hukuk tazminat (m.57-58) yansıma riski notu.

## Plugin bağlamı

Bu beceri `rekabet-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
