---
name: risk-ve-strateji
description: "Taşıma uyuşmazlığında dava/uzlaşma yolu seçimi, sorumluluk sınırının kalkma ihtimali, tahsil ve sigorta-rücu olasılıklarının tartılması ve müvekkile yön gösterilmesi gerektiğinde kullanılır."
---

# Risk Değerlendirmesi ve Strateji

## Görev
Taşıma uyuşmazlığında müvekkilin pozisyonunu (lehte/aleyhte) tartmak, sorumluluk sınırı ve tahsil riskini değerlendirip dava, uzlaşma veya sigorta yoluna ilişkin strateji önermek.

## Soğuk başlangıç (intake)
1. Müvekkil yük sahibi/sigortacı mı yoksa taşıyıcı/komisyoncu mu?
2. Talep tutarı sorumluluk sınırının (m.882/CMR m.23) üstünde mi?
3. Kasıt/pervasızlık (m.886 / CMR m.29) iddiasını destekleyen olgu var mı?
4. Geçerli nakliyat/CMR sigortası var mı; rücu zinciri ne?

## Denetim şeması
1. **Sorumluluk eksenli risk:** Olayın objektif sorumluluk (TTK m.875) kapsamına girip girmediği; kurtuluş sebeplerinin (m.876, m.878) güçlü olup olmadığı.
2. **Sınırın belirleyiciliği:** Talep, kg x 8,33 SDR sınırını aşıyorsa, m.886/CMR m.29 (kasıt-pervasızlık) ispatlanmadıkça aşkın kısım tahsil edilemez. Bu nedenle sınırın kalkması ihtimali dava değerini belirler.
3. **Sürelerin etkisi:** İhbar/rezerv ve 1/3 yıllık zamanaşımı (m.855/CMR m.32) — kaçırılmış süre aleyhe ağır risk; durdurma imkânları değerlendirilir.
4. **Tahsil/sigorta:** Taşıyıcının mali durumu, CMR/sorumluluk sigortası kapsamı; sigortacının halefiyetle rücu (TTK m.1472) hattı.
5. **Çözüm yolu seçimi:** Dava şartı arabuluculuğun zorunlu olduğu (TTK m.5/A) dikkate alınarak; tutar, kanıt gücü ve süre baskısına göre sulh/arabuluculuk veya dava önerisi.
6. **Senaryo analizi:** İyimser/kötümser/olası senaryolarda tahsil edilebilir tutar aralığı ve maliyet (harç, ekspertiz, vekâlet).
7. **Ara sonuç:** Önerilen yol, gerekçesi ve müvekkile sunulacak risk haritası.

## Çıktı modülleri
- Lehte/aleyhte olgu ve risk matrisi.
- Beklenen değer/senaryo tablosu (sınırlı vs. sınırsız sorumluluk).
- Strateji notu (arabuluculuk/sulh/dava) ve sonraki adım listesi.

## Plugin bağlamı

Bu beceri `tasima-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
