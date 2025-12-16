═══════════════════════════════════════════════════════════════════════════════════
                    ANÁLISE ESTATÍSTICA DE VARIAÇÃO DE EMG
                    Ativação Muscular (Reto Femoral): Sessões 19-23
═══════════════════════════════════════════════════════════════════════════════════

📊 RESUMO EXECUTIVO

Este documento apresenta os resultados da análise estatística de variação de EMG
(Eletromiografia - Delta = sinal máximo - sinal mínimo) coletados do banco de dados
clinic.db para as sessões 19-23 do projeto PBL. A análise compara a perna esquerda
(parética, afetada pelo AVC) com a perna direita (controle, saudável) e valida a
normalidade dos dados através do teste Shapiro-Wilk.

O EMG mede a ativação elétrica do RETO FEMORAL (músculo anterior da coxa), responsável
pela extensão de quadril e importante na marcha e reabilitação.

═══════════════════════════════════════════════════════════════════════════════════

1️⃣ DADOS BRUTOS COLETADOS

┌──────────────────────────────────────────────────────────────────────────┐
│ DELTAS EMG CALCULADOS (ΔSignal = Sinal Máximo - Sinal Mínimo)           │
│ Unidade: µV (microvolts)                                                 │
├─────────────┬──────────────────┬──────────────────┬──────────────────────┤
│ Sessão      │ Esquerda (µV)    │ Direita (µV)     │ Diferença (µV)       │
├─────────────┼──────────────────┼──────────────────┼──────────────────────┤
│ 19          │ 2.153            │ 2.803            │ +650                 │
│ 20          │ 1.482            │ 2.292            │ +810                 │
│ 21          │ 1.521            │ 3.237            │ +1.716               │
│ 22          │ 2.034            │ 2.583            │ +549                 │
│ 23          │ 1.182            │ 2.718            │ +1.536               │
├─────────────┼──────────────────┼──────────────────┼──────────────────────┤
│ MÉDIA       │ 1.674            │ 2.727            │ +1.053               │
│ MEDIANA     │ 1.521            │ 2.718            │ +952                 │
│ MÍNIMO      │ 1.182            │ 2.292            │ +549                 │
│ MÁXIMO      │ 2.153            │ 3.237            │ +1.716               │
└─────────────┴──────────────────┴──────────────────┴──────────────────────┘

INTERPRETAÇÃO: A perna direita (controle) apresenta maior variação de sinal EMG
(2.727 µV) em relação à perna esquerda (1.674 µV), com diferença média de 1.053 µV
(ou ~63% maior na direita). Isso sugere ativação muscular mais robusta e consistente
na perna saudável.

═══════════════════════════════════════════════════════════════════════════════════

2️⃣ ESTATÍSTICAS DESCRITIVAS COMPLETAS

PERNA ESQUERDA (PARÉTICA):
┌─────────────────────────────────────────────────────────────────────────┐
│ Métrica                    │ Valor                                      │
├────────────────────────────┼──────────────────────────────────────────────┤
│ Contagem (n)               │ 5 sessões                                  │
│ Média (μ)                  │ 1.674 µV                                   │
│ Mediana                    │ 1.521 µV                                   │
│ Desvio Padrão (σ)          │ 0.407 µV                                   │
│ Variância (σ²)             │ 0.165 (µV)²                                │
│ Mínimo                     │ 1.182 µV                                   │
│ Máximo                     │ 2.153 µV                                   │
│ Amplitude (Range)          │ 0.971 µV                                   │
│ 1º Quartil (Q1)            │ 1.482 µV                                   │
│ 3º Quartil (Q3)            │ 2.034 µV                                   │
│ Intervalo Interquartil     │ 0.552 µV                                   │
│ Coef. Variação (CV)        │ 24.29%                                     │
└────────────────────────────┴──────────────────────────────────────────────┘

PERNA DIREITA (CONTROLE):
┌─────────────────────────────────────────────────────────────────────────┐
│ Métrica                    │ Valor                                      │
├────────────────────────────┼──────────────────────────────────────────────┤
│ Contagem (n)               │ 5 sessões                                  │
│ Média (μ)                  │ 2.727 µV                                   │
│ Mediana                    │ 2.718 µV                                   │
│ Desvio Padrão (σ)          │ 0.345 µV                                   │
│ Variância (σ²)             │ 0.119 (µV)²                                │
│ Mínimo                     │ 2.292 µV                                   │
│ Máximo                     │ 3.237 µV                                   │
│ Amplitude (Range)          │ 0.945 µV                                   │
│ 1º Quartil (Q1)            │ 2.583 µV                                   │
│ 3º Quartil (Q3)            │ 2.803 µV                                   │
│ Intervalo Interquartil     │ 0.220 µV                                   │
│ Coef. Variação (CV)        │ 12.65%                                     │
└────────────────────────────┴──────────────────────────────────────────────┘

INTERPRETAÇÃO: 
- Ambas as pernas mostram ATIVAÇÃO MUSCULAR NORMAL (CV < 60%)
- Perna ESQ: Maior variabilidade (CV 24.29%) = Ativação menos consistente
- Perna DIR: Menor variabilidade (CV 12.65%) = Ativação mais consistente
- Mediana ≈ Média em ambas → Distribuição simétrica
- A perna parética tem 2.5x MAIS VARIAÇÃO que a saudável (CV 24% vs 12%)

═══════════════════════════════════════════════════════════════════════════════════

3️⃣ TESTE DE NORMALIDADE - SHAPIRO-WILK (EXPLICAÇÃO DIDÁTICA)

O QUE É E POR QUÊ USAMOS?
─────────────────────────

O teste de Shapiro-Wilk é um teste estatístico que verifica se um conjunto de
dados segue uma distribuição normal (distribuição de Gauss ou curva em sino).

IMPORTÂNCIA:
  Muitos testes estatísticos (como t-test e ANOVA) assumem que os dados são
  normalmente distribuídos. ANTES de usar esses testes, precisamos validar
  se nossos dados realmente são normais.

COMO FUNCIONA - 5 PASSOS:
──────────────────────────

PASSO 1 - ORDENAR OS DADOS
  Os dados são ordenados em ordem crescente:
  
  Perna Esquerda ordenada:  [1.182, 1.482, 1.521, 2.034, 2.153] µV
  Perna Direita ordenada:   [2.292, 2.583, 2.718, 2.803, 3.237] µV

PASSO 2 - CALCULAR COEFICIENTES ESPECIAIS
  O teste usa coeficientes derivados matematicamente por Shapiro e Wilk.
  Estes coeficientes foram tabulados e variam conforme o tamanho da amostra.
  Para n=5 (5 sessões), usa-se uma tabela específica de coeficientes.

PASSO 3 - COMPARAR COM DISTRIBUIÇÃO NORMAL ESPERADA
  A questão é: "Como esses dados reais se comportam em relação ao que
  esperaríamos de uma distribuição normal perfeita?"
  
  Uma distribuição normal perfeita teria esta forma:
  
         Distribuição Normal
              │
            5 │      ╱╲
              │    ╱    ╲
            3 │  ╱        ╲
              │╱            ╲
         ─────┼────────────────────
             0  1.5  2.0  2.5  3.0  3.5

PASSO 4 - GERAR ESTATÍSTICA W (SHAPIRO-WILK)
  W é um número entre 0 e 1 que mede o "ajuste" dos dados à normalidade:
  
    • W = 0.95 a 1.00  →  Dados MUY próximos da normal ✓✓✓
    • W = 0.90 a 0.95  →  Dados próximos da normal ✓✓
    • W = 0.85 a 0.90  →  Dados razoavelmente normais ✓
    • W < 0.85         →  Dados podem não ser normais ✗

PASSO 5 - CALCULAR P-VALUE
  O p-value é calculado baseado em W e representa a probabilidade de:
  "Se os dados fossem normalmente distribuídos, qual a chance de observarmos
  um valor de W tão extremo ou mais extremo do que o observado?"

REGRA DE DECISÃO - A PARTE IMPORTANTE:
──────────────────────────────────────

  HIPÓTESE NULA (H₀): "Os dados SÃO normalmente distribuídos"
  HIPÓTESE ALTERNATIVA (H₁): "Os dados NÃO são normalmente distribuídos"

  • Se p-value > 0.05:
    "Não temos evidência suficiente para rejeitar H₀"
    → Concluímos que dados SÃO normais ✓

  • Se p-value ≤ 0.05:
    "Temos evidência suficiente para rejeitar H₀"
    → Concluímos que dados NÃO são normais ✗

Nível de significância (α = 0.05):
  É como dizer: "Queremos estar 95% confiantes em nossas conclusões"
  Em outras palavras: "Aceitamos até 5% de chance de erro"

═══════════════════════════════════════════════════════════════════════════════════

4️⃣ RESULTADOS DO TESTE SHAPIRO-WILK

PERNA ESQUERDA (PARÉTICA):
┌─────────────────────────────────────────────────────────────────────────┐
│ Estatística W (Shapiro-Wilk)   │ 0.916589                               │
│ P-value                        │ 0.508177                               │
│ Resultado                      │ ✓ NORMAL (p > 0.05)                  │
│                                │                                        │
│ INTERPRETAÇÃO PASSO A PASSO:                                            │
│                                                                         │
│ 1. O teste calculou W = 0.916589 para os dados da perna esquerda       │
│                                                                         │
│ 2. Baseado nisso, gerou um p-value de 0.508177                         │
│                                                                         │
│ 3. Este p-value significa: "Se os dados fossem normais, teríamos       │
│    50.82% de probabilidade de observar um W tão extremo ou pior."      │
│                                                                         │
│ 4. Como 50.82% > 5% (nosso limite), NÃO rejeitamos a normalidade       │
│                                                                         │
│ 5. CONCLUSÃO: Os dados SÃO normalmente distribuídos ✓                 │
│                                                                         │
│ Em outras palavras: "Não temos evidência contra a normalidade,         │
│ então assumimos que os dados são normais!"                              │
└─────────────────────────────────────────────────────────────────────────┘

PERNA DIREITA (CONTROLE):
┌─────────────────────────────────────────────────────────────────────────┐
│ Estatística W (Shapiro-Wilk)   │ 0.974982                               │
│ P-value                        │ 0.906157                               │
│ Resultado                      │ ✓ NORMAL (p > 0.05)                  │
│                                │                                        │
│ INTERPRETAÇÃO PASSO A PASSO:                                            │
│                                                                         │
│ 1. O teste calculou W = 0.974982 para os dados da perna direita        │
│                                                                         │
│ 2. Baseado nisso, gerou um p-value de 0.906157                         │
│                                                                         │
│ 3. Este p-value significa: "Se os dados fossem normais, teríamos       │
│    90.62% de probabilidade de observar um W tão extremo ou pior."      │
│                                                                         │
│ 4. Como 90.62% > 5% (nosso limite), NÃO rejeitamos a normalidade       │
│                                                                         │
│ 5. CONCLUSÃO: Os dados SÃO normalmente distribuídos ✓                 │
│                                                                         │
│ Em outras palavras: "Não temos evidência contra a normalidade,         │
│ então assumimos que os dados são normais!"                              │
│                                                                         │
│ NOTA: W = 0.974982 é EXCELENTE (muito próximo a 1) = Dados muito      │
│ bem distribuídos normalmente!                                           │
└─────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════════

5️⃣ CONCLUSÃO GERAL DO TESTE SHAPIRO-WILK

✓ PERNA ESQUERDA:  W = 0.916589, p = 0.508177 → NORMAL
✓ PERNA DIREITA:   W = 0.974982, p = 0.906157 → NORMAL (EXCELENTE FIT)

IMPLICAÇÕES:
─────────────

1. Ambos os conjuntos de dados são normalmente distribuídos

2. Isso valida o uso de TESTES PARAMÉTRICOS para análises futuras:
   • T-test pareado (comparar ESQ vs DIR)
   • ANOVA (comparar entre as 5 sessões)
   • Regressão linear (análise de tendência)

3. NÃO precisamos de:
   • Testes não-paramétricos (Mann-Whitney, Kruskal-Wallis)
   • Transformações logarítmicas dos dados
   • Tratamentos especiais para não-normalidade

═══════════════════════════════════════════════════════════════════════════════════

6️⃣ ANÁLISE CLÍNICA DOS RESULTADOS

ACHADO PRINCIPAL: ASSIMETRIA DE ATIVAÇÃO MUSCULAR

A perna direita (controle, saudável) apresenta maior variação de sinal EMG
(2.727 µV) em comparação à perna esquerda (parética, afetada pelo AVC) (1.674 µV).

Diferença média: 1.053 µV (ou ~63% maior na direita)

Mas MAIS IMPORTANTE: A perna direita tem MENOR VARIABILIDADE INTRA-SESSIONAL
(CV 12.65% vs 24.29%), sugerindo ativação muscular mais controlada e consistente.

PADRÕES OBSERVADOS:

Sessão 19 - FORTE ATIVAÇÃO ESQUERDA:
  • ESQ: 2.153 µV (MÁXIMA da esquerda)
  • DIR: 2.803 µV
  • Diferença: +650 µV (menor das diferenças)
  • Interpretação: Sessão com bom recrutamento da perna parética

Sessão 20 - FRACA ATIVAÇÃO ESQUERDA:
  • ESQ: 1.482 µV (próximo à média)
  • DIR: 2.292 µV (MÍNIMA da direita)
  • Diferença: +810 µV
  • Interpretação: Ambas em padrão mais baixo

Sessão 21 - MÁXIMA ASSIMETRIA:
  • ESQ: 1.521 µV
  • DIR: 3.237 µV (MÁXIMA da direita)
  • Diferença: +1.716 µV (MAIOR)
  • Interpretação: Forte ativação da perna controle vs fraca esquerda

Sessão 22 - PADRÃO INTERMEDIÁRIO:
  • ESQ: 2.034 µV (próximo à média)
  • DIR: 2.583 µV
  • Diferença: +549 µV
  • Interpretação: Ativação mais simétrica

Sessão 23 - FRACA ATIVAÇÃO ESQUERDA:
  • ESQ: 1.182 µV (MÍNIMA geral)
  • DIR: 2.718 µV
  • Diferença: +1.536 µV
  • Interpretação: Forte assimetria no final do período

═══════════════════════════════════════════════════════════════════════════════════

7️⃣ VALIDAÇÃO ESTATÍSTICA

Os dados coletados satisfazem os pressupostos para análises paramétricas:

✓ Normalidade: Comprovada por Shapiro-Wilk (p > 0.05 em ambas)
✓ Amostra: 5 sessões (tamanho apropriado para teste Shapiro-Wilk)
✓ Independência: Cada sessão é independente
✓ Escalas: Dados contínuos (sinal EMG em µV)
✓ Homogeneidade de variância: CV DIR (12.65%) < CV ESQ (24.29%)

═══════════════════════════════════════════════════════════════════════════════════

8️⃣ ARQUIVOS FORNECIDOS

emg_analysis.py
  → Script Python que realiza:
    1. Conexão com banco clinic.db
    2. Extração de dados brutos de EMG (JSON)
    3. Cálculo de deltas EMG (max - min)
    4. Teste Shapiro-Wilk
    5. Geração de boxplot
    6. Exportação em Excel

analise_emg_completa_*.xlsx
  → Relatório Excel com 4 abas:
    - Dados por Sessão (deltas para cada perna)
    - Estatísticas Esquerda (descritivas EMG)
    - Estatísticas Direita (descritivas EMG)
    - Shapiro-Wilk (resultados dos testes)

boxplot_deltas_emg_*.png
  → Gráfico PNG com boxplot comparativo entre pernas
    Mostra:
    - Mediana (linha central)
    - Q1 e Q3 (caixa)
    - Whiskers (extremos)
    - Comparação visual ESQ vs DIR

═══════════════════════════════════════════════════════════════════════════════════

9️⃣ COMO USAR

EXECUTAR A ANÁLISE:
  1. Abra PowerShell/Terminal
  2. Navegue até a pasta: cd analysis
  3. Execute: python emg_analysis.py
  4. O script irá:
     - Conectar ao banco de dados
     - Calcular todos os valores
     - Gerar novo Excel
     - Gerar novo PNG (boxplot)
     - Exibir resultados no console

VER RESULTADOS:
  • Abra o arquivo .xlsx para ver tabelas detalhadas
  • Abra o arquivo .png para ver o gráfico (boxplot)
  • Leia este README_EMG.txt para entender os resultados

═══════════════════════════════════════════════════════════════════════════════════

PRÓXIMAS ANÁLISES RECOMENDADAS

1. TESTE T PAREADO:
   Questão: "Há diferença significativa entre perna ESQ e DIR?"
   Método: Comparar os 5 pares de deltas EMG
   Resultado esperado: Provavelmente significante (DIR > ESQ)

2. CORRELAÇÃO COM ÂNGULO:
   Questão: "Maior ativação EMG está associada com maior amplitude de movimento?"
   Método: Correlacionar deltas EMG com deltas angulares
   Resultado esperado: Correlação positiva

3. CORRELAÇÃO COM ECG:
   Questão: "Há sincronismo entre ativação do reto femoral e isquiotibial?"
   Método: Correlacionar deltas EMG com deltas ECG
   Resultado esperado: Correlação positiva (coativação)

4. ANÁLISE DE FADIGA:
   Questão: "Há redução de ativação ao longo das sessões?"
   Método: Regressão linear (sessão vs delta EMG)
   Resultado esperado: Possível padrão de fadiga ou aprendizado

═══════════════════════════════════════════════════════════════════════════════════

🎓 GLOSSÁRIO DE TERMOS

EMG (Eletromiografia): Técnica que mede a atividade elétrica dos músculos
µV (Microvolts): Unidade de medida de potencial elétrico (1 µV = 10⁻⁶ V)
Delta (ΔSignal): Diferença entre sinal máximo e mínimo em uma sessão
Reto Femoral: Músculo anterior da coxa (quadríceps), importante na extensão
Quartil: Valor que divide os dados em 4 partes iguais (Q1 = 25%, Q3 = 75%)
Mediana: Valor central que divide a distribuição no meio (50%)
Desvio Padrão: Medida de dispersão (variabilidade) dos dados
Coef. Variação: Desvio padrão dividido pela média, em percentagem
Shapiro-Wilk: Teste estatístico para normalidade
P-value: Probabilidade de observar dados tão extremos por acaso
Parética: Afetada por paralisia (perna esquerda - pós-AVC)
Controle: Não afetada (perna direita - referência saudável)
Coativação: Ativação simultânea de músculos agonistas e antagonistas

═══════════════════════════════════════════════════════════════════════════════════

Data: 03/12/2025
Análise: Variação EMG PBL (Sessões 19-23)
Sensor: Reto Femoral (Músculo Anterior)
Status: ✓ COMPLETO
Versão: 1.0

═══════════════════════════════════════════════════════════════════════════════════
