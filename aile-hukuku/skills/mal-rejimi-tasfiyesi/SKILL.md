---
name: mal-rejimi-tasfiyesi
description: "Edinilmiş mallara katılma rejiminin tasfiyesi, katılma alacağı ve değer artış payı hesabı, mal gruplarının ayrıştırılması ve sözleşmesel rejimlerin sonuçları gerektiğinde kullanılır; boşanmadan ayrı bir dava olarak kurgulanır."
---

# Mal Rejimi Tasfiyesi ve Katılma Alacağı

## Görev
Sona eren mal rejimini tasfiye etmek; mal gruplarını ayırmak, katılma alacağı (TMK m.231, m.236) ve değer artış payını (m.227) hesaplamak, aile konutu ve tasfiyenin usulünü belirlemek.

## Soğuk başlangıç (intake)
1. Evlenme tarihi ve mal rejimi türü nedir (yasal/sözleşmesel)?
2. Rejim hangi tarihte ve nasıl sona erdi (dava tarihi, ölüm, sözleşme)?
3. Hangi mallar var: taşınmaz, araç, banka hesabı, şirket payı, SGK/birikim?
4. Mal alımları kişisel mi (miras/bağış) yoksa edinilmiş gelirle mi finanse edildi?

## Denetim şeması
1. **Rejim ve sona erme tarihi.** Yasal rejim edinilmiş mallara katılmadır (m.202). Tasfiyede mal varlıkları rejimin **sona erdiği andaki** durumlarına göre, değerleri ise **tasfiye/karar anına** göre belirlenir (m.225, m.227, m.235). Sona erme tarihi genellikle boşanma dava tarihidir (m.225/2).
2. **Mal gruplarının ayrılması.** Her eşin kişisel malları (m.220: miras/bağış yoluyla gelenler, manevi tazminat, kişisel kullanım eşyası) ile edinilmiş malları (m.219: çalışma karşılığı edinimler, sosyal güvenlik edimleri, kişisel malların gelirleri) ayrıştırılır. İspatlanamayan mal edinilmiş sayılır (m.222).
3. **Hesap kalemleri.** Eklenecek değerler (karşılıksız kazandırmalar, mal kaçırma — m.229), denkleştirme (m.230), değer artış payı (m.227: bir eşin diğerinin malına katkısı), artık değer ve **katılma alacağı = artık değerin yarısı** (m.231, m.236). Katılma alacağında zamanaşımı ve faiz başlangıcı (m.239) gözetilir.
4. **Aile konutu ve tasarruf.** Aile konutu şerhi ve eşin rızası (m.194); konutun/ev eşyasının sağ kalan veya hak sahibi eşe özgülenmesi (m.240, m.279).
5. **Ara sonuç.** Bilanço (kişisel/edinilmiş ayrımı) + katılma alacağı tutarı + dava türü (alacak/aynileştirme) raporlanır. Tasfiye boşanmadan **ayrı dava** olup boşanma kesinleşmeden hüküm kurulamaz (talep edilse de bekletici mesele).

## Çıktı modülleri
- Mal envanteri ve kişisel/edinilmiş tasnif tablosu.
- Katılma alacağı / değer artış payı hesap çizelgesi.
- Tasfiye dava dilekçesi için talep sonucu ve delil (tapu, banka, SGK kaydı) listesi.

## Plugin bağlamı

Bu beceri `aile-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
