---
name: cikis-exit-rekabet-vergi
description: "Girişimin çıkış senaryoları (satış, ikincil pay devri, halka arz) planlanırken veya işlemin rekabet izni eşiği, vergi ve teşvik (TGB, Ar-Ge, melek yatırımcı, kurumlar) boyutu değerlendirilirken kullanılır."
---

# Çıkış (Exit), Rekabet İzni ve Vergi-Teşvik

## Görev
Çıkış yolunu ve onun düzenleyici/vergisel sonuçlarını planlamak: stratejik satış, ikincil pay devri (secondary) veya halka arz; rekabet izni eşiği ve vergi/teşvik optimizasyonu.

## Soğuk başlangıç (intake)
1. Çıkış tipi: tüm/çoğunluk satışı, ikincil pay satışı, halka arz?
2. Devredilen kontrol/pay oranı ve işlem büyüklüğü ne (rekabet eşiği için)?
3. Satıcı gerçek kişi mi, kurum mu (vergi rejimi farklı)?
4. Şirket TGB/Ar-Ge teşviklerinden yararlanıyor mu; çıkış bunları etkiler mi?
5. SHA'daki drag/tag/önalım çıkışta nasıl işleyecek?

## Denetim şeması
1. Rekabet izni: Devralma kontrol değişikliği yaratıyor ve ciro eşikleri aşılıyorsa Rekabet Kurulu izni gerekir (4054 m.7 ve 2010/4 sayılı Tebliğ eşikleri). İzinsiz kapanış geçersizlik/idari para cezası riski; eşikleri güncel tebliğden teyit et. Erken aşamada genellikle eşik altıdır.
2. SHA çıkış hükümleri: Drag-along ile çoğunluk azınlığı satışa sürükler; tag-along ile azınlık katılır; önalım hakları işletilir. Bunlar taraflar arası borç (TBK); ayni engel için esas sözleşmesel bağlam.
3. Vergi — gerçek kişi: Pay/iştirak hissesi satış kazancında GVK değer artışı kazancı kuralları; anonim şirket hisse senedi (bastırılmış) için iki yıllık elde tutma istisnası gibi koşullar — güncel GVK metninden teyit et.
4. Vergi — kurum: İştirak hissesi satış kazancı istisnası (KVK m.5/1-e: belirli oran ve süre şartıyla) ve emisyon primi istisnası; şartları (elde tutma süresi, fon hesabı) güncel 5520 metninden teyit et.
5. Teşvik etkisi: TGB istisnası (4691) ve Ar-Ge (5746) faaliyet şartına bağlıdır; ortaklık değişimi kural olarak teşviki sonlandırmaz ama faaliyet/bölge şartının sürmesi denetlenmeli. Melek yatırımcı (BKY) indirimi GVK mük. m.82 koşulları.
6. Halka arz: SPK rejimi (6362) — izahname, kamuyu aydınlatma; ayrı uzmanlık alanı, ilgili beceriye yönlendir.
7. İspat/şekil: İşlem belgeleri, kurumsal kararlar, gerekiyorsa Rekabet Kurulu başvurusu; vergi pozisyonu için mali müşavir teyidi.

## Çıktı modülleri
- Çıkış senaryosu ve adım planı (drag/tag/önalım işleyişi).
- Rekabet izni gereklilik testi (eşik kontrol notu).
- Vergi/teşvik etki analizi ve doğrulama listesi (oran/süreler [doldurulacak]).

## Plugin bağlamı

Bu beceri `girisim-startup-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
