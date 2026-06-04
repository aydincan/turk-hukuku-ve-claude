---
name: ehliyet-ve-temsil
description: "Bir kişinin yaptığı hukuki işlemin ehliyet yönünden geçerli olup olmadığı; küçüğün, kısıtlının veya ayırt etme gücü tartışmalı kişinin işleminin akıbeti sorgulandığında kullanılır."
---

# Hak ve Fiil Ehliyeti, Sınırlı Ehliyetsiz İşlemleri

## Görev
Bir hukuki işlemin ehliyet süzgecinden geçip geçmediğini belirlemek: işlemi yapanın hangi ehliyet katmanına düştüğünü saptayıp işlemin geçerli, kesin hükümsüz, askıda hükümsüz (icazete bağlı) ya da iptal edilebilir olduğunu gerekçelendirmek.

## Soğuk başlangıç (intake)
- İşlemi yapanın yaşı ve durumu: ergin mi, kaç yaşında, vesayet/kısıtlılık var mı?
- İşlem anında ayırt etme gücü var mıydı (akıl hastalığı, sarhoşluk, geçici bilinç kaybı iddiası)?
- İşlem türü: borç altına sokuyor mu, karşılıksız kazandırma mı, kişiye sıkı sıkıya bağlı hak mı?
- Yasal temsilci (veli/vasi) onayı/izni var mı; varsa önceden mi sonradan mı?

## Denetim şeması
1. **Ayırt etme gücü** — TMK m.13: yaş, akıl hastalığı/zayıflığı, sarhoşluk veya benzer sebeple makul davranma yeteneğinden yoksun olmayan kişi ayırt etme gücüne sahiptir. Yoklukta (m.15) işlem kural olarak kesin hükümsüzdür (m.14-15).
2. **Katman belirleme** — Tam ehliyetli: işlem geçerli. Tam ehliyetsiz (m.14-15): kişisel olarak hak kuramaz, işlemleri hükümsüz. Sınırlı ehliyetsiz (m.16): ayırt etme gücü olan küçük/kısıtlı.
3. **Sınırlı ehliyetsizin işlemi** — TMK m.16: yasal temsilcinin rızası olmadıkça borç altına giremez; ancak (a) karşılıksız kazanma ve (b) kişiye sıkı sıkıya bağlı hakları tek başına kullanabilir. Borçlandırıcı işlem temsilcinin rızasına bağlıdır; rıza yoksa işlem askıda hükümsüzdür ve icazetle (TBK m.451 vd. kıyasen onam) geçerli hâle gelebilir.
4. **Sorumluluk** — TMK m.16/2: yasal temsilcinin rızası dışında borçlanan sınırlı ehliyetsiz, sebepsiz zenginleşme (TBK m.77 vd.) ölçüsünde veya kasten ehliyetsizliğine güveni boşa çıkarmışsa sorumlu olur.
5. **Tüzel kişide** — TMK m.49-50: tüzel kişi organları aracılığıyla fiil ehliyetini kullanır; organların hukuki işlemleri ve kusurları tüzel kişiyi bağlar.
6. **Dürüstlük denetimi** — TMK m.2: ehliyetsizliğin kötüniyetle/çelişkili biçimde ileri sürülmesi korunmaz.

## Çıktı modülleri
- Ehliyet katmanı tespiti + işlemin akıbeti (geçerli/butlan/askıda/iptal).
- İcazet veya yasal temsilci onayı için yapılması gerekenler.
- İspat yükü notu (ayırt etme gücü yokluğunu iddia eden ispatlar — m.6).
- İlkesel içtihat atfı, künye `[doğrulanacak]`.

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
