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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
