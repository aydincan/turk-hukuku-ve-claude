---
name: kisilik-hakki-koruma-semasi
description: "Şeref ve itibara, özel hayata, beden bütünlüğüne, isme ya da resme yönelik bir saldırı iddiasında saldırının hukuka aykırılığını ve uygun talep yolunu belirlemek için kullanılır."
---

# Kişilik Hakkı İhlali Denetim Şeması (m.24-25)

## Görev
Bir kişilik değerine (şeref-itibar, özel/gizli alan, beden ve ruh bütünlüğü, ad, resim, ses) yönelik müdahalenin hukuka aykırı saldırı oluşturup oluşturmadığını TMK m.24 süzgecinden geçirmek ve m.25'teki davalardan uygununu seçmek.

## Soğuk başlangıç (intake)
- Hangi kişilik değeri zedelendi: şeref/itibar mı, özel hayat mı, beden bütünlüğü mü, ad/resim mi?
- Müdahale ne zaman, hangi araçla (söz, yazı, yayın, görüntü, fiil) yapıldı; sürüyor mu, tekrar tehlikesi var mı?
- Saldıran kim; bir hukuka uygunluk sebebi (rıza, üstün kamu/özel yarar, yetki kullanımı) ileri sürüyor mu?
- İstenen: önleme, durdurma, tespit, maddi/manevi tazminat, kazancın iadesi?

## Denetim şeması
1. **Saldırının tespiti** — TMK m.24/1: kişilik hakkı hukuka aykırı saldırıya uğrayan, hâkimden koruma isteyebilir. Önce bir kişilik değerine müdahale ortaya konur.
2. **Hukuka aykırılık karinesi** — TMK m.24/2: her saldırı hukuka aykırıdır; saldıranın hukuka uygunluk sebebi ispatı gerekir. Hukuka uygunluk sebepleri: (a) zarar görenin rızası, (b) daha üstün nitelikte özel veya kamusal yarar, (c) kanunun verdiği yetkinin kullanılması.
3. **Menfaat tartımı** — Özellikle ifade/basın özgürlüğü ile çatışmada: gerçeklik, güncellik, kamu yararı ve konu-ifade arasındaki ölçü (öz-biçim dengesi) ölçütleri tartılır. Anayasa m.13 ölçülülük ve AYM bireysel başvuru içtihadı esas alınır.
4. **Talep türleri — TMK m.25/1**: (a) saldırı tehlikesinin önlenmesi (men) davası; (b) sürmekte olan saldırıya son verilmesi (durdurma/ref); (c) sona ermiş saldırının hukuka aykırılığının tespiti davası. Ayrıca düzeltme/cevap, kararın yayınlanması istenebilir.
5. **Tazminat — TMK m.25/3 yollamasıyla**: maddi tazminat (TBK m.49 vd.), manevi tazminat (TBK m.58; bedensel zarar/ölümde m.56), saldırı sonucu elde edilen kazancın vekâletsiz iş görme hükümlerine göre iadesi.
6. **İhtiyati tedbir** — HMK m.389 vd.: yayın/saldırının durdurulması için tedbir; ölçülülük ve ifade özgürlüğü dikkate alınır.

## Çıktı modülleri
- Saldırı + hukuka aykırılık + savunma (uygunluk sebebi) tablosu.
- Menfaat tartımı gerekçesi (özellikle yayın hâllerinde).
- Seçilen dava türü ve talep sonucu taslağı.
- İlkesel AYM/Yargıtay atfı, künye `[doğrulanacak]` (kararlarbilgibankasi.anayasa.gov.tr).

## Plugin bağlamı

Bu beceri `kisiler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
