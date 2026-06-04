---
name: anonim-limited-kurulus
description: "Anonim veya limited şirket kuruluşu, esas/şirket sözleşmesinin zorunlu içeriği, sermaye taahhüdü ve ayni sermaye, tescil ve MERSİS adımları gündeme geldiğinde; kuruluş sürecinin eksiksiz ve geçerli kurgulanması için kullanılır."
---

# AŞ ve Ltd. Kuruluş ve Esas Sözleşme

## Görev
Sermaye şirketini geçerli biçimde kurmak: tip seçimi, esas/şirket sözleşmesi içeriği, sermaye taahhüdü ve ödeme, tescil-ilan; kuruluş sakatlıklarını önlemek.

## Soğuk başlangıç (intake)
1. AŞ mı Ltd. mi; ortak sayısı, tek kişilik mi?
2. Sermaye miktarı ve yapısı: nakdi/ayni; ayni varsa konusu?
3. Faaliyet konusu ve ticaret unvanı belirlendi mi?
4. Yönetim yapısı tercihi (AŞ'de tek üyeli YK mümkün; Ltd.'de müdür) ne?
5. Özel hak/imtiyaz, pay devri sınırı, oy hakkı düzenlemesi isteniyor mu?

## Denetim şeması
1. Asgari sermaye: AŞ m.332 (esas sermaye asgari tutarı; kayıtlı sermaye sistemi m.332/2); Ltd. m.580. Olay tarihindeki güncel tutarı teyit et.
2. Ortak/kurucu: AŞ tek kişiyle kurulabilir (m.338); Ltd. tek ortakla (m.574); azami ortak sayısı Ltd.'de 50 (m.574).
3. Esas sözleşme zorunlu içeriği: AŞ m.339 (unvan, merkez, konu, sermaye ve paylar, yönetim, ilan şekli); Ltd. m.576. Noter onayı veya sicil müdürü huzurunda imza (m.575).
4. Sermayenin ödenmesi: AŞ nakdî sermayenin tescilden önce ödenmesi ve kalanın 24 ayda ödenmesi (m.344, m.459/1 atfı); ayni sermaye değerlemesi mahkemece atanan bilirkişi (m.343); ayni sermaye üzerinde sınırlı ayni hak/haciz olmaması (m.342).
5. Ayni sermaye ve devralma: m.342-343; kuruluşta devralınacak işletme/ayınlar m.349 (kurucular beyanı).
6. Tescil ve tüzel kişilik: m.354-355 (AŞ), m.585-588 (Ltd.); MERSİS üzerinden başvuru; tescille tüzel kişilik doğar. İzne tabi şirketlerde Bakanlık izni (m.333).
7. İspat/şekil: Şekle aykırı esas sözleşme hükmü geçersiz; emredici hükme aykırılık m.340/579.

## Çıktı modülleri
- Kuruluş checklist'i (sermaye, sözleşme, tescil, MERSİS).
- Esas/şirket sözleşmesi taslağı (zorunlu maddeler, [doldurulacak] yer tutucularla).
- Ayni sermaye/değerleme ve özel hak notu.

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
