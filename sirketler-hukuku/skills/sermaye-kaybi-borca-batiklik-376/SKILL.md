---
name: sermaye-kaybi-borca-batiklik-376
description: "Şirketin son bilançosunda sermaye ve kanuni yedeklerin yarısının ya da üçte ikisinin karşılıksız kalması veya borca batıklık (teknik iflas) ortaya çıktığında; m.376 iyileştirme tedbirlerini, YK yükümlülüklerini ve mahkemeye bildirim/konkordato seçeneklerini belirlemek için kullanılır."
---

# Sermaye Kaybı ve Borca Batıklık (TTK m.376)

## Görev
Sermaye kaybı/borca batıklık eşiğini saptamak; yönetim kurulunun çağrı, tedbir önerme ve mahkemeye bildirim yükümlülüklerini işletmek; teknik iflasa karşı iyileştirme yollarını planlamak.

## Soğuk başlangıç (intake)
1. Son yıllık/ara bilançoya göre sermaye + kanuni yedeklerin ne kadarı karşılıksız?
2. Borca batıklık şüphesi var mı (aktifler borçları karşılamıyor mu)?
3. YK genel kurulu çağırdı mı; hangi tedbirler önerildi/uygulandı?
4. Sermaye artırımı/azaltımı, sermaye taahhüdü veya borçların ertelenmesi mümkün mü?
5. Konkordato başvurusu düşünülüyor mu; alacaklı yapısı nasıl?

## Denetim şeması
1. Yarı kaybı (m.376/1): Son bilançoya göre sermaye + kanuni yedeklerin yarısı karşılıksızsa, YK genel kurulu derhal toplantıya çağırır ve iyileştirici tedbirleri sunar (bilgilendirme + öneri).
2. Üçte iki kaybı (m.376/2): Sermaye + kanuni yedeklerin üçte ikisi karşılıksızsa, genel kurul ya kalan üçte birle yetinmeye (sermaye azaltımı) ya da sermayenin tamamlanmasına/artırılmasına karar vermeli; aksi halde şirket kendiliğinden sona erer. Tamamlama akçesi ve azaltım-artırım kombinasyonu.
3. Borca batıklık (m.376/3): Aktiflerin şirket borçlarını karşılamadığı yönünde işaretler varsa YK, hem işletmenin devamlılığı esasına hem muhtemel satış değerine göre ara bilanço düzenler. Batıklık varsa YK durumu mahkemeye bildirir (iflas talebi).
4. İflasın ertelenmesi yerine: Bildirim öncesi/yerine İİK m.285 vd. konkordato yoluna gidilebilir; iyileştirme projesi ve mühlet.
5. Bağlı düzenlemeler: m.376 uygulamasına ilişkin Bakanlık tebliği (zararların mahsubu, yabancı para/kur etkilerinin değerlendirilmesi gibi geçici/idari ölçütler) güncel metinden teyit edilmeli.
6. Sorumluluk bağı: m.376 yükümlülüklerinin ihlali YK üyeleri için m.553 sorumluluğu doğurabilir.
7. İspat: Bilanço/ara bilanço ve değerleme belgeleri esas; batıklık tespiti mahkemece bilirkişi ile.

## Çıktı modülleri
- Eşik tespiti tablosu (yarı/üçte iki/borca batıklık).
- YK çağrı ve tedbir önerisi taslağı; genel kurul karar seçenekleri.
- Mahkemeye bildirim veya konkordato yol haritası.

## Plugin bağlamı

Bu beceri `sirketler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
