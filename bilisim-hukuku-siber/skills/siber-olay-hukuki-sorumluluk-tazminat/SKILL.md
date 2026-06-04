---
name: siber-olay-hukuki-sorumluluk-tazminat
description: "Veri ihlali, sistem kesintisi veya siber saldırı sonrası kurum-müşteri-iş ortağı arasındaki tazminat ve sözleşmesel sorumluluğu; kusur, illiyet ve zarar denetimini yapmak gerektiğinde kullanılır."
---

# Siber Olaydan Doğan Hukuki Sorumluluk ve Tazminat

## Görev
Bir siber olay sonrası kimin, kime, hangi hukuki sebeple ve ne kadar sorumlu olduğunu (haksız fiil/sözleşme) çözmek; tazminat talebi veya savunma stratejisi kurmak.

## Soğuk başlangıç (intake)
1. Zarar gören kim, zarar ne? (maddi kayıp, itibar, veri kaybı, manevi zarar?)
2. Taraflar arasında sözleşme var mı? (hizmet, işleme, SLA?)
3. Olayın sebebi ne? (kurumun tedbirsizliği, üçüncü kişi saldırısı, çalışan kusuru?)
4. Talep mi savunma mı, muhatap kim?

## Denetim şeması
1. **Sorumluluk temeli seçimi.** Sözleşme varsa borca aykırılık (TBK m.112 vd.) ve borçlunun yardımcı kişilerden sorumluluğu (TBK m.116) önceliklidir; sözleşme yoksa haksız fiil (TBK m.49). Çoğu olayda yarışan sebep söz konusudur; zarar görenin lehine olan seçilebilir.
2. **Haksız fiil unsurları (TBK m.49 vd.).** Fiil (güvenlik tedbirini almama/ihmal), hukuka aykırılık (KVKK m.12 ihlali, gizlilik ihlali), kusur, zarar ve illiyet bağı aranır. KVKK m.12 yükümlülüğünün ihlali hukuka aykırılığın güçlü göstergesidir. Üçüncü kişinin saldırısı illiyeti kesebilir; ancak öngörülebilir saldırıya karşı tedbirsizlik kusuru ortadan kaldırmaz.
3. **Manevi tazminat ve veri.** Kişilik hakkı ihlali (TMK m.24; TBK m.58) ve özel hayatın ihlali manevi tazminata esas olabilir; veri ihlalinde ilgili kişilerin zararı somutlaştırılır.
4. **İspat yükü ve hesap.** Sözleşmesel sorumlulukta borçlu kusursuzluğunu (TBK m.112) ispatlar; haksız fiilde kural olarak zarar görenin ispatı gerekir, KVKK m.12 ise tedbir ispatını kuruma yükler. Zarar kalemleri (fiili zarar, yoksun kalınan kâr, gideri yapılan müdahale masrafları) belgelenir; tazminattan indirim sebepleri (TBK m.52) gözetilir.
5. **Ara sonuç.** Sorumlu sıfatı, hukuki sebep, ispat dağılımı ve zamanaşımı (TBK m.72 haksız fiilde; m.146/147 sözleşmesel) netleştirilir.

## Çıktı modülleri
- Sorumluluk haritası (taraf-sebep-kusur-illiyet-zarar).
- Tazminat hesap çerçevesi ve indirim notu.
- Talep/ihtar veya savunma dilekçesi iskeleti.

## Plugin bağlamı

Bu beceri `bilisim-hukuku-siber` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
