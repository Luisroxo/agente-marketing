# Componentes das Seções 5-8 - Lovable.dev

## 🏆 **FORMSECTION5.TSX - Concorrência e Diferenciais**

```tsx
import React from 'react';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Checkbox } from '@/components/ui/checkbox';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

interface FormData {
  principaisConcorrentes: string;
  principalDiferencial: string;
  marketingConcorrentes: string[];
}

interface Props {
  data: FormData;
  updateData: (updates: Partial<FormData>) => void;
}

const FormSection5: React.FC<Props> = ({ data, updateData }) => {
  const handleMarketingConcorrentesChange = (value: string, checked: boolean) => {
    const current = data.marketingConcorrentes || [];
    if (checked) {
      updateData({ marketingConcorrentes: [...current, value] });
    } else {
      updateData({ marketingConcorrentes: current.filter(item => item !== value) });
    }
  };

  const marketingOptions = [
    { value: 'redes-sociais', label: 'Redes sociais' },
    { value: 'google-ads', label: 'Google Ads' },
    { value: 'panfletos', label: 'Panfletos' },
    { value: 'radio-tv', label: 'Rádio/TV' },
    { value: 'outdoor', label: 'Outdoor' },
    { value: 'eventos', label: 'Eventos' },
    { value: 'parcerias', label: 'Parcerias' },
    { value: 'boca-a-boca', label: 'Boca a boca' },
    { value: 'pouco-marketing', label: 'Não fazem muito marketing' },
    { value: 'outros', label: 'Outros' }
  ];

  return (
    <div className="space-y-6">
      {/* Principais Concorrentes */}
      <div>
        <Label htmlFor="principaisConcorrentes" className="text-base font-medium text-gray-700">
          🎯 Principais concorrentes *
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Cite 2-3 empresas que considera como principais concorrentes
        </p>
        <Input
          id="principaisConcorrentes"
          value={data.principaisConcorrentes}
          onChange={(e) => updateData({ principaisConcorrentes: e.target.value })}
          placeholder="Ex: Empresa A, Empresa B, Empresa C"
          className="mt-2 h-12"
          required
        />
      </div>

      {/* Principal Diferencial */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          💎 Seu principal diferencial *
        </Label>
        <Select value={data.principalDiferencial} onValueChange={(value) => updateData({ principalDiferencial: value })}>
          <SelectTrigger className="mt-2 h-12">
            <SelectValue placeholder="O que te destaca da concorrência?" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="preco-baixo">Preço mais baixo</SelectItem>
            <SelectItem value="qualidade-superior">Qualidade superior</SelectItem>
            <SelectItem value="atendimento-personalizado">Atendimento personalizado</SelectItem>
            <SelectItem value="localizacao-estrategica">Localização estratégica</SelectItem>
            <SelectItem value="inovacao-tecnologia">Inovação/tecnologia</SelectItem>
            <SelectItem value="tradicao-confianca">Tradição/confiança</SelectItem>
            <SelectItem value="variedade-produtos">Variedade de produtos</SelectItem>
            <SelectItem value="agilidade-rapidez">Agilidade/rapidez</SelectItem>
            <SelectItem value="outros">Outros</SelectItem>
          </SelectContent>
        </Select>
      </div>

      {/* Marketing dos Concorrentes */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          📢 Marketing dos concorrentes * (múltiplas opções)
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Como seus concorrentes fazem divulgação?
        </p>
        <div className="mt-3 grid grid-cols-1 md:grid-cols-2 gap-3">
          {marketingOptions.map((option) => (
            <div key={option.value} className="flex items-center space-x-2">
              <Checkbox
                id={`marketing-${option.value}`}
                checked={data.marketingConcorrentes?.includes(option.value) || false}
                onCheckedChange={(checked) => handleMarketingConcorrentesChange(option.value, checked as boolean)}
              />
              <Label htmlFor={`marketing-${option.value}`} className="text-sm cursor-pointer">
                {option.label}
              </Label>
            </div>
          ))}
        </div>
      </div>

      <div className="bg-yellow-50 p-4 rounded-lg border border-yellow-200">
        <p className="text-sm text-yellow-700">
          🔍 <strong>Análise competitiva:</strong> Entender a concorrência é fundamental para 
          posicionar sua empresa de forma única no mercado.
        </p>
      </div>
    </div>
  );
};

export default FormSection5;
```

---

## 💰 **FORMSECTION6.TSX - Vendas e Canais**

```tsx
import React from 'react';
import { Label } from '@/components/ui/label';
import { Checkbox } from '@/components/ui/checkbox';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

interface FormData {
  canaisVenda: string[];
  canalMaisVende: string;
  marketingAtual: string[];
}

interface Props {
  data: FormData;
  updateData: (updates: Partial<FormData>) => void;
}

const FormSection6: React.FC<Props> = ({ data, updateData }) => {
  const handleCanaisVendaChange = (value: string, checked: boolean) => {
    const current = data.canaisVenda || [];
    if (checked) {
      updateData({ canaisVenda: [...current, value] });
    } else {
      updateData({ canaisVenda: current.filter(item => item !== value) });
    }
  };

  const handleMarketingAtualChange = (value: string, checked: boolean) => {
    const current = data.marketingAtual || [];
    if (checked) {
      updateData({ marketingAtual: [...current, value] });
    } else {
      updateData({ marketingAtual: current.filter(item => item !== value) });
    }
  };

  const canaisVendaOptions = [
    { value: 'loja-fisica', label: 'Loja física' },
    { value: 'whatsapp', label: 'WhatsApp' },
    { value: 'instagram', label: 'Instagram' },
    { value: 'site-proprio', label: 'Site próprio' },
    { value: 'marketplace', label: 'Marketplace (Mercado Livre, etc)' },
    { value: 'telefone', label: 'Telefone' },
    { value: 'vendedor-externo', label: 'Vendedor externo' },
    { value: 'eventos-feiras', label: 'Eventos/feiras' },
    { value: 'outros', label: 'Outros' }
  ];

  const marketingAtualOptions = [
    { value: 'redes-organicas', label: 'Redes sociais orgânicas' },
    { value: 'google-ads', label: 'Google Ads' },
    { value: 'facebook-instagram-ads', label: 'Facebook/Instagram Ads' },
    { value: 'whatsapp-marketing', label: 'WhatsApp Marketing' },
    { value: 'email-marketing', label: 'E-mail marketing' },
    { value: 'panfletos', label: 'Panfletos' },
    { value: 'boca-a-boca', label: 'Boca a boca' },
    { value: 'parcerias', label: 'Parcerias' },
    { value: 'nao-faco', label: 'Não faço marketing' },
    { value: 'outros', label: 'Outros' }
  ];

  return (
    <div className="space-y-6">
      {/* Principais Canais de Venda */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          📦 Principais canais de venda * (múltiplas opções)
        </Label>
        <div className="mt-3 grid grid-cols-1 md:grid-cols-2 gap-3">
          {canaisVendaOptions.map((option) => (
            <div key={option.value} className="flex items-center space-x-2">
              <Checkbox
                id={`canal-${option.value}`}
                checked={data.canaisVenda?.includes(option.value) || false}
                onCheckedChange={(checked) => handleCanaisVendaChange(option.value, checked as boolean)}
              />
              <Label htmlFor={`canal-${option.value}`} className="text-sm cursor-pointer">
                {option.label}
              </Label>
            </div>
          ))}
        </div>
      </div>

      {/* Canal que Mais Vende */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          🏅 Canal que mais vende *
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Qual canal trouxe mais vendas nos últimos 12 meses?
        </p>
        <Select value={data.canalMaisVende} onValueChange={(value) => updateData({ canalMaisVende: value })}>
          <SelectTrigger className="mt-2 h-12">
            <SelectValue placeholder="Selecione o canal mais eficiente" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="loja-fisica">Loja física</SelectItem>
            <SelectItem value="whatsapp">WhatsApp</SelectItem>
            <SelectItem value="instagram">Instagram</SelectItem>
            <SelectItem value="site-proprio">Site próprio</SelectItem>
            <SelectItem value="marketplace">Marketplace</SelectItem>
            <SelectItem value="telefone">Telefone</SelectItem>
            <SelectItem value="vendedor-externo">Vendedor externo</SelectItem>
            <SelectItem value="eventos">Eventos</SelectItem>
            <SelectItem value="outros">Outros</SelectItem>
          </SelectContent>
        </Select>
      </div>

      {/* Marketing Atual */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          📊 Marketing atual * (múltiplas opções)
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Que tipo de marketing você faz atualmente?
        </p>
        <div className="mt-3 grid grid-cols-1 md:grid-cols-2 gap-3">
          {marketingAtualOptions.map((option) => (
            <div key={option.value} className="flex items-center space-x-2">
              <Checkbox
                id={`marketing-atual-${option.value}`}
                checked={data.marketingAtual?.includes(option.value) || false}
                onCheckedChange={(checked) => handleMarketingAtualChange(option.value, checked as boolean)}
              />
              <Label htmlFor={`marketing-atual-${option.value}`} className="text-sm cursor-pointer">
                {option.label}
              </Label>
            </div>
          ))}
        </div>
      </div>

      <div className="bg-green-50 p-4 rounded-lg border border-green-200">
        <p className="text-sm text-green-700">
          💡 <strong>Otimização de canais:</strong> Identificaremos quais canais têm mais potencial 
          para aumentar suas vendas baseado no seu perfil de negócio.
        </p>
      </div>
    </div>
  );
};

export default FormSection6;
```

---

## 🌐 **FORMSECTION7.TSX - Presença Digital**

```tsx
import React from 'react';
import { Label } from '@/components/ui/label';
import { Textarea } from '@/components/ui/textarea';
import { Checkbox } from '@/components/ui/checkbox';

interface FormData {
  redesSociais: string[];
  linksRedes: string;
  ferramentasUsa: string[];
}

interface Props {
  data: FormData;
  updateData: (updates: Partial<FormData>) => void;
}

const FormSection7: React.FC<Props> = ({ data, updateData }) => {
  const handleRedesSociaisChange = (value: string, checked: boolean) => {
    const current = data.redesSociais || [];
    if (checked) {
      updateData({ redesSociais: [...current, value] });
    } else {
      updateData({ redesSociais: current.filter(item => item !== value) });
    }
  };

  const handleFerramentasChange = (value: string, checked: boolean) => {
    const current = data.ferramentasUsa || [];
    if (checked) {
      updateData({ ferramentasUsa: [...current, value] });
    } else {
      updateData({ ferramentasUsa: current.filter(item => item !== value) });
    }
  };

  const redesSociaisOptions = [
    { value: 'instagram', label: 'Instagram', emoji: '📸' },
    { value: 'facebook', label: 'Facebook', emoji: '👥' },
    { value: 'whatsapp-business', label: 'WhatsApp Business', emoji: '💬' },
    { value: 'site-proprio', label: 'Site próprio', emoji: '🌐' },
    { value: 'google-meu-negocio', label: 'Google Meu Negócio', emoji: '📍' },
    { value: 'linkedin', label: 'LinkedIn', emoji: '💼' },
    { value: 'tiktok', label: 'TikTok', emoji: '🎵' },
    { value: 'youtube', label: 'YouTube', emoji: '🎥' },
    { value: 'nao-tenho', label: 'Não tenho presença online', emoji: '❌' },
    { value: 'outros', label: 'Outros', emoji: '➕' }
  ];

  const ferramentasOptions = [
    { value: 'whatsapp-business', label: 'WhatsApp Business', emoji: '💬' },
    { value: 'sistema-vendas', label: 'Sistema de vendas/PDV', emoji: '💳' },
    { value: 'planilhas', label: 'Planilhas Excel/Google', emoji: '📊' },
    { value: 'crm', label: 'CRM (RD, Pipedrive, etc)', emoji: '🎯' },
    { value: 'email-marketing', label: 'E-mail marketing', emoji: '📧' },
    { value: 'agendamento', label: 'Agendamento online', emoji: '📅' },
    { value: 'delivery-apps', label: 'Delivery apps', emoji: '🛵' },
    { value: 'nao-uso', label: 'Não uso ferramentas digitais', emoji: '❌' },
    { value: 'outros', label: 'Outros', emoji: '➕' }
  ];

  return (
    <div className="space-y-6">
      {/* Redes Sociais e Site */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          📱 Redes sociais e site * (múltiplas opções)
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Onde sua empresa tem presença online?
        </p>
        <div className="mt-3 grid grid-cols-1 md:grid-cols-2 gap-3">
          {redesSociaisOptions.map((option) => (
            <div key={option.value} className="flex items-center space-x-2">
              <Checkbox
                id={`rede-${option.value}`}
                checked={data.redesSociais?.includes(option.value) || false}
                onCheckedChange={(checked) => handleRedesSociaisChange(option.value, checked as boolean)}
              />
              <Label htmlFor={`rede-${option.value}`} className="text-sm cursor-pointer flex items-center space-x-1">
                <span>{option.emoji}</span>
                <span>{option.label}</span>
              </Label>
            </div>
          ))}
        </div>
      </div>

      {/* Links das Redes Sociais */}
      <div>
        <Label htmlFor="linksRedes" className="text-base font-medium text-gray-700">
          🔗 Links das redes sociais (opcional)
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Compartilhe os links das suas redes sociais e site (se tiver)
        </p>
        <Textarea
          id="linksRedes"
          value={data.linksRedes}
          onChange={(e) => updateData({ linksRedes: e.target.value })}
          placeholder="Instagram: @suaempresa&#10;Site: www.suaempresa.com&#10;Facebook: fb.com/suaempresa"
          className="mt-2 min-h-[100px]"
        />
      </div>

      {/* Ferramentas que Usa */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          🤖 Ferramentas que usa * (múltiplas opções)
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Que ferramentas digitais você utiliza?
        </p>
        <div className="mt-3 grid grid-cols-1 md:grid-cols-2 gap-3">
          {ferramentasOptions.map((option) => (
            <div key={option.value} className="flex items-center space-x-2">
              <Checkbox
                id={`ferramenta-${option.value}`}
                checked={data.ferramentasUsa?.includes(option.value) || false}
                onCheckedChange={(checked) => handleFerramentasChange(option.value, checked as boolean)}
              />
              <Label htmlFor={`ferramenta-${option.value}`} className="text-sm cursor-pointer flex items-center space-x-1">
                <span>{option.emoji}</span>
                <span>{option.label}</span>
              </Label>
            </div>
          ))}
        </div>
      </div>

      <div className="bg-purple-50 p-4 rounded-lg border border-purple-200">
        <p className="text-sm text-purple-700">
          🚀 <strong>Transformação digital:</strong> Avaliaremos seu nível de digitalização e 
          sugeriremos ferramentas para otimizar seus processos e aumentar vendas.
        </p>
      </div>
    </div>
  );
};

export default FormSection7;
```

---

## 📝 **FORMSECTION8.TSX - Informações Finais**

```tsx
import React from 'react';
import { Label } from '@/components/ui/label';
import { Textarea } from '@/components/ui/textarea';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

interface FormData {
  melhorContato: string;
  informacoesExtras: string;
}

interface Props {
  data: FormData;
  updateData: (updates: Partial<FormData>) => void;
}

const FormSection8: React.FC<Props> = ({ data, updateData }) => {
  return (
    <div className="space-y-6">
      {/* Melhor Forma de Contato */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          📞 Melhor forma de contato *
        </Label>
        <Select value={data.melhorContato} onValueChange={(value) => updateData({ melhorContato: value })}>
          <SelectTrigger className="mt-2 h-12">
            <SelectValue placeholder="Como prefere ser contatado?" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="whatsapp">📱 WhatsApp</SelectItem>
            <SelectItem value="email">📧 E-mail</SelectItem>
            <SelectItem value="telefone">☎️ Telefone</SelectItem>
            <SelectItem value="instagram">📸 Instagram Direct</SelectItem>
            <SelectItem value="outros">➕ Outros</SelectItem>
          </SelectContent>
        </Select>
      </div>

      {/* Informações Extras */}
      <div>
        <Label htmlFor="informacoesExtras" className="text-base font-medium text-gray-700">
          💡 Informações extras (opcional)
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Há algo mais importante que devemos saber sobre sua empresa?
        </p>
        <Textarea
          id="informacoesExtras"
          value={data.informacoesExtras}
          onChange={(e) => updateData({ informacoesExtras: e.target.value })}
          placeholder="Alguma informação especial, desafios específicos, projetos futuros, sazonalidade do negócio..."
          className="mt-2 min-h-[120px]"
        />
      </div>

      {/* Resumo Final */}
      <div className="bg-gradient-to-r from-blue-50 to-green-50 p-6 rounded-lg border border-blue-200">
        <div className="text-center">
          <h3 className="text-lg font-semibold text-gray-800 mb-2">
            🎯 Quase lá! Você está prestes a receber uma análise completa
          </h3>
          <p className="text-sm text-gray-600 mb-4">
            Em poucos minutos você terá em mãos um relatório personalizado com estratégias 
            específicas para fazer sua empresa crescer.
          </p>
          
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4">
            <div className="text-center">
              <div className="text-2xl mb-1">📊</div>
              <div className="text-xs text-gray-600">Análise Completa</div>
            </div>
            <div className="text-center">
              <div className="text-2xl mb-1">🎯</div>
              <div className="text-xs text-gray-600">Estratégias Personalizadas</div>
            </div>
            <div className="text-center">
              <div className="text-2xl mb-1">📈</div>
              <div className="text-xs text-gray-600">Plano de Crescimento</div>
            </div>
            <div className="text-center">
              <div className="text-2xl mb-1">🚀</div>
              <div className="text-xs text-gray-600">Resultados Práticos</div>
            </div>
          </div>
        </div>
      </div>

      <div className="text-center text-sm text-gray-500">
        <p>🔒 Seus dados estão protegidos e serão usados exclusivamente para sua análise</p>
      </div>
    </div>
  );
};

export default FormSection8;
```