---
name: tapu-sicili-ve-iptal-tescil
description: "Tapu kaydının gerçek hak durumunu yansıtmadığı (yolsuz tescil, sahtecilik, muvazaa, hata) hâllerde; tapu iptali ve tescil davası, tescile güven ilkesi ile iyiniyetli üçüncü kişinin korunması ve şerhlerin etkisi için kullanılır."
---

# Tapu Sicili, Tescile Güven ve Tapu İptali-Tescil

## Görev
Tapu kaydı ile gerçek hak durumu arasındaki çelişkiyi gidermek: yolsuz tescili düzelttirmek (tapu iptali ve tescil) ya da tescile güvenerek hak kazanmış iyiniyetli üçüncü kişiyi savunmak.

## Soğuk başlangıç (intake)
- Tapu kaydı şu an kimin adına; müvekkil gerçek hak sahibi olduğunu hangi sebebe dayandırıyor (miras, satış, muvazaa, sahtecilik)?
- Yolsuz tescilden sonra taşınmaz üçüncü bir kişiye devredildi mi; bu kişi iyiniyetli mi?
- Kayıt üzerinde şerh/beyan/ipotek var mı?
- Talep edilen: iptal-tescil mi, tazminat mı, yoksa her ikisi mi?

## Denetim şeması
1. **Sicilin gücü**: Tapu kaydı doğruluk karinesi taşır (TMK m.7, m.992); ayni haklar tescille doğar ve aleniyet kazanır (m.1021 vd.).
2. **Yolsuz tescil (m.1024-1025)**: Geçerli bir hukuki sebebe dayanmayan veya bağlayıcı olmayan işlemle yapılan tescil yolsuzdur. Gerçek hak sahibi, kaydın düzeltilmesini (tapu iptali ve tescil) isteyebilir (m.1025).
3. **Tescile güven ilkesi (m.1023)**: Tapu kaydına iyiniyetle güvenerek ayni hak kazanan üçüncü kişinin kazanımı korunur. Bu durumda gerçek hak sahibinin aynen iadesi mümkün olmaz; tazminata yönelir.
4. **İyiniyetin sınırı (m.3)**: Üçüncü kişi, durumun gerektirdiği özeni göstermemişse veya yolsuzluğu biliyor/bilmesi gerekiyorsa m.1023 korumasından yararlanamaz. Sahtecilik, vekâlette yetki aşımı, muvazaa iddialarında iyiniyet titizlikle denetlenir [ilkeler için karararama.yargitay.gov.tr].
5. **Şerh ve beyanlar**: Kişisel hakların şerhi (örn. satış vaadi, kira) bu hakları ayni etki kazandırarak sonraki maliklere ileri sürülebilir kılar (m.1009 vd.).
6. **Devletin sorumluluğu**: Tapu sicilinin tutulmasından doğan zararlardan Devlet kusursuz sorumludur (m.1007).
7. **Ara sonuç**: İyiniyetli kazanım yoksa iptal-tescil; varsa gerçek hak sahibi için tazminat (gerekirse m.1007 yolu).

## Çıktı modülleri
- Tapu iptali ve tescil dava dilekçesi iskeleti (kayıt bilgisi, sebep, talep).
- İyiniyet/üçüncü kişi koruması değerlendirme tablosu.
- Tedbir talebi notu (kaydın devrini önleyici ihtiyati tedbir / m.1010 şerh).
- Yetki: HMK m.12 (taşınmazın yeri).

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
