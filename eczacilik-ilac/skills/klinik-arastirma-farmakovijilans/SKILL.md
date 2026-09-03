---
name: klinik-arastirma-farmakovijilans
description: "Klinik araştırma izinleri, gönüllü onamı, etik kurul ve advers etki/farmakovijilans yükümlülükleri ile bunlara bağlı sorumluluk konularında kullanılır."
---

# Klinik Araştırma ve Farmakovijilans

## Görev
Klinik araştırmanın izin, etik ve gönüllü koruması boyutlarını ve ruhsat sahibinin farmakovijilans (advers etki izleme) yükümlülüklerini denetlemek.

## Soğuk başlangıç (intake)
- Konu klinik araştırma izni/yürütülmesi mi, yoksa pazardaki ürünün advers etki bildirimi mi?
- Araştırmada faz, etik kurul onayı, gönüllü bilgilendirilmiş onamı durumu nedir?
- Farmakovijilansta: ciddi advers etki bildirim süresi kaçırıldı mı, PSUR/risk yönetim planı var mı?
- TİTCK denetimi/yaptırımı veya gönüllü zararı iddiası var mı?

## Denetim şeması
1. **Dayanak.** İlaç ve Biyolojik Ürünlerin Klinik Araştırmaları Hakkında Yönetmelik ve İyi Klinik Uygulamaları kılavuzu; farmakovijilans için ilgili TİTCK düzenlemesi; etik temelde Anayasa m.17 (kişinin maddi-manevi varlığı, rızası olmadan deneye tabi tutulamama).
2. **Klinik araştırma denetimi.** TİTCK izni + etik kurul onayı + geçerli bilgilendirilmiş gönüllü onamı zorunlu. Ara sonuç: üç katman da tamam mı; onam aydınlatma ölçütünü karşılıyor mu?
3. **Gönüllü koruması ve sorumluluk.** Gönüllü sigortası, zarar halinde tazminat; haksız fiil sorumluluğu (TBK m.49 vd.) ve aydınlatma kusuru değerlendirilir.
4. **Farmakovijilans yükümlülüğü.** Ruhsat sahibinin ciddi advers reaksiyonları süresinde bildirme, PSUR/PBRER ve risk yönetim planı sunma yükümlülüğü; ihlalde TİTCK idari yaptırımı (birel işlem → İYUK m.7).
5. **Eşgüdüm.** İhlal hem idari yaptırım hem ürün sorumluluğu (zarar gören hasta) doğurabilir; süreçler ayrı yürür.

## Çıktı modülleri
- İzin/etik/onam üçlü uygunluk kontrol listesi.
- Farmakovijilans yükümlülük takvimi ve eksik bildirim analizi.
- Yaptırıma karşı dava veya tazminat değerlendirme notu.

## Plugin bağlamı

Bu beceri `eczacilik-ilac` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
