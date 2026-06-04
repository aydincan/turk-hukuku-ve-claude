---
name: hak-ve-yukumluluk-teorisi
description: "Bir menfaatin gerçekten sübjektif hak olup olmadığı, hak türleri (mutlak-nispi, yenilik doğuran, def'i-itiraz) ve hak-yetki-yükümlülük ilişkileri çözümlenmek istendiğinde; Hohfeld ve menfaat/irade teorileri çerçevesinde kullanın."
---

# Hak, Yükümlülük ve Hukuki İlişki Teorisi

## Görev
Sübjektif hak kavramını analiz etmek; bir talebin gerçek bir hak mı, yetki/beklenti mi
olduğunu ayırmak; hak türlerini ve karşı kavramları (yükümlülük, def'i, itiraz) sistematize
etmek. Bu çözümleme dava dilekçesinde "talep sonucu" ve "hukuki sebep" kurarken doğrudan işe yarar.

## Soğuk başlangıç (intake)
- İddia edilen şey bir sübjektif hak mı, yoksa korunan basit bir menfaat/beklenti mi?
- Hak mutlak mı (herkese karşı, ör. mülkiyet) nispi mi (belirli kişiye karşı, ör. alacak)?
- Talep, yenilik doğuran (kurucu/değiştirici/bozucu) bir hakka mı dayanıyor?
- Karşı tarafın elinde def'i mi (ör. zamanaşımı) yoksa itiraz mı (ör. ödeme) var?

## Denetim şeması
1. **Hak teorisini seç.** İrade teorisi (hak = korunan irade gücü) ile menfaat teorisi
   (hak = hukuken korunan menfaat, Jhering) arasında somut menfaate uygun olanı kullan; çoğu
   Türk doktrini karma yaklaşımı benimser.
2. **Hohfeld dörtlüsünü uygula.** Talep hakkı–yükümlülük, özgürlük/serbesti–hak yokluğu,
   yetki (kudret)–tâbilik, bağışıklık–yetersizlik ilişkilerini ayır. "Hak" denilen şeyin
   hangi kutucuğa düştüğünü belirle; bu, kime karşı ne talep edilebileceğini netleştirir.
3. **Hak türünü sınıfla.** Mutlak/nispi; ayni/şahsi; yenilik doğuran (TMK ve TBK'da örnekler:
   bozucu yenilik doğuran fesih hakkı gibi); devredilebilir/kişiye sıkı bağlı. Mutlak hak,
   üçüncü kişilere karşı korunma (haksız fiil/istihkak) imkânı verir.
4. **Karşı kavramı tespit et.** Def'i (hakkı ileri sürmeye bağlı, ör. zamanaşımı def'i,
   TBK m.161; hâkim re'sen dikkate almaz) ile itiraz (hakkın doğmadığını/sona erdiğini
   gösteren, hâkim re'sen dikkate alır) ayrımını yap. Ara sonuç: ispat yükü ve usul sonucu buradan çıkar.
5. **İspat yükü.** Hakkı iddia eden, hakkın doğum vakıalarını; karşı taraf, sona erme/engelleyici
   vakıaları ispatla yükümlüdür (TMK m.6; HMK m.190). Bunu hak teorisi sonucuyla hizala.

## Çıktı modülleri
- Hak nitelendirme notu (gerçek hak mı / menfaat mi).
- Hohfeld ilişki tablosu (talep–yükümlülük vb.).
- Hak türü etiketi ve sonuçları (mutlak/nispi, yenilik doğuran).
- Def'i/itiraz ayrımı ve ispat yükü dağılımı.

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
