---
name: muafiyet-menfi-tespit
description: "Bir anlaşma veya uygulamanın grup muafiyetinden yararlanıp yararlanmadığını, bireysel muafiyet (m.5) şartlarını sağlayıp sağlamadığını ya da menfi tespit (m.8) uygunluğunu değerlendirmek istendiğinde kullanılır."
---

# Muafiyet ve Menfi Tespit Değerlendirmesi

## Görev
m.4 kapsamına giren bir anlaşmanın grup muafiyeti tebliğleriyle veya bireysel muafiyetle (m.5) hukuka uygun hâle gelip gelmediğini, gerekirse menfi tespit (m.8) yolunu değerlendirmek.

## Soğuk başlangıç (intake)
- Anlaşma türü dikey mi, yatay işbirliği mi, teknoloji transferi/Ar-Ge/uzmanlaşma mı?
- Tarafların ilgili pazar payları yaklaşık ne düzeyde?
- Anlaşmada ağır/açık kısıtlama (RSF tespiti, bölge yasağı, fiyat tespiti) var mı?
- Anlaşmanın iddia edilen etkinlik/verimlilik kazanımı nedir?

## Denetim şeması
1. **Grup muafiyeti süzgeci** — anlaşma tipine göre ilgili tebliğe bakılır: dikey anlaşmalar için 2002/2 sayılı Tebliğ; ayrıca yatay işbirliği için ilgili tebliğ/kılavuzlar (uzmanlaşma, Ar-Ge, teknoloji transferi). Pazar payı eşiği aşılmıyor ve tebliğdeki ağır kısıtlama yoksa anlaşma topluca muaftır; ayrıca başvuru gerekmez (kendiliğinden uygulama sistemi).
2. **Ağır kısıtlama kontrolü** — dikeyde yeniden satış fiyatının tespiti, mutlak bölgesel koruma gibi kısıtlamalar grup muafiyetini kaldırır; bu durumda yalnızca bireysel muafiyet tartışılabilir.
3. **Bireysel muafiyet (m.5)** — dört şart **birlikte** sağlanmalı: (a) mal/hizmet üretiminde veya dağıtımında iyileşme ya da ekonomik/teknik gelişme, (b) tüketicinin bundan yarar sağlaması, (c) rekabetin gereğinden fazla sınırlanmaması, (d) ilgili pazarın önemli bölümünde rekabetin ortadan kalkmaması. İspat yükü teşebbüstedir.
4. **Menfi tespit (m.8)** — anlaşmanın m.4/m.6 kapsamına girmediğinin Kurul'ca tespiti istenebilir; muafiyetten kavramsal olarak farklıdır (muafiyet kapsama girer ama izin alır; menfi tespit kapsam dışıdır).
5. **Ara sonuç** — grup muafiyeti var / bireysel muafiyet savunulabilir / muafiyet riskli, anlaşma revize edilmeli sonuçlarından biri; gerekiyorsa sorunlu hükümler için alternatif lafız önerilir.

## Çıktı modülleri
- Grup muafiyeti uygunluk kontrol listesi (pazar payı + ağır kısıtlama).
- Bireysel muafiyet dört-şart analizi (kanıt ile).
- Sözleşme hükmü revizyon/redline önerileri.
- Menfi tespit vs. muafiyet yol kararı.

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
