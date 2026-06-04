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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
