---
name: zilyetlik-ve-korunmasi
description: "Tapu veya mülkiyet ispatı olmaksızın fiilî hâkimiyetin gasp ya da saldırı ile bozulduğu durumlarda; zilyetlik karinesi, gaspta geri alma, saldırıyı durdurma davaları ve kısa hak düşürücü süreler için kullanılır."
---

# Zilyetlik ve Zilyetliğin Korunması

## Görev
Mülkiyet ispatına girmeden, eşya üzerindeki fiilî hâkimiyetin (zilyetliğin) gasp veya saldırı yoluyla bozulmasına karşı hızlı koruma sağlamak; zilyetlik karinelerini ve dava yollarını işletmek.

## Soğuk başlangıç (intake)
- Müvekkil eşyayı fiilen elinde mi tutuyordu; doğrudan mı dolaylı zilyet mi (kiraya vermiş, emanet etmiş)?
- Zilyetlik nasıl bozuldu: zorla/gizlice alındı (gasp) mı, yoksa tecavüz/rahatsız etme (saldırı) mı?
- Fiili ve faili ne zaman öğrendi; üzerinden ne kadar süre geçti?
- Müvekkil sadece zilyetliğe mi dayanmak istiyor, yoksa mülkiyet de ispatlanabilir mi?

## Denetim şeması
1. **Zilyetliğin tanımı**: Eşya üzerinde fiilî hâkimiyet (TMK m.973). Aslî/fer'î, doğrudan/dolaylı zilyetlik ayrımı husumeti belirler.
2. **Karineler**: Taşınır zilyedi onun maliki sayılır (m.985); önceki zilyet de o sıradaki malik karinesinden yararlanır (m.986). Bu karineler ispat yükünü tersine çevirir.
3. **Gasptan korunma (m.981-982)**: Zilyetliği gasp edilen kişi kuvvet kullanarak (m.981) ya da dava yoluyla eşyayı geri isteyebilir; taşınmazda el koyanı çıkarıp yeniden zilyet olabilir (m.982).
4. **Saldırının önlenmesi (m.983)**: Zilyetliğine saldırılan, saldırının önlenmesini ve sebebinin giderilmesini isteyebilir.
5. **Hak düşürücü süre (m.984)**: Dava, fiilin ve failin öğrenilmesinden başlayarak 2 ay ve her hâlde fiilden itibaren 1 yıl içinde açılmalıdır. Bu süre kesin olup re'sen gözetilir.
6. **Sınır**: Zilyetlik davasında hakkın esası (mülkiyet) tartışılmaz; yalnızca fiilî durum korunur. Esasa ilişkin iddialar ayrı dava (istihkak/el atma) gerektirir.
7. **Ara sonuç**: Süre içindeyse hızlı koruma (geri verme/saldırının durdurulması); süre geçmişse mülkiyete dayalı dava yoluna geçiş.

## Çıktı modülleri
- Zilyetlik davası dilekçesi iskeleti ve süre uyarısı (2 ay / 1 yıl).
- Gasp/saldırı nitelendirme tablosu.
- Mülkiyet davasına geçiş için köprü notu.

## Plugin bağlamı

Bu beceri `esya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
