---
name: gorev-yetki-belirleme
description: "Davanın hangi mahkemede (sulh hukuk, asliye hukuk, tüketici, iş, ticaret, aile, kadastro) ve hangi yer mahkemesinde açılacağını belirlemek; kesin yetki halleri, yetki sözleşmesi ve görevsizlik/yetkisizlik kararı sonrası dosyanın akıbeti için."
---

# Görev ve Yetki Tayini

## Görev
Davanın görevli mahkemesini ve yetkili yer mahkemesini doğru saptamak; kesin görev/yetki ile düzenleyici yetki ayrımını kurmak.

## Soğuk başlangıç (intake)
- Uyuşmazlığın konusu ve tarafları kim? (tüketici, işçi, tacir, eş, taşınmaz?)
- Dava değeri/konusu özel görevli mahkeme gerektiriyor mu?
- Davalının yerleşim yeri ve uyuşmazlık bağlantı yeri neresi?
- Geçerli bir yetki sözleşmesi var mı (tacirler/kamu tüzel kişileri arasında)?

## Denetim şeması
1. **Genel görev**: HMK m.2 uyarınca asliye hukuk mahkemesi asıl görevli; sulh hukukun görevi m.4'te sayılan işlerle (kira ilişkisinden doğan davalar dâhil belli işler, taksim, ortaklığın giderilmesi vb.) sınırlıdır.
2. **Özel görevli mahkemeler**: tüketici uyuşmazlıkları → tüketici mahkemesi (6502 sayılı Kanun); iş uyuşmazlıkları → iş mahkemesi (7036); ticari davalar → asliye ticaret mahkemesi (TTK m.4-5); aile → aile mahkemesi (4787); kadastro → kadastro mahkemesi; fikri haklar → FSHHM. Görev kamu düzenindendir, re'sen gözetilir (HMK m.1, m.114/1-c).
3. **Genel yetki**: Davalının yerleşim yeri mahkemesi (HMK m.6).
4. **Özel/seçimlik yetki**: Sözleşmeden doğan davada ifa yeri (m.10); haksız fiilde fiilin işlendiği/zararın doğduğu yer (m.16); taşınmazın aynına ilişkin davada taşınmazın bulunduğu yer **kesin yetki** (m.12).
5. **Kesin yetki halleri** sözleşmeyle değiştirilemez; **yetki sözleşmesi** (m.17-18) yalnızca tacir/kamu tüzel kişileri arasında ve kesin yetki olmayan hallerde geçerlidir.
6. **Görevsizlik/yetkisizlik kararı** (m.20): Kararın kesinleşmesinden itibaren iki hafta içinde dosyanın görevli/yetkili mahkemeye gönderilmesi istenmezse dava açılmamış sayılır — bu süre kritiktir.

Ara sonuç: "Görevli mahkeme + yetkili yer + kesin mi seçimlik mi" çıktısı.

## Çıktı modülleri
- Görevli mahkeme gerekçesi (madde atıflı).
- Yetkili yer mahkemesi seçenekleri ve kesin/seçimlik etiketi.
- Görevsizlik/yetkisizlik halinde iki haftalık gönderme uyarısı.

## Plugin bağlamı

Bu beceri `hukuk-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
