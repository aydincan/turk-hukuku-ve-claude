---
name: ozet-cikarma
description: "Uzun bir dava dosyasını, bilirkişi raporunu, sözleşmeyi veya yazışma zincirini hukukçu olmayan bir karar verici için kısa, yalın ve doğru yönetici özetine indirgemek gerektiğinde kullanılır."
---

# Belge Özeti ve Yönetici Özeti Çıkarma

## Görev
Uzun ve teknik bir hukuki belgeyi (dosya, rapor, sözleşme, yazışma) hukukçu olmayan bir okuyucunun
hızlıca kavrayacağı kısa bir yönetici özetine indirgemek; kritik bilgiyi düşürmeden, gereksiz
ayrıntıyı eleyerek.

## Soğuk başlangıç (intake)
1. Özetlenecek belge ve uzunluğu?
2. Karar verici kim ve özetten ne bekliyor (onay, risk değerlendirmesi, durum bilgisi)?
3. İstenen uzunluk (yarım sayfa, bir sayfa)?
4. Vurgulanması gereken karar noktaları var mı?

## Denetim şeması
1. ÇEKİRDEK BİLGİYİ AYIR: Belgeden taraf/konu, talep/sonuç, kritik tarih-süre, parasal büyüklük ve
   risk çıkarılır; bunlar özetin omurgasıdır ve asla düşürülmez.
2. PİRAMİT DİZİLİŞ: Sonuç/öneri en üste, gerekçe altına, ayrıntı en sona konur (ters piramit).
3. KARAR NOKTALARINI İŞARETLE: Okuyucunun aksiyon alması gereken hususlar (imza, onay, süre,
   bütçe) ayrıca belirginleştirilir.
4. DOĞRULUK SÜZGECİ (ispat/sadakat): Özet, kaynaktaki hiçbir şartı veya çekinceyi yanlış
   mutlaklaştırmaz; sayılar ve süreler kaynakla birebir doğrulanır.
5. BELİRSİZLİK İŞARETİ: Kaynakta açık olmayan veya teyit gereken noktalar "[doğrulanacak]" /
   "[doldurulacak]" ile bırakılır, tahminle doldurulmaz.
6. ARA SONUÇ: Özet, karar verici için yeterli ve doğru mu; kritik bir tarih/tutar/risk atlanmış mı.

## Çıktı modülleri
- Tek paragraf yönetici özeti (sonuç önce).
- Anahtar bilgiler tablosu (taraflar / konu / tutar / kritik tarih / risk).
- Karar/aksiyon noktaları listesi.
- Ayrıntı için asıl belgeye yönlendirme ve "[doğrulanacak]" notları.

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
