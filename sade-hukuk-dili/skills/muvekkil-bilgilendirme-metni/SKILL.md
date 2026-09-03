---
name: muvekkil-bilgilendirme-metni
description: "Müvekkile davanın/işin durumunu, seçeneklerini ve sonraki adımları anlatan yazılı bilgilendirme metni üretmek; aydınlatma yükümlülüğünü yalın ama eksiksiz yerine getirmek gerektiğinde kullanılır."
---

# Müvekkil Bilgilendirme ve Aydınlatma Metni

## Görev
Müvekkile sürecin neresinde olunduğunu, hangi seçeneklerin bulunduğunu, olası sonuçları ve
sonraki adımları anlatan yapılandırılmış bir bilgilendirme metni hazırlamak; vekilin aydınlatma
borcunu (TBK m.506; Avukatlık K. m.34, TBB Meslek Kuralları m.3-4) sade ama eksiksiz karşılamak.

## Soğuk başlangıç (intake)
1. İş hangi aşamada (danışma, dava açma, tahkikat, karar, icra)?
2. Müvekkile sunulacak karar/seçenek var mı (sulh, istinaf, vazgeçme)?
3. Maliyet, süre ve başarı ihtimali hakkında beklenti yönetimi gerekiyor mu?
4. Acil bir süre veya talimat alınması gereken nokta var mı?

## Denetim şeması
1. DURUM TESPİTİ: İşin bugünkü hukuki durumu yalın dille özetlenir (ne yaptık, nerede duruyoruz).
2. SEÇENEKLER VE SONUÇLARI: Her seçeneğin olası sonucu, maliyeti ve riski dengeli sunulur; vekil
   abartılı başarı vaadinden kaçınır (meslek kuralları, dürüstlük). Olasılık dili kullanılır:
   "garanti" yerine "lehimize güçlü/zayıf gerekçe".
3. SÜRE VE TALİMAT (kritik sonuç): Müvekkilin karar vermesi gereken son tarih takvimle yazılır;
   kanun yolu süreleri (örn. istinaf/temyiz iki hafta) ve hak düşürücü süreler ayrıca uyarılır.
4. MALİYET ŞEFFAFLIĞI: Vekâlet ücreti, harç, gider ve karşı vekâlet ücreti riski açıkça belirtilir;
   beklenti yönetimi yapılır.
5. ONAY/TALİMAT İZİ (ispat): Müvekkilin onayını gerektiren konularda yazılı talimat istenir; bu,
   ileride uyuşmazlıkta vekilin lehine ispat aracıdır.
6. ARA SONUÇ: Metin müvekkili yanıltıcı kesinlik içermeden, tüm seçenekleri ve süreleri kapsıyor mu.

## Çıktı modülleri
- "Bugün neredeyiz" özeti.
- Seçenekler / sonuç / maliyet / risk tablosu.
- Karar verilmesi gereken konular ve son tarih.
- Onay/talimat istenen satır ve hukuki tavsiye notu.

## Plugin bağlamı

Bu beceri `sade-hukuk-dili` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
