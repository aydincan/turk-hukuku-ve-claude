---
name: tasdik-ve-ret-kararlari
description: "Konkordatonun tasdiki için aranan şartların denetimi, tasdik veya ret kararının sonuçları ve bu kararlara karşı kanun yollarının işletilmesi gerektiğinde kullanılır."
---

# Tasdik, Ret ve Kanun Yolları

## Görev
Konkordatonun mahkemece tasdiki için İİK m.305 şartlarını denetlemek, tasdik (m.306) ve ret (m.308) kararlarının sonuçlarını çözümlemek, kanun yollarını (istinaf/temyiz) işletmek.

## Soğuk başlangıç (intake)
- Komiserin esas hakkındaki raporu mahkemeye sunuldu mu?
- Çoğunluk sağlandı, depo şartları yerine getirildi mi?
- İmtiyazlı alacakların ödenmesi güvenceye bağlandı mı?
- Tasdik/ret kararı verildi mi, hangi tarihli?

## Denetim şeması
1. **Tasdik şartları (m.305).** (a) Teklifin borçlunun kaynaklarıyla orantılı olması (rehinli malların satışından veya devamlı işletmeden elde edilecek gelir gözetilir); (b) İİK m.206/1. sırada yer alan alacakların tam ödenmesinin güvenceye bağlanması (alacaklı vazgeçmedikçe); (c) yargılama giderleri ve konkordatonun yerine getirilmesi için gerekli giderlerin depo edilmesi.
2. **Tasdik kararı (m.306).** Mahkeme tasdik kararında alacaklıların hangi ölçüde alacaklarından vazgeçtiğini, ödeme takvimini ve gerekirse bir kayyım/denetim mekanizmasını gösterir. Tasdik kararı ilan ve tescil edilir.
3. **Tasdikin sonuçları (m.308/c-h).** Konkordato, tasdik edilmeyen alacaklar dâhil tüm alacaklılar için bağlayıcı hâle gelir (çekişmeli alacaklar ve rehinli/yakın istisnaları saklı). Rehinli alacaklılarla yapılan anlaşma ayrıca düzenlenir (m.308/h).
4. **Ret (m.308).** Şartlar yoksa talep reddedilir; borçlu iflasa tabi ise ve borca batıksa doğrudan iflasına karar verilebilir (m.308/son). İspat yükü: tasdik şartlarının varlığını borçlu ortaya koyar.
5. **Kanun yolları.** Tasdik/ret kararına karşı istinaf ve temyiz yolu (İİK ve HMK genel hükümleri çerçevesinde) açıktır; süreler titizlikle hesaplanır. Yargıtay 23. Hukuk Dairesi içtihadı esas alınır `[doğrulanacak — karararama.yargitay.gov.tr]`. Ara sonuç: hangi kanun yoluna, hangi sürede başvurulacağı.

## Çıktı modülleri
- Tasdik şartları denetim raporu.
- Tasdik/ret kararı sonuç analizi.
- İstinaf/temyiz dilekçesi taslağı (yer tutuculu) ve süre hesabı.
- Karar sonrası icra/tescil adımları listesi.

## Plugin bağlamı

Bu beceri `konkordato-yeniden-yapilandirma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
