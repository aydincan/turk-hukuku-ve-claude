---
name: durustluk-kurali-ve-hakkin-kotuye-kullanilmasi
description: "Lafzen haklı görünen bir talep ya da savunma somut olayda hakkaniyete aykırı düştüğünde; çelişkili davranış, hakkın geç kullanılması veya menfaat dengesizliği iddiası gündeme geldiğinde TMK m.2 süzgecini uygulamak için kullanılır."
---

# Dürüstlük Kuralı ve Hakkın Kötüye Kullanılması

## Görev
Bir hakkın kullanımının ya da bir yükümlülüğün TMK m.2 dürüstlük kuralıyla bağdaşıp bağdaşmadığını denetlemek ve hakkın açıkça kötüye kullanılmasının hukuk düzenince korunmayacağı sonucunu gerekçelendirmek.

## Soğuk başlangıç (intake)
- Hangi hak/yetki kullanılıyor ve karşı taraf hangi davranışın dürüstlüğe aykırı olduğunu söylüyor?
- Talep sahibi daha önce aksi yönde davranıp güven yaratmış mı (venire contra factum proprium)?
- Hak çok geç mi kullanılıyor; karşı tarafta haklı bir güven oluştu mu?
- Talebin lafzî dayanağı (sözleşme maddesi/kanun hükmü) nedir?

## Denetim şeması
1. **Önce kural, sonra korrektif** — TMK m.2 bağımsız bir talep kaynağı değil, mevcut hak/borcun kullanımını sınırlayan tamamlayıcı süzgeçtir. Önce hakkın varlığı ve kapsamı kuralla tespit edilir.
2. **Dürüstlük ölçütü** — Aynı durumdaki dürüst ve makul kişinin davranışı esas alınır; sözleşmenin boşlukları dürüstlük kuralıyla doldurulur, yan yükümlülükler (sadakat, özen, koruma, bilgilendirme) buradan doğar.
3. **Kötüye kullanma tipleri** — (a) Çelişkili davranış (*venire contra factum proprium*); (b) hakkın çok geç kullanılması ve yaratılan güvene aykırılık; (c) hakkı kullanmakta meşru menfaatin yokluğu, salt zarar verme; (d) menfaatler arası aşırı oransızlık; (e) kendi hukuka aykırılığından yarar sağlama.
4. **İspat** — TMK m.6 uyarınca kötüye kullanmayı iddia eden ispatla yükümlüdür; ancak hâkim açık kötüye kullanmayı re'sen gözetir (kamu düzeni boyutu).
5. **Sonuç** — Açıkça kötüye kullanılan hak korunmaz: talep reddedilir, def'i etkisizleşir veya hak sınırlanır; hakkın tümden düşmesi istisnadır, ölçülülük gözetilir.
6. **İyiniyetle ilişki** — TMK m.2 (dürüstlük, davranış kuralı) ile TMK m.3 (iyiniyet, bir hakkın kazanılmasında bilgisizliğin korunması) karıştırılmaz.

## Çıktı modülleri
- Hakkın tespiti + kötüye kullanma tipi eşleştirmesi.
- Güven/çelişki kronolojisi.
- İspat yükü dağılımı.
- Sonuç önerisi (ret/sınırlama) + ilkesel içtihat `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `hukuk-metodolojisi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
