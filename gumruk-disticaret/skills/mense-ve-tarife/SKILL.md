---
name: mense-ve-tarife
description: "Eşyanın menşeinin belirlenmesi, tercihli/tercihsiz menşe, GTİP sınıflandırması, menşe ispat belgeleri ve ek mali yükümlülük ihtilaflarında; menşe ve tarife eksenli ek tahakkuk ve önlemleri analiz etmek için kullanılır."
---

# Menşe, Tarife Sınıflandırma ve Tercihli Ticaret

## Görev
Eşyanın menşeini ve tarife pozisyonunu (GTİP) doğru saptamak; tercihli menşe iddialarını, menşe ispat belgelerini ve menşe/sınıflandırma kaynaklı ek tahakkuk ile ticaret politikası önlemlerini (antidamping, EMY, korunma) değerlendirmek.

## Soğuk başlangıç (intake)
- Beyan edilen menşe ülke ve GTİP nedir; hangi ispat belgesi sunuldu (EUR.1, A.TR, menşe şahadetnamesi, fatura beyanı)?
- Tercihli tarife mi talep edildi; uygulanan anlaşma hangisi?
- Eşya antidamping, ek mali yükümlülük veya korunma önlemi kapsamında mı?
- İdarenin tespiti menşe değişikliği mi, GTİP değişikliği mi, belge geçersizliği mi?

## Denetim şeması
1. Tercihsiz menşe (m.18-21): Tamamen bir ülkede elde edilen eşya o ülke menşelidir; birden çok ülke katkısı varsa "son esaslı, ekonomik bakımdan haklı işçilik veya işlem" ölçütü uygulanır (m.19). Bu ölçüt antidamping/EMY için belirleyicidir.
2. Tercihli menşe: İlgili STA/Gümrük Birliği kuralları ve menşe protokolleri uygulanır. A.TR Gümrük Birliği'nde serbest dolaşım belgesidir, menşe ispatı değildir; EUR.1/EUR-MED ve fatura beyanı tercihli menşe ispatıdır. Belge geçerli, süresinde ve usulüne uygun olmalı.
3. Sonradan kontrol: Menşe belgelerinin doğruluğu ihracatçı ülke idaresi nezdinde sonradan kontrole tabidir; olumsuz/teyitsiz sonuç tercihli oranın geri alınmasına ve ek tahakkuka yol açar.
4. Tarife sınıflandırma: GTİP, Armonize Sistem İzahnamesi ve Genel Yorum Kuralları ile belirlenir. Tereddütte BTB (Bağlayıcı Tarife Bilgisi) başvurusu yapılır; BTB sahibini ve idareyi bağlar.
5. İspat yükü: Tercihli oran iddiasında bulunan yükümlü geçerli menşe ispat belgesini ve menşe kurallarına uygunluğu ortaya koyar; idare reddini somut sonradan kontrol sonucu veya teknik tespitle gerekçelendirir.
6. Ara sonuç: Doğru menşe, GTİP ve uygulanacak oran ile önlem belirlenir; ek tahakkuk ve ceza riskinin hukuki dayanağı saptanır. İlkesel içtihat için Danıştay 7. Daire kararlarına bakılabilir [doğrulanacak].

## Çıktı modülleri
- Menşe/GTİP analiz notu ve belge geçerlilik kontrolü
- Sonradan kontrol cevabına itiraz taslağı
- BTB başvuru taslağı (gerekirse)

## Plugin bağlamı

Bu beceri `gumruk-disticaret` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
