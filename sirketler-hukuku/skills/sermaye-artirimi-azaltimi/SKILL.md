---
name: sermaye-artirimi-azaltimi
description: "Anonim veya limited şirkette esas/kayıtlı sermaye artırımı, rüçhan hakkı, ayni sermaye, sermaye azaltımı ve alacaklıların korunması işlemleri planlanırken; usul, nisap ve tescil adımlarını eksiksiz kurmak için kullanılır."
---

# Sermaye Artırımı ve Azaltımı

## Görev
Sermaye işleminin türünü (artırım/azaltım, esas/kayıtlı sermaye) saptamak; gerekli kararları, nisapları, rüçhan ve alacaklı koruma adımlarını ve tescili doğru sıralamak.

## Soğuk başlangıç (intake)
1. İşlem artırım mı azaltım mı; AŞ kayıtlı sermaye sisteminde mi?
2. Artırım nakdî mi, ayni mi, iç kaynaktan mı (fonların sermayeye eklenmesi)?
3. Önceki sermayenin tamamı ödendi mi (artırım ön şartı)?
4. Rüçhan hakkı sınırlanacak mı; gerekçesi var mı?
5. Azaltımda amaç (zarar kapatma / sermaye iadesi) ve alacaklı durumu ne?

## Denetim şeması
1. Esas sermaye artırımı (AŞ): m.456-458; genel kurul kararı ve esas sözleşme değişikliği; mevcut payların bedellerinin tamamen ödenmiş olması kural (m.456/1, istisnalar). Nakdî/ayni artırım m.456, m.342-343 atfı.
2. Kayıtlı sermaye sistemi: tavan içinde YK kararıyla artırım m.460; halka açık olmayanlarda Bakanlık izni ve esas sözleşme yetkisi.
3. Rüçhan hakkı: m.461 — her pay sahibi yeni payları mevcut oranıyla alma hakkına sahip; sınırlama ancak haklı sebeple ve nitelikli nisapla (m.461/2), eşit işlem ilkesi.
4. İç kaynaktan artırım: m.462 (yedekler/fonlar); bilanço ve denetim raporu şartı.
5. Sermaye azaltımı: m.473-475 — alacaklılara çağrı ve alacakların temini (m.474); zarar sebebiyle azaltımda çağrı muafiyeti (m.474/3); azaltımla eşzamanlı artırım m.473/2.
6. Ltd.: artırım m.590-591 atfı (AŞ hükümleri uygulanır); azaltım m.592.
7. Tescil/ilan ve sıra: Karar → (gerekiyorsa) bilirkişi raporu/denetim → ödeme → tescil. İşlem tescille hüküm ifade eder.
8. İspat: Nisap ve ödeme belgeleri şirkette; rüçhan ihlali iddiası pay sahibince.

## Çıktı modülleri
- Sermaye işlemi adım planı ve nisap tablosu.
- Genel kurul/YK karar taslağı (rüçhan, ayni değerleme notlu).
- Alacaklı çağrısı/azaltım takvimi.

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
