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
