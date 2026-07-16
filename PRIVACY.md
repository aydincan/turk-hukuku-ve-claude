# Gizlilik Politikası — Privacy Policy

Bu proje bir **Agent Skills** (beceri) koleksiyonudur; yalnızca düz metin (Markdown)
talimatlardan oluşur. **Becerilerin kendisi çalıştırılabilir kod, hook, arka plan süreci,
telemetri veya ağ çağrısı içermez ve bir MCP sunucusu paketlemez.** Beceriler, kuruluysa
isteğe bağlı MCP sunucularını kullanmayı önerebilir (bkz. [İsteğe bağlı MCP sunucuları](#isteğe-bağlı-mcp-sunucuları)).

## Veri toplama: YOK

- Bu skill'ler **hiçbir kişisel veri toplamaz, saklamaz veya iletmez.**
- Hiçbir uzak sunucuya veri göndermez; tamamen **yerel** çalışır — kullandığınız yapay zekâ
  aracının (Claude Code / OpenAI Codex / Google Gemini CLI) içinde, sizin makinenizde ya da
  oturumunuzda.
- Proje sahibi kullanıcıların verilerine **erişmez**; herhangi bir analitik veya izleme yoktur.

## İsteğe bağlı MCP sunucuları

Beceriler, **kuruluysa** resmî metni doğrudan kaynağından çekmek için ayrı ve isteğe bağlı
MCP sunucularını (`turk-hukuku-mevzuat-mcp`, `turk-hukuku-ictihat-mcp`) kullanmanızı önerebilir.
Bu sunucular bu depoya **dahil değildir**; ayrı olarak kurulur ve her birinin kendi gizlilik
notuna tabidir.

- Bu sunucular, **yalnızca sizin yaptığınız sorguyu** ilgili resmî ve kamuya açık kaynaklara
  (`mevzuat.gov.tr`, UYAP Emsal, Yargıtay / Danıştay / AYM karar siteleri) iletir.
- **Hiçbir kişisel veri toplamaz, saklamaz veya proje sahibine göndermez; telemetri yoktur.**
- Sorgu metninizde müvekkil veya kişisel veri bulundurmamaya dikkat edin (KVKK, meslek sırrı).

## Kullanıcı girdileri

Skill'lere sağladığınız belgeler ve metinler, kullandığınız yapay zekâ aracının kendi
gizlilik ve veri işleme politikalarına tabidir — bu proje o işlemeye taraf değildir.
Müvekkil/kişisel veri kullanırken kendi KVKK ve meslek sırrı yükümlülüklerinizi gözetin
(bkz. [`SORUMLULUK-REDDI.md`](./SORUMLULUK-REDDI.md)).

## İletişim

Sorular için bu depoda bir **issue** açabilirsiniz.

---

**In English:** This project is a collection of Agent Skills made only of plain-text
(Markdown) instructions. The skills themselves contain **no executable code, hooks, telemetry,
or network calls** and **bundle no MCP server**, and they **collect, store, or transmit no
personal data**. They run entirely locally inside the AI tool you use. The skills may, however,
recommend optional, separately-installed MCP servers (`turk-hukuku-mevzuat-mcp`,
`turk-hukuku-ictihat-mcp`) which, when installed, send **only your query** to official public
sources (`mevzuat.gov.tr`, UYAP Emsal, etc.), store nothing, and have no telemetry. Any inputs
you provide are subject to that tool's own privacy policy, not this project's.
