---
name: hukuki-pozitivizm-ve-norm-teorisi
description: "Bir normun nereden bağlayıcılık aldığı, üst norma aykırı alt normun akıbeti veya geçerlilik-meşruiyet ayrımı tartışıldığında; Kelsen ve Hart çizgisinde norm geçerliliğini Türk norm hiyerarşisine bağlamak için kullanın."
---

# Hukuki Pozitivizm ve Norm Geçerliliği

## Görev
Bir normun geçerliliğini (bağlayıcılığını) kaynağına dayalı olarak analiz etmek; Kelsen'in
saf hukuk teorisi (temel norm/basamak teorisi) ve Hart'ın tanıma kuralı çerçevesini Türk
pozitif norm hiyerarşisine (Anayasa m.11, m.90/son) bağlamak.

## Soğuk başlangıç (intake)
- Sorun bir alt normun (yönetmelik/tüzük) üst norma (kanun/Anayasa) aykırılığı mı?
- Norm yürürlükte ama içeriği "haksız" mı görünüyor (geçerlilik mi, meşruiyet mi sorusu)?
- Milletlerarası bir andlaşma ile kanun çatışması var mı (m.90/son devrede mi)?
- İddia akademik mi yoksa norm denetimi/iptal argümanı üretmeye mi yönelik?

## Denetim şeması
1. **Geçerlilik ölçütünü belirle.** Pozitivizmde bir norm, üst normun öngördüğü usul ve
   yetkiyle konulmuşsa geçerlidir; içeriğin "adil" olması geçerlilik şartı değildir
   (geçerlilik ≠ meşruiyet). Bunu açıkça ayır.
2. **Basamağı kur.** Anayasa m.11 (Anayasanın bağlayıcılığı/üstünlüğü) ve m.90/son (temel
   hak andlaşmalarının kanuna üstünlüğü) ile somut normu hiyerarşide konumla. Tanıma kuralı
   (Hart) burada "Türkiye'de hangi normlar hukuktur" sorusunun pozitif cevabıdır.
3. **Aykırılığın akıbetini ayır.** Kanunun Anayasaya aykırılığı → AYM norm denetimi
   (Anayasa m.148 vd.); yönetmeliğin kanuna/Anayasaya aykırılığı → idari yargıda iptal
   (2577 İYUK) ve Anayasa m.124 düzenleme yetkisi sınırı. Geçersizlik kendiliğinden değil,
   yetkili merci kararıyla tespit edilir.
4. **Geçerlilik-meşruiyet gerilimini işaretle.** Norm geçerli ama içeriksel olarak ağır
   adaletsizse, salt pozitivist cevap yetersiz kalır; bu noktada doğal hukuk/Radbruch
   tartışmasına köprü kur (ayrı beceriye yönlendir). Ara sonuç: geçerli ≠ her durumda uygulanmalı.
5. **Dayanak.** Kelsen (Saf Hukuk Teorisi) ve Hart (Hukuk Kavramı) ile Türk anayasa öğretisine
   atıf yap; sayfa [doğrulanacak]. Norm denetimi kararı zikredilecekse künye
   kararlarbilgibankasi.anayasa.gov.tr üzerinden teyit edilir, doğrulanmadıkça [doğrulanacak].

## Çıktı modülleri
- Norm hiyerarşisi şeması (somut norm yerleştirilmiş).
- Geçerlilik/meşruiyet ayrım notu.
- Aykırılık halinde başvurulacak denetim yolu (AYM / idari yargı) ve madde atfı.

## Plugin bağlamı

Bu beceri `hukuk-felsefesi-genel-teori` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
