---
name: tacir-sifati-ve-sonuclari
description: "Bir kisinin tacir sayilip sayilmadigini ve tacir olmaya bagli yukumluluk ve ayricaliklari (basiretli davranma, faiz, fatura itirazi, ucret/ceza indirimi isteyememe) belirlemek gerektiginde kullanilir."
---

# Tacir Sıfatı ve Hukuki Sonuçları

## Görev
Müvekkilin veya karşı tarafın tacir olup olmadığını saptamak ve buna bağlanan yükümlülük ile ayrıcalıkları somut olaya uygulamak. Tacir sıfatı, ispat yükünden faiz oranına, sorumluluktan görevli mahkemeye kadar zincirleme etki doğurur.

## Soğuk başlangıç (intake)
1. Kişi gerçek kişi mi, tüzel kişi mi; ticaret siciline kayıtlı mı?
2. Bir ticari işletmeyi kendi adına mı işletiyor (kısmen de olsa)?
3. Esnaf mı, yoksa esnaf sınırını aşan tacir mi?
4. Uyuşmazlık fatura, faiz, ceza indirimi veya basiret yükümüyle mi ilgili?

## Denetim şeması
1. **Gerçek kişi tacir:** TTK m.12/1 — ticari işletmeyi kısmen de olsa kendi adına işleten kişi tacirdir. TTK m.12/3: işletmeyi açtığını ilan eden veya sicile kaydettiren, fiilen işletmese de tacir gibi sorumlu olur (tacir gibi sorumluluk). Küçük/kısıtlı adına işletme: TTK m.13.
2. **Tüzel kişi tacir:** Ticaret şirketleri (kollektif, komandit, AŞ, ltd., kooperatif) ticari işletme işletmese de tacir sayılır; TTK m.16 ayrıca amacına varmak için ticari işletme işleten dernek ve kamu tüzel kişilerini kapsar. Devlet, il, belediye gibi kamu tüzel kişileri kural olarak tacir sayılmaz (m.16/2).
3. **Tacir olmanın sonuçları (yükümlülük):** Basiretli iş adamı gibi davranma (TTK m.18/2); ticaret unvanı seçme ve kullanma; ticari defter tutma (m.64); iflasa tabi olma; ihbar/ihtarların şekli (m.18/3 — noter, taahhütlü mektup, telgraf, KEP).
4. **Tacir olmanın sonuçları (ayrıcalık/karine):** Ücret ve faiz isteme hakkı (TTK m.20); fatura ve teyit mektubuna 8 gün içinde itiraz edilmezse içeriğin kabul sayılması (m.21); aşırı ücret/ceza koşulunun indirilmesini isteyememe (TTK m.22 — tacir olan borçlu fahiş cezai şartın indirilmesini TBK m.182'ye dayanarak isteyemez); müteselsil sorumluluk karinesi (m.7).
5. **İspat:** Tacir sıfatını iddia eden ispatlar; ticaret sicili kaydı güçlü karine sağlar (m.36). Ara sonuç: sıfat tespit edildikten sonra ilgili her özel hüküm tek tek uygulanır.

## Çıktı modülleri
- Tacir sıfatı tespit notu (dayanak madde + sicil kaydı).
- Sıfata bağlı yükümlülük/ayrıcalık kontrol listesi.
- Karşı tarafa karşı kullanılabilecek karineler (m.7, m.21, m.22).

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
