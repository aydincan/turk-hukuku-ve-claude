---
name: deniz-sigortasi-pandi
description: "Gemi (tekne), yük veya sorumluluk (P&I) sigortalarında riziko, beyan yükümlülüğü, tazminat ve rücu uyuşmazlıkları çıktığında; poliçe ve kulüp kuralları çerçevesinde teminat kapsamını ve sigortacının rücu hakkını değerlendirmek için kullan."
---

# Deniz Sigortası ve P&I

## Görev
Tekne, yük veya sorumluluk (P&I) sigortasında rizikonun teminat kapsamında olup olmadığını, sigortalının beyan ve özen yükümlülüklerini, tazminat hesabını ve sigortacının halefiyet/rücu hakkını değerlendirmek.

## Soğuk başlangıç (intake)
- Sigorta türü nedir (tekne/H&M, yük/kargo, sorumluluk/P&I)?
- Poliçe hangi klozlara tabi (örn. Institute Clauses) ve P&I kulüp kuralları nasıl?
- Riziko gerçekleşti mi; sebep nedir; istisna kapsamına giriyor mu?
- Sigortalı beyan ve değişiklik bildirim yükümlülüklerini yerine getirdi mi?

## Denetim şeması
1. **Sözleşme ve uygulanacak kurallar**: Deniz sigortasına TTK m.1401 vd. genel hükümleri ile poliçe/kloz ve P&I kulüp kuralları birlikte uygulanır; emredici ve düzenleyici hükümleri ayırt et.
2. **Beyan yükümlülüğü**: Sigortalının riziko sözleşme yapılırken doğru beyan ve sonradan ağırlaşmayı bildirme borcunu denetle; ihlalin sigortacıya cayma/tazminattan kaçınma hakkı verip vermediğini değerlendir.
3. **Teminat ve istisnalar**: Rizikonun teminat kapsamında olup olmadığını, klozdaki istisnaları (savaş, kötü niyet, denize elverişsizlik bilgisi) ve sigortalının özen borcunu kontrol et.
4. **Tazminat hesabı ve sovtaj**: Tam/kısmi zıya, müşterek avarya katkısı, kurtarma masrafı ve sovtaj (hurda) değerini dikkate alarak tazminatı hesapla; sigorta bedeli ile sigorta değeri ilişkisini (aşkın/eksik sigorta) uygula.
5. **Halefiyet/rücu ve ara sonuç**: Ödeme yapan sigortacı, sigortalının zarar verene karşı haklarına halef olur (TTK m.1472); P&I'da kulübün rücu ve "pay to be paid" kuralını değerlendir. Çıktıda teminat kararını ve rücu yolunu gerekçelendir; sigorta tazminatı zamanaşımına dikkat et.

## Çıktı modülleri
- Teminat/istisna değerlendirme tablosu
- Tazminat hesap taslağı (zıya türü, sovtaj, avarya)
- Rücu/halefiyet ve kulüp kuralı strateji notu

## Plugin bağlamı

Bu beceri `deniz-ticareti-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
