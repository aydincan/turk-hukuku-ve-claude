---
name: nisap-oy-ve-karar-alma
description: "Genel kurulda toplanti ve karar yetersayilari, agirlastirilmis nisaplar, oyda imtiyaz, oydan yoksunluk ve toplantinin ertelenmesi konularinda hesap ve denetim yapilacaksa kullanilir."
---

# Toplantı Nisabı, Oy ve Karar Alma

## Görev
Genel kurulda toplantı ve karar yetersayılarını doğru hesaplamak; ağırlaştırılmış nisapları, oyda imtiyazı ve oydan yoksunluğu denetleyerek kararın geçerli alınıp alınmadığını belirlemek.

## Soğuk başlangıç (intake)
1. Karar konusu olağan bir karar mı, esas sözleşme değişikliği mi, m.421'in özel nisap gerektiren hâllerinden biri mi (tür değiştirme, tabiiyet değişikliği, pay senetleri devrinin sınırlanması vb.)?
2. Esas sözleşmede ağırlaştırılmış nisap var mı?
3. Oyda imtiyazlı pay veya oydan yoksunluk doğuran ilişki (m.436) söz konusu mu?
4. İlk toplantıda nisap sağlandı mı; ikinci toplantı yapıldı mı?

## Denetim şeması
1. **Genel nisap:** Kanun veya esas sözleşmede aksi öngörülmedikçe GK, sermayenin **en az dörtte birini** karşılayan payların sahipleriyle toplanır; bu nisap toplantı süresince korunur. İlk toplantıda sağlanamazsa ikinci toplantıda nisap aranmaz (m.418). Kararlar, toplantıda hazır bulunan oyların çoğunluğuyla alınır.
2. **Ağırlaştırılmış nisaplar:** m.421 belirli esas sözleşme değişiklikleri için özel nisaplar getirir; örneğin bilanço zararlarının kapatılması için ek ödeme/yükümlülük, tabiiyet/merkez değişikliği gibi hâllerde **oybirliği** veya nitelikli çoğunluk aranır. Konu hangi fıkraya giriyorsa o fıkranın nisabı uygulanır; yanlış nisap iptal sebebidir.
3. **Oyda imtiyaz ve yoksunluk:** Oyda imtiyaz m.479 sınırları içinde geçerlidir (esas sözleşme değişikliği, ibra ve sorumluluk davasında imtiyaz kullanılamaz — m.479/3). Pay sahibi, kendisi/eşi/alt-üstsoyu ile şirket arasındaki kişisel nitelikli işlerde ve ibra/sorumlulukta oy kullanamaz (m.436).
4. **Erteleme:** Finansal tabloların müzakeresi, azlığın talebiyle bir ay sonraya ertelenir (m.420); bu hak gündeme bağlılıktan bağımsızdır.
5. **İspat yükü/ara sonuç:** Nisabın varlığı hazır bulunanlar listesi (m.415) ve tutanakla (m.422) ispatlanır. Nisap hatası, oydan yoksun payların oya katılması veya imtiyazın yasak alanda kullanılması kararı iptale açar; bazı temel ihlaller (sermayenin korunması) butlana gidebilir.

## Çıktı modülleri
- Nisap hesap tablosu (toplantı + karar nisabı, ilk/ikinci toplantı).
- m.421 konu-nisap eşleştirme cetveli.
- Oydan yoksunluk/imtiyaz uygunluk notu.

## Plugin bağlamı

Bu beceri `anonim-sirket-genel-kurul` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
