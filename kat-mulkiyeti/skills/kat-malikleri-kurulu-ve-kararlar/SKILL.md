---
name: kat-malikleri-kurulu-ve-kararlar
description: "Kat malikleri kurulunun olağan/olağanüstü toplanması, çağrı usulü, toplantı ve karar yeter sayılarının hesabı ile hangi kararların oybirliği gerektirdiğinin belirlenmesi gerektiğinde; geçerli bir karar üretmek veya bir kararın usulen sakatlığını saptamak için kullanılır."
---

# Kat Malikleri Kurulu — Toplantı, Çağrı ve Nisaplar

## Görev
Kat malikleri kurulunun usulüne uygun toplanmasını ve geçerli karar almasını sağlamak; çağrı, toplantı ve karar nisaplarını doğru hesaplamak; oybirliği gerektiren istisnaî halleri ayırmak. Aynı şema, alınmış bir kararın usul sakatlığını tespit etmek için de kullanılır.

## Soğuk başlangıç (intake)
- Toplantı olağan mı (yılda bir, plana göre) yoksa olağanüstü mü; kim çağırdı?
- Çağrı tüm maliklere, toplantı tarihinden en az 15 gün önce, gündemle birlikte yapıldı mı (m.29)?
- İlk toplantıda yeter sayı (sayı + arsa payı çoğunluğu) sağlandı mı; sağlanmazsa ikinci toplantı yapıldı mı?
- Alınacak/alınan karar oybirliği gerektiren bir konu mu?

## Denetim şeması
1. **Toplanma (KMK m.29)**: Kurul, yönetim planında belirlenen zamanda, belirlenmemişse yılda bir kez toplanır; önemli sebeplerle yöneticinin, denetçinin veya maliklerin 1/3'ünün istemiyle olağanüstü toplanır. Çağrı, toplantıdan en az 15 gün önce, gündemi de belirterek bütün maliklere imza/taahhütlü mektupla bildirilir.
2. **Toplantı yeter sayısı (m.30)**: Kurul, kat maliklerinin **sayı ve arsa payı bakımından yarısından fazlasıyla** (çift çoğunluk) toplanır ve aynı çoğunlukla karar alır. İlk toplantıda nisap yoksa, ikinci toplantı (en geç 15 gün sonra) **katılanların salt çoğunluğuyla** karar verebilir (m.30/3); yönetici seçiminde benzer kolaylık vardır.
3. **Karar yeter sayısı**: Kural çift çoğunluktur (m.32). Ancak istisnalar: anataşınmazın bir hakla kısıtlanması/eklenmesi, faydalı yenilikler m.42 (sayı+arsa payı çoğunluğu / lüks yeniliklerde ilgili maliklerin katılımı), yönetim planı değişikliği 4/5 (m.28).
4. **Oybirliği gereken haller**: Anagayrimenkulün mimari/estetik durumunu etkileyen değişiklikler ve ortak yerlerde inşaat-onarım dışı esaslı değişiklik (m.19/2), ortak yer üzerinde ayni hak/ilave kat (m.44), ortak yerin bir kat malikine tahsisi/devri (m.45) **bütün kat maliklerinin oybirliğini** gerektirir.
5. **Temsil ve oy**: Her malik arsa payına bakılmaksızın bir oy hakkına sahiptir; bir kişinin birden çok bağımsız bölümü varsa her bölüm için oy kullanır, ancak oyların 1/3'ünü geçemez (m.31). Vekâletle temsil mümkündür (m.31/son).
6. **Ara sonuç**: Çağrı + nisap + doğru karar yeter sayısı tamsa karar geçerli; eksikse karar iptali (m.33) gündemde.

## Çıktı modülleri
- Çağrı ve gündem şablonu (15 gün, imza/taahhütlü).
- Nisap hesap tablosu (sayı / arsa payı / oybirliği taraması).
- Toplantı tutanağı ve karar defteri iskeleti.
- Usul sakatlığı kontrol listesi (iptal davasına köprü).

## Plugin bağlamı

Bu beceri `kat-mulkiyeti` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
