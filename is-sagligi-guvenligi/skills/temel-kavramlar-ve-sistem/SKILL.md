---
name: temel-kavramlar-ve-sistem
description: "İş sağlığı ve güvenliği dosyasının hangi eksende (idari uyum, iş kazası tazminatı, SGK rücuu, ceza) ele alınacağını ve 6331 ile 5510-TBK katmanlarının nasıl ayrıştırılacağını belirlemek için kullanılır."
---

# Temel Kavramlar ve Sistematik

## Görev
İSG dosyasını üç hukuki katmana ayırmak (idari/önleyici 6331; sosyal güvenlik 5510; tazminat TBK), olayı doğru eksene oturtmak ve sonraki becerilere yön vermek. Çoğu dosya karmadır; her katman ayrı altlanır.

## Soğuk başlangıç (intake)
- İşyerinin tehlike sınıfı (az tehlikeli / tehlikeli / çok tehlikeli) ve toplam çalışan sayısı nedir?
- Talep ne yönde: idari ceza/uyum mu, iş kazası-meslek hastalığı tazminatı mı, SGK rücuu mu, ceza soruşturması mı?
- Somut bir kaza/olay var mı; varsa SGK bildirimi yapıldı mı, kusur/bilirkişi raporu mevcut mu?
- Müvekkil sıfatı: işveren mi, çalışan/hak sahibi mi, İSG profesyoneli mi?

## Denetim şeması
1. **Kapsam (6331 m.2):** İşyeri ve çalışan 6331 kapsamında mı? Kapsam dışı istisnaları ele (ör. Kanun m.2/2'deki sınırlı haller). Kapsam belirlenmeden yükümlülük tartışılmaz.
2. **Tehlike sınıfı süzgeci:** İş güvenliği uzmanı/işyeri hekimi zorunluluğu, kurul kuruluşu (m.22 — 50+ çalışan ve altı aydan fazla süren işler), eğitim periyotları tehlike sınıfına bağlıdır. Sınıfı yanlış belirlemek tüm değerlendirmeyi bozar.
3. **Eksen ayrımı:**
   - İdari uyum/ceza → 6331 m.4-22 yükümlülükleri + m.26 idari para cezası.
   - Tazminat → işverenin gözetme borcu (TBK m.417/2), zarar haksız fiile tabi (m.417/3, m.49 vd.).
   - SGK rücuu → 5510 m.21, işverenin kusuru oranında.
   - Ceza → TCK m.85-89 (taksirle öldürme/yaralama), kusur ve öngörülebilirlik.
4. **Ara sonuç:** Her eksen için ayrı bir not düş; ispat yükü ve görevli merci farklıdır (idari ceza → sulh ceza hâkimliği itirazı; tazminat ve rücu → iş mahkemesi).
5. **İstisna/öncelik:** İşveren vekili, alt işveren-asıl işveren birlikteliği ve geçici iş ilişkisi varsa sorumlu süjeyi netleştir.

## Çıktı modülleri
- Eksen haritası (idari / SGK / tazminat / ceza) tablosu.
- Tehlike sınıfı ve çalışan sayısına göre yükümlülük matrisi.
- Sonraki becerilere yönlendirme notu.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
