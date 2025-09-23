# Componentes das Seções 2-4 - Lovable.dev

## 🎯 **FORMSECTION2.TSX - Objetivos e Metas**

```tsx
import React from 'react';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

interface FormData {
  principalObjetivo: string;
  metaCrescimento: string;
}

interface Props {
  data: FormData;
  updateData: (updates: Partial<FormData>) => void;
}

const FormSection2: React.FC<Props> = ({ data, updateData }) => {
  return (
    <div className="space-y-6">
      {/* Principal Objetivo */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          📈 Principal objetivo para os próximos 12 meses *
        </Label>
        <Select value={data.principalObjetivo} onValueChange={(value) => updateData({ principalObjetivo: value })}>
          <SelectTrigger className="mt-2 h-12">
            <SelectValue placeholder="Selecione seu principal objetivo" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="aumentar-vendas">Aumentar vendas</SelectItem>
            <SelectItem value="novos-clientes">Conquistar novos clientes</SelectItem>
            <SelectItem value="presenca-online">Melhorar presença online</SelectItem>
            <SelectItem value="expandir-mercados">Expandir para novos mercados</SelectItem>
            <SelectItem value="ticket-medio">Aumentar ticket médio</SelectItem>
            <SelectItem value="fidelizar">Fidelizar clientes atuais</SelectItem>
            <SelectItem value="outros">Outros</SelectItem>
          </SelectContent>
        </Select>
      </div>

      {/* Meta de Crescimento */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          💰 Meta de crescimento em vendas *
        </Label>
        <Select value={data.metaCrescimento} onValueChange={(value) => updateData({ metaCrescimento: value })}>
          <SelectTrigger className="mt-2 h-12">
            <SelectValue placeholder="Qual sua meta de crescimento?" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="ate-20">Até 20%</SelectItem>
            <SelectItem value="20-50">20% a 50%</SelectItem>
            <SelectItem value="50-100">50% a 100%</SelectItem>
            <SelectItem value="mais-100">Mais de 100%</SelectItem>
            <SelectItem value="manter">Manter o atual</SelectItem>
            <SelectItem value="nao-sei">Não sei ainda</SelectItem>
          </SelectContent>
        </Select>
      </div>

      <div className="bg-blue-50 p-4 rounded-lg border border-blue-200">
        <p className="text-sm text-blue-700">
          💡 <strong>Dica:</strong> Metas claras ajudam a definir estratégias mais assertivas. 
          Consideraremos seu objetivo na análise personalizada.
        </p>
      </div>
    </div>
  );
};

export default FormSection2;
```

---

## 👥 **FORMSECTION3.TSX - Conhecendo Seus Clientes**

```tsx
import React from 'react';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Textarea } from '@/components/ui/textarea';
import { Checkbox } from '@/components/ui/checkbox';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

interface FormData {
  perfilCliente: string;
  comoEncontram: string[];
  motivoEscolha: string;
  problemaResolve: string;
}

interface Props {
  data: FormData;
  updateData: (updates: Partial<FormData>) => void;
}

const FormSection3: React.FC<Props> = ({ data, updateData }) => {
  const handleComoEncontramChange = (value: string, checked: boolean) => {
    const current = data.comoEncontram || [];
    if (checked) {
      updateData({ comoEncontram: [...current, value] });
    } else {
      updateData({ comoEncontram: current.filter(item => item !== value) });
    }
  };

  const comoEncontramOptions = [
    { value: 'indicacao', label: 'Indicação de amigos/família' },
    { value: 'local', label: 'Passam em frente ao local' },
    { value: 'redes-sociais', label: 'Redes sociais' },
    { value: 'google', label: 'Google/Internet' },
    { value: 'whatsapp', label: 'WhatsApp' },
    { value: 'anuncios', label: 'Anúncios tradicionais' },
    { value: 'eventos', label: 'Eventos/feiras' },
    { value: 'outros', label: 'Outros' }
  ];

  return (
    <div className="space-y-6">
      {/* Perfil do Cliente */}
      <div>
        <Label htmlFor="perfilCliente" className="text-base font-medium text-gray-700">
          👤 Perfil do seu cliente ideal *
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Descreva brevemente quem é seu cliente típico (idade, perfil, necessidades)
        </p>
        <Textarea
          id="perfilCliente"
          value={data.perfilCliente}
          onChange={(e) => updateData({ perfilCliente: e.target.value })}
          placeholder="Ex: Mulheres de 25-45 anos, mães, que buscam praticidade no dia a dia"
          className="mt-2 min-h-[100px]"
          required
        />
      </div>

      {/* Como Encontram */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          🔍 Como seus clientes te encontram? * (múltiplas opções)
        </Label>
        <div className="mt-3 grid grid-cols-1 md:grid-cols-2 gap-3">
          {comoEncontramOptions.map((option) => (
            <div key={option.value} className="flex items-center space-x-2">
              <Checkbox
                id={option.value}
                checked={data.comoEncontram?.includes(option.value) || false}
                onCheckedChange={(checked) => handleComoEncontramChange(option.value, checked as boolean)}
              />
              <Label htmlFor={option.value} className="text-sm cursor-pointer">
                {option.label}
              </Label>
            </div>
          ))}
        </div>
      </div>

      {/* Motivo da Escolha */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          ⭐ Principal motivo para escolherem você *
        </Label>
        <Select value={data.motivoEscolha} onValueChange={(value) => updateData({ motivoEscolha: value })}>
          <SelectTrigger className="mt-2 h-12">
            <SelectValue placeholder="Selecione o principal diferencial" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="preco">Preço competitivo</SelectItem>
            <SelectItem value="qualidade">Qualidade superior</SelectItem>
            <SelectItem value="atendimento">Atendimento diferenciado</SelectItem>
            <SelectItem value="localizacao">Localização conveniente</SelectItem>
            <SelectItem value="variedade">Variedade de produtos</SelectItem>
            <SelectItem value="confianca">Confiança/tradição</SelectItem>
            <SelectItem value="inovacao">Inovação</SelectItem>
            <SelectItem value="outros">Outros</SelectItem>
          </SelectContent>
        </Select>
      </div>

      {/* Problema que Resolve */}
      <div>
        <Label htmlFor="problemaResolve" className="text-base font-medium text-gray-700">
          🎯 Problema que você resolve *
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Qual a principal dificuldade dos seus clientes que você resolve?
        </p>
        <Textarea
          id="problemaResolve"
          value={data.problemaResolve}
          onChange={(e) => updateData({ problemaResolve: e.target.value })}
          placeholder="Ex: Falta de tempo para cozinhar refeições saudáveis"
          className="mt-2 min-h-[100px]"
          required
        />
      </div>
    </div>
  );
};

export default FormSection3;
```

---

## 📊 **FORMSECTION4.TSX - Satisfação e Indicação**

```tsx
import React from 'react';
import { Label } from '@/components/ui/label';
import { Slider } from '@/components/ui/slider';

interface FormData {
  nivelSatisfacao: number;
  probabilidadeIndicacao: number;
}

interface Props {
  data: FormData;
  updateData: (updates: Partial<FormData>) => void;
}

const FormSection4: React.FC<Props> = ({ data, updateData }) => {
  const getSatisfacaoLabel = (value: number) => {
    const labels = {
      1: 'Pouco satisfeitos',
      2: 'Satisfação baixa',
      3: 'Satisfação média',
      4: 'Bem satisfeitos',
      5: 'Muito satisfeitos'
    };
    return labels[value as keyof typeof labels] || 'Satisfação média';
  };

  const getNPSLabel = (value: number) => {
    if (value <= 6) return 'Detratores (críticos)';
    if (value <= 8) return 'Neutros (passivos)';
    return 'Promotores (defensores)';
  };

  const getNPSColor = (value: number) => {
    if (value <= 6) return 'text-red-600';
    if (value <= 8) return 'text-yellow-600';
    return 'text-green-600';
  };

  return (
    <div className="space-y-8">
      {/* Nível de Satisfação */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          😊 Nível de satisfação dos clientes *
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Como você avalia a satisfação geral dos seus clientes?
        </p>
        
        <div className="mt-4">
          <div className="flex justify-between text-sm text-gray-500 mb-2">
            <span>1 - Pouco satisfeitos</span>
            <span>5 - Muito satisfeitos</span>
          </div>
          
          <Slider
            value={[data.nivelSatisfacao]}
            onValueChange={(value) => updateData({ nivelSatisfacao: value[0] })}
            max={5}
            min={1}
            step={1}
            className="mt-2"
          />
          
          <div className="mt-3 text-center">
            <div className="inline-flex items-center space-x-2 bg-blue-50 px-4 py-2 rounded-lg">
              <span className="text-2xl">😊</span>
              <span className="font-medium text-blue-700">
                {data.nivelSatisfacao}/5 - {getSatisfacaoLabel(data.nivelSatisfacao)}
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Probabilidade de Indicação (NPS) */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          🗣️ Probabilidade de indicação (NPS) *
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Qual a chance de um cliente indicar sua empresa?
        </p>
        
        <div className="mt-4">
          <div className="flex justify-between text-sm text-gray-500 mb-2">
            <span>0 - Jamais indicaria</span>
            <span>10 - Com certeza indicaria</span>
          </div>
          
          <Slider
            value={[data.probabilidadeIndicacao]}
            onValueChange={(value) => updateData({ probabilidadeIndicacao: value[0] })}
            max={10}
            min={0}
            step={1}
            className="mt-2"
          />
          
          <div className="mt-3 text-center">
            <div className="inline-flex items-center space-x-2 bg-gray-50 px-4 py-2 rounded-lg">
              <span className="text-2xl">🗣️</span>
              <span className={`font-medium ${getNPSColor(data.probabilidadeIndicacao)}`}>
                {data.probabilidadeIndicacao}/10 - {getNPSLabel(data.probabilidadeIndicacao)}
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Explicação NPS */}
      <div className="bg-gradient-to-r from-blue-50 to-green-50 p-4 rounded-lg border border-blue-200">
        <h4 className="font-medium text-gray-700 mb-2">💡 Sobre o Net Promoter Score (NPS):</h4>
        <div className="text-sm text-gray-600 space-y-1">
          <p><span className="text-red-600 font-medium">0-6:</span> Detratores - podem prejudicar sua reputação</p>
          <p><span className="text-yellow-600 font-medium">7-8:</span> Neutros - satisfeitos mas não promovem</p>
          <p><span className="text-green-600 font-medium">9-10:</span> Promotores - defensores da sua marca</p>
        </div>
      </div>
    </div>
  );
};

export default FormSection4;
```