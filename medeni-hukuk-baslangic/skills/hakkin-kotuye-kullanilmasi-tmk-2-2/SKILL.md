---
name: hakkin-kotuye-kullanilmasi-tmk-2-2
description: "Lafzen haklı görünen bir talep veya savunma somut olayda hakkaniyete açıkça aykırı düştüğünde; çelişkili davranış, hakkın geç kullanılması, salt zarar verme veya menfaat dengesizliği iddiası gündeme geldiğinde TMK m.2/2 süzgecini uygulamak için kullanılır."
---

# Hakkın Kötüye Kullanılması Yasağı (TMK m.2/2)

## Görev
Bir hakkın kullanımının somut olayda açıkça kötüye kullanma teşkil edip etmediğini denetlemek ve "bir hakkın açıkça kötüye kullanılmasını hukuk düzeni korumaz" sonucunu (TMK m.2/2) gerekçelendirmek.

## Soğuk başlangıç (intake)
- Hangi hak/yetki kullanılıyor ve karşı taraf hangi davranışı kötüye kullanma sayıyor?
- Hak sahibi daha önce aksi yönde davranıp güven yarattı mı (çelişkili davranış)?
- Hak çok geç mi kullanılıyor; karşı tarafta haklı bir güven oluştu mu?
- Hakkın kullanımında meşru bir menfaat var mı, yoksa salt zarar verme mi?

## Denetim şeması
1. **Önce hakkı tespit et** — TMK m.2/2 mevcut bir hakkın kullanımını sınırlar; önce hakkın varlığı ve kapsamı özel normla belirlenir. Süzgeç, kuralın sonucunu düzeltir.
2. **"Açıkça" eşiği** — Her dengesizlik değil, yalnızca *açık* kötüye kullanma korunmaz. Eşik yüksektir; sıradan menfaat çatışması yetmez.
3. **Tipoloji** — (a) Çelişkili davranış (*venire contra factum proprium*); (b) hakkın çok geç kullanılması ve yaratılan güvene aykırılık; (c) meşru menfaat yokluğu / salt başkasına zarar verme; (d) edimler arası aşırı oransızlık; (e) kendi hukuka aykırı davranışından yarar sağlama; (f) hakkın amacından saptırılması.
4. **İspat** — TMK m.6 / HMK m.190: kötüye kullanmayı iddia eden ispatla yükümlüdür. Ancak açık kötüye kullanma kamu düzenini ilgilendirdiğinden hâkimce re'sen gözetilebilir.
5. **Sonuç ve ölçülülük** — Açıkça kötüye kullanılan hak korunmaz: talep reddedilir, def'i etkisizleşir veya hak sınırlanır. Hakkın tümden düşürülmesi son çaredir; ölçülü ve gerekli olanla yetinilir.
6. **m.3 ile fark** — m.2/2 davranış denetimi, m.3 bilgisizliğin (iyiniyet) korunmasıdır; karıştırılmaz.

## Çıktı modülleri
- Hakkın tespiti + kötüye kullanma tipi eşleştirmesi.
- Güven/çelişki kronolojisi (tarih sırasıyla).
- "Açıklık" eşiği değerlendirmesi.
- Sonuç önerisi (ret/sınırlama) + ilkesel içtihat `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `medeni-hukuk-baslangic` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
