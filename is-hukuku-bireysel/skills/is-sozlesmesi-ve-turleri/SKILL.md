---
name: is-sozlesmesi-ve-turleri
description: "İş sözleşmesinin kurulması, türü (belirli/belirsiz, tam/kısmi, deneme süreli, çağrı üzerine), işçi sıfatı ve İş Kanunu kapsamı tartışması gerektiğinde; sözleşme tipinin alacaklara ve feshe etkisini çözmek için kullan."
---

# İş Sözleşmesi ve Türleri

## Görev
İlişkinin iş sözleşmesi olup olmadığını, hangi rejime (4857 sayılı İş K. mı, TBK hizmet sözleşmesi mi) tabi olduğunu ve sözleşme türünü belirleyip; türün fesih, ihbar ve alacaklara etkisini ortaya koymak.

## Soğuk başlangıç (intake)
1. İşçi ne iş yapıyor, kime karşı, hangi tarihler arasında çalıştı?
2. Yazılı sözleşme var mı; süre belirli mi belirsiz mi, tam mı kısmi mi?
3. Deneme süresi kararlaştırıldı mı; çağrı üzerine/uzaktan/evden çalışma var mı?
4. Çalışan başka iş yapan/serbest çalışan/alt işveren işçisi olarak mı konumlandırıldı?

## Denetim şeması
1. **İşçi sıfatı ve bağımlılık (İş K. m.2, m.8):** Ücret karşılığı, iş görme ve bağımlılık unsurları var mı? Bağımlılık yoksa eser/vekâlet ilişkisine kayabilir.
2. **Kapsam (İş K. m.4):** İlişki istisnalardan biri mi (ör. ev hizmetleri, 50'den az işçili tarım, çırak/stajyer)? İstisna ise TBK m.393 vd. uygulanır. İspat yükü kapsam dışı olduğunu iddia edende.
3. **Tür belirleme:**
   - Süre: Belirli süreli sözleşme objektif sebebe bağlıdır (m.11); sebep yoksa belirsiz süreli sayılır. Zincirleme belirli süreli sözleşmeler kural olarak baştan belirsiz süreli kabul edilir.
   - Çalışma yoğunluğu: Kısmi süreli işçi (m.13) tam süreliye göre ayrımcılığa uğratılamaz; haklar süreyle orantılıdır.
   - Deneme süresi (m.15): En çok iki ay (TİS ile dört aya kadar); deneme içinde bildirimsiz ve tazminatsız fesih mümkün, ancak ücret ve doğmuş haklar saklı.
4. **Ara sonuç:** Tür, iş güvencesi kapsamını (m.18: 30+ işçi, 6 ay kıdem) ve ihbar önelini etkiler. Belirli süreli sözleşmede ihbar tazminatı kural olarak doğmaz; sürenin sonundan önce haksız feshte kalan süre ücreti (TBK m.438) gündeme gelir.

## Çıktı modülleri
- İlişkinin nitelendirilmesi ve tabi olduğu kanun.
- Sözleşme türü ve buna bağlı hak/güvence haritası.
- Belirli süre sapması varsa yeniden nitelendirme gerekçesi.
- Eksik bilgi için [doldurulacak] not listesi.

## Plugin bağlamı

Bu beceri `is-hukuku-bireysel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
