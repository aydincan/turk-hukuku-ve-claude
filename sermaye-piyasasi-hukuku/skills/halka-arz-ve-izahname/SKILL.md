---
name: halka-arz-ve-izahname
description: "Payların veya borçlanma araçlarının halka arzı, izahname/ihraç belgesi hazırlığı ve onayı, izahnamenin gerçeği yansıtmamasından doğan sorumluluk konuları gündeme geldiğinde kullanılır."
---

# Halka Arz ve İzahname

## Görev
Halka arz sürecini SPK m.4-11 ve ilgili Kurul tebliğleri çerçevesinde yapılandırmak; izahname/ihraç belgesi içeriğini denetlemek; izahname sorumluluğu (m.10) riskini değerlendirmek.

## Soğuk başlangıç (intake)
- İhraç türü: pay mı borçlanma aracı mı; ilk halka arz mı, bedelli/bedelsiz sermaye artırımı mı?
- Halka arz mı, yoksa istisna kapsamında tahsisli satış mı (m.11)?
- İzahname mi, ihraç belgesi mi gerekiyor; aracılık yüklenimi sözleşmesi var mı?
- Hangi taraf danışılıyor: ihraççı, aracı kurum, yatırımcı (zarar gören) mi?

## Denetim şeması
1. **Halka arz/istisna ayrımı:** İşlem SPK m.4 anlamında halka arz mı, yoksa m.11 ve tebliğdeki istisna (nitelikli yatırımcı, asgari tutar) kapsamında mı belirlenir. İstisna varsa izahname yerine ihraç belgesi gündeme gelir.
2. **İzahname hazırlığı ve onayı:** İzahnamenin Kurul onayına sunulması, içeriğinin ihraççı, ihraç ve riskleri tam, doğru, anlaşılır yansıtması aranır (m.4, m.6-8); özet bölümü ve risk faktörleri kontrol edilir.
3. **Sorumluluk denetimi (m.10):** İzahnamede yer alan yanlış, yanıltıcı veya eksik bilgiden ihraççı; ihraççı yoksa/karşılanamıyorsa garanti veren, ihraca aracılık eden lider kuruluş, hazırlayanlar ve onaylayan bağımsız denetçi/değerleme kuruluşu kusurları oranında sorumludur. Ara sonuç: zarar gören yatırımcının kime, hangi sırayla başvuracağı netleşir.
4. **İspat yükü:** Bilginin yanlışlığı ve zararla illiyeti yatırımcıda; gerekli özeni gösterdiğini ispat ise sorumlu tarafta (m.10 mantığı). Zarar, ihraç fiyatı ile gerçek değer/satış değeri farkı üzerinden kurulur.
5. **Süre:** Tazminat talebinde zamanaşımı için SPK m.10 ve TBK genel zamanaşımı birlikte değerlendirilir; tarih ve öğrenme anı dosyaya işlenir.

## Çıktı modülleri
- Halka arz/istisna nitelendirme notu
- İzahname içerik denetim listesi (risk faktörleri, finansallar, onay)
- Sorumluluk zinciri ve muhatap analizi (m.10)
- İhraççı için uyum kontrol listesi veya yatırımcı için talep iskeleti

## Plugin bağlamı

Bu beceri `sermaye-piyasasi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
