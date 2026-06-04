---
name: gaiplik-olum-karinesi
description: "Bir kişi uzun süredir kayıpsa, ölüm tehlikesi içinde kaybolmuşsa ya da kişiliğin/ölümün ispatı sorun olduğunda gaiplik kararı veya nüfusa ölüm kaydı için kullanılır."
---

# Gaiplik ve Ölüm Karinesi

## Görev
Kayıp bir kişinin hukuki durumunu belirlemek: ölüm tehlikesi içinde kaybolma veya uzun süreli haber alınamama hâllerinde gaiplik kararı (TMK m.32 vd.) almak ya da ölüm karinesi/ölü olarak kaydı (TMK m.31, m.44) için doğru yolu kurmak.

## Soğuk başlangıç (intake)
- Kişi ölüm tehlikesi içinde mi (deprem, sel, kaza, savaş) kayboldu, yoksa uzun süredir haber mi alınamıyor?
- Son haberin/kaybın üzerinden ne kadar zaman geçti?
- Cesedi bulunamamasına rağmen ölümünde kuşku yok mu (ölüm karinesi), yoksa belirsizlik mi var (gaiplik)?
- Talebi kim yapıyor; miras, evlilik, sigorta gibi hangi hak buna bağlı?

## Denetim şeması
1. **Ölüm karinesi** — TMK m.31: bir kimse ölümüne kesin gözle bakılmayı gerektiren durumlar içinde (ör. cesedi bulunamasa da) kaybolursa, gerçekten ölmüş gibi mirası açılır; nüfusa ölü kaydı için mahkeme/idari işlem gerekir (m.44).
2. **Gaiplik sebepleri** — TMK m.32: ölüm tehlikesi içinde kaybolan veya kendisinden uzun süre haber alınamayan ve ölümü hakkında kuvvetli olasılık bulunan kişinin, hakları ölümüne bağlı olanların başvurusuyla gaipliğine karar verilir.
3. **Süreler** — TMK m.33: ölüm tehlikesi içinde kaybolmada en az **bir yıl**, son haberden itibaren en az **beş yıl** geçmesi gerekir. Mahkeme ilanla araştırma yapar; bir yıl içinde haber gelmezse gaiplik kararı verir.
4. **Görev ve yetki** — TMK m.32/2: gaiplik kararı, kişinin son yerleşim yeri ya da Türkiye'deki son yerleşim yeri mahkemesinden istenir; asliye hukuk mahkemesi görevlidir.
5. **Sonuçlar** — Gaiplik kararıyla miras gaipliğe (kaybolma/son haber tarihine) göre açılır; mirasçılar teminat gösterir (TMK m.35). Evlilik kendiliğinden sona ermez; sona erdirme için ayrı talep/karar gerekir (TMK m.131).

## Çıktı modülleri
- Karine mi gaiplik mi ayrımı + dayanak.
- Süre hesabı (kayıp/son haber tarihinden itibaren).
- Başvuru iskeleti (görevli/yetkili mahkeme, ilan talebi, sonuç).
- Bağlı hak notu (miras açılışı, sigorta, evlilik) ve `[doldurulacak]` tarih yerleri.

## Plugin bağlamı

Bu beceri `kisiler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
