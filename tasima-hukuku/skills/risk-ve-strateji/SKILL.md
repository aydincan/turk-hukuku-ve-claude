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
