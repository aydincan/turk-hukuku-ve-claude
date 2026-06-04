---
name: sure-zamanasimi-takvimi
description: "Başvuru, itiraz, yıllık ücret, dava ve tazminat zamanaşımı sürelerinin hesaplanması ve takip edilmesi gerektiğinde kullanılır; hak kaybını önleyen süre disiplini için temel beceridir."
---

# Süreler ve Zamanaşımı

## Görev
Patent/faydalı model sürecindeki idari süreleri (başvuru, rüçhan, itiraz, ücret) ve dava/tazminat zamanaşımı sürelerini eksiksiz çıkarmak; hak düşürücü ve telafi edilebilir süreleri ayırmak.

## Soğuk başlangıç (intake)
1. Hangi aşamadasın: başvuru, inceleme, itiraz, tescil sonrası, dava?
2. Başvuru/rüçhan/yayım/tescil tarihleri ne?
3. Yıllık ücretler güncel mi; kaçırılan ödeme var mı?
4. Tecavüz/tazminat talebi varsa fiil ne zaman öğrenildi ve gerçekleşti?

## Denetim şeması
1. **Koruma süreleri.** Patent 20 yıl (SMK m.101), faydalı model 10 yıl; süreler başvuru tarihinden işler ve uzatılamaz. Ara sonuç: koruma hangi tarihte sona eriyor?
2. **Rüçhan süresi (SMK m.93).** Paris/PCT rüçhanı ilk başvurudan 12 ay; bu süre yenilik referans tarihini belirler ve kaçırılması telafisi güç hak kaybı doğurur.
3. **İtiraz süresi (SMK m.99).** Patent verme kararının yayımından itibaren altı ay içinde itiraz; YİDD kararına karşı iptal davası süresi (kararın tebliğinden itibaren) kanunda öngörülen süredir — kaçırılırsa idari karar kesinleşir.
4. **Yıllık ücretler (SMK m.101).** Koruma yıllık ücretin süresinde ödenmesine bağlıdır; ödenmeyen yıl için ek süre/cezalı ödeme imkânını ve hakkın düşmesini kontrol et.
5. **Tecavüz/tazminat zamanaşımı (SMK m.157).** SMK m.157, sınai mülkiyet hakkına tecavüzden doğan tazminat istemlerinde TBK m.72 zamanaşımına atıf yapar: zararı ve faili öğrenmeden itibaren iki yıl ve her halde fiilden itibaren on yıl; fiil aynı zamanda suç oluşturup ceza zamanaşımı daha uzunsa o süre uygulanır. Sürekli/yenilenen tecavüzde zamanaşımının her fiil için yeniden işlemesini değerlendir.

## Çıktı modülleri
- Aşamaya göre süre tablosu (başlangıç-bitiş-sonuç).
- Hak düşürücü / telafi edilebilir süre ayrımı.
- Yıllık ücret ödeme takvimi.
- Zamanaşımı hesabı ve uyarı notu.

## Plugin bağlamı

Bu beceri `patent-faydali-model` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
