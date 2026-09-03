---
name: ticaret-unvani-ve-isletme-adi
description: "Ticaret unvaninin olusturulmasi, zorunlu/secimlik ekler, unvanin korunmasi ve unvana tecavuz; benzer unvan veya isletme adi kullanimina karsi tespit-men-tazminat talepleri gerektiginde kullanilir."
---

# Ticaret Unvanı ve İşletme Adı

## Görev
Ticaret unvanının doğru oluşturulup oluşturulmadığını denetlemek ve unvan/işletme adına yönelik tecavüze karşı koruma araçlarını kurmak. Unvan, tacirin kimliği ve ticari itibarının taşıyıcısıdır.

## Soğuk başlangıç (intake)
1. Tacir gerçek kişi mi, hangi şirket türü mü (unvan çekirdeği değişir)?
2. Mevcut unvan zorunlu unsurları taşıyor mu?
3. Çakışan/benzer unvan veya işletme adı kim tarafından kullanılıyor, hangi tarihten beri?
4. İltibas (karıştırılma) ve zarar somut mu?

## Denetim şeması
1. **Unvanın oluşturulması:** TTK m.41-46 — gerçek kişi tacirde ad-soyad çekirdek; şirketlerde tür ve faaliyet konusu zorunlu (AŞ/Ltd. ibaresi şart, m.43-44). Ek ve sıfatlar gerçeğe aykırı, yanıltıcı, kamu düzenine aykırı olamaz (m.46). Unvan Türkçe esaslı kurulur.
2. **Tek unvan ve kullanma:** Her tacirin işletmesiyle ilgili işlemlerinde unvanını kullanma zorunluluğu (TTK m.39); belgelerde unvan, sicil numarası ve internet sitesi bilgisi (m.39/2). Unvan tescil ve ilan edilir (m.40).
3. **Unvanın korunması:** TTK m.50 — usulen tescil ve ilan edilen unvanı kullanma hakkı münhasıran sahibine aittir. TTK m.52 — unvana tecavüz edilen kişi: tespit, men (engelleme), tecavüzün sonucu olan maddi durumun ortadan kaldırılması (ref), kusur varsa maddi tazminat, ağır hal varsa manevi tazminat isteyebilir. Haksız rekabet hükümleriyle (TTK m.54 vd.) yarışma mümkündür.
4. **İşletme adı:** TTK m.53 — işletme adı işletmeyi tanıtır, tescil edilince benzer şekilde korunur.
5. **İspat:** Önceki tarihli tescil/kullanım, karıştırılma ihtimali ve zarar (tazminat için) ispatlanır. Ara sonuç: zorunlu unsur eksikse unvan düzeltilir; tecavüz varsa m.52 talepleri kurulur, ihtiyati tedbir istenebilir.

## Çıktı modülleri
- Unvan uygunluk denetim notu (zorunlu/yasak unsur kontrolü).
- Tecavüz halinde m.52 talep matrisi (tespit/men/ref/tazminat).
- İhtarname ve dava dilekçesi talep sonucu taslağı.

## Plugin bağlamı

Bu beceri `ticari-isletme-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
