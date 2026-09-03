---
name: kvkk-buro-uyumu
description: "Hukuk bürosunun veri sorumlusu olarak KVKK yükümlülüklerini kurgularken; aydınlatma, saklama-imha, VERBİS, aktarım ve veri ihlali süreçlerini denetlerken kullanılır."
---

# Büro KVKK Uyumu

## Görev
Hukuk bürosunun veri sorumlusu sıfatıyla kişisel veri işleme faaliyetlerini KVKK'ya uygun hale getirmek: işleme şartı, aydınlatma, güvenlik, saklama-imha, aktarım ve ihlal yönetimi.

## Soğuk başlangıç (intake)
1. Büro hangi veri kategorilerini işliyor (müvekkil, karşı taraf, tanık, çalışan; özel nitelikli veri var mı)?
2. Veriler nerede tutuluyor (UYAP harici sistem, bulut, fiziki dosya) ve kimlerle paylaşılıyor?
3. Aydınlatma metni, saklama-imha politikası, VERBİS kaydı mevcut mu?
4. Yurt dışına veri aktarımı (yurt dışı bulut, yabancı müvekkil) var mı?

## Denetim şeması
1. **İşleme şartı (KVKK m.5-6)**: Her işleme amacı bir hukuki sebebe bağlanır — vekâlet/sözleşmenin ifası, hukuki yükümlülük, meşru menfaat; özel nitelikli veride m.6 daha katı şartlar. Avukatlık faaliyetinde işleme çoğunlukla sözleşme ifası ve hukuki yükümlülüğe dayanır; açık rıza son çare kabul edilir.
2. **Aydınlatma (KVKK m.10)**: Müvekkil ve diğer ilgili kişilere kimliği, amaç, aktarım, toplama yöntemi ve haklar bildirilir. Vekâlet ilişkisinin sır niteliği (1136 m.36) ile uyum kurulur.
3. **Güvenlik (KVKK m.12)**: Teknik/idari tedbirler — erişim yetkisi, şifreleme, fiziki dosya güvenliği, çalışan gizlilik taahhüdü.
4. **Saklama-imha**: Her veri kategorisi için saklama süresi (dava/zamanaşımı/mevzuat gerekleri) ve süre sonunda imha/anonimleştirme planı.
5. **Aktarım (KVKK m.8-9)**: Bilirkişi, mahkeme, karşı vekil, mali müşavir aktarımları amaca uygun ve hukuki sebebe bağlı; yurt dışı aktarımda m.9 rejimi.
6. **İhlal (KVKK m.12/5)**: Veri ihlalinde Kurula ve etkilenen ilgili kişiye gecikmeksizin (Kurul kararıyla 72 saat ölçütü) bildirim süreci hazır tutulur.
7. **Ara sonuç**: Her kategori için şart + aydınlatma + saklama + güvenlik karşılanmışsa uyum sağlanmıştır; eksikler boşluk listesine yazılır.

## Çıktı modülleri
- Veri işleme envanteri (kategori, amaç, hukuki sebep, saklama, alıcı).
- Aydınlatma metni ve gerekirse açık rıza metni taslağı.
- Saklama-imha politikası ve ihlal müdahale akışı.
- Uyum boşluğu raporu ve eylem planı.

## Plugin bağlamı

Bu beceri `hukuk-burosu-yonetimi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
