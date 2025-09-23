# Formulário Profissional - Código Lovable.dev

## 🚀 **INSTRUÇÕES DE IMPLEMENTAÇÃO**

### **1. Criar novo projeto no Lovable.dev:**
1. Acesse https://lovable.dev
2. Clique em "New Project" 
3. Nome: "Análise de Marketing"
4. Template: "React App"

### **2. Substituir o código principal:**

---

## 📱 **APP.TSX - COMPONENTE PRINCIPAL**

```tsx
import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Progress } from '@/components/ui/progress';
import { CheckCircle } from 'lucide-react';
import FormSection1 from './components/FormSection1';
import FormSection2 from './components/FormSection2';
import FormSection3 from './components/FormSection3';
import FormSection4 from './components/FormSection4';
import FormSection5 from './components/FormSection5';
import FormSection6 from './components/FormSection6';
import FormSection7 from './components/FormSection7';
import FormSection8 from './components/FormSection8';
import SuccessPage from './components/SuccessPage';

interface FormData {
  // Seção 1: Fundamentos
  nomeEmpresa: string;
  tipoNegocio: string;
  propostaValor: string;
  anoFundacao: number;
  alcanceClientes: string;
  
  // Seção 2: Objetivos
  principalObjetivo: string;
  metaCrescimento: string;
  
  // Seção 3: Clientes
  perfilCliente: string;
  comoEncontram: string[];
  motivoEscolha: string;
  problemaResolve: string;
  
  // Seção 4: Satisfação
  nivelSatisfacao: number;
  probabilidadeIndicacao: number;
  
  // Seção 5: Concorrência
  principaisConcorrentes: string;
  principalDiferencial: string;
  marketingConcorrentes: string[];
  
  // Seção 6: Vendas
  canaisVenda: string[];
  canalMaisVende: string;
  marketingAtual: string[];
  
  // Seção 7: Digital
  redesSociais: string[];
  linksRedes: string;
  ferramentasUsa: string[];
  
  // Seção 8: Finais
  melhorContato: string;
  informacoesExtras: string;
}

const App = () => {
  const [currentSection, setCurrentSection] = useState(1);
  const [isCompleted, setIsCompleted] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [formData, setFormData] = useState<FormData>({
    nomeEmpresa: '',
    tipoNegocio: '',
    propostaValor: '',
    anoFundacao: new Date().getFullYear(),
    alcanceClientes: '',
    principalObjetivo: '',
    metaCrescimento: '',
    perfilCliente: '',
    comoEncontram: [],
    motivoEscolha: '',
    problemaResolve: '',
    nivelSatisfacao: 3,
    probabilidadeIndicacao: 5,
    principaisConcorrentes: '',
    principalDiferencial: '',
    marketingConcorrentes: [],
    canaisVenda: [],
    canalMaisVende: '',
    marketingAtual: [],
    redesSociais: [],
    linksRedes: '',
    ferramentasUsa: [],
    melhorContato: '',
    informacoesExtras: ''
  });

  const totalSections = 8;
  const progress = (currentSection / totalSections) * 100;

  const updateFormData = (updates: Partial<FormData>) => {
    setFormData(prev => ({ ...prev, ...updates }));
  };

  const nextSection = () => {
    if (currentSection < totalSections) {
      setCurrentSection(prev => prev + 1);
    } else {
      handleSubmit();
    }
  };

  const prevSection = () => {
    if (currentSection > 1) {
      setCurrentSection(prev => prev - 1);
    }
  };

  const handleSubmit = async () => {
    setIsSubmitting(true);
    
    try {
      // Integração com seu webhook
      const response = await fetch('http://localhost:5000/webhook/tally', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          data: {
            fields: formData
          },
          eventId: `lovable-${Date.now()}`,
          eventType: 'FORM_RESPONSE',
          createdAt: new Date().toISOString()
        })
      });

      if (response.ok) {
        setIsCompleted(true);
      } else {
        throw new Error('Erro ao enviar formulário');
      }
    } catch (error) {
      console.error('Erro:', error);
      alert('Erro ao enviar formulário. Tente novamente.');
    } finally {
      setIsSubmitting(false);
    }
  };

  if (isCompleted) {
    return <SuccessPage />;
  }

  const renderSection = () => {
    switch (currentSection) {
      case 1:
        return <FormSection1 data={formData} updateData={updateFormData} />;
      case 2:
        return <FormSection2 data={formData} updateData={updateFormData} />;
      case 3:
        return <FormSection3 data={formData} updateData={updateFormData} />;
      case 4:
        return <FormSection4 data={formData} updateData={updateFormData} />;
      case 5:
        return <FormSection5 data={formData} updateData={updateFormData} />;
      case 6:
        return <FormSection6 data={formData} updateData={updateFormData} />;
      case 7:
        return <FormSection7 data={formData} updateData={updateFormData} />;
      case 8:
        return <FormSection8 data={formData} updateData={updateFormData} />;
      default:
        return null;
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-green-50">
      <div className="container mx-auto px-4 py-8 max-w-4xl">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-4">
            🎯 Análise Completa de Marketing
          </h1>
          <p className="text-lg text-gray-600 mb-6">
            Descubra as melhores estratégias para fazer sua empresa crescer
          </p>
          
          {/* Progress Bar */}
          <div className="mb-8">
            <div className="flex justify-between text-sm text-gray-500 mb-2">
              <span>Seção {currentSection} de {totalSections}</span>
              <span>{Math.round(progress)}% completo</span>
            </div>
            <Progress value={progress} className="h-3" />
          </div>
        </div>

        {/* Form Card */}
        <Card className="shadow-xl border-0 bg-white/80 backdrop-blur-sm">
          <CardHeader className="text-center">
            <CardTitle className="text-2xl text-gray-700">
              {currentSection === 1 && "📊 Fundamentos do Negócio"}
              {currentSection === 2 && "🎯 Objetivos e Metas"}
              {currentSection === 3 && "👥 Conhecendo Seus Clientes"}
              {currentSection === 4 && "📊 Satisfação e Indicação"}
              {currentSection === 5 && "🏆 Concorrência e Diferenciais"}
              {currentSection === 6 && "💰 Vendas e Canais"}
              {currentSection === 7 && "🌐 Presença Digital"}
              {currentSection === 8 && "📝 Informações Finais"}
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-6">
            {renderSection()}
            
            {/* Navigation Buttons */}
            <div className="flex justify-between pt-6 border-t">
              <Button
                variant="outline"
                onClick={prevSection}
                disabled={currentSection === 1}
                className="min-w-[120px]"
              >
                ← Anterior
              </Button>
              
              <Button
                onClick={nextSection}
                disabled={isSubmitting}
                className="min-w-[120px] bg-blue-600 hover:bg-blue-700"
              >
                {isSubmitting ? (
                  "Enviando..."
                ) : currentSection === totalSections ? (
                  <>
                    <CheckCircle className="w-4 h-4 mr-2" />
                    Finalizar Análise
                  </>
                ) : (
                  "Próximo →"
                )}
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Footer */}
        <div className="text-center mt-8 text-gray-500">
          <p>🔒 Suas informações estão seguras e serão usadas apenas para análise</p>
        </div>
      </div>
    </div>
  );
};

export default App;
```

---

## 📝 **COMPONENTES DAS SEÇÕES**

### **FORMSECTION1.TSX - Fundamentos do Negócio**

```tsx
import React from 'react';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

interface FormData {
  nomeEmpresa: string;
  tipoNegocio: string;
  propostaValor: string;
  anoFundacao: number;
  alcanceClientes: string;
}

interface Props {
  data: FormData;
  updateData: (updates: Partial<FormData>) => void;
}

const FormSection1: React.FC<Props> = ({ data, updateData }) => {
  return (
    <div className="space-y-6">
      {/* Nome da Empresa */}
      <div>
        <Label htmlFor="nomeEmpresa" className="text-base font-medium text-gray-700">
          🏢 Nome da sua empresa *
        </Label>
        <Input
          id="nomeEmpresa"
          value={data.nomeEmpresa}
          onChange={(e) => updateData({ nomeEmpresa: e.target.value })}
          placeholder="Digite o nome da sua empresa"
          className="mt-2 h-12"
          required
        />
      </div>

      {/* Tipo do Negócio */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          🎯 Tipo do seu negócio *
        </Label>
        <Select value={data.tipoNegocio} onValueChange={(value) => updateData({ tipoNegocio: value })}>
          <SelectTrigger className="mt-2 h-12">
            <SelectValue placeholder="Selecione a categoria que melhor descreve sua empresa" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="loja-fisica">Loja Física</SelectItem>
            <SelectItem value="servicos">Serviços</SelectItem>
            <SelectItem value="ecommerce">Loja Virtual/E-commerce</SelectItem>
            <SelectItem value="produtos-digitais">Produtos Digitais</SelectItem>
            <SelectItem value="consultoria">Consultoria</SelectItem>
            <SelectItem value="alimentacao">Restaurante/Alimentação</SelectItem>
            <SelectItem value="beleza">Beleza/Estética</SelectItem>
            <SelectItem value="saude">Saúde/Bem-estar</SelectItem>
            <SelectItem value="educacao">Educação</SelectItem>
            <SelectItem value="outros">Outros</SelectItem>
          </SelectContent>
        </Select>
      </div>

      {/* Proposta de Valor */}
      <div>
        <Label htmlFor="propostaValor" className="text-base font-medium text-gray-700">
          💡 Sua proposta de valor (Coração do seu negócio) *
        </Label>
        <p className="text-sm text-gray-500 mt-1">
          Complete a frase: "Nós ajudamos _____ a _____ através de _____"
        </p>
        <Input
          id="propostaValor"
          value={data.propostaValor}
          onChange={(e) => updateData({ propostaValor: e.target.value })}
          placeholder="Ex: pequenos empresários a aumentar vendas através de marketing digital"
          className="mt-2 h-12"
          required
        />
      </div>

      {/* Ano de Fundação */}
      <div>
        <Label htmlFor="anoFundacao" className="text-base font-medium text-gray-700">
          📅 Ano de fundação *
        </Label>
        <Input
          id="anoFundacao"
          type="number"
          value={data.anoFundacao}
          onChange={(e) => updateData({ anoFundacao: parseInt(e.target.value) })}
          placeholder="Ex: 2020"
          className="mt-2 h-12"
          min="1900"
          max={new Date().getFullYear()}
          required
        />
      </div>

      {/* Alcance dos Clientes */}
      <div>
        <Label className="text-base font-medium text-gray-700">
          🌍 Alcance dos seus clientes *
        </Label>
        <Select value={data.alcanceClientes} onValueChange={(value) => updateData({ alcanceClientes: value })}>
          <SelectTrigger className="mt-2 h-12">
            <SelectValue placeholder="Selecione o alcance geográfico" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="local">Principalmente local (cidade/bairro)</SelectItem>
            <SelectItem value="regional">Regional (estado/região)</SelectItem>
            <SelectItem value="nacional">Nacional</SelectItem>
            <SelectItem value="internacional">Internacional</SelectItem>
          </SelectContent>
        </Select>
      </div>
    </div>
  );
};

export default FormSection1;
```

Quer que eu continue criando os outros 7 componentes das seções? Cada um será otimizado com:

✅ **Design profissional** com Tailwind CSS
✅ **Validações em tempo real**
✅ **Campos responsivos** 
✅ **UX moderna** (animações suaves)
✅ **Integração perfeita** com seu backend

**Continue?** 🚀

<function_calls>
<invoke name="manage_todo_list">
<parameter name="operation">write