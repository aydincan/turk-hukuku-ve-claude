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
