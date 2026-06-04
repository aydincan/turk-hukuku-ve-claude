---
name: adil-yargilanma-hakki
description: "Mahkemeye erişim, gerekçeli karar, silahların eşitliği, makul sürede yargılanma, çelişmeli yargılama, masumiyet karinesi gibi adil yargılanma güvencelerinin ihlali iddia edildiğinde kullanılır."
---

# Adil Yargılanma Hakkı İhlali

## Görev
Anayasa m.36 ve AİHS m.6 kapsamındaki adil yargılanma güvencelerinden hangisinin somut olayda ihlal edildiğini tespit etmek ve kanun yolu şikâyetinden ayırmak.

## Soğuk başlangıç (intake)
- Hangi yargılamada, hangi güvence ihlal edildi (erişim, gerekçe, eşitlik, süre)?
- Mahkeme esaslı iddialarınızı/delillerinizi gerekçeyle karşıladı mı?
- Yargılama ne kadar sürdü; gecikme kime atfedilebilir?
- Şikâyetiniz sonucun yanlışlığına mı, usulün adilliğine mi ilişkin?

## Denetim şeması
1. Uygulanabilirlik — m.36: medeni hak ve yükümlülükler ile suç isnadı uyuşmazlıklarında güvence devreye girer.
2. Mahkemeye erişim — aşırı harç, katı süre/şekil yorumu, fiilî engeller erişim hakkını ölçüsüzce sınırlıyorsa ihlal doğar (m.13 ölçülülük süzgeci).
3. Gerekçeli karar hakkı — mahkeme, davanın sonucuna etkili, esaslı iddiaları karşılamak zorundadır; susulan esaslı itiraz ihlal nedeni olabilir. Her argümana ayrı yanıt aranmaz.
4. Silahların eşitliği ve çelişmeli yargılama — taraflardan birine tanınan usuli üstünlük, sunulan görüş/delile yanıt imkânının verilmemesi ihlaldir.
5. Makul süre — uyuşmazlığın karmaşıklığı, tarafların ve yargı makamlarının tutumu, başvurucu için önem ölçütleriyle değerlendirilir; yargı kaynaklı uzun gecikme ihlaldir.
6. Masumiyet karinesi ve diğer ceza güvenceleri — m.38 ile birlikte değerlendirilir.

Sınır: Delil takdiri ve hukuk kuralının yorumu kural olarak kanun yolu şikâyetidir; ancak takdir "açık keyfîlik / bariz takdir hatası" düzeyindeyse anayasal denetime girer.

İspat yükü: ihlali oluşturan usuli kusuru ve sonuca etkisini başvurucu gösterir.

Ara sonuç: ihlal edilen alt güvence(ler) ve dayanak.

## Çıktı modülleri
- İhlal edilen güvence başlıkları ve gerekçe.
- Kanun yolu şikâyeti / anayasal şikâyet ayrımı notu.
- Makul süre hesabı (varsa).
- AYM/AİHM ilke ölçütlerine atıf [doğrulanacak].

## Plugin bağlamı

Bu beceri `anayasa-mahkemesi-bireysel-basvuru` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
