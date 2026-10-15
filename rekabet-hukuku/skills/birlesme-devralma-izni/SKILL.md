---
name: birlesme-devralma-izni
description: "Bir birleşme, devralma, ortak girişim veya kontrol değişikliği işleminin Rekabet Kurulu iznine tabi olup olmadığını, bildirim eşiklerini ve esas inceleme riskini değerlendirmek istendiğinde kullanılır."
---

# Birleşme ve Devralma İzni (m.7)

## Görev
İşlemin 4054 m.7 ve Birleşme/Devralma Tebliği (2010/4) kapsamında bildirime tabi bir yoğunlaşma oluşturup oluşturmadığını, ciro eşiklerini ve etkin rekabetin önemli ölçüde azalıp azalmayacağını değerlendirmek.

## Soğuk başlangıç (intake)
- İşlem türü: birleşme, hisse/varlık devri, ortak girişim kuruluşu?
- Kontrolde kalıcı değişiklik doğuyor mu (tek/ortak kontrol)?
- Tarafların Türkiye ve dünya ciroları yaklaşık ne düzeyde?
- Taraflar aynı pazarda rakip mi (yatay), tedarik zincirinde mi (dikey)?

## Denetim şeması
1. **Yoğunlaşma var mı (m.7, Tebliğ 2010/4)** — kontrolde kalıcı değişiklik gerekir. Geçici/finansal işlemler, grup içi yeniden yapılanmalar kural olarak yoğunlaşma sayılmaz. Tam işlevsel ortak girişimler bildirime tabidir.
2. **Bildirim eşikleri** — Tebliğ 2010/4'teki ciro eşiklerinin aşılıp aşılmadığı kontrol edilir (Türkiye ciroları ve taraf bazlı eşikler; teknoloji teşebbüsleri için özel eşik kuralı). **Eşik tutarları periyodik güncellendiğinden güncel Tebliğ metninden doğrulanır.**
3. **Zorunlu bildirim ve bekleme** — eşik aşılıyorsa işlem Kurul izni olmadan hukuken geçerlilik kazanmaz (m.7); izinden önce kapanış (gun-jumping) yaptırım riskidir.
4. **Esas inceleme** — etkin rekabetin özellikle hâkim durum yaratılması/güçlendirilmesi yoluyla önemli ölçüde azalıp azalmayacağı; yatay örtüşme, dikey/portföy etkileri, koordinasyon riski incelenir. HHI ve pazar payı eşikleri ön eleme aracıdır.
5. **Çözümler (taahhüt)** — rekabet endişesi varsa yapısal (elden çıkarma) veya davranışsal taahhütler sunulabilir; koşullu izin verilebilir.
6. **Ara sonuç** — bildirime tabi değil / koşulsuz izin beklenir / endişeli (taahhüt gerekli) / yasaklama riski şeklinde sonuçlandırılır.

## Çıktı modülleri
- Bildirim gerekliliği kararı ve eşik hesabı (güncel Tebliğ ile doğrulanacak).
- Yatay/dikey örtüşme ve risk haritası.
- Bildirim formu için bilgi/veri ihtiyaç listesi.
- Olası taahhüt senaryoları ve gun-jumping uyarısı.

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
