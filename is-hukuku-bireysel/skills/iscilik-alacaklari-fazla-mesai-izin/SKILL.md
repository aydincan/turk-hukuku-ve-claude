---
name: iscilik-alacaklari-fazla-mesai-izin
description: "Fazla çalışma, ulusal bayram-genel tatil, hafta tatili ücreti ve yıllık izin alacaklarının doğup doğmadığını ve tutarını çözmek gerektiğinde; çalışma sürelerini, zamları ve takdiri indirimi kapsayan alacak hesabı için kullan."
---

# İşçilik Alacakları — Fazla Çalışma, UBGT, Hafta Tatili, Yıllık İzin

## Görev
Ücret dışı işçilik alacaklarını (fazla çalışma, fazla sürelerle çalışma, UBGT, hafta tatili, yıllık izin ücreti) doğru zam ve hesap esaslarıyla belirlemek.

## Soğuk başlangıç (intake)
1. Günlük/haftalık fiili çalışma saatleri ve düzeni nasıldı?
2. Bayram-genel tatil ve hafta tatillerinde çalışıldı mı?
3. Yıllık izinler kullandırıldı mı; izin defteri/imzalı belge var mı?
4. Bordrolarda fazla çalışma/tatil tahakkuku görünüyor mu?

## Denetim şeması
1. **Çalışma süresi (m.63):** Haftalık çalışma 45 saat. Aşan kısım fazla çalışmadır.
2. **Fazla çalışma / fazla sürelerle çalışma (m.41):** 45 saati aşan çalışma fazla çalışma → saat ücreti **%50 zamlı**. Sözleşmeyle haftalık süre 45'in altında belirlenmişse, bu süre ile 45 arasındaki çalışma fazla sürelerle çalışma → **%25 zamlı**. Yıllık fazla çalışma 270 saatle sınırlıdır (sınır aşımı çalışmayı geçersiz kılmaz, fazlasını da hak doğurur).
3. **UBGT (m.47):** Ulusal bayram ve genel tatil günü çalışılırsa, çalışılmayan o gün için bir günlük ücret zaten ödenir; çalışıldığında ayrıca her gün için bir günlük ücret daha → o günkü çalışma toplam iki yevmiye.
4. **Hafta tatili (m.46):** Tatilde çalışmadan bir günlük ücret hak edilir. Hafta tatilinde çalışıldıysa Yargıtay uygulamasında çalışılan gün için ilave 1,5 yevmiye doğar.
5. **Yıllık izin (m.53, 59):** Hizmet süresine göre 1-5 yıl 14 gün, 5-15 yıl 20 gün, 15+ yıl 26 gün (asgari, 18 yaş altı ve 50 yaş üstü en az 20 gün). Kullandırılmayan izin sözleşme sonunda **son ücret** üzerinden ücrete dönüşür (m.59). İspat yükü kullandırıldığına dair işverende (imzalı izin belgesi).
6. **İspat ve indirim:** Fazla çalışma işçide ispat; tanıkla ispatta ve uzun süreli/günlük çalışmalarda hakkaniyet/takdiri indirim uygulanabilir. İmzalı bordroda tahakkuk varsa o aylar dışlanır.

## Çıktı modülleri
- Alacak kalemleri tablosu (zam oranı + dönem + tutar mantığı).
- İspat yükü ve delil durumu notu.
- Takdiri indirim öngörüsü.
- Zamanaşımı uyarısı (ücret nitelikli alacaklarda 5 yıl).

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
