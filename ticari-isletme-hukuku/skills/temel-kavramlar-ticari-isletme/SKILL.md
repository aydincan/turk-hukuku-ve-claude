---
name: temel-kavramlar-ticari-isletme
description: "Bir uyusmazlik veya islemde ticari isletme, ticari is, tacir ve ticari hukum kavramlarinin yerini belirlemek; hangi norm rejiminin (TTK ozel hukum mu, TBK genel hukum mu) uygulanacagini cozmek gerektiginde kullanilir."
---

# Temel Kavramlar ve Sistematik

## Görev
Olayı doğru nitelendirip uygulanacak hukuku belirlemek: iş ticari mi, taraflar tacir mi, hangi norm rejimi devreye girer? Bu nitelendirme faiz türünü, müteselsil sorumluluğu, ispatı ve görevli mahkemeyi belirlediğinden tüm ticari işletme analizinin giriş kapısıdır.

## Soğuk başlangıç (intake)
1. Taraflar kim; gerçek kişi mi, ticaret şirketi mi, esnaf mı?
2. İşin konusu nedir (mal/hizmet alımı, kredi, kefalet, rekabet ihlali)?
3. Bir ticari işletmeyi ilgilendiriyor mu, yoksa kişisel/tüketici işlemi mi?
4. Yazılı sözleşme, fatura, cari hesap var mı?

## Denetim şeması
1. **Ticari işletme var mı?** TTK m.11: esnaf faaliyeti sınırını aşan, gelir sağlamayı hedefleyen, bağımsız ve sürekli faaliyet. Esnaf sınırı için ilgili kararnameye bak; sınır altı faaliyet TTK Birinci Kitap dışındadır.
2. **İş ticari mi?** TTK m.3: Kanunda düzenlenen işler + bir ticari işletmeyi ilgilendiren işler ticari iştir. TTK m.19/2: taraflardan biri için ticari olan iş, kural olarak diğeri için de ticari sayılır (ticari iş karinesi). İstisna: kanunda aksi öngörülmüş haller.
3. **Taraf tacir mi?** Gerçek kişide TTK m.12 (ticari işletmeyi kısmen de olsa kendi adına işleten); tüzel kişide ticaret şirketleri ve TTK m.16'daki diğer kuruluşlar. Donatma iştiraki ayrıca tacir sayılır.
4. **Norm sırası (TTK m.1/2):** ticari hüküm (TTK ve diğer ticari kanunlar) → ticari örf ve âdet (TTK m.2) → TBK/TMK genel hükümler. İspat yükü: ticari iş ve tacir sıfatını ileri süren ispatlar; ticaret siciline tescil görünüşe güven doğurur (TTK m.36-37).
5. **Ara sonuç:** Tacir + ticari iş ise; basiretli davranma yükümü (TTK m.18/2), müteselsil sorumluluk karinesi (TTK m.7), ticari faiz (TTK m.8-9), fatura/teyit rejimi (TTK m.21) ve görevli ticaret mahkemesi (TTK m.4, m.5/A arabuluculuk) devreye girer.

## Çıktı modülleri
- Nitelendirme tablosu: taraf-sıfat / iş niteliği / uygulanacak norm rejimi.
- Sonuç doğuran etkiler listesi (faiz, sorumluluk, görev, süre).
- Karşı tarafın nitelendirmeye itiraz argümanları ve cevap.

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
