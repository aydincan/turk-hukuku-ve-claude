---
name: gecikme-ziya-hasar-talepleri
description: "Eşyanın geç teslimi, kaybı veya hasarı sonrası ihbar/rezerv sürelerinin tutturulması, zararın belgelenmesi ve talebin doğru muhataba yöneltilmesi gerektiğinde kullanılır; hak kaybı doğuran sürelere odaklanır."
---

# Gecikme, Ziya ve Hasar Taleplerinin Yönetimi

## Görev
Zarar olayı sonrası hak sahibinin yapması gereken ihbar/rezerv işlemlerini süresinde planlamak, zararı belgelemek ve talebi doğru taşıyıcıya yöneltmek; hak kaybını önlemek.

## Soğuk başlangıç (intake)
1. Olay ne: gecikme mi, tam/kısmi ziya mı, hasar mı; hasar açık mı gizli mi?
2. Eşya teslim alındı mı; teslim tarihi nedir; ihbar/rezerv yapıldı mı?
3. Taşıma iç hukuka mı (TTK) yoksa CMR'ye mi tabi?
4. Zarar nasıl belgelendi (tutanak, fotoğraf, ekspertiz, fatura)?

## Denetim şeması
1. **İhbar/rezerv süreleri (TTK):** TTK m.889 — açıkça belli hasarda teslim sırasında, gizli hasarda teslimi izleyen 7 gün içinde yazılı bildirim; gecikmede teslimden itibaren 21 gün içinde bildirim. Süre kaçırılırsa eşyanın doğru teslim edildiği varsayılır.
2. **İhbar/rezerv süreleri (CMR):** CMR m.30 — açık hasarda teslimde, gizli hasarda 7 gün, gecikmede 21 gün. Rezervsiz teslim, iyi teslim karinesi doğurur.
3. **Ziyanın belgelenmesi:** Tam ziya halinde teslim için kararlaştırılan sürenin (kural olarak 30 gün, sözleşmesel sürenin sonu) geçmesiyle eşya kaybolmuş sayılabilir (CMR m.20). Tutanak, ekspertiz ve değer belgeleri toplanmalı.
4. **Muhatabın belirlenmesi:** Akdî taşıyıcı, fiilî taşıyıcı (TTK m.879) ve komisyoncu (m.926-928) arasında doğru muhatap seçilmeli; müteselsil sorumluluk değerlendirilmeli.
5. **Tazminatın kapsamı:** Ziya/hasarda eşya değeri ve m.882 sınırı; CMR m.23/4 uyarınca taşıma ücreti ve masraflar.
6. **Zamanaşımı:** TTK m.855 / CMR m.32 (1 yıl; kasıt-ağır kusurda 3 yıl). Yazılı talep CMR'de süreyi durdurur (m.32/2).
7. **Ara sonuç:** Hangi taleplerin canlı, hangilerinin sürede/zamanaşımında düştüğü.

## Çıktı modülleri
- İhbar/rezerv süre takvimi ve hak kaybı uyarı listesi.
- Zarar belgeleme kontrol listesi (tutanak/ekspertiz/fatura).
- Talep mektubu taslağı (muhatap, dayanak madde, tutar, süre durdurma).

## Plugin bağlamı

Bu beceri `tasima-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
