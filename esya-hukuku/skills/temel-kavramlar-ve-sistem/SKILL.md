---
name: temel-kavramlar-ve-sistem
description: "Eşya hukuku uyuşmazlığını ilk kez nitelendirirken; ayni hak mı zilyetlik mi borç ilişkisi mi, taşınır mı taşınmaz mı, mülkiyet mi sınırlı ayni hak mı sorularını ayırmak ve doğru hukuki temeli kurmak için kullanılır."
---

# Temel Kavramlar ve Ayni Hak Sistematiği

## Görev
Önündeki olayı eşya hukuku sistematiğine oturtmak: hangi hakkın ihlal edildiğini, hakkın mutlak (ayni) mı yoksa nispi (alacak) mı olduğunu, taşınır/taşınmaz ayrımını ve uygulanacak normu belirlemek. Doğru nitelendirme sonraki tüm adımların (talep, süre, yetki, ispat) önkoşuludur.

## Soğuk başlangıç (intake)
- Uyuşmazlık konusu eşya taşınmaz mı (arsa, bina, bağımsız bölüm) yoksa taşınır mı (araç, makine, eşya)?
- Talep sahibi malik mi, zilyet mi, yoksa sınırlı ayni hak (intifa, ipotek, geçit) sahibi mi?
- Talep eşyanın aynına mı (geri alma, el atmanın önlenmesi) yoksa para/tazminata mı yöneliyor?
- Karşı tarafın hakkı bir tapu kaydına mı, sözleşmeye mi, fiilî zilyetliğe mi dayanıyor?

## Denetim şeması
1. **Hakkın türü**: TMK m.683 mülkiyetin kullanma-yararlanma-tasarruf yetkilerini verir; mutlak haktır, herkese karşı ileri sürülür. Ayni haklar sınırlı sayı (numerus clausus) ilkesine tabidir: taraflar yeni tür ayni hak ihdas edemez. Talep bir sözleşmeden doğuyorsa (örn. satış vaadi) henüz ayni hak değil, kişisel hak vardır.
2. **Taşınır/taşınmaz ayrımı**: Taşınmazlarda aleniyet aracı tapu sicilidir (m.997 vd.) ve kazanım kural olarak tescille olur (m.705/1). Taşınırlarda aleniyet zilyetliktir; mülkiyet teslimle geçer (m.762 vd.) ve zilyetlik karinesi (m.985) işler.
3. **Mülkiyet biçimi**: Paylı mülkiyette (m.688 vd.) her paydaş belirli pay üzerinde tasarruf edebilir; elbirliği mülkiyetinde (m.701 vd., örn. tereke) tasarruf ancak oybirliğiyle ve bütün üzerinde mümkündür. Bu ayrım dava ehliyetini ve husumeti belirler.
4. **Sınırlı ayni hak süzgeci**: İrtifaklar (m.779 vd.), taşınmaz yükü (m.839), rehin (m.850 vd., m.939 vd.) malikin yetkisini sınırlar. Bunların varlığı tapu kaydından veya teslimden okunur.
5. **Ara sonuç**: Talebin eşya hukukuna mı borçlar hukukuna mı dayandığını ve hangi davanın açılacağını tespit et. İspat yükü TMK m.6 uyarınca hakkı iddia edene aittir.

## Çıktı modülleri
- Nitelendirme notu (hak türü, eşya türü, mülkiyet biçimi).
- Olası talep türleri listesi ve dayandığı madde.
- Bir sonraki uzman beceriye yönlendirme (istihkak, el atma, tapu, zilyetlik, rehin).

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
