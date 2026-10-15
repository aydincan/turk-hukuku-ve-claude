---
name: muvekkil-iletisim-bilgilendirme
description: "Siber olay veya bilişim ihtilafında müvekkili, yönetim kurulunu, çalışanları veya etkilenen ilgili kişileri hukuken doğru ama anlaşılır biçimde bilgilendirmek ve bildirim metinleri kurmak gerektiğinde kullanılır."
---

# Müvekkil ve Paydaş İletişimi

## Görev
Teknik ve hukuki açıdan karmaşık bir siber olayı, ilgili paydaşlara (müvekkil/yönetim, çalışanlar, etkilenen ilgili kişiler, düzenleyici) doğru, ölçülü ve anlaşılır biçimde aktaracak iletişim metinlerini kurmak.

## Soğuk başlangıç (intake)
1. Muhatap kim? (yönetim kurulu, müvekkil, çalışanlar, etkilenen müşteriler, basın?)
2. Hangi mesaj zorunlu, hangisi ihtiyari? (yasal bildirim mi, bilgilendirme mi?)
3. Hassasiyet düzeyi ne? (devam eden tehdit, soruşturma gizliliği, itibar?)
4. Hangi olgular kesin doğrulanmış, hangileri henüz belirsiz?

## Denetim şeması
1. **Mesaj-muhatap eşleştirmesi.** Her paydaşa içerik ve dil ayarlanır: yönetime risk/karar odaklı, çalışanlara talimat odaklı, ilgili kişilere KVKK m.12/5 bildirim içeriği (ihlalin niteliği, etkilenen veriler, önlemler, başvuru kanalları), düzenleyiciye resmi ve eksiksiz.
2. **Doğruluk ve ölçü.** Sadece doğrulanmış olgular paylaşılır; belirsizlikler abartılmadan/küçümsenmeden ifade edilir. Sorumluluk doğurabilecek peşin kabul ifadelerinden kaçınılır; aynı zamanda yanıltıcı/eksik bilgi yaptırım riski yaratır.
3. **Gizlilik ve ayrıcalık.** Soruşturma gizliliği (CMK), avukat-müvekkil gizliliği ve ticari sır gözetilir; iç hukuki değerlendirme notları ile dışa açık bildirimler ayrılır.
4. **Eylem yönlendirmesi.** İlgili kişilere somut koruyucu adımlar (şifre değişimi, kart bloke, dolandırıcılık uyarısı) ve başvuru kanalı sunulur; çalışanlara müdahale talimatı verilir.
5. **Ara sonuç.** Hangi metnin kime, hangi kanaldan, hangi zamanlamayla gideceği ve hukuki onay gereği belirlenir. İçtihat/karar atfı yapılacaksa künye doğrulanır; doğrulanmamışsa `[doğrulanacak]` işaretlenir.

## Çıktı modülleri
- Paydaş-mesaj matrisi ve zamanlama.
- İlgili kişi bilgilendirme / çalışan talimatı / yönetim brifing metinleri.
- Sade dil özeti ve hukuki onay/uyarı notu.

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
