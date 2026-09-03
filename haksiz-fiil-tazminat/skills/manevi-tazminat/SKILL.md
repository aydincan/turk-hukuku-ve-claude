---
name: manevi-tazminat
description: "Ölüm, bedensel bütünlüğün ihlali veya kişilik hakkı saldırısı nedeniyle manevi tazminat istenebileceğinde; talebin şartlarını, miktar ölçütlerini ve hak sahiplerini belirlemek için kullanılır."
---

# Manevi Tazminat Talebi

## Görev
Manevi zararın varlığını ve manevi tazminatın şartlarını TBK m.56 (bedensel zarar/ölüm) ve m.58 ile TMK m.24-25 (kişilik hakkı) çerçevesinde denetlemek; miktarın hakkaniyet ölçütlerini ve hak sahiplerini belirlemek. Manevi tazminat zenginleşme aracı değildir; tatmin ve denkleştirme amacı taşır.

## Soğuk başlangıç (intake)
- İhlal edilen değer ne (yaşam, beden/sağlık, onur-saygınlık, özel hayat, ad)?
- Ölüm/ağır bedensel zarar varsa yakınların durumu (eş, çocuk, ana-baba) nedir?
- Saldırının ağırlığı, süresi ve tarafların kusur durumu?
- Maddi tazminatla birlikte mi isteniyor?

## Denetim şeması
1. **Hukuki temeli seç.** Bedensel zarar/ölümde TBK m.56; kişilik hakkı ihlalinde TBK m.58 ile TMK m.24-25 birlikte uygulanır. Sözleşmeye aykırılıkta da koşulları varsa kişilik ihlali için manevi tazminat istenebilir.
2. **Şartlar.** Hukuka aykırı fiil, manevi zarar (acı, elem, üzüntü, kişiliğe saldırı) ve illiyet bağı; kusur kural olarak aranır, ancak objektif sorumluluk hallerinde içtihatla manevi tazminat da kabul edilebilir (`[doğrulanacak]`).
3. **Hak sahipleri.** Bedensel zararda doğrudan zarar gören; ölümde ve ağır bedensel zararda yakınlar (m.56/2) manevi tazminat isteyebilir. Talep kişiye sıkı sıkıya bağlıdır; kural olarak devredilmez, mirasçıya kalması sınırlıdır.
4. **Miktar ölçütleri.** Olayın özelliği, tarafların ekonomik-sosyal durumu, kusurun ağırlığı, saldırının niteliği ve ihlalin sonuçları göz önünde tutulur; somut ve gerekçeli takdir gerekir. Tek kalem, bölünmez taleptir.
5. **Birlikte istemler.** Maddi tazminat, durdurma/önleme (TMK m.25) ve özür/yayın gibi taleplerle birlikte değerlendirilir.
6. **Ara sonuç ve ispat.** Manevi zararın varlığını ve ağırlığını zarar gören ortaya koyar; miktarda hâkimin takdiri esastır. Talep sonucu makul ve gerekçeli tutulur.

## Çıktı modülleri
- Talep şartları ve hak sahibi kontrol listesi.
- Miktar gerekçe notu (ölçütler + somut olay).
- Talep sonucu paragrafı taslağı (m.56/m.58 dayanaklı).

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
