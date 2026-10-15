---
name: temel-kavramlar-ve-sistematik
description: "Miras dosyasına ilk dokunuşta uygulanacak kavram haritası ve sıralama; ölüm anı, tereke, külli halefiyet, mirasçı türleri ve hangi kuralın hangi sırayla işletileceğini belirlemek gerektiğinde kullanılır."
---

# Temel Kavramlar ve Sistematik

## Görev
Miras uyuşmazlığını TMK Üçüncü Kitap sistematiğine (m.495-682) oturtmak; ölüm anı, tereke, mirasçı türleri ve analiz sırasını netleştirip doğru alt-beceriye yönlendirmek.

## Soğuk başlangıç (intake)
- Mirasbırakan ne zaman ve nerede öldü? (1.1.2002 öncesi ise eski MK uygulanır.)
- Hayatta olan yakınlar kimler? (eş, çocuk, ana-baba, kardeş, torun)
- Vasiyetname, miras sözleşmesi ya da sağlararası devir/bağış var mı?
- Tereke neleri kapsıyor? (taşınmaz, banka, şirket payı, borç)
- Talep ne? (pay alma, iptal, tenkis, ret, paylaşma)

## Denetim şeması
1. **Ölüm anını sabitle (m.575).** Miras ölümle açılır; haklar ve değerler bu ana göre belirlenir. Birlikte ölüm karinesi (m.29) gündeme gelebilir.
2. **Tereke kapsamını çıkar.** Aktif ve pasif; miras külli halefiyetle bir bütün olarak geçer (m.599). Kişiye sıkı bağlı haklar (manevi tazminat istisnaları, intifa) terekeye girmez.
3. **Mirasçı sıfatını belirle.** Yasal mirasçılık zümre sistemi (m.495-501) ve sağ kalan eşin payı (m.499) ile; atanmış mirasçı/lehine vasiyet varsa ölüme bağlı tasarrufu ayrıca incele.
4. **Mirasçılık engellerini tara.** Mirastan yoksunluk (m.578), ıskat (m.510-513), feragat sözleşmesi (m.528), ret (m.605).
5. **Saklı pay süzgecini uygula (m.505-506).** Tasarruf edilebilir oran aşılmış mı? Aşılmışsa tenkis becerisine geç.
6. **Ara sonuç:** payları kesirli olarak hesapla, çekişmeli/çekişmesiz işi ayır, görevli mahkemeyi tespit et (HMK m.2/m.4).

İspat yükü genel kurala tabidir (TMK m.6, HMK m.190): mirasçı sıfatını iddia eden soybağı/nüfus kaydıyla, tasarrufun geçersizliğini iddia eden onu ispatlar.

## Çıktı modülleri
- Mirasçı ve pay tablosu (zümre, kesir, oran)
- Tereke aktif/pasif envanteri
- Uygulanacak hukuk notu (ölüm tarihine göre MK seçimi)
- Yönlendirme: hangi alt-beceri ve hangi dava/işlem

## Plugin bağlamı

Bu beceri `miras-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
