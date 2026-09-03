---
name: temel-kavramlar-ve-sistem
description: "Basın ve medya hukukunun temel kavramlarını, mecra türlerini ve uygulanacak rejimi belirlemek; ifade özgürlüğü ile kişilik hakkı dengesinin genel çerçevesini kurmak gerektiğinde kullanılır."
---

# Temel Kavramlar ve Sistematik

## Görev
Somut olayın hangi medya rejimine girdiğini saptamak, ifade-basın özgürlüğü (Anayasa m.26, m.28) ile kişilik hakkı (TMK m.24) ekseninde uygulanacak normları haritalamak ve doğru yol/merci seçimine zemin hazırlamak.

## Soğuk başlangıç (intake)
1. Yayın hangi mecrada çıktı: basılı eser, radyo/TV, internet haber sitesi, sosyal medya?
2. Yayın tarihi ve hâlâ erişilebilir mi (online ise URL)?
3. İçerik bir maddi vakıa iddiası mı yoksa değer yargısı/eleştiri mi?
4. Mağdur gerçek kişi mi, tüzel kişi mi, kamu görevlisi/siyasetçi mi?
5. Talep ne: düzeltme, içeriğin kaldırılması, tazminat, ceza şikâyeti?

## Denetim şeması
1. **Mecra tespiti**: Basılı/süreli yayın ise 5187 sayılı Basın Kanunu (m.2 tanımlar) devreye girer; işitsel-görsel ise 6112 sayılı Kanun; internet ise 5651 sayılı Kanun. Mecra, görevli mercii (sulh ceza hâkimliği, asliye hukuk, RTÜK) belirler.
2. **Koruma katmanı**: Her mecrada genel koruma da uygulanır — kişilik hakkı (TMK m.24-25), haksız fiil tazminatı (TBK m.49, m.58), ceza (TCK m.125 hakaret, m.134 özel hayat).
3. **Hukuka aykırılık ön süzgeci**: TMK m.24/II uyarınca üstün nitelikte özel/kamusal yarar, rıza veya kanunun verdiği yetki varsa ihlal hukuka uygun sayılır. Haber verme hakkı çerçevesinde gerçeklik, güncellik, kamu yararı ve öz-biçim dengesi aranır.
4. **Ara sonuç**: İhlal var ve hukuka uygunluk sebebi yoksa; mağdurun statüsüne (kamuya mal olmuş kişi katlanma eşiği yüksektir) göre yol/merci ve süre seçilir.

## Çıktı modülleri
- Mecra-rejim eşleştirme tablosu
- Uygulanacak normlar listesi (madde atıflı)
- Yol/merci ve süre özeti
- Bir sonraki uzman beceriye yönlendirme notu

## Plugin bağlamı

Bu beceri `basin-medya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
