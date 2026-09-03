---
name: karar-iptal-davasi
description: "Kanuna, esas sozlesmeye veya durustluk kuralina aykiri bir genel kurul kararinin iptali istenecekse; davaci sifati, uc aylik sure, yetkili-gorevli mahkeme ve teminat konularinda strateji ve dilekce gerektiginde kullanilir."
---

# Genel Kurul Kararının İptali Davası

## Görev
Sakat bir genel kurul kararına karşı iptal davasını kurgulamak; davacı sıfatını, süreyi, görev-yetkiyi denetleyip dava dilekçesi iskeletini hazırlamak.

## Soğuk başlangıç (intake)
1. Karar tarihi nedir; üç aylık süre ne zaman dolar?
2. Davacı toplantıda hazır mıydı; muhalefet şerhi tutanağa geçti mi?
3. İptal sebebi kanuna mı, esas sözleşmeye mi, dürüstlük kuralına mı aykırılık?
4. Karar tescil edilmiş mi; yürütmenin geri bırakılması (kararın icrasının ertelenmesi) gerekiyor mu?

## Denetim şeması
1. **Sebep:** İptal sebebi, kararın **kanuna, esas sözleşmeye ya da dürüstlük kuralına aykırı** olmasıdır (m.445). Önce butlan/yokluk ihtimalini ele; salt iptal edilebilir sakatlık varsa m.445 yolu işletilir.
2. **Davacı sıfatı (m.446):** (a) toplantıda hazır bulunup karara olumsuz oy verip **muhalefetini tutanağa geçirten** pay sahibi; (b) toplantıya çağrının/gündemin usulsüzlüğü, yetkisiz kişilerin katılması gibi hâllerde hazır olup olmadığına bakılmaksızın pay sahibi; (c) yönetim kurulu; (d) kararın icrası YK üyelerinin sorumluluğunu doğuracaksa her bir YK üyesi.
3. **Süre:** İptal davası, **karar tarihinden itibaren üç ay** içinde açılır; bu süre hak düşürücüdür, re'sen gözetilir (m.445). Süre kaçırılmışsa yalnızca butlan/yokluk ileri sürülebilir.
4. **Görev-yetki:** Görevli mahkeme **asliye ticaret mahkemesi** (TTK m.5/1); yetkili mahkeme şirket **merkezinin** bulunduğu yerdir (m.448/1). Dava şirkete karşı açılır.
5. **Usul (m.448-449):** Mahkeme davayı YK'ye bildirir, ilan ettirir; YK'nin görüşünü alır. Mahkeme, davacıların muhtemel kötüniyetli davranışlarından doğacak zarar için **teminat** isteyebilir (m.448). Şartları varsa kararın icrası geri bırakılabilir.
6. **Etki (m.450):** İptal/butlan kararı kesinleşince **bütün pay sahipleri** hakkında hüküm doğurur; YK kararı tescil ve ilan ettirir.
7. **İspat yükü/ara sonuç:** İptal sebebini ve davacı sıfatı şartlarını (muhalefet şerhi vb.) davacı ispatlar. Süre veya sıfat eksikse dava reddedilir; bu hâlde butlan/yokluk değerlendirilir.

## Çıktı modülleri
- İptal davası dava dilekçesi iskeleti (vakıa-hukuki sebep-talep sonucu).
- Süre ve davacı sıfatı kontrol listesi.
- Teminat ve icranın geri bırakılması talep notu.

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
