---
name: cevre-izin-lisans
description: "Emisyon, deşarj, gürültü gibi çevre izinleri ile geri kazanım/bertaraf lisanslarının alınması, askıya alınması veya iptaline ilişkin işlem ve uyuşmazlıklarda; EÇBS/e-Çevre süreçlerinde ve izinsiz faaliyet riski değerlendirmesinde kullan."
---

# Çevre İzin ve Lisansları

## Görev
Bir tesisin tabi olduğu çevre izni/lisansını belirlemek, başvuru ve yenileme sürecini yönetmek, izin işlemlerine veya izinsiz faaliyet yaptırımlarına karşı strateji kurmak.

## Soğuk başlangıç (intake)
1. Tesis hangi faaliyet kolunda; çevreye etki bakımından hangi sınıfta yer alıyor?
2. Hangi izin konuları gerekli: hava emisyonu, atıksu deşarjı, gürültü, derin deniz deşarjı, tehlikeli madde?
3. Geçici faaliyet belgesi veya çevre izni/lisansı mevcut mu; süresi/yenileme durumu?
4. İdari yaptırım (durdurma, para cezası) uygulandı mı?

## Denetim şeması
1. **Yükümlülüğün kaynağı**: 2872 m.11 ve m.12, faaliyet sahibine arıtma/önleme ve izin yükümlülüğü yükler. Çevre İzin ve Lisans Yönetmeliği tesisleri çevresel etkilerine göre sınıflandırır ve izin konularını belirler.
2. **Süreç**: Başvuru EÇBS/e-Çevre üzerinden yapılır; geçici faaliyet belgesi sonrası belirli sürede çevre izni alınması gerekir. Süreye uyulmaması belgenin iptali ve faaliyet durdurma sonucunu doğurabilir.
3. **İzinsiz faaliyet sonucu**: 2872 m.15 faaliyetin durdurulmasını, m.20-23 idari para cezalarını öngörür; izinsiz deşarj/emisyon ağırlaştırıcıdır.
4. **İşleme itiraz**: İznin verilmemesi, askıya alınması veya iptali ile durdurma/ceza kararları idari işlemdir; iptal davası 2577 sayılı İYUK'a tabidir (süre kural olarak 60 gün, yürütmenin durdurulması talep edilebilir).
5. **İspat ve ara sonuç**: Ölçüm raporları, emisyon/deşarj analizleri ve EÇBS kayıtları esastır; usulüne uygun olmayan numune/ölçüm ceza işlemini sakatlayabilir.

## Çıktı modülleri
- İzin/lisans kapsam tablosu (konu + dayanak)
- Başvuru/yenileme yol haritası ve süre takvimi
- İzin işlemine veya durdurma kararına karşı dava iskeleti
- Ölçüm/numune usul denetimi notu

## Plugin bağlamı

Bu beceri `cevre-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
