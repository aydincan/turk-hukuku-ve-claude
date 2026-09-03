---
name: ceza-ve-tazminat-sorumlulugu
description: "Kişisel verinin hukuka aykırı kaydı, ele geçirilmesi veya yok edilmemesi nedeniyle TCK suçları gündeme geldiğinde ya da ilgili kişinin uğradığı zararın tazmini istenirken kullanılır."
---

# Cezai Sorumluluk ve Tazminat

## Görev
KVKK ihlallerinin idari boyutunun ötesinde cezai (TCK m.135-140) ve özel hukuk (tazminat) sonuçlarını değerlendirmek; suç duyurusu, ceza yargılaması veya tazminat davası stratejisini kurmak.

## Soğuk başlangıç (intake)
1. Eylem nedir — verinin hukuka aykırı kaydı, başkasına verme/ele geçirme, yok etmeme?
2. Müvekkil mağdur (ilgili kişi) mu, şüpheli/sanık mı?
3. Bir zarar doğdu mu; maddi mi, manevi mi, kişilik hakkı ihlali var mı?
4. Aynı olay hem Kurul yaptırımına hem savcılık soruşturmasına konu mu?

## Denetim şeması
1. **TCK m.135 — verileri hukuka aykırı kaydetme**: Hukuka aykırı olarak kişisel veriyi kaydeden cezalandırılır; özel nitelikli veride ağırlaştırıcı hal vardır.
2. **TCK m.136 — verileri hukuka aykırı verme/ele geçirme/yayma**: Kişisel veriyi hukuka aykırı olarak başkasına veren, yayan veya ele geçiren için ceza öngörülür; m.137 nitelikli haller (kamu görevlisi, meslek sağladığı kolaylık).
3. **TCK m.138 — verileri yok etmeme**: Süresi geçtiği halde sistemde verileri yok etmeyenler cezalandırılır; bu, KVKK m.7 imha yükümlülüğünün cezai yaptırımıdır.
4. **Tazminat**: İlgili kişi, KVKK m.11/1-g'deki zararın giderilmesi talebini genel hükümlere dayanarak ileri sürer; haksız fiil (TBK m.49 vd.) ve kişilik hakkı ihlali (TMK m.24-25, TBK m.58 manevi tazminat) çerçevesinde maddi/manevi tazminat istenebilir. Görevli mahkeme kural olarak asliye hukuk mahkemesidir.
5. **Ara sonuç**: İdari, cezai ve hukuki yollar paralel işleyebilir; Kurul kararı ceza/tazminat davasında delil değeri taşır ancak bağlayıcı değildir.

İspat yükü: Suçta kast ve hukuka aykırılığı iddia makamı; tazminatta zarar, kusur ve illiyet bağını davacı ispatlar.

## Çıktı modülleri
- TCK m.135-138 unsur eşleştirme tablosu.
- Suç duyurusu veya savunma dilekçesi iskeleti.
- Maddi/manevi tazminat dava dilekçesi taslağı ve zarar kalemleri.

## Plugin bağlamı

Bu beceri `kvkk-veri-koruma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
