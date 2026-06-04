export const meta = {
  name: 'ornek-dosya-uretimi',
  description: 'Türk hukuku için anonim/kurgusal örnek dava dosyaları üretir (senaryo başına bir ajan)',
  phases: [{ title: 'Senaryolar', detail: 'her senaryo için olay özeti + gerçekçi belgeler' }],
};

const A = (typeof args === 'string') ? JSON.parse(args) : (args || {});
const BASE = A.base_dir;
const SENARYOLAR = A.senaryolar || [];
if (!SENARYOLAR.length) throw new Error('args.senaryolar boş');

function prompt(s) {
  const belgeler = s.belgeler.map((b) => `  - ${b}`).join('\n');
  const eklentiler = (s.eklentiler || []).join(', ');
  return `Sen deneyimli bir Türk hukukçususun. Görevin, "${s.baslik}" konulu TAMAMEN KURGUSAL ve
ANONİM bir örnek dava dosyası hazırlamak. Bu dosya, hukuk skill'lerini gerçekçi bir senaryoyla
denemek için kullanılacak. Çıktın dosyalara yazılacak; insana mesaj değildir.

Alan: ${s.alan}
İlgili eklentiler (dosyanın denenebileceği): ${eklentiler}

ŞU KLASÖRE yaz (Write tool, mutlak yol): \`${BASE}/${s.slug}/\`
Oluşturulacak dosyalar:
  - README.md   (olay özeti + kullanım)
${belgeler}

KURALLAR:
- TAMAMEN KURGUSAL ve ANONİM. Gerçek kişi, şirket, TCKN, adres, esas/karar numarası KULLANMA.
  Kurgusal ve açıkça kurgusal isimler kullan (ör. "Demir Yapı Lt. Şti.", "A. Yılmaz",
  "(M) Bankası A.Ş."). Tarih ve tutarlar gerçekçi ama uydurma olsun.
- Her dosyanın EN ÜSTÜNE şu satırı koy:
  "> ⚠️ Bu belge tamamen KURGUSAL ve anonimdir; gerçek bir kişi, olay veya dava ile ilgisi yoktur. Eğitim/deneme amaçlıdır."
- README.md şunları içersin:
  1) Kısa olay özeti (taraflar [kurgusal], uyuşmazlık, talepler)
  2) Kronoloji (tarih sırasıyla 5-8 olay)
  3) "Hangi becerilerle denenebilir" — ${eklentiler} eklentilerinden somut beceri/işlem önerileri
  4) "Örnek sorular" — kullanıcının Claude'a sorabileceği 3-5 soru
  5) Klasördeki belgelerin kısa listesi
- Belge dosyaları gerçekçi olsun: ihtarname/tebligat/sözleşme/dilekçe metinleri usule uygun
  yapıda; .csv dosyaları geçerli CSV (başlık satırı + veri) olsun.
- Mevzuata atıf yaparken madde/fıkra doğru olsun (ör. İş K. m.17, TBK m.299, İYUK m.7).
  İçtihat künyesi UYDURMA; gerekiyorsa "[doğrulanacak]" yaz.
- Yalnızca Türkçe.

Tüm dosyaları yazdıktan sonra tek satır onay döndür: "yazildi: ${s.slug}, <dosya sayısı> dosya".`;
}

phase('Senaryolar');
await parallel(
  SENARYOLAR.map((s) => () =>
    agent(prompt(s), { label: `senaryo:${s.slug}`, phase: 'Senaryolar', agentType: 'general-purpose' })
  )
);
log(`${SENARYOLAR.length} senaryo denendi (doğrulama diskte).`);
return { denenen: SENARYOLAR.length };
