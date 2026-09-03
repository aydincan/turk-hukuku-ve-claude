---
name: gorev-yetki-ve-forum
description: "Kullanıcı davayı hangi mahkemede ve hangi yerde açacağını bilmek istediğinde, sulh-asliye-tüketici ayrımı veya yetkili yer (yerleşim, sözleşme, haksız fiil yeri) sorusu gündeme geldiğinde kullanılır."
---

# Görev, Yetki ve Doğru Mahkemenin Belirlenmesi

## Görev
Davanın hangi tür mahkemede (görev) ve hangi yerdeki mahkemede (yetki) açılacağını doğru saptamak; yanlış mahkemede açıp süre ve harç kaybetmeyi önlemek.

## Soğuk başlangıç (intake)
- Uyuşmazlığın konusu ve yaklaşık değeri nedir?
- Karşı tarafın yerleşim yeri/adresi neresi?
- Bir sözleşme var mı, varsa ifa yeri neresi?
- Haksız fiil/zarar nerede gerçekleşti?
- Taşınmaz söz konusu mu?

## Denetim şeması
1. **Görev (tür):** Görev kamu düzenindendir, re'sen incelenir (HMK m.114/1-c). Sulh hukukun görevi HMK m.4'te sayılıdır (kira ilişkisinden doğan davalar, paydaşlığın/ortaklığın giderilmesi, zilyetliğin korunması, taşınır/taşınmaz teslimi). Sayılmayan işlerde genel görevli asliye hukuktur (m.2). Tüketici işlemiyse tüketici mahkemesi/hakem heyeti (6502 sayılı Kanun); iş ilişkisiyse iş mahkemesi.
2. **Yetki (yer) — genel kural:** Davalının yerleşim yeri mahkemesi (HMK m.6). Birden fazla davalı varsa herhangi birinin yerleşim yeri (m.7).
3. **Özel/seçimlik yetki:** Sözleşmeden doğan davada sözleşmenin ifa yeri (HMK m.10); haksız fiilde fiilin işlendiği veya zararın doğduğu yer (m.16); taşınmaza ilişkin ayni hak ve zilyetlik davalarında taşınmazın bulunduğu yer **kesin yetkilidir** (m.12). Tüketici, kendi yerleşim yeri tüketici hakem heyetine de başvurabilir.
4. **İspat yükü/itiraz:** Yetki itirazı, kesin yetki yoksa, ilk itiraz olarak cevap dilekçesinde ileri sürülür (HMK m.116, 117); süresinde yapılmazsa yetki kesinleşir. Görev ise her aşamada incelenir.
5. **Ara sonuç:** Görevli mahkeme türü + yetkili yer kombinasyonu netleşir; kesin yetki varsa seçimlik yetki kapanır.

## Çıktı modülleri
- Forum kararı (görevli mahkeme + yetkili yer + gerekçe maddesi).
- Alternatif yetkili yerler listesi (seçimlik yetkide).
- Yanlış forum riski ve görevsizlik/yetkisizlik kararının sonuçları (HMK m.20 süre/dosya gönderme) notu.

## Plugin bağlamı

Bu beceri `kendini-temsil-asliye` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
