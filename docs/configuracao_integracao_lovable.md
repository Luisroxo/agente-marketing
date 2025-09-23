# Configuração de Integração - Lovable.dev + Webhook

## 🔗 **CONFIGURAÇÃO DO WEBHOOK NO LOVABLE.DEV**

### **1. Atualizar App.tsx:**

Substitua a função `handleSubmit` no seu arquivo `App.tsx` do Lovable.dev:

```typescript
const handleSubmit = async () => {
  setIsSubmitting(true);
  
  try {
    // 🔥 URL do seu webhook local (para desenvolvimento)
    // Para produção, use ngrok ou hospede o webhook
    const response = await fetch('http://localhost:5000/webhook/tally', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
      body: JSON.stringify({
        data: {
          fields: {
            // Mapeamento dos campos do formulário
            'Nome da empresa': formData.nomeEmpresa,
            'Tipo do negócio': formData.tipoNegocio,
            'Proposta de valor': formData.propostaValor,
            'Ano de fundação': formData.anoFundacao,
            'Alcance dos clientes': formData.alcanceClientes,
            'Principal objetivo': formData.principalObjetivo,
            'Meta de crescimento': formData.metaCrescimento,
            'Perfil do cliente ideal': formData.perfilCliente,
            'Como clientes encontram': formData.comoEncontram,
            'Motivo da escolha': formData.motivoEscolha,
            'Problema que resolve': formData.problemaResolve,
            'Nível de satisfação': formData.nivelSatisfacao,
            'Probabilidade de indicação (NPS)': formData.probabilidadeIndicacao,
            'Principais concorrentes': formData.principaisConcorrentes,
            'Principal diferencial': formData.principalDiferencial,
            'Marketing dos concorrentes': formData.marketingConcorrentes,
            'Canais de venda': formData.canaisVenda,
            'Canal que mais vende': formData.canalMaisVende,
            'Marketing atual': formData.marketingAtual,
            'Redes sociais e site': formData.redesSociais,
            'Links das redes sociais': formData.linksRedes,
            'Ferramentas que usa': formData.ferramentasUsa,
            'Melhor forma de contato': formData.melhorContato,
            'Informações extras': formData.informacoesExtras
          }
        },
        eventId: `lovable-${Date.now()}`,
        eventType: 'FORM_RESPONSE',
        createdAt: new Date().toISOString(),
        formId: 'analise-marketing-lovable',
        responseId: `resp-${Date.now()}`
      })
    });

    if (response.ok) {
      console.log('✅ Formulário enviado com sucesso!');
      setIsCompleted(true);
    } else {
      const error = await response.text();
      console.error('❌ Erro no servidor:', error);
      throw new Error(`Erro ${response.status}: ${error}`);
    }
  } catch (error) {
    console.error('❌ Erro ao enviar:', error);
    
    // Fallback: mostrar mensagem de erro amigável
    alert(`Ops! Tivemos um problema técnico. 
    
Seu formulário foi preenchido corretamente, mas houve uma falha na conexão.

Por favor:
1. Anote suas respostas principais
2. Entre em contato conosco pelo WhatsApp
3. Ou tente novamente em alguns minutos

Pedimos desculpas pelo inconveniente! 🙏`);
  } finally {
    setIsSubmitting(false);
  }
};
```

---

## 🌐 **OPÇÃO PARA PRODUÇÃO (USANDO NGROK)**

Para que o Lovable.dev (hospedado na nuvem) acesse seu webhook local, use ngrok:

### **1. Instalar ngrok:**
```bash
# Download em: https://ngrok.com/download
# Ou via chocolatey: choco install ngrok
```

### **2. Expor webhook publicamente:**
```bash
ngrok http 5000
```

### **3. Usar URL pública no Lovable.dev:**
```typescript
// Substitua por sua URL do ngrok
const response = await fetch('https://abc123.ngrok.io/webhook/tally', {
  // ... resto do código
});
```

---

## 🧪 **TESTE DE INTEGRAÇÃO**

### **1. Testar webhook diretamente:**

Abra no navegador: http://localhost:5000/webhook/test

Ou via PowerShell:
```powershell
Invoke-WebRequest -Uri "http://localhost:5000/webhook/test" -Method POST -ContentType "application/json" -Body '{"test": true}'
```

### **2. Verificar dashboard:**

Acesse: http://localhost:8507

---

## 📋 **CHECKLIST DE IMPLEMENTAÇÃO**

### **No Lovable.dev:**
- [ ] Atualizar função handleSubmit no App.tsx
- [ ] Configurar URL do webhook (localhost ou ngrok)
- [ ] Testar envio de formulário
- [ ] Validar campos obrigatórios

### **No seu sistema:**
- [x] Webhook rodando em localhost:5000
- [x] Dashboard rodando em localhost:8507
- [ ] Teste de recebimento de dados
- [ ] Validação da análise automática

### **Produção (opcional):**
- [ ] Configurar ngrok para acesso público
- [ ] Ou hospedar webhook em servidor
- [ ] Configurar domínio personalizado

---

## 🎯 **PRÓXIMOS PASSOS IMEDIATOS:**

1. **Atualizar código no Lovable.dev** (copie o handleSubmit acima)
2. **Fazer teste completo** do formulário
3. **Verificar recebimento** no dashboard localhost:8507
4. **Ajustar se necessário**

**Pronto para testar?** 🚀