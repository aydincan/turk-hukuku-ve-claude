---
name: uyusmazlik-yetki-ve-tahkim-sarti
description: "Uygulanacak hukuk, yetkili mahkeme, tahkim şartı ve arabuluculuk klozlarının geçerliliğini ve müvekkil için elverişliliğini incelemek gerektiğinde kullanılır."
---

# Uyuşmazlık Çözümü, Yetki ve Tahkim Şartı

## Görev
Sözleşmenin uyuşmazlık mimarisini (uygulanacak hukuk, yetkili mahkeme, tahkim/arabuluculuk) denetlemek; klozların geçerliliğini ve müvekkil açısından elverişliliğini değerlendirmek.

## Soğuk başlangıç (intake)
- Taraflar tacir/kamu tüzel kişisi mi (yetki sözleşmesi geçerliliği için)?
- Yabancılık unsuru var mı (milletlerarası tahkim/uygulanacak hukuk)?
- Metin mahkeme mi, tahkim mi öngörüyor; nerede, hangi kurumda?
- Dava şartı arabuluculuk kapsamında bir uyuşmazlık mı (ticari/işçi-işveren/kira)?

## Denetim şeması
1. **Yetki sözleşmesi**: HMK m.17 — yetki sözleşmesi yalnızca **tacirler veya kamu tüzel kişileri** arasında geçerlidir; tüketici/işçi gibi zayıf tarafla yapılan yetki kaydı geçersizdir. Münhasır/seçimlik yetki ayrımı (m.17/f.2) ve kesin yetki halleri kontrol edilir.
2. **Tahkim şartı**: HMK m.412 vd. — tahkim sözleşmesi yazılı şekle tabidir (m.412/f.3), uyuşmazlık tahkime elverişli olmalıdır (m.408: taşınmaz ayni hakları ve iki tarafın iradesine tabi olmayan işler tahkime elverişsiz). Tüketici uyuşmazlıklarında tahkim şartı zayıf tarafı bağlamada sakıncalıdır. Milletlerarası tahkimde 4686 sayılı Kanun.
3. **Tahkim klozunun yeterliliği**: Kurum (ISTAC/ICC), yer, dil, hakem sayısı, uygulanacak usul ve esas hukuku net mi? "Patolojik" (belirsiz/çelişik) tahkim şartı işaretlenir.
4. **Uygulanacak hukuk**: Yabancılık unsuru varsa MÖHUK serbest seçim; emredici hükümler (kamu düzeni) saklı.
5. **Arabuluculuk**: Ticari (TTK m.5/A), işçi-işveren ve kira uyuşmazlıklarında **dava şartı arabuluculuk** zorunluluğu (6325 ve ilgili kanunlar) hatırlanır; sözleşmesel ihtiyari arabuluculuk basamağı eklenebilir.
6. **Ara sonuç**: Müvekkil için elverişli forum mu; kloz icra edilebilir mi, değiştirilmeli mi?

## Çıktı modülleri
- Uyuşmazlık mimarisi değerlendirme notu (geçerlilik + elverişlilik).
- Önerilen yetki/tahkim/arabuluculuk lafzı (kurum-yer-dil-hukuk net).
- Patolojik kloz uyarısı ve düzeltme önerisi.

## Plugin bağlamı

Bu beceri `sozlesme-inceleme-redline` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
