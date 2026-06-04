<<<REFERANS>>>
# Yapay Zekâ ve Veri Hukuku — Metodoloji ve Çalışma Referansı

## Alanın sistematiği
Türkiye'de "yapay zekâ hukuku" bağımsız ve kodifiye bir alan değildir; mevcut normların yapay zekâ uygulamalarına uyarlanmasıyla işler. Çalışırken her dosyayı önce üç eksende konumlandırın: (1) hangi katman — kişisel veri/veri yönetişimi mi, sözleşmesel/ticari mi, sorumluluk/tazminat mı, fikri mülkiyet mi, sektörel düzenleme mi; (2) yapay zekânın rolü — karar destek, tam otomatik karar, üretken model (LLM/görüntü), profilleme/skorlama; (3) tarafların sıfatı — geliştirici/sağlayıcı, dağıtan/uygulayıcı (deployer), veri sorumlusu/işleyen, ilgili kişi/zarar gören. Bu konumlandırma uygulanacak normu, görevli mercii ve ispat yükünü büyük ölçüde belirler. Türkiye'de 2024 itibarıyla yatay bir "Yapay Zekâ Kanunu" yoktur; bu nedenle AB Yapay Zekâ Tüzüğü (Regulation (EU) 2024/1689) yalnızca karşılaştırmalı/yön gösterici kaynaktır, doğrudan uygulanmaz — bunu müvekkile net söyleyin.

## Başat normlar ve madde atıfları
- **6698 sayılı KVKK**: işleme şartları ve genel ilkeler (m.4 hukuka uygunluk, ölçülülük, amaçla bağlılık), açık rıza dışı işleme şartları (m.5), özel nitelikli veri (m.6), aydınlatma yükümlülüğü (m.10), ilgili kişinin hakları ve **münhasıran otomatik sistemlerle analiz edilerek aleyhe sonuç doğmasına itiraz** (m.11/1-g), veri güvenliği (m.12), yurt dışına aktarım (m.9 — 7499 sayılı Kanun'la değişik), Kurula şikâyet ve dava (m.14-15), Kurul yaptırımları (m.18).
- **TBK 6098**: sözleşme dışı sorumlulukta haksız fiil (m.49 vd.), kusursuz sorumluluk halleri — özellikle **adam çalıştıranın sorumluluğu (m.66)** ve **tehlike sorumluluğu / tehlikeli işletme (m.71)**, sözleşmeye aykırılık (m.112 vd.), genel işlem koşulları denetimi (m.20-25).
- **6502 sayılı TKHK** ve **6502 kapsamı dışında 6/3/2003 mehazlı AB Ürün Sorumluluğu mantığı**: yapay zekâ gömülü ürün/üründe ayıp tartışmalarında tüketici işlemi boyutu.
- **5846 sayılı FSEK**: eğitim verisi olarak eser kullanımı (çoğaltma m.22, işleme m.21), eser sahibi sıfatı tartışması (m.1/B, m.8 — yapay zekânın eser sahibi olamayacağı), istisnalar dar yorumlanır.
- **6769 sayılı SMK**: yapay zekâ üretimi içerik/tasarım/marka ve buluşta gerçek hak sahipliği.
- **Sektörel**: 5411 (kredi skorlama/bankacılık), 5510 ve 4857 (istihdam/işe alım algoritmaları), 1219/3359 (klinik karar destek), 6362 SPK (algoritmik işlem/robo-danışmanlık), 2577 İYUK (kamu idaresinin otomatik karar işlemleri).
- **Karşılaştırmalı**: AB Yapay Zekâ Tüzüğü 2024/1689 (yasak uygulamalar, yüksek riskli sistemler, GPAI yükümlülükleri) ve GDPR m.22 — Türk müvekkili AB pazarına dokunuyorsa doğrudan uygulanabilir.

## Çalışma yöntemi
1. **Yer/uygulama tespiti**: Sistem AB'ye hizmet/ürün sunuyor mu? Sunuyorsa AB Tüzüğü ve GDPR doğrudan devreye girebilir; sadece Türkiye'ye sunuyorsa KVKK + TBK + sektörel mevzuat eksenine oturtun.
2. **Tarih kilidi**: KVKK m.9 (yurt dışı aktarım) ve idari para cezası tutarları 7499 sayılı Kanun ve yıllık yeniden değerleme ile değişti; olay tarihindeki yürürlük halini sabitleyin.
3. **Teknik gerçek tespiti**: Modelin eğitim verisi kaynağı, çıktının insan denetiminden geçip geçmediği, log/kayıt tutulup tutulmadığı hukuki sonucu belirler; varsayım yapmayın, belge/teknik dokümanı isteyin.
4. **Sözleşme-düzenleme ayrımı**: Aynı olguda hem KVKK uyum/yaptırım riski hem sözleşmesel sorumluluk doğabilir; ayrı denetleyin.

## Kaynak hijyeni
Mevzuatı resmî kaynaktan (mevzuat.gov.tr, Resmî Gazete) ve olay tarihindeki yürürlük haliyle doğrulayın; Kurul ilke kararları ve rehberleri için kvkk.gov.tr esastır. İçtihat için karararama.yargitay.gov.tr (sözleşme/haksız fiil), karararama.danistay.gov.tr (kamu otomatik karar/idari işlem) ve kararlarbilgibankasi.anayasa.gov.tr kullanın. Daire ve esas/karar numarasını uydurmayın; doğrulanmamış künyeyi [doğrulanacak] olarak işaretleyin. AB Tüzüğü ve Kurul kararları hızla değiştiğinden her atıfta versiyon/tarih kontrol edin.
<<<BECERI>>>
slug: temel-kavramlar-ve-sistem
ad: Yapay Zekâ Hukuku Temel Kavramlar ve Sistematik
aciklama: Yapay zekâ içeren bir dosyayı katman (veri-KVKK, sözleşme, sorumluluk, fikri mülkiyet, sektörel), sistemin rolü (karar destek, tam otomatik karar, üretken model, profilleme) ve tarafların sıfatı eksenlerinde konumlandırıp doğru normu ve görevli mercii belirlemek gerektiğinde kullanılır.
<<<GOVDE>>>
# Yapay Zekâ Hukuku Temel Kavramlar ve Sistematik

## Görev
Yapay zekâ unsuru içeren dosyayı doğru hukuki katmana oturtmak; Türkiye'de yatay bir YZ kanunu bulunmadığını dikkate alarak uygulanacak norm setini (KVKK 6698, TBK 6098, FSEK/SMK, sektörel) ve görevli mercii hızlıca tespit ederek sonraki uzman becerilere giriş kapısını açmak.

## Soğuk başlangıç (intake)
1. Sistem ne yapıyor: karar destek mi, tam otomatik karar mı, üretken model (metin/görüntü) mü, profilleme/skorlama mı?
2. Müvekkilin sıfatı: model geliştiren/sağlayan, sistemi kullanan (deployer), veri sorumlusu/işleyen, zarar gören/ilgili kişi mi?
3. Coğrafi erişim: sistem AB'deki kişilere ürün/hizmet sunuyor mu (AB Tüzüğü/GDPR riski)?
4. Uyuşmazlık türü: veri/KVKK uyumu mu, sözleşmesel mi, tazminat mı, fikri mülkiyet mi, kamu işlemi mi?

## Denetim şeması
1. **Katman tespiti**: Kişisel veri işleniyorsa KVKK (m.4 ilkeler, m.5-6 şartlar) devrede; otomatik kararla aleyhe sonuç varsa m.11/1-g; sözleşmesel ilişki varsa TBK 6098; zarar varsa haksız fiil (TBK m.49 vd.) veya kusursuz sorumluluk (m.66, m.71); içerik/eser üretimi varsa FSEK/SMK. Ara sonuç: hangi norm seti baskın.
2. **Sistemin rolü**: Tam otomatik karar mı (insan denetimi yok), insan onaylı karar destek mi? Bu ayrım KVKK m.11 itiraz hakkını ve sorumluluk dağılımını belirler.
3. **Yer/uygulama**: AB pazarına dokunuyorsa AB Yapay Zekâ Tüzüğü 2024/1689 ve GDPR m.22 doğrudan; yalnız Türkiye ise bu metinler karşılaştırmalı kaynaktır, bağlayıcı değildir. Müvekkile bunu açıkça belirt.
4. **Görevli merci**: KVKK ihlalinde Kurul (m.14) ve sulh/asliye hukuk; tüketici işleminde tüketici mahkemesi/hakem heyeti; kamu otomatik işleminde idari yargı (İYUK); fikri hakta FSHM.
5. **Tarih kilidi**: KVKK m.9 aktarım rejimi ve ceza tutarları değişti; olay tarihini sabitle.

## Çıktı modülleri
- Dosya konumlandırma notu (katman + sistemin rolü + norm seti).
- Uygulanır/karşılaştırmalı norm ayrımı (KVKK/TBK vs. AB Tüzüğü).
- Görevli merci ve hangi uzman beceriye geçileceğine dair yönlendirme.
<<<BECERI>>>
slug: otomatik-karar-profilleme
ad: Otomatik Karar ve Profilleme Denetimi
aciklama: Bireyi etkileyen kredi skoru, işe alım eleme, sigorta fiyatlama, içerik moderasyonu gibi münhasıran otomatik kararlar ve profilleme söz konusu olduğunda KVKK m.11/1-g itiraz hakkı, hukuki dayanak ve insan denetimi gerekliliği değerlendirildiğinde kullanılır.
<<<GOVDE>>>
# Otomatik Karar ve Profilleme Denetimi

## Görev
Bir yapay zekâ sisteminin kişi hakkında ürettiği kararın "münhasıran otomatik" olup olmadığını, hukuki dayanağını ve ilgili kişinin KVKK m.11/1-g kapsamındaki itiraz hakkını denetleyerek uyum ve savunma stratejisi çıkarmak.

## Soğuk başlangıç (intake)
1. Karar neyi etkiliyor: kredi, sigorta primi, işe alım, abonelik, içerik kaldırma, fiyatlandırma?
2. Sürece insan müdahalesi var mı; varsa anlamlı/etkin bir gözden geçirme mi yoksa biçimsel onay mı?
3. Hangi veriler işleniyor; özel nitelikli (sağlık, biyometrik, etnik) veri var mı?
4. İlgili kişiye otomatik karar uygulandığı aydınlatma metninde belirtilmiş mi?

## Denetim şeması
1. **Münhasıran otomatik mi**: KVKK m.11/1-g, kişinin "münhasıran otomatik sistemlerle analiz edilmesi suretiyle aleyhine bir sonucun ortaya çıkmasına itiraz" hakkını tanır. Anlamlı insan denetimi varsa "münhasıran otomatik" değildir; biçimsel onay yeterli sayılmaz. Ara sonuç: itiraz hakkı doğar mı.
2. **İşleme şartı**: m.5 — açık rıza ya da sözleşmenin kurulması/ifası, hukuki yükümlülük, meşru menfaat gibi bir şart; özel nitelikli veride m.6 daha dar şartlar. Dayanak yoksa işlemenin kendisi hukuka aykırı.
3. **İlkeler**: m.4 — amaçla bağlılık, ölçülülük, doğruluk. Modelin yanlı/güncel olmayan veriyle aleyhe sonuç üretmesi doğruluk ilkesine aykırılık delili olabilir.
4. **Aydınlatma**: m.10 — otomatik karar/profilleme yapıldığı, mantığı ve sonuçları konusunda bilgilendirme. Eksikse aydınlatma ihlali.
5. **Sonuç ve yol**: İhlalde m.13 ilgili kişi başvurusu, ardından m.14 Kurula şikâyet; aleyhe sonuçta tazminat için TBK/haksız fiil değerlendirilir. AB'ye dokunuyorsa GDPR m.22 (kural olarak yasak) karşılaştırmalı kontrol.

İlke kararı ve rehberler için kvkk.gov.tr; doğrulanmamış Kurul/yargı künyesini [doğrulanacak] işaretle.

## Çıktı modülleri
- Münhasıran otomatik karar testi sonucu (evet/hayır + gerekçe).
- İşleme şartı ve aydınlatma uyum tablosu.
- İtiraz/başvuru dilekçesi veya savunma stratejisi taslağı.
<<<BECERI>>>
slug: veri-yonetisim-egitim-verisi
ad: Veri Yönetişimi ve Eğitim Verisi Uyumu
aciklama: Bir yapay zekâ modelinin eğitiminde veya çalıştırılmasında kullanılan veri kümelerinin hukuka uygunluğu, kişisel veri içerip içermediği, kaynağı ve amaç sınırı değerlendirildiğinde ve web kazıma (scraping) ile veri toplama riski incelendiğinde kullanılır.
<<<GOVDE>>>
# Veri Yönetişimi ve Eğitim Verisi Uyumu

## Görev
Model eğitiminde ve çalıştırılmasında kullanılan veri kümelerinin kaynağını, hukuki dayanağını ve amaç sınırını denetleyerek veri yönetişimi uyum haritası ve risk azaltma önlemleri çıkarmak.

## Soğuk başlangıç (intake)
1. Eğitim verisi nereden: kullanıcı verisi, kamuya açık web (scraping), satın alınan/lisanslı set, sentetik veri?
2. Veride kişisel veri var mı; anonimleştirme/takma adlandırma yapıldı mı?
3. Verinin ilk toplanma amacı ile model eğitimi amacı uyumlu mu?
4. Üçüncü kişi/işleyen kullanılıyor mu; veri işleme sözleşmesi var mı?

## Denetim şeması
1. **Kişisel veri tespiti**: Veri kümesinde gerçek kişi belirli/belirlenebilir mi (KVKK m.3). Anonim veri KVKK dışı; ancak "yeniden kişiselleştirilebilir" takma adlı veri hâlâ kişisel veridir. Ara sonuç: KVKK uygulanır mı.
2. **İşleme şartı ve amaç**: m.5 dayanağı (çoğu eğitimde meşru menfaat tartışılır; özel nitelikli veride m.6 çok dar) ve m.4 amaçla bağlılık — başka amaçla toplanan verinin model eğitiminde kullanımı "ikincil işleme" sorununu doğurur, bağdaşırlık değerlendirilir.
3. **Web kazıma**: Kamuya açık olması KVKK muafiyeti değildir; m.28/1-d istisnası dar yorumlanır. Ayrıca kaynağın kullanım şartları (sözleşmesel) ve FSEK ihlali ayrıca denetlenir.
4. **Güvenlik ve işleyen**: m.12 teknik/idari tedbirler; üçüncü kişi işliyorsa veri işleyen sözleşmesi ve sorumluluk paylaşımı. Yurt dışı eğitim altyapısı varsa m.9 aktarım rejimi.
5. **Belgeleme**: Veri kaynağı envanteri, dayanak ve DPIA benzeri etki değerlendirmesi ispat yükünü veri sorumlusunda karşılayacak biçimde tutulmalı.

İçtihat ve Kurul yaklaşımı için kvkk.gov.tr ve karararama.danistay.gov.tr; künyeyi [doğrulanacak] işaretle.

## Çıktı modülleri
- Eğitim verisi kaynak ve dayanak envanteri.
- Risk haritası (scraping/ikincil işleme/özel nitelikli veri).
- Uyum aksiyon listesi ve veri işleyen sözleşmesi maddeleri.
<<<BECERI>>>
slug: algoritmik-seffaflik-aciklanabilirlik
ad: Algoritmik Şeffaflık ve Açıklanabilirlik
aciklama: İlgili kişinin veya denetçinin bir yapay zekâ kararının mantığına, kullanılan verilere ve karara dair açıklama talep etmesi durumunda aydınlatma ve bilgi verme yükümlülüğünün kapsamı ile ticari sır sınırı dengelendiğinde kullanılır.
<<<GOVDE>>>
# Algoritmik Şeffaflık ve Açıklanabilirlik

## Görev
Bir yapay zekâ sisteminin işleyişi ve ürettiği karar hakkında açıklama yükümlülüğünün kapsamını belirlemek; ilgili kişinin bilgi hakkı ile geliştiricinin ticari sır/fikri mülkiyet menfaatini dengeleyerek uygun şeffaflık seviyesini tasarlamak.

## Soğuk başlangıç (intake)
1. Talep eden kim: ilgili kişi, Kurul/denetçi, sözleşmenin karşı tarafı, mahkeme?
2. Ne isteniyor: kararın gerekçesi, kullanılan veri kategorileri, modelin mantığı, kaynak kod?
3. Sistemde aydınlatma metni ve karar gerekçesi loglanıyor mu?
4. Ticari sır/lisans kısıtı veya üçüncü kişi modeli (kapalı API) var mı?

## Denetim şeması
1. **Yükümlülüğün kaynağı**: KVKK m.10 aydınlatma (işlemenin amacı, otomatik karar varlığı), m.11 bilgi talep hakkı ve m.13 başvuru. Bu, kaynak kodun teslimini değil, kararın mantığı ve sonuçları konusunda anlamlı bilgiyi gerektirir. Ara sonuç: talep edilen şeffaflık seviyesi.
2. **Kapsam sınırı**: Şeffaflık, ticari sır ve fikri mülkiyetle (FSEK/SMK, TTK haksız rekabet) sınırlanır; ancak bu sınır bilgi hakkını tamamen bertaraf edemez — "anlamlı açıklama" verilmelidir. Denge ölçülülükle kurulur.
3. **Yargısal talepte**: HMK m.219-220 belgelerin ibrazı ve bilirkişi incelemesi yoluyla teknik açıklama sağlanabilir; mahkeme önünde ticari sır tedbirleriyle inceleme istenebilir.
4. **Kamu kararında**: İdarenin otomatik işleminde gerekçe yükümlülüğü ve İYUK kapsamında bilgi edinme/savunma hakları; gerekçesiz idari işlem sakatlık sebebi.
5. **Belgeleme**: Karar gerekçesinin ve model versiyonunun loglanması, sonradan açıklanabilirliği ve ispatı sağlar.

Kurul rehberleri için kvkk.gov.tr; yargı uygulaması için karararama portalları, künye [doğrulanacak].

## Çıktı modülleri
- Şeffaflık seviyesi matrisi (talep eden / verilecek bilgi / sınır).
- Açıklama metni taslağı (ticari sır korunarak).
- Logging/açıklanabilirlik öneri listesi.
<<<BECERI>>>
slug: yapay-zeka-sorumluluk
ad: Yapay Zekâ Kaynaklı Zarar ve Sorumluluk
aciklama: Bir yapay zekâ sistemi (otonom karar, üretken çıktı, gömülü ürün) bir kişiye zarar verdiğinde geliştirici, kullanan ve veri sağlayıcı arasında sorumluluğun haksız fiil, kusursuz sorumluluk ve sözleşme temelinde dağıtılması gerektiğinde kullanılır.
<<<GOVDE>>>
# Yapay Zekâ Kaynaklı Zarar ve Sorumluluk

## Görev
Yapay zekâ kaynaklı bir zararda sorumluluğun hukuki temelini (haksız fiil, kusursuz sorumluluk, sözleşmeye aykırılık) belirleyip geliştirici, sistemi kullanan ve veri sağlayıcı arasındaki dağılımı ve ispat yükünü çözümlemek.

## Soğuk başlangıç (intake)
1. Zarar nasıl doğdu: hatalı/önyargılı karar, yanlış üretken çıktı (uydurma bilgi), otonom cihaz/araç davranışı, veri sızıntısı?
2. Taraflar arasında sözleşme var mı (kullanım koşulları, hizmet sözleşmesi)?
3. Sistemi işleten kim; çıktı insan denetiminden geçti mi?
4. Zarar bedensel/mali/manevi mi; mağdur tüketici mi, işletme mi?

## Denetim şeması
1. **Sözleşme/haksız fiil ayrımı**: Taraflar arasında sözleşme varsa öncelik TBK m.112 vd. (gereği gibi ifa etmeme) ve sorumluluk sınırlaması/genel işlem koşulu denetimi (m.20-25). Sözleşme yoksa haksız fiil (m.49 vd.): fiil, hukuka aykırılık, kusur, zarar, illiyet. Ara sonuç: hangi rejim.
2. **Kusursuz sorumluluk**: Yapay zekâyı bir yardımcı kişi gibi kullanan işletme için **adam çalıştıranın sorumluluğu (TBK m.66)** ve riski yüksek otonom sistemlerde **tehlike sorumluluğu / tehlikeli işletme (TBK m.71)** tartışılır; bu hallerde kusur ispatı gerekmez, illiyet ve zarar yeter.
3. **İlliyet ve ispat**: YZ kararının "kara kutu" niteliği illiyetin ispatını zorlaştırır; bilirkişi, log ve model dokümanı kritik. İspat yükü kural olarak zarar görende; kusursuz sorumlulukta kusur dışındaki unsurlar yeterli.
4. **Üretken model çıktısı**: Yanlış/iftira niteliğinde çıktıda kişilik hakkı ihlali (TMK m.24-25, TBK m.58 manevi tazminat) ve sağlayıcının özen yükümlülüğü.
5. **Rücu ve dağıtım**: Müteselsil sorumlulukta (TBK m.61) iç ilişkide kusur/sözleşme uyarınca rücu; geliştirici-kullanan arası sözleşmedeki tazmin ve sorumluluk maddeleri belirleyici.

AB'de Ürün Sorumluluğu Direktifi reformu karşılaştırmalı kaynaktır, Türkiye'de doğrudan uygulanmaz. Künyeyi [doğrulanacak] işaretle.

## Çıktı modülleri
- Sorumluluk temeli ve taraf matrisi.
- İspat ve delil (log/bilirkişi) gereksinim listesi.
- Tazminat talebi veya savunma stratejisi taslağı.
<<<BECERI>>>
slug: ab-yz-tuzugu-risk-siniflandirma
ad: AB Yapay Zekâ Tüzüğü ve Risk Sınıflandırması
aciklama: Müvekkilin yapay zekâ sistemi AB pazarına ürün veya hizmet sunduğunda ya da karşılaştırmalı uyum hedeflendiğinde AB Yapay Zekâ Tüzüğü kapsamında yasak/yüksek riskli/sınırlı risk sınıflandırması ve yükümlülükler değerlendirildiğinde kullanılır.
<<<GOVDE>>>
# AB Yapay Zekâ Tüzüğü ve Risk Sınıflandırması

## Görev
Bir yapay zekâ sisteminin AB Yapay Zekâ Tüzüğü (Regulation (EU) 2024/1689) kapsamında risk sınıfını belirlemek ve buna bağlı yükümlülükleri tespit etmek; Türkiye için bunun bağlayıcı değil karşılaştırmalı/sözleşmesel bir referans olduğunu netleştirmek.

## Soğuk başlangıç (intake)
1. Sistem AB'deki kullanıcılara/pazara sunuluyor mu, çıktısı AB'de kullanılıyor mu?
2. Müvekkilin rolü: sağlayıcı (provider), uygulayıcı (deployer), ithalatçı, dağıtıcı?
3. Sistem ne yapıyor: biyometrik tanıma, kredi/işe alım skorlama, kritik altyapı, genel amaçlı model (GPAI)?
4. Mevcut uyum belgeleri (teknik dokümantasyon, uygunluk değerlendirmesi) var mı?

## Denetim şeması
1. **Uygulanabilirlik**: Tüzük Türkiye'de doğrudan yürürlükte değildir. AB'ye ürün/hizmet sunuluyorsa ülke-dışı etki nedeniyle uygulanabilir; yalnız Türkiye içiyse yön gösterici/sözleşmesel referanstır. Ara sonuç: bağlayıcı mı, referans mı.
2. **Risk sınıfı**: (a) Yasak uygulamalar (ör. sosyal puanlama, manipülatif sistemler); (b) Yüksek riskli sistemler (biyometri, eğitim, istihdam, kredi, kamu hizmeti, kritik altyapı) — uygunluk değerlendirmesi, risk yönetimi, veri yönetişimi, insan gözetimi, kayıt tutma yükümlülükleri; (c) Sınırlı risk — şeffaflık (örn. sohbet botu/derin sahte etiketleme); (d) Asgari risk.
3. **GPAI/temel model**: Genel amaçlı modeller için teknik dokümantasyon, telif uyum politikası ve sistemik risk eşiği yükümlülükleri.
4. **Rol bazlı yükümlülük**: Sağlayıcı ve uygulayıcı için farklı görevler; sözleşmeyle rollerin ve sorumlulukların netleştirilmesi gerekir.
5. **Türkiye'ye yansıma**: Tüzük yükümlülükleri Türk müvekkiline ancak sözleşme veya AB'ye erişim üzerinden gelir; Türkiye'de paralel uyum çoğu zaman KVKK + sektörel mevzuatla sağlanır.

Tüzük metni ve yürürlük takvimi sık güncellenir; her atıfta resmî AB kaynağından versiyon kontrol et, künyeyi [doğrulanacak] işaretle.

## Çıktı modülleri
- Risk sınıflandırma sonucu ve gerekçesi.
- Rol bazlı yükümlülük tablosu.
- Türkiye-AB uyum köprüsü ve sözleşmesel aktarım önerisi.
<<<BECERI>>>
slug: yz-sozlesmeleri-risk-dagitimi
ad: Yapay Zekâ Sözleşmeleri ve Sözleşmesel Risk Dağıtımı
aciklama: Yapay zekâ modeli geliştirme, lisanslama, API kullanımı, SaaS veya entegrasyon sözleşmeleri hazırlanırken ya da incelenirken sorumluluk, veri kullanımı, fikri mülkiyet, performans garantisi ve tazminat maddeleri tasarlandığında kullanılır.
<<<GOVDE>>>
# Yapay Zekâ Sözleşmeleri ve Sözleşmesel Risk Dağıtımı

## Görev
Yapay zekâ geliştirme/lisans/SaaS/API sözleşmelerinde tarafların risk, veri, fikri mülkiyet ve sorumluluk dengesini TBK çerçevesinde tasarlamak veya incelemek; eksik, asimetrik veya geçersiz şartları tespit edip redline önermek.

## Soğuk başlangıç (intake)
1. Sözleşme tipi: model geliştirme/eser, lisans, API/SaaS abonelik, entegrasyon/danışmanlık?
2. Müvekkil hangi taraf: sağlayıcı mı, kullanan/alıcı mı?
3. Eğitim/girdi/çıktı verisi kime ait, modeli iyileştirmede kullanılıyor mu?
4. Çıktı üzerinde fikri hak kime; ticari sır ve KVKK boyutu var mı?

## Denetim şeması
1. **Konu ve tip tayini**: Eser/geliştirme ağırlıklıysa TBK eser sözleşmesi (m.470 vd.) ve ayıba karşı tekeffül; sürekli hizmet/lisans ise hizmet/atipik sözleşme. Ara sonuç: hangi tip ve emredici hükümler.
2. **Veri ve KVKK maddeleri**: Girdi verisinin model eğitiminde kullanımı için açık yetki; veri işleyen sıfatı doğuyorsa KVKK m.12 uyumlu veri işleme sözleşmesi ve m.9 aktarım taahhütleri. Eksikse uyum açığı.
3. **Fikri mülkiyet**: Çıktı ve modelin hak sahipliği, lisans kapsamı, üçüncü kişi açık kaynak/lisans uyumu (FSEK/SMK). "Çıktı üzerinde hak garanti edilemez" gerçeğini sözleşmeye yansıt.
4. **Performans ve sorumluluk**: SLA, doğruluk/halüsinasyon riskine ilişkin garanti sınırları; sorumluluk sınırlaması maddeleri TBK m.115 (ağır kusur/kasıtta geçersizlik) ve genel işlem koşulu denetimi (m.20-25) süzgecinden geçirilir.
5. **Tazminat/rücu**: Üçüncü kişi taleplerinde tazmin (indemnity), veri ihlali ve fikri hak ihlali için tahsis; cezai şart ve fesih.

Emredici hüküm ve tüketici işlemi varsa 6502 TKHK ek denetimi. İçtihat künyesini [doğrulanacak] işaretle.

## Çıktı modülleri
- Risk maddesi haritası (veri/IP/sorumluluk/SLA).
- Redline ve alternatif lafız önerileri.
- Müzakere notu ve risk skoru.
<<<BECERI>>>
slug: telif-fikri-mulkiyet-yz
ad: Yapay Zekâ ve Fikri Mülkiyet
aciklama: Üretken yapay zekânın eğitiminde eser kullanımı, ürettiği içeriğin eser/tasarım/marka sahipliği, telif ihlali iddiası veya açık kaynak lisans uyumu gündeme geldiğinde FSEK ve SMK çerçevesinde değerlendirme yapıldığında kullanılır.
<<<GOVDE>>>
# Yapay Zekâ ve Fikri Mülkiyet

## Görev
Yapay zekâ ile eser/içerik ilişkisini iki yönden çözmek: girdi tarafında eğitim verisi olarak eser kullanımının telif boyutu; çıktı tarafında üretilen içeriğin hak sahipliği ve ihlal değerlendirmesi.

## Soğuk başlangıç (intake)
1. Sorun girdi tarafında mı (eğitim verisinde eser kullanımı) yoksa çıktı tarafında mı (üretilen içerik)?
2. Üretilen çıktı esere benzer mi; somut bir eserin kopyası/işlemesi iddiası var mı?
3. Modelin lisansı/açık kaynak bileşenleri ve kullanım koşulları neler?
4. Müvekkil hak sahibi mi, kullanıcı mı, geliştirici mi?

## Denetim şeması
1. **Çıktıda eser sahipliği**: FSEK m.1/B ve m.8 — eser, sahibinin hususiyetini taşıyan fikrî üründür ve sahibi gerçek kişidir. Tamamen otomatik üretilen çıktı, insan hususiyeti yoksa "eser" sayılmayabilir; insanın yaratıcı katkısı oranında koruma tartışılır. Ara sonuç: çıktı korunan eser mi.
2. **Eğitim verisinde kullanım**: Korunan eserlerin izinsiz model eğitiminde çoğaltılması (m.22) ve işlenmesi (m.21) mali hakları ilgilendirir; FSEK istisnaları (m.30 vd.) dar yorumlanır, genel "metin-veri madenciliği" istisnası Türk hukukunda açıkça düzenlenmemiştir.
3. **İhlal değerlendirmesi**: Çıktı somut bir eserin kopyası/işlemesi ise tecavüz; benzerlik ve esinlenme ayrımı yapılır. Tecavüzde ref/men (FSEK m.66-67) ve tazminat (m.68 — üç kata kadar) gündeme gelir.
4. **Marka/tasarım/buluş**: SMK kapsamında YZ üretimi tasarım/markada gerçek hak sahipliği; buluşta mucit gerçek kişi olmalıdır.
5. **Lisans uyumu**: Açık kaynak ve veri seti lisans şartlarına uyum sözleşmesel ve telifsel olarak ayrı denetlenir.

FSHM uygulaması için karararama.yargitay.gov.tr; AB ve ABD'deki davalar yalnız karşılaştırmalı kaynaktır, künye [doğrulanacak].

## Çıktı modülleri
- Girdi/çıktı telif risk haritası.
- Eser/koruma değerlendirme notu.
- İhlal iddiasına karşı savunma veya hak talebi taslağı.
<<<BECERI>>>
slug: yz-yonetisim-uyum-programi
ad: Kurumsal Yapay Zekâ Yönetişimi ve Uyum Programı
aciklama: Bir kurumda yapay zekâ sistemlerinin geliştirilmesi veya kullanılması için iç politika, etki değerlendirmesi, envanter, insan gözetimi ve sorumluluk yapısı kurulması istendiğinde proaktif uyum programı tasarlandığında kullanılır.
<<<GOVDE>>>
# Kurumsal Yapay Zekâ Yönetişimi ve Uyum Programı

## Görev
Bir kurumun yapay zekâ kullanımını hukuki riske karşı yöneten iç yönetişim programını tasarlamak: envanter, politika, etki değerlendirmesi, insan gözetimi ve sorumluluk dağılımı.

## Soğuk başlangıç (intake)
1. Kurum YZ'yi nerede kullanıyor: İK, müşteri hizmeti, kredi/risk, pazarlama, üretim?
2. Sistemler iç geliştirme mi, üçüncü taraf (kapalı API) mi?
3. Kişisel veri ve özel nitelikli veri işleniyor mu; VERBİS kaydı var mı?
4. Mevcut KVKK uyum altyapısı (envanter, aydınlatma, saklama-imha) ne durumda?

## Denetim şeması
1. **Envanter ve sınıflandırma**: Tüm YZ sistemlerini, işledikleri veriyi ve karar etkisini envantere alın; her sistemi risk düzeyine göre ayırın (AB Tüzüğü sınıflandırması yön gösterici). Ara sonuç: yüksek etkili sistemler önceliklendirilir.
2. **KVKK uyumu**: m.4 ilkeler, m.5-6 işleme şartı, m.10 aydınlatma (otomatik karar açıklaması), m.11 hak süreçleri, m.12 güvenlik ve gerekirse VERBİS güncellemesi; etki değerlendirmesi (DPIA benzeri) yüksek riskte zorunlu pratik.
3. **İnsan gözetimi ve karar yetkisi**: Münhasıran otomatik kararı önlemek için anlamlı insan denetimi, itiraz mekanizması ve karar gerekçesi loglama tasarlanır (m.11/1-g riski yönetimi).
4. **Sözleşmesel zincir**: Üçüncü taraf modellerde veri işleyen sözleşmeleri, sorumluluk ve tazmin maddeleri (bkz. YZ sözleşmeleri becerisi).
5. **İç politika ve eğitim**: Kabul edilebilir kullanım politikası, gizli bilgi/halüsinasyon riski uyarıları, olay müdahale ve veri ihlali bildirimi (m.12) akışı.

Kurul rehberlerini kvkk.gov.tr'den güncel takip et; doğrulanmamış kaynağı [doğrulanacak] işaretle.

## Çıktı modülleri
- YZ envanteri ve risk sınıflandırma tablosu.
- Uyum boşluğu raporu ve aksiyon planı.
- İç politika ve insan gözetimi prosedürü taslağı.
<<<BECERI>>>
slug: sektorel-yz-uygulama
ad: Sektörel Yüksek Riskli Yapay Zekâ Uygulamaları
aciklama: Sağlıkta klinik karar destek, bankacılıkta kredi skorlama, istihdamda işe alım eleme, sigortada fiyatlama veya kamuda otomatik işlem gibi yüksek etkili yapay zekâ kullanımlarında sektörel mevzuat ile KVKK birlikte değerlendirildiğinde kullanılır.
<<<GOVDE>>>
# Sektörel Yüksek Riskli Yapay Zekâ Uygulamaları

## Görev
Bireyin haklarını doğrudan etkileyen sektörel YZ kullanımlarında uygulanacak özel mevzuatı KVKK ile birlikte değerlendirip uyum ve sorumluluk şemasını çıkarmak.

## Soğuk başlangıç (intake)
1. Hangi sektör: sağlık, bankacılık/kredi, istihdam, sigorta, kamu idaresi, sermaye piyasası?
2. YZ kararı bireyi nasıl etkiliyor (kredi reddi, işe alım eleme, tanı önerisi, prim)?
3. Sektörel düzenleyici (BDDK, SGK, TİTCK, SPK, ilgili idare) onay/kayıt gerektiriyor mu?
4. Nihai kararı insan mı veriyor, sistem mi?

## Denetim şeması
1. **Sektör normu tespiti**: Sağlıkta hekimin özen ve aydınlatılmış onam yükümlülüğü (1219/3359, TBK vekâlet), klinik karar destek hekimin sorumluluğunu kaldırmaz; bankacılık/kredide 5411 ve düzenlemeleri; istihdamda 4857 ve eşit davranma; sigortada 5684/TTK; kamuda 2577 İYUK ve gerekçeli işlem. Ara sonuç: baskın sektörel norm.
2. **KVKK katmanı**: Her halde m.4-6 işleme şartı, m.10 aydınlatma ve m.11/1-g otomatik karar itirazı uygulanır; sağlık/biyometrik veride m.6 özel nitelikli rejim.
3. **İnsan denetimi**: Tanı, kredi reddi ve işe alım eleme gibi kararlarda anlamlı insan gözetimi hem sorumluluk hem KVKK açısından kritiktir; biçimsel onay yetmez.
4. **Ayrımcılık riski**: Modelin korunan özellikler üzerinden dolaylı ayrımcılık üretmesi eşitlik ilkesi ve m.4 doğruluk/hukuka uygunluk ihlali doğurabilir; istihdamda 4857 ayrımcılık tazminatı.
5. **Sorumluluk**: Hatalı sektörel kararda sektörel sorumluluk (ör. hekim/banka) ile YZ sağlayıcı sorumluluğu (bkz. sorumluluk becerisi) birlikte değerlendirilir.

İçtihat için karararama.yargitay.gov.tr ve karararama.danistay.gov.tr; künye [doğrulanacak].

## Çıktı modülleri
- Sektör + KVKK çifte uyum tablosu.
- İnsan gözetimi ve ayrımcılık riski değerlendirmesi.
- Sektörel onay/kayıt yol haritası.
<<<BECERI>>>
slug: dava-usul-gorev-yetki
ad: Yapay Zekâ Uyuşmazlıklarında Dava, Usul ve Görev-Yetki
aciklama: Yapay zekâ kaynaklı bir uyuşmazlık yargıya veya Kurula taşınırken görevli merci, yetkili mahkeme, başvuru yolu, dava türü, ihtiyati tedbir ve süreler belirlendiğinde ve usul yol haritası çıkarıldığında kullanılır.
<<<GOVDE>>>
# Yapay Zekâ Uyuşmazlıklarında Dava, Usul ve Görev-Yetki

## Görev
Yapay zekâ kaynaklı uyuşmazlıkta doğru merci, dava türü, yetkili mahkeme ve süreyi tespit ederek usul yol haritası ve gerekirse ihtiyati tedbir stratejisi çıkarmak.

## Soğuk başlangıç (intake)
1. Uyuşmazlığın özü: KVKK ihlali, sözleşmeye aykırılık, haksız fiil/tazminat, fikri hak, kamu işlemi?
2. Taraflar tacir/tüketici mi; aralarında tahkim veya yetki sözleşmesi var mı?
3. Bir Kurul/idare işlemi mi tebliğ edildi, tebliğ tarihi nedir?
4. Acil koruma (içerik kaldırma, delil tespiti, yürütmenin durdurulması) gerekiyor mu?

## Denetim şeması
1. **Yol ayrımı**: KVKK ihlalinde önce m.13 veri sorumlusuna başvuru, ardından m.14 Kurula şikâyet; Kurul kararına karşı idari yargı (İYUK m.7, kural 60 gün). Tazminat talebi için adli yargıda dava (TBK temelli). Ara sonuç: idari mi adli mi.
2. **Görev-yetki (adli)**: Sözleşme/haksız fiilde HMK genel hükümleri (m.5 vd.); ticari işte ticaret mahkemesi (TTK m.4, m.5/A dava şartı arabuluculuk); tüketici işleminde tüketici mahkemesi/hakem heyeti (6502); fikri hakta FSHM; kişilik hakkında asliye hukuk.
3. **Dava türü ve talep**: Tespit, eda (tazminat), men/ref (kişilik hakkı TMK m.25, FSEK m.66-67) veya iptal (kamu işlemi). Talep sonucu net ve HMK m.119 unsurlarıyla kurulur.
4. **İhtiyati koruma**: HMK m.389 vd. ihtiyati tedbir (içerik/erişim), m.400 vd. delil tespiti (model çıktısı/log), kamu işleminde İYUK m.27 yürütmenin durdurulması.
5. **İspat ve bilirkişi**: YZ uyuşmazlıkları teknik bilirkişi gerektirir (HMK m.266); log, model dokümanı ve çıktı kayıtları erkenden güvenceye alınmalı.

İçtihat ve görev tartışmaları için karararama portalları; künyeyi [doğrulanacak] işaretle, esas/karar numarası uydurma.

## Çıktı modülleri
- Merci/dava türü/süre yol haritası.
- İhtiyati tedbir-delil tespiti stratejisi.
- Görev-yetki ve arabuluculuk kontrol notu.
<<<BECERI>>>
slug: musteri-iletisim-risk-bilgilendirme
ad: Müvekkil İletişimi ve Yapay Zekâ Risk Bilgilendirmesi
aciklama: Teknik bir yapay zekâ konusunun hukuki risklerini müvekkile yalın ve doğru biçimde anlatmak, beklenti yönetimi yapmak ve mevzuat belirsizliğini şeffafça aktarmak gerektiğinde bilgilendirme ve risk haritası üretildiğinde kullanılır.
<<<GOVDE>>>
# Müvekkil İletişimi ve Yapay Zekâ Risk Bilgilendirmesi

## Görev
Yapay zekâya ilişkin teknik-hukuki riskleri müvekkilin anlayacağı yalın Türkçeyle, hukuki doğruluğu koruyarak aktarmak; özellikle Türkiye'de yatay YZ kanunu olmamasından doğan belirsizliği ve AB Tüzüğü'nün bağlayıcı olmadığını net biçimde iletmek.

## Soğuk başlangıç (intake)
1. Müvekkilin teknik/hukuki bilgi düzeyi ve asıl kaygısı nedir?
2. Hangi karar verilecek: ürünü yayınlamak, veri kullanmak, sözleşme imzalamak, uyuşmazlığa girmek?
3. Risk toleransı ve zaman/bütçe kısıtı nedir?
4. AB pazarına dokunan bir boyut var mı (uygulanabilir hukuk farkı)?

## Denetim şeması
1. **Çerçeveleme**: Sorunu hukuki katmanlara ayırarak anlat (veri/KVKK, sözleşme, sorumluluk, fikri mülkiyet); her katmanda "kesin / muhtemel / belirsiz" şeklinde risk seviyesi belirt. Ara sonuç: müvekkil neyin kesin neyin gri olduğunu görür.
2. **Belirsizliğin dürüst aktarımı**: Türkiye'de YZ'ye özgü yatay kanun yok; mevcut normların uyarlanmasıyla çalışılıyor ve içtihat henüz oturmuş değil. Bunu olduğu gibi söyle; kesinlik vaadi verme.
3. **Uygulanır hukuk uyarısı**: AB Yapay Zekâ Tüzüğü ve GDPR yalnızca AB'ye dokunulduğunda devreye girer; Türkiye içi kullanım için KVKK + sektörel mevzuat esastır.
4. **Aksiyon ve öncelik**: Riski azaltan somut adımları (aydınlatma, insan gözetimi, sözleşme maddesi, log) öncelik sırasıyla öner; her adımın hangi riski düşürdüğünü açıkla.
5. **Karar müvekkilin**: Seçenekleri ve sonuçlarını sun; ticari kararı müvekkile bırak, hukuki çerçeveyi sen koy.

İddialı her hukuki dayanağı mevzuat madde/fıkra ile bağla; doğrulanmamış içtihat künyesini paylaşma, [doğrulanacak] işaretle.

## Çıktı modülleri
- Yalın dilde risk haritası (kesin/muhtemel/belirsiz).
- Öncelikli aksiyon listesi ve gerekçesi.
- Bilgilendirme notu / e-posta taslağı.
<<<SON>>>
