---
name: tecavuz-tespiti-ve-talepler
description: "Patent/faydalı model hakkına tecavüz edilip edilmediği, hangi fiillerin tecavüz sayıldığı ve hangi taleplerin ileri sürülebileceği değerlendirildiğinde kullanılır; hak sahibinin saldırı stratejisi için temel beceridir."
---

# Patent Hakkına Tecavüz Tespiti ve Talepler

## Görev
SMK m.141 kapsamında tecavüz fiilini saptamak ve SMK m.149-151 uyarınca ileri sürülebilecek talepleri (tespit, men, ref, tazminat, el koyma, imha) belirlemek.

## Soğuk başlangıç (intake)
1. Hakka konu patent/faydalı model geçerli ve ayakta mı (yıllık ücretler ödendi mi)?
2. Karşı tarafın fiili ne: üretim, satış, kullanım, ithalat, stoklama, dolaylı tecavüz?
3. Tecavüz iddiası hangi istem(ler)e dayanıyor; eşdeğer mi literal mi?
4. Zarar/yoksun kazanç verisi, lisans bedeli emsali var mı?

## Denetim şeması
1. **Hakkın geçerliliği ve ayakta olması.** Belge verilmiş, hükümsüz kılınmamış ve yıllık ücretleri ödenmiş olmalı (SMK m.101). Faydalı modelde tecavüz davası açılırken araştırma raporu talebi gerekebileceğini değerlendir.
2. **Tecavüz fiili (SMK m.141).** İzinsiz üretim, satışa sunma, satma, kullanma, ithalat, ticari amaçla elde bulundurma; usul patentinde usulün kullanımı ve doğrudan elde edilen ürün; ayrıca dolaylı/araç sağlama yoluyla tecavüz. Ara sonuç: fiil m.141 kapsamında mı?
3. **Kapsam denetimi.** Fiil, istem yorumu (SMK m.89) ile koruma kapsamına giriyor mu? Bu, istem-ürün eşleştirmesiyle yapılır (bkz. istem yorumu becerisi).
4. **Savunma süzgeci.** Önceki kullanım hakkı (SMK m.87), tüketilme (SMK m.152), hükümsüzlük def'i, deneme amaçlı/özel kullanım istisnaları (SMK m.85/3) karşı tarafın elinde mi?
5. **Talepler (SMK m.149).** Tespit, muhtemel tecavüzün önlenmesi, durdurma (men), giderme (ref), tazminat (maddi/manevi), el koyma/imha, kararın ilanı. Tazminatta yoksun kalınan kazanç SMK m.151 üç yöntemden biriyle (lisans analojisi dahil) hesaplanır.

## Çıktı modülleri
- Tecavüz fiili nitelendirmesi (m.141 hangi bent).
- İstem-ürün kapsam eşleştirmesi özeti.
- Karşı tarafın savunma/def'i envanteri.
- Talep listesi ve tazminat hesap yöntemi önerisi.

## Plugin bağlamı

Bu beceri `patent-faydali-model` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
