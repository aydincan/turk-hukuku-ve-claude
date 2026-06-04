export const meta = {
  name: 'turk-hukuku-icerik-uretimi',
  description: 'Her Türk hukuku eklentisi için uzman ajan, metodoloji referansı + uzman beceri gövdelerini Türkçe yazar',
  phases: [
    { title: 'Üretim', detail: 'eklenti başına bir uzman hukukçu ajan içerik yazar' },
  ],
};

const A = (typeof args === 'string') ? JSON.parse(args) : (args || {});
const PARTS = A.parts_dir;
const CATALOG = A.catalog_path;
const SLUGS = A.slugs || [];
if (!SLUGS.length) throw new Error('args.slugs boş — args: ' + JSON.stringify(args).slice(0, 200));

const SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    slug: { type: 'string' },
    ok: { type: 'boolean' },
    n_beceri: { type: 'integer' },
    not: { type: 'string', description: 'kısa durum/sorun notu' },
  },
  required: ['slug', 'ok', 'n_beceri'],
};

function buildPrompt(slug) {
  return `Sen Türk hukukunun "${slug}" alanında uzman, uygulamaya hâkim bir hukukçusun.
Görevin: Claude Code için bu alana ait bir eklentinin UZMAN BECERİLERİNİ ve bir METODOLOJİ
REFERANS belgesini TÜRKÇE yazmak. Çıktın bir dosyaya yazılacak; insana mesaj değildir.

ADIM 1 — BAĞLAM: \`${CATALOG}\` dosyasını Read ile aç; \`eklentiler\` dizisinde
slug == "${slug}" olan girdiyi bul (baslik, aciklama, kanunlar, anahtar). Bu alanın
gerçek Türk mevzuatına ve uygulamasına sadık kal.

ADIM 2 — 9 ila 13 adet UZMAN beceri tasarla. NOT: giriş/triyaj becerisi 'genel-bakis'
OTOMATİK üretiliyor; ONU YAZMA. Becerileri bu alanın gerçek iş ihtiyaçlarına göre seç:
temel kavram/sistematik, ana denetim şeması ve şartlar, önemli alt-konular, dava/usul ve
görev-yetki, dilekçe/sözleşme/başvuru taslağı, süreler ve zamanaşımı, ispat/delil,
risk-strateji, müvekkil/karşı taraf iletişimi gibi — yalnızca ALANA UYGUN olanları.

Her beceri için:
- slug: yalnızca [a-z0-9-]; Türkçe harf sadeleştir (ı→i, ş→s, ğ→g, ü→u, ö→o, ç→c).
- ad: Türkçe başlık.
- aciklama: 1-2 cümle; becerinin NE ZAMAN kullanılacağını anlatan, eşleştirmeye yarayan
  zengin Türkçe açıklama (çift tırnak KULLANMA, tek satır).
- govde: ≈250-450 kelime Markdown. İskelet:
    # <ad>
    ## Görev
    ## Soğuk başlangıç (intake)   → alana uygun 3-5 kısa soru
    ## Denetim şeması             → GERÇEK madde atıflarıyla adım adım (şartlar, istisnalar,
                                    ispat yükü, ara sonuç). Somut ve uygulanabilir olsun.
    ## Çıktı modülleri

ADIM 3 — referans: ≈400-650 kelimelik metodoloji belgesi (alanın sistematiği, başat
normlar ve madde atıfları, çalışma yöntemi, kaynak hijyeni).

KATI KURALLAR:
- Yalnızca Türkçe. Hukuki ve uygulanabilir; ders kitabı girişi değil, çalışan hukukçu dili.
- Mevzuatı madde/fıkra ile DOĞRU ver (ör. "TBK m.49", "TCK m.21", "HMK m.119", "İİK m.67").
  Kanun numaralarını ve madde numaralarını doğru kullan.
- İÇTİHAT: Yargıtay/Danıştay/AYM/BAM KARAR NUMARASI **UYDURMA**. İlkesel atıf yap ve künyeyi
  \`[doğrulanacak]\` diye işaretle ya da arama kaynağını an (karararama.yargitay.gov.tr,
  karararama.danistay.gov.tr, kararlarbilgibankasi.anayasa.gov.tr). ASLA sahte esas/karar
  numarası yazma.
- 'Kaynak kuralı', 'Bu beceri ne yapmaz', 'Plugin bağlamı' ve sorumluluk reddi bloklarını
  YAZMA — bunlar üretici tarafından otomatik ekleniyor. Sadece maddi gövdeye odaklan.

ADIM 4 — Çıktıyı AYNEN şu formatta, ŞU dosyaya Write ile yaz (mutlak yol):
\`${PARTS}/${slug}.part.md\`

DOSYA FORMATI (aynen bu sınırlayıcılar, başka hiçbir şey ekleme — kod bloğu/markdown çiti yok):
<<<REFERANS>>>
...referans markdown (çok satırlı)...
<<<BECERI>>>
slug: temel-kavramlar-ve-sistem
ad: Temel Kavramlar ve Sistematik
aciklama: ... tek satır ...
<<<GOVDE>>>
...govde markdown (çok satırlı)...
<<<BECERI>>>
slug: ...
ad: ...
aciklama: ...
<<<GOVDE>>>
...
<<<SON>>>

Kurallar: 'aciklama' TEK satır. 'slug/ad/aciklama' satırları '<<<GOVDE>>>' den ÖNCE gelir.
Gövde bir sonraki '<<<BECERI>>>' veya '<<<SON>>>' e kadar sürer. En sonda '<<<SON>>>' olsun.

ÖNEMLİ: Asıl teslimat DOSYAYI YAZMAKTIR. Mutlaka Write tool ile yukarıdaki mutlak yola yaz.
Dosyayı yazdıktan sonra yalnızca tek satırlık onay döndür: \`yazildi: ${slug}, <beceri sayısı> beceri\`.
İçeriği sohbete METİN olarak dökme; dosyaya yaz.`;
}

phase('Üretim');

// Sıralı küçük gruplar — aynı anda 78 ajan fırlatmanın yarattığı yığılmayı önler.
// Şema (StructuredOutput) yok: asıl teslimat dosya yazımı; doğrulama diskte yapılır.
const CHUNK = (A.chunk && Number(A.chunk)) || 8;
let denenen = 0;
for (let i = 0; i < SLUGS.length; i += CHUNK) {
  const batch = SLUGS.slice(i, i + CHUNK);
  log(`Grup ${Math.floor(i / CHUNK) + 1} (${batch.length}): ${batch.join(', ')}`);
  await parallel(
    batch.map((slug) => () =>
      agent(buildPrompt(slug), {
        label: `yaz:${slug}`,
        phase: 'Üretim',
        agentType: 'general-purpose',
      })
    )
  );
  denenen += batch.length;
}

log(`Denenen: ${denenen} eklenti (${Math.ceil(SLUGS.length / CHUNK)} grup). Doğrulama diskte.`);
return { denenen };
