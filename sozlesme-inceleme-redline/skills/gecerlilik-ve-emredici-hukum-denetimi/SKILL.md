---
name: gecerlilik-ve-emredici-hukum-denetimi
description: "Bir maddenin veya bütün sözleşmenin emredici hükme, ahlaka veya kamu düzenine aykırı olup olmadığını, kısmi mi tam mı hükümsüz olduğunu değerlendirmek gerektiğinde kullanılır."
---

# Geçerlilik ve Emredici Hüküm Denetimi

## Görev
Sözleşme hükümlerini geçerlilik süzgecinden geçirmek; kesin hükümsüz, iptal edilebilir veya yazılmamış sayılacak kayıtları ayıklamak ve kısmi butlanın metni nasıl etkilediğini belirlemek.

## Soğuk başlangıç (intake)
- Hangi madde şüpheli; emredici bir hükmü mü aşıyor (faiz tavanı, asgari işçi hakkı, tüketici koruması)?
- Edimin konusu baştan imkânsız veya hukuka aykırı mı?
- İrade sakatlığı (hata/hile/korkutma) veya gabin belirtisi var mı?
- Sözleşme matbu/standart mı (GİK denetimi gerekir)?

## Denetim şeması
1. **Konu denetimi**: TBK m.27/f.1 — kanunun emredici hükümlerine, ahlaka, kamu düzenine, kişilik haklarına aykırı veya konusu imkânsız sözleşme kesin hükümsüzdür. Örn. ölünceye kadar rekabet yasağı kişilik hakkını aşarsa, ölçüsüz münhasırlık.
2. **Kısmi butlan**: TBK m.27/f.2 — sakatlık yalnız bazı hükümleri etkiliyorsa kural olarak diğerleri ayakta kalır; ancak bu hükümler olmadan sözleşme yapılmayacağı anlaşılırsa tamamı geçersiz. "Severability/bölünebilirlik" kaydı bu sonucu yönlendirir.
3. **GİK içerik denetimi**: TBK m.21 (şaşırtıcı/beklenmedik kayıt yazılmamış sayılır), m.24 (tek taraflı değiştirme yasağı), m.25 (dürüstlüğe aykırı, karşı tarafı ağırlaştıran kayıt geçersiz). Tüketicide TKHK m.5 ek koruma.
4. **İrade sakatlığı/gabin**: TBK m.30-39 iptal hakkı (1 yıl, m.39); m.28 gabin (aşırı yararlanma).
5. **İspat yükü**: Hükümsüzlüğü ileri süren ispatla yükümlüdür (TMK m.6); kesin hükümsüzlük hâkimce resen dikkate alınır, ileri sürülmesi süreye bağlı değildir.
6. **Ara sonuç**: Geçersiz/yazılmamış kayıtların listesi ve metnin ayakta kalan kısmı; redline öncesi temizlik haritası.

## Çıktı modülleri
- Geçersiz/iptal edilebilir/yazılmamış sayılacak madde tablosu.
- Kısmi butlan etkisi ve bölünebilirlik kaydı önerisi.
- Emredici hüküm ihlali için düzeltme veya çıkarma talebi.

## Plugin bağlamı

Bu beceri `sozlesme-inceleme-redline` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
