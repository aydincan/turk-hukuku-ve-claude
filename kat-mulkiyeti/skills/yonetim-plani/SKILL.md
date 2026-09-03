---
name: yonetim-plani
description: "Sitenin anayasası niteliğindeki yönetim planının düzenlenmesi, bir hükmünün yorumlanması, değiştirilmesi ya da yönetim planına aykırı uygulamaların tartışılması gündeme geldiğinde; bağlayıcılık, değişiklik nisabı ve emredici KMK hükümleriyle sınır için kullanılır."
---

# Yönetim Planı — İçerik, Değişiklik ve Yorum

## Görev
Anagayrimenkulün yönetimini düzenleyen yönetim planının hukuki niteliğini, bağlayıcılığını ve içerik sınırlarını belirlemek; bir hükmün yorumu, değiştirilmesi veya plana aykırı uygulama uyuşmazlıklarını çözmek.

## Soğuk başlangıç (intake)
- Yürürlükteki yönetim planı tapuya tescilli mi; tarihi ve son değişikliği nedir?
- Uyuşmazlık planın bir hükmünün anlamına mı, plana aykırı bir uygulamaya mı, yoksa plan değişikliğine mi ilişkin?
- Tartışılan konu KMK'nın emredici bir hükmüyle (örn. oybirliği gereken haller) çelişiyor mu?
- Plan değişikliği için gerekli nisap sağlanmış mı; karşı çıkan malik var mı?

## Denetim şeması
1. **Hukuki nitelik (KMK m.28)**: Yönetim planı, anagayrimenkulün yönetim tarzını, kullanma maksat ve şeklini, yönetici ve denetçilerin alacağı ücreti ve yönetime ilişkin diğer hususları düzenleyen **sözleşme** niteliğinde belgedir. Bütün kat maliklerini, onların külli/cüzi haleflerini ve yöneticileri bağlar (m.28/1).
2. **Bağlayıcılık ve aleniyet**: Yönetim planı ve değişiklikleri, bağımsız bölüm maliklerini bağlamak için tapu kütüğüne işlenir; sonradan malik olanlar da bilgisi olmasa dahi bağlıdır.
3. **Değişiklik nisabı (m.28/3)**: Yönetim planının değiştirilmesi için **bütün kat maliklerinin beşte dördünün (4/5) oyu** şarttır. Bu nitelikli çoğunluk sağlanmadan yapılan değişiklik geçersizdir; aykırılık karar iptali yoluyla ileri sürülür.
4. **Emredici hükümlerle sınır**: Yönetim planı KMK'nın emredici hükümlerine aykırı düzenleme getiremez. Örneğin oybirliği aranan haller (m.19/2 anataşınmazda değişiklik, m.44 ilave inşaat, m.45 ortak yer devri) plan ile çoğunluğa indirilemez.
5. **Yorum yöntemi**: Plan hükmü TMK m.1-2 ve sözleşme yorumu ilkeleriyle (dürüstlük kuralı, amaçsal yorum) yorumlanır; açık hüküm yoksa KMK'nın tamamlayıcı hükümleri uygulanır.
6. **Ara sonuç**: Hüküm geçerli ve bağlayıcı mı; değişiklik 4/5 nisabını sağlıyor mu; aykırı uygulama için karar iptali/eksikliğin giderilmesi (m.33) gerekli mi?

## Çıktı modülleri
- Yönetim planı hüküm analizi ve yorum notu.
- Değişiklik için nisap (4/5) ve usul kontrol listesi.
- Emredici hükümle çatışma taraması ve geçersizlik değerlendirmesi.

## Plugin bağlamı

Bu beceri `kat-mulkiyeti` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
