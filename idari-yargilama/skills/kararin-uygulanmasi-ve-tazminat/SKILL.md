---
name: kararin-uygulanmasi-ve-tazminat
description: "İdarenin lehe kararı uygulamaması, kararın gereğinin yerine getirilmesi ve uygulamama nedeniyle tazminat talebi gündeme geldiğinde kullanılır; iptal kararının geriye yürür etkisi ve idarenin tesis etmesi gereken işlemin belirlenmesinde başvurulur."
---

# İptal Kararının Uygulanması ve Tazminat

## Görev
Lehe sonuçlanan idari davanın gereğinin idarece eksiksiz ve süresinde yerine getirilmesini sağlamak; uygulamama hâlinde başvurulacak yolları ve tazminat imkânını kurgulamak.

## Soğuk başlangıç (intake)
- Karar hangi işlemi iptal etti; idarenin tesis etmesi gereken yeni işlem ne?
- Karar idareye tebliğ edildi mi; üzerinden ne kadar süre geçti?
- İdare kararı uygulamadı mı, eksik mi uyguladı, yoksa şeklen uygulayıp aynı sonucu mu doğurdu?
- Uygulamama nedeniyle doğan zarar var mı?

## Denetim şeması
1. **Uygulama zorunluluğu ve süre** (Anayasa m.138/4; İYUK m.28/1): İdare, idari yargı kararlarının gereğini **gecikmeksizin** ve kararın tebliğinden itibaren en geç **30 gün** içinde yerine getirmek zorundadır. Bu süre kamu düzenine ilişkindir.
2. **İptal kararının etkisi**: İptal kararı işlemi tesis edildiği andan itibaren (geçmişe etkili) ortadan kaldırır; idare iptalden önceki hukuki duruma dönmek ve kararın gerekçesine uygun işlem tesis etmekle yükümlüdür. Kararın etrafından dolanan (aynı sakatlıkla yeniden işlem) tutum hukuka aykırıdır.
3. **Uygulamama hâlinde tazminat** (İYUK m.28/3): Kararın gereği yerine getirilmezse ilgili, idare aleyhine maddi ve manevi tazminat davası açabilir. Ayrıca kararı kasten yerine getirmeyen kamu görevlilerinin kişisel sorumluluğu gündeme gelebilir (İYUK m.28 ilgili fıkrası); kişisel kusurla devlet aleyhine rücu ilişkisi gözetilir.
4. **Parasal kararların infazı** (İYUK m.28/2): Tazminat ve vergi davalarında hükmedilen tutar için genel hükümler ve idarenin ödeme süresi uygulanır; idare aleyhine ilamların icrasında özel sınırlamalar gözetilir.
5. **Ara sonuç**: Uygulamama yazılı olarak idareye hatırlatılır (başvuru/ihtar) ve tarih ispatlanır; gerekirse yeni işlem yine iptal davasına konu edilir.

## Çıktı modülleri
- İdarenin yapması gereken işlem/eylem listesi (karar gerekçesine bağlı)
- Uygulama süresi takibi ve ihtar metni
- Tazminat davası seçeneği değerlendirmesi

## Plugin bağlamı

Bu beceri `idari-yargilama` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
