---
name: pay-alim-teklifi-cagri
description: "Halka açık ortaklıkta yönetim kontrolünün ele geçirilmesi, zorunlu veya gönüllü pay alım teklifi (çağrı), muafiyet halleri ve çağrı yükümlülüğünün doğumu değerlendirileceğinde kullanılır."
---

# Pay Alım Teklifi (Çağrı) ve Yönetim Devri

## Görev
Halka açık ortaklıkta kontrol değişimi sonucu doğan zorunlu pay alım teklifi (çağrı) yükümlülüğünü SPK m.25-26 ve çağrı tebliği çerçevesinde belirlemek; muafiyet hallerini ve çağrı fiyatını değerlendirmek.

## Soğuk başlangıç (intake)
- Hedef ortaklıkta kontrol/yönetim kim tarafından, hangi oranda ele geçirildi?
- Pay devri doğrudan mı, dolaylı mı; birlikte hareket eden kişiler var mı?
- Çağrı zorunlu mu, gönüllü mü; muafiyet talebi gündemde mi?
- Müvekkil teklifte bulunan, hedef ortaklık yönetimi yoksa azınlık pay sahibi mi?

## Denetim şeması
1. **Kontrol tespiti:** Yönetim kontrolünü sağlayan oran/imtiyazın ele geçirilip geçirilmediği (SPK m.26 ve tebliğdeki eşik) belirlenir; doğrudan/dolaylı edinim ve birlikte hareket eden kişiler değerlendirilir.
2. **Çağrı yükümlülüğünün doğumu:** Kontrolün edinildiği an esas alınarak diğer pay sahiplerine pay alım teklifinde bulunma zorunluluğu doğup doğmadığı saptanır; ara sonuç olarak çağrı zorunlu mu gönüllü mü netleşir.
3. **Muafiyet:** Tebliğde sayılan hallerde (örneğin sermaye artırımına katılım, grup içi yapı değişikliği, finansal güçlük) Kurul'dan muafiyet talep edilebilirliği değerlendirilir.
4. **Çağrı fiyatı:** Asgari çağrı fiyatının belirlenme yöntemi (önceki işlem fiyatları/edinim bedeli) tebliğe göre hesaplanır; eksik fiyatlama azınlık pay sahibi açısından risktir.
5. **Yaptırım/ihlal:** Çağrı yükümlülüğünün ihlali idari yaptırım (m.103) ve oy haklarının kullanımına ilişkin tedbirler doğurur. İspatta edinim tarih ve oranları belge ile kurulur.

## Çıktı modülleri
- Kontrol/çağrı yükümlülüğü analizi
- Muafiyet değerlendirmesi ve başvuru iskeleti
- Çağrı fiyatı hesap notu
- Azınlık pay sahibi için hak/talep çerçevesi

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
