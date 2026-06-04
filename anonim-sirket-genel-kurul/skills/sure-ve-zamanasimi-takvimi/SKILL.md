---
name: sure-ve-zamanasimi-takvimi
description: "Genel kurul cevresindeki hak dusurucu sureler, ilan-toplanti araligi, iptal davasi suresi, olagan toplanti suresi ve ilgili tescil sureleri hesaplanacak ve takvimlenecekse kullanilir."
---

# Süre ve Zamanaşımı Takvimi

## Görev
Genel kurul sürecindeki tüm kritik süreleri tespit edip kronolojik takvime dökmek; özellikle hak düşürücü iptal süresini ve usul sürelerini kaçırma riskini önlemek.

## Soğuk başlangıç (intake)
1. Hangi tarihler kesin (ilan, toplantı, karar, tescil)?
2. Sorun toplantı öncesi planlama mı, açılmış/açılacak dava süresi mi?
3. Süre hesabında esas alınacak başlangıç olayı net mi (karar tarihi mi, tescil mi)?
4. Resmî tatil/adli tatil süreyi etkiliyor mu?

## Denetim şeması
1. **İlan-toplantı aralığı:** Çağrı ilanı ile toplantı günü arasında **en az iki hafta** bulunmalıdır (m.414); ilan günü hesaba katılmaz. Bu süreye uyulmaması iptal sebebidir.
2. **Olağan toplantı süresi:** Olağan GK, her faaliyet dönemi sonundan itibaren **üç ay** içinde yapılır (m.409/1). Aşılması kararı tek başına sakatlamaz ama YK sorumluluğu doğurabilir.
3. **İptal davası süresi:** İptal davası **karar tarihinden itibaren üç ay** içinde açılır (m.445); hak düşürücüdür, re'sen gözetilir, durmaz/kesilmez. Bu sürenin kaçırılması yalnızca butlan/yokluk yolunu bırakır (bunlar süresizdir).
4. **Azlık çağrı talebi:** Azlığın çağrı/gündem talebine YK'nin **yedi iş günü** içinde olumlu cevap vermemesi mahkemeye başvuru hakkını doğurur (m.411-412).
5. **Erteleme:** Finansal tabloların müzakeresi azlık talebiyle **bir ay** ertelenir (m.420).
6. **Tescil:** Tescile tabi kararlar için YK tescil ve ilan ödevini gecikmeksizin yerine getirir; tescil tarihi, üçüncü kişilere karşı hüküm doğurma ve aleniyet bakımından esastır.
7. **İspat yükü/ara sonuç:** Sürenin başlangıç olayını (karar/ilan tarihi) ileri süren taraf belgeyle gösterir. Adli tatilde HMK m.104 vd. uygulanır; hak düşürücü sürelerin adli tatille uzayıp uzamadığı somut olayda denetlenir.

## Çıktı modülleri
- Kronolojik süre takvimi (olay-tarih-norm-son gün).
- Hak düşürücü süre uyarı panosu (iptal 3 ay).
- Kaçırılan süre senaryosunda alternatif yol (butlan/yokluk) notu.

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
