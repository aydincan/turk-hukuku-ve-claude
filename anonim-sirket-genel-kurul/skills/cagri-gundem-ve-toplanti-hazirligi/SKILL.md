---
name: cagri-gundem-ve-toplanti-hazirligi
description: "Genel kurul toplantisinin cagri usulu, ilan, gundem hazirligi, cagrisiz toplanti ve Bakanlik temsilcisi gibi toplanti oncesi adimlarinin mevzuata uygunlugu denetlenecekse veya bir toplanti kurgulanacaksa kullanilir."
---

# Çağrı, Gündem ve Toplantı Hazırlığı

## Görev
Genel kurulun usulüne uygun toplanması için çağrı, ilan, gündem, davet ve Bakanlık temsilcisi adımlarını kurgulamak veya yapılmış bir toplantının hazırlık aşamasını denetlemek.

## Soğuk başlangıç (intake)
1. Çağrıyı kim yaptı: yönetim kurulu mu, mahkeme izniyle azlık mı, tasfiye memuru mu?
2. Esas sözleşmede çağrı usulü/süresi için özel düzenleme var mı; pay senetleri nama mı hamiline mi?
3. Toplantı tarihi, ilan tarihi ve Türkiye Ticaret Sicili Gazetesi (TTSG) ilanı arasındaki süre nedir?
4. Tüm pay sahipleri toplantıda hazır mı (çağrısız toplantı imkânı)?

## Denetim şeması
1. **Çağrıya yetki:** Kural olarak çağrı yönetim kuruluna aittir (TTK m.410/1); YK toplanamıyor/karar alamıyorsa pay sahibi mahkemeye başvurabilir (m.410/2). Azlık, gerekçe göstererek YK'den çağrı isteyebilir; reddedilirse mahkemeden çağrı izni alır (m.411-412).
2. **İlan ve süre:** Çağrı, esas sözleşmedeki şekilde, ayrıca şirketin internet sitesinde ve TTSG'de ilanla yapılır; ilan ile toplantı arasında **en az iki hafta** bulunmalıdır (m.414). Sürenin başlangıcı ilan günü hariç tutularak hesaplanır.
3. **Gündem:** Çağrıda gündem belirtilir (m.413); gündemde olmayan konu görüşülemez (m.413/2) — istisnalar: azlığın m.420 ertelemesi, m.439 özel denetçi talebi, YK üyelerinin görevden alınması ve yenilerinin seçimi gündeme bağlılık ilkesi dışındadır. Genel ifadeli gündem maddesi (örn. "diğer konular") esaslı kararlara dayanak olamaz; aksi iptal sebebidir.
4. **Çağrısız toplantı:** Bütün pay sahipleri/temsilcileri toplantıda hazır olur ve hiçbiri itiraz etmezse çağrı merasimine uyulmadan karar alınabilir (m.416). Toplantı boyunca bu bütünlük korunmalıdır; biri ayrılırsa nisap denetlenir.
5. **Bakanlık temsilcisi:** İlgili Yönetmelik uyarınca belirli toplantılarda (sermaye artırımı/azaltımı, tür değiştirme, birleşme, esas sözleşme değişikliği vb.) Bakanlık temsilcisinin bulunması zorunludur; yokluğu kararı sakatlar.
6. **İspat yükü/ara sonuç:** Çağrı ve ilanın yapıldığını şirket belgeyle ispatlar. Süre/gündem/temsilci eksiği genel kural olarak iptal sebebidir; çağrı hiç yapılmamış ve çağrısız toplantı şartları da yoksa yokluk gündeme gelir.

## Çıktı modülleri
- Çağrı metni ve TTSG ilan taslağı (gündem maddeleriyle).
- Süre/uygunluk kontrol listesi (iki haftalık ilan, internet sitesi, temsilci).
- Çağrısız toplantı tutanak başlığı ve hazır bulunma beyanı taslağı.

## Plugin bağlamı

Bu beceri `anonim-sirket-genel-kurul` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
