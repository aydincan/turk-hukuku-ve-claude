---
name: gorev-yetki-yargi-yolu
description: "Fikri-sınai bir davada hangi mahkemenin (FSHM, asliye hukuk, Ankara FSHM) görevli, hangi yerin yetkili olduğunu, hukuk-ceza-idari yol ayrımını ve TÜRKPATENT aleyhine dava merkezini belirlemek gerektiğinde kullanılır."
---

# Görev, Yetki ve Yargı Yolu

## Görev
Davayı doğru mahkemede, doğru yerde ve doğru yargı kolunda açmak; görevsizlik/yetkisizlik riskini ve TÜRKPATENT kararlarına karşı dava merkezini netleştirmek.

## Soğuk başlangıç (intake)
- Talep tecavüz/tazminat mı, hükümsüzlük mü, yoksa TÜRKPATENT (YİDK) kararının iptali mi?
- Karşı taraf gerçek/tüzel kişi mi, TÜRKPATENT mi?
- Tecavüz fiili nerede gerçekleşti veya etkisi nerede görüldü; davalının yerleşim yeri neresi?
- Bulunduğunuz yerde ihtisas FSHM var mı?

## Denetim şeması
1. Görev: Fikri-sınai hukuk uyuşmazlıkları Fikrî ve Sınaî Haklar Hukuk Mahkemesi'nde görülür (SMK m.156/1; FSEK m.76). İhtisas mahkemesi bulunmayan yerde HSK'nın görevlendirdiği asliye hukuk mahkemesi FSHM sıfatıyla bakar; bu husus dilekçede belirtilir.
2. TÜRKPATENT kararları: Kurum kararlarının (YİDK) iptali ve Kurum aleyhine hükümsüzlük/sicil davaları münhasıran Ankara FSHM'de açılır (SMK m.156/2). İdari karara karşı süre kaçırılmamalı (SMK m.20-21 itiraz süreçleri tüketilmeli).
3. Yetki (tecavüz/tazminat): Hak sahibi davacı, kendi yerleşim yeri yahut hukuka aykırı fiilin gerçekleştiği veya etkilerinin görüldüğü yer mahkemesinde dava açabilir (SMK m.156/3). Tecavüz edenin açacağı davada genel yetki (HMK m.6) uygulanır.
4. Yargı kolu ayrımı: Tecavüz/tazminat/hükümsüzlük adli yargıdadır; ancak gümrük el koyma idari işlemine itiraz ve YİDK öncesi idari aşama farklı kanallardır. Ceza boyutu (SMK m.30 marka suçları, FSEK m.71-72) FSHM Ceza/asliye ceza yolundadır.
5. Ara sonuç: İspat yükü görevsizlik itirazında davalıya geçmez; görev kamu düzenindendir, re'sen gözetilir (HMK m.114/1-c). Yanlış mahkemede açılan davada görevsizlik/yetkisizlik üzerine HMK m.20 süresi izlenir.

## Çıktı modülleri
- Görev-yetki tespit notu (madde gerekçeli).
- TÜRKPATENT dava merkezi ve süre uyarısı.
- Yetki itirazı veya yetki sözleşmesi değerlendirmesi.

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
