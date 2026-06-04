---
name: muteselsil-borcluluk-ve-devir
description: "Birden çok borçlunun aynı borçtan birlikte sorumlu olduğu, alacağın temlik edildiği veya borcun başkasına geçtiği durumlarda taraflar arası ilişkiyi çözmek için kullanılır."
---

# Müteselsil Borçluluk, Alacağın Devri ve Borcun Üstlenilmesi

## Görev
Birden çok borçlu/alacaklı arasındaki teselsül ilişkisini, iç-dış ilişki ve rücuyu çözmek; alacağın devri ve borcun üstlenilmesinin geçerlilik ve sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
- Borçlular birden çok mu; teselsül kararlaştırıldı mı yoksa kanundan mı doğuyor?
- Alacaklı kime, ne kadar başvurdu; ödeyen borçlunun rücu hakkı ne?
- Alacak bir başkasına devredildi mi; yazılı temlik var mı?
- Borç bir üçüncü kişiye mi geçti; alacaklının rızası alındı mı?

## Denetim şeması
1. Müteselsil borçluluğun kaynağı: TBK m.162 — teselsül ya borçluların beyanıyla ya kanunla doğar (örn. ortak haksız fiil m.61, adi şirket). Aksi belirtilmedikçe bölünebilir borçlarda teselsül karinesi yoktur.
2. Dış ilişki: m.163 — alacaklı borcun tamamını dilediği borçludan isteyebilir; biri ifa edince hepsi borçtan kurtulur. Borçluların def'ileri: ortak def'iler herkese, kişisel def'iler yalnız ilgiliye ait (m.164-165).
3. İç ilişki ve rücu: m.167 — aksi kararlaştırılmadıkça borçlular eşit pay taşır; fazlasını ödeyen, payları oranında diğerlerine rücu eder; ödeyemeyenin payı paylaştırılır. Halefiyet (m.168) ile alacaklının teminatlarına girer.
4. Alacağın devri (temlik): m.183-194 — kural olarak borçlunun rızası gerekmez; geçerlilik için yazılı şekil (m.184). Devirden önce borçluya yöneltilen def'iler yeni alacaklıya karşı da ileri sürülebilir (m.188); iyiniyetli borçlunun eski alacaklıya ifası (m.186).
5. Borcun üstlenilmesi: m.195-201 — iç üstlenme + dış üstlenme; borçlunun değişmesi alacaklının kabulüne bağlıdır (m.196). Kabule kadar iç ilişki, ret hâlinde sonuçlar; teminatların akıbeti (m.198-199).
6. İspat yükü: Teselsülü/temliki ileri süren yazılı dayanağı; rücu ve payları ödeyen borçlu ispatlar.

## Çıktı modülleri
- Teselsül haritası (dış ilişki/iç ilişki/rücu).
- Temlik veya borç üstlenme sözleşmesi taslağı iskeleti.
- Def'i ve teminat akıbeti kontrol listesi.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
