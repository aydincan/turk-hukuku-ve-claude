---
name: temel-kavramlar-ve-sistem
description: "Rekabet hukukunun yapısını, 4054 sayılı Kanunun üç ekseni ile temel kavramları (teşebbüs, hâkim durum, ilgili pazar) anlamak ve bir olayı doğru eksene yerleştirmek istendiğinde kullanılır; ilk teşhis ve yol haritası için başvurulur."
---

# Temel Kavramlar ve Sistematik

## Görev
Rekabet hukuku sorununu 4054 sayılı Kanunun sistematiğine oturtmak; teşebbüs, ilgili pazar, hâkim durum gibi temel kavramları somut olaya uygulayarak doğru denetim eksenini (m.4 / m.6 / m.7) belirlemek.

## Soğuk başlangıç (intake)
- Sorun bir anlaşma/işbirliği mi, tek bir teşebbüsün tek taraflı davranışı mı, yoksa bir birleşme/devralma işlemi mi?
- Taraflar kim; teşebbüs sıfatı taşıyorlar mı; faaliyet gösterilen mal/hizmet ve coğrafi alan nedir?
- Yaklaşık pazar payları ve rakipler biliniyor mu?
- Talep eden konumu: müvekkil ihlalci taraf mı, mağdur/şikâyetçi mi, işlem yapan mı?

## Denetim şeması
1. **Teşebbüs sıfatı (4054 m.3)** — ekonomik faaliyet yürüten her birim teşebbüstür; hukuki forma bakılmaz. Aynı ekonomik bütünlük içindeki şirketler tek teşebbüs sayılabilir (grup içi anlaşmalar m.4 kapsamı dışıdır).
2. **Üç eksenden hangisi?**
   - Birden çok teşebbüs arası irade uyuşması/koordinasyon → **m.4** (anlaşma, uyumlu eylem, teşebbüs birliği kararı).
   - Tek teşebbüsün pazar gücüne dayalı davranışı → **m.6** (hâkim durum testi sonrası).
   - Kontrol değişikliği doğuran yoğunlaşma → **m.7** (eşik kontrolü).
3. **İlgili pazar tanımı** — İlgili Pazarın Tanımlanmasına İlişkin Kılavuz uyarınca ürün pazarı (talep/arz ikamesi, SSNIP mantığı) ve coğrafi pazar. Pazar dar tanımlanırsa pay yükselir; bu nedenle her tarafça stratejik bir adımdır.
4. **Pazar gücü göstergeleri** — pazar payı, giriş engelleri, alıcı gücü, HHI yoğunlaşması. Hâkim durum (m.6) ve yoğunlaşma değerlendirmesi (m.7) bu göstergelere dayanır.
5. **Ara sonuç** — olayın hangi eksende, hangi ilgili pazarda ve hangi pay/güç düzeyinde olduğu netleştirilir; ispat yükü kural olarak ihlal iddiasında bulunan/Kurul'dadır, muafiyet iddiasında ise teşebbüstedir (m.5).

## Çıktı modülleri
- Olay-eksen eşleştirme tablosu (m.4/m.6/m.7).
- Ön ilgili pazar taslağı ve pay tahmini.
- Sonraki adım önerisi: ilgili uzman beceriye yönlendirme (kartel, hâkim durum, birleşme, muafiyet, usul).
- Açık veri eksiklikleri ve doğrulanacak hususlar listesi.

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
