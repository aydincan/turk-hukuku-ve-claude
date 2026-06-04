---
name: temel-kavramlar-ve-sistem
description: "Bir hukuki metni sadeleştirme işine başlamadan önce sade dilin temel ilkelerini, anlama-aktarma-doğrulama katmanlarını ve hukuki doğruluğu koruma sınırlarını kurmak gerektiğinde kullanılır."
---

# Sade Dilin Temel İlkeleri ve Sistematiği

## Görev
Sade hukuk dili işinin yöntemsel temelini kurmak: bir metnin neden, kim için ve hangi düzeyde
sadeleştirileceğini belirlemek; anlama-aktarma-doğrulama katmanlarını uygulayıp hukuki doğruluğu
korumak. Bu beceri, sonraki tüm sadeleştirme işlerinin altlığını verir.

## Soğuk başlangıç (intake)
1. Sadeleştirilecek belge nedir (dilekçe, mahkeme kararı, sözleşme, ihtarname, bilirkişi raporu)?
2. Okuyucu kim (müvekkil, karşı taraf, tanık, hukukçu olmayan yönetici, tüketici)?
3. Amaç ne (bilgilendirme, karar verdirme, onay alma, itiraz hazırlığı)?
4. İstenen düzey: tam çeviri mi, kısa özet mi, terim sözlüğü mü?
5. Bağlayıcı/asıl metin elinizde mi; eksik bilgi var mı?

## Denetim şeması
1. ANLAMA: Kaynak metnin hukuki iskeleti çıkarılır — hangi norm (madde/fıkra ile), hangi süre,
   hangi şart, hangi sonuç, hangi risk. Sadeleştirmeden önce metin hukuken doğru anlaşılmalıdır.
   Vekilin aydınlatma borcu (TBK m.506; Avukatlık K. 1136 s. m.34) bu doğruluğu zorunlu kılar.
2. KİTLE VE DÜZEY: Okuyucuya göre düzey seçilir. Tüketici metinlerinde anlaşılırlık aynı zamanda
   uyum ölçütüdür (TKHK m.4-5; genel işlem koşullarında TBK m.20-23).
3. AKTARMA: Tek fikir-tek cümle, etken çatı, kısa paragraf; jargon ilk geçtiği yerde parantezle
   açıklanır; süreler takvim tarihiyle somutlanır.
4. NÜANS KORUMA (ispat/anlam yükü): Koşullu ifadeler ("…hâlinde", "…koşuluyla") mutlaklaştırılmaz;
   "zamanaşımı" ile "hak düşürücü süre", "fesih/iptal/dönme", "müteselsil sorumluluk" gibi
   terimler açıklanır ama yanlış eşanlamlıyla değiştirilmez.
5. DOĞRULAMA (ara sonuç): Sade metin kaynakla satır satır karşılaştırılır; düşen hak, süre, şart
   veya çekince var mı denetlenir. Anlamı değiştiren basitleştirme geri alınır.
6. İSTİSNA: Hukuki kesinlik gerektiren bağlayıcı belgelerde (icra emri, ihtarname tebliği) sade
   metin yalnızca açıklayıcı eşlik metni olur; asıl metnin yerini almaz.

## Çıktı modülleri
- Sadeleştirme brifi: belge künyesi, okuyucu, düzey.
- Katman notları: anlaşılan hukuki iskelet (madde atıflarıyla).
- Sade metin + korunması gereken terimler listesi.
- Doğrulama kontrol satırı ve "[doldurulacak]" yer tutucuları.

## Plugin bağlamı

Bu beceri `sade-hukuk-dili` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
