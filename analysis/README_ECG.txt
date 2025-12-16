═══════════════════════════════════════════════════════════════════════════════════
                    ANÁLISE ESTATÍSTICA DE VARIAÇÃO DE ECG
                    Ativação Muscular (Isquiotibial): Sessões 19-23
═══════════════════════════════════════════════════════════════════════════════════

📊 RESUMO EXECUTIVO

Este documento apresenta os resultados da análise estatística de variação de ECG
(Eletrocardiografia de Superfície - Delta = sinal máximo - sinal mínimo) coletados
do banco de dados clinic.db para as sessões 19-23 do projeto PBL. A análise compara
a perna esquerda (parética, afetada pelo AVC) com a perna direita (controle, saudável)
e valida a normalidade dos dados através do teste Shapiro-Wilk.

O ECG neste projeto mede a ativação elétrica do ISQUIOTIBIAL (músculo posterior da
coxa), responsável pela flexão de joelho e importante na marcha e reabilitação.

NOTA: Denominação "ECG" aqui refere-se ao sensor de atividade muscular no isquiotibial,
não ao eletrocardiograma cardíaco tradicional.

═══════════════════════════════════════════════════════════════════════════════════

1️⃣ DADOS BRUTOS COLETADOS

┌──────────────────────────────────────────────────────────────────────────┐
│ DELTAS ECG CALCULADOS (ΔSignal = Sinal Máximo - Sinal Mínimo)           │
│ Unidade: mV (millivolts)                                                 │
├─────────────┬──────────────────┬──────────────────┬──────────────────────┤
│ Sessão      │ Esquerda (mV)    │ Direita (mV)     │ Diferença (mV)       │
├─────────────┼──────────────────┼──────────────────┼──────────────────────┤
│ 19          │ 4.095            │ 4.095            │ 0                    │
│ 20          │ 1.650            │ 2.368            │ +718                 │
│ 21          │ 2.791            │ 3.865            │ +1.074               │
│ 22          │ 1.704            │ 2.426            │ +722                 │
│ 23          │ 4.095            │ 3.315            │ -780 (ESQ > DIR)     │
├─────────────┼──────────────────┼──────────────────┼──────────────────────┤
│ MÉDIA       │ 2.867            │ 3.214            │ +0.347               │
│ MEDIANA     │ 2.791            │ 3.315            │ +0.722               │
│ MÍNIMO      │ 1.650            │ 2.368            │ -780                 │
│ MÁXIMO      │ 4.095            │ 4.095            │ +1.074               │
└─────────────┴──────────────────┴──────────────────┴──────────────────────┘

INTERPRETAÇÃO: A variação de ativação do isquiotibial é MAIS HETEROGÊNEA que a do
reto femoral. Interessante: na sessão 23, a perna esquerda (parética) teve MAIOR
ativação que a direita (+4.095 vs +3.315), sugerindo possível compensação ou
recrutamento acentuado do isquiotibial nessa sessão.

Diferença média (DIR - ESQ): 0.347 mV (ou ~12% maior na direita em média, mas com
MUITA variabilidade entre sessões).

═══════════════════════════════════════════════════════════════════════════════════

2️⃣ ESTATÍSTICAS DESCRITIVAS COMPLETAS

PERNA ESQUERDA (PARÉTICA):
┌─────────────────────────────────────────────────────────────────────────┐
│ Métrica                    │ Valor                                      │
├────────────────────────────┼──────────────────────────────────────────────┤
│ Contagem (n)               │ 5 sessões                                  │
│ Média (μ)                  │ 2.867 mV                                   │
│ Mediana                    │ 2.791 mV                                   │
│ Desvio Padrão (σ)          │ 1.210 mV                                   │
│ Variância (σ²)             │ 1.464 (mV)²                                │
│ Mínimo                     │ 1.650 mV                                   │
│ Máximo                     │ 4.095 mV (LIMITE de ADC de 12 bits)         │
│ Amplitude (Range)          │ 2.445 mV                                   │
│ 1º Quartil (Q1)            │ 1.704 mV                                   │
│ 3º Quartil (Q3)            │ 4.095 mV                                   │
│ Intervalo Interquartil     │ 2.391 mV (MUITO GRANDE!)                   │
│ Coef. Variação (CV)        │ 42.20%                                     │
└────────────────────────────┴──────────────────────────────────────────────┘

PERNA DIREITA (CONTROLE):
┌─────────────────────────────────────────────────────────────────────────┐
│ Métrica                    │ Valor                                      │
├────────────────────────────┼──────────────────────────────────────────────┤
│ Contagem (n)               │ 5 sessões                                  │
│ Média (μ)                  │ 3.214 mV                                   │
│ Mediana                    │ 3.315 mV                                   │
│ Desvio Padrão (σ)          │ 0.798 mV                                   │
│ Variância (σ²)             │ 0.637 (mV)²                                │
│ Mínimo                     │ 2.368 mV                                   │
│ Máximo                     │ 4.095 mV                                   │
│ Amplitude (Range)          │ 1.727 mV                                   │
│ 1º Quartil (Q1)            │ 2.426 mV                                   │
│ 3º Quartil (Q3)            │ 3.865 mV                                   │
│ Intervalo Interquartil     │ 1.439 mV                                   │
│ Coef. Variação (CV)        │ 24.83%                                     │
└────────────────────────────┴──────────────────────────────────────────────┘

INTERPRETAÇÃO: 
- PERNA ESQ: ALTA variabilidade (CV 42.20%) = Ativação do isquiotibial MUITO
  inconsistente, sugerindo possível fraqueza, espasticidade ou falta de controle
  neuromuscular fino no músculo posterior parético.

- PERNA DIR: Variabilidade MODERADA (CV 24.83%) = Ativação mais consistente que
  a esquerda, mas ainda significativamente maior que o EMG (comparar com EMG DIR
  que era 12.65%).

- ACHADO IMPORTANTE: O isquiotibial (ECG) é mais variável que o reto femoral (EMG)
  em AMBAS as pernas. Isso pode indicar que o posterior é menos controlado durante
  o exercício, ou que a tarefa específica recrutava mais inconsistentemente os
  flexores de joelho.

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
  
  Perna Esquerda ordenada:  [1.650, 1.704, 2.791, 4.095, 4.095] mV
  Perna Direita ordenada:   [2.368, 2.426, 3.315, 3.865, 4.095] mV
  
  NOTA: Sessão 23 ESQ tem DOIS valores em 4.095 (limite de ADC de 12 bits)
  Isso pode indicar saturação do sinal.

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
             0  2.0  3.0  4.0  5.0

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
│ Estatística W (Shapiro-Wilk)   │ 0.828192                               │
│ P-value                        │ 0.134834                               │
│ Resultado                      │ ✓ NORMAL (p > 0.05)                  │
│                                │                                        │
│ INTERPRETAÇÃO PASSO A PASSO:                                            │
│                                                                         │
│ 1. O teste calculou W = 0.828192 para os dados da perna esquerda       │
│                                                                         │
│ 2. Baseado nisso, gerou um p-value de 0.134834                         │
│                                                                         │
│ 3. Este p-value significa: "Se os dados fossem normais, teríamos       │
│    13.48% de probabilidade de observar um W tão extremo ou pior."      │
│                                                                         │
│ 4. Como 13.48% > 5% (nosso limite), NÃO rejeitamos a normalidade       │
│                                                                         │
│ 5. CONCLUSÃO: Os dados SÃO normalmente distribuídos ✓                 │
│                                                                         │
│ PORÉM: W = 0.828192 é "aceitável mas não excelente". Indica que os    │
│ dados têm algum desvio da normalidade perfeita (e.g., os dois 4.095    │
│ no Q3 causam ligeira distorção), mas ainda mantemos normalidade.       │
└─────────────────────────────────────────────────────────────────────────┘

PERNA DIREITA (CONTROLE):
┌─────────────────────────────────────────────────────────────────────────┐
│ Estatística W (Shapiro-Wilk)   │ 0.877749                               │
│ P-value                        │ 0.299234                               │
│ Resultado                      │ ✓ NORMAL (p > 0.05)                  │
│                                │                                        │
│ INTERPRETAÇÃO PASSO A PASSO:                                            │
│                                                                         │
│ 1. O teste calculou W = 0.877749 para os dados da perna direita        │
│                                                                         │
│ 2. Baseado nisso, gerou um p-value de 0.299234                         │
│                                                                         │
│ 3. Este p-value significa: "Se os dados fossem normais, teríamos       │
│    29.92% de probabilidade de observar um W tão extremo ou pior."      │
│                                                                         │
│ 4. Como 29.92% > 5% (nosso limite), NÃO rejeitamos a normalidade       │
│                                                                         │
│ 5. CONCLUSÃO: Os dados SÃO normalmente distribuídos ✓                 │
│                                                                         │
│ NOTA: W = 0.877749 é melhor que a esquerda, indicando distribuição    │
│ um pouco mais próxima da normalidade, mas ainda com variabilidade.     │
└─────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════════

5️⃣ CONCLUSÃO GERAL DO TESTE SHAPIRO-WILK

✓ PERNA ESQUERDA:  W = 0.828192, p = 0.134834 → NORMAL (marginalmente)
✓ PERNA DIREITA:   W = 0.877749, p = 0.299234 → NORMAL

IMPLICAÇÕES:
─────────────

1. Ambos os conjuntos de dados são TECNICAMENTE normalmente distribuídos

2. Isso valida o uso de TESTES PARAMÉTRICOS para análises futuras:
   • T-test pareado (comparar ESQ vs DIR)
   • ANOVA (comparar entre as 5 sessões)
   • Regressão linear (análise de tendência)

3. PORÉM, com ressalvas:
   • Dados ESQ mostram maior variabilidade que EMG
   • Possível saturação de ADC em sessão 23 (dois valores em 4.095)
   • Recomenda-se considerar testes não-paramétricos como análise complementar

4. NÃO precisamos de:
   • Transformações extremas dos dados
   • Tratamentos drásticos para não-normalidade

═══════════════════════════════════════════════════════════════════════════════════

6️⃣ ANÁLISE CLÍNICA DOS RESULTADOS

ACHADO PRINCIPAL: VARIABILIDADE ACENTUADA DO ISQUIOTIBIAL PARÉTICO

A perna esquerda (parética) mostra ALTA VARIABILIDADE de ativação do isquiotibial
(CV 42.20% vs DIR 24.83%), sugerindo FALTA DE CONTROLE MOTOR fino do músculo
posterior durante a marcha/exercício.

PADRÕES OBSERVADOS:

Sessão 19 - MÁXIMA ATIVAÇÃO (AMBAS):
  • ESQ: 4.095 mV (MÁXIMA e SATURADA)
  • DIR: 4.095 mV (SATURADA também)
  • Diferença: 0 (iguais, ambas em limite de ADC)
  • Interpretação: Forte recrutamento bilateral, possivelmente sintonia muscular
                   mas também com possível saturação de sinal

Sessão 20 - PADRÃO INTERMEDIÁRIO:
  • ESQ: 1.650 mV (MÍNIMA geral)
  • DIR: 2.368 mV
  • Diferença: +718 mV
  • Interpretação: Fraca ativação do isquiotibial esquerdo

Sessão 21 - MODERADA ASSIMETRIA:
  • ESQ: 2.791 mV (próxima à média)
  • DIR: 3.865 mV
  • Diferença: +1.074 mV
  • Interpretação: Padrão mais consistente

Sessão 22 - PADRÃO BAIXO:
  • ESQ: 1.704 mV (MÍNIMA próxima à 20)
  • DIR: 2.426 mV (MÍNIMA da direita)
  • Diferença: +722 mV
  • Interpretação: Ambas com ativação reduzida

Sessão 23 - INVERSÃO! ESQUERDA MELHOR QUE DIREITA:
  • ESQ: 4.095 mV (MÁXIMA e SATURADA)
  • DIR: 3.315 mV
  • Diferença: -780 mV (ESQ > DIR por 780!)
  • Interpretação: AUMENTO DRAMÁTICO de ativação da perna parética no isquiotibial!
                   Possível compensação, espasticidade, ou POSSÍVEL MELHORA!

═══════════════════════════════════════════════════════════════════════════════════

7️⃣ VALIDAÇÃO ESTATÍSTICA

Os dados coletados apresentam características especiais:

✓ Normalidade: Comprovada por Shapiro-Wilk (p > 0.05 em ambas)
✓ Amostra: 5 sessões (tamanho apropriado para teste Shapiro-Wilk)
✓ Independência: Cada sessão é independente

⚠ RESSALVAS:
  ✗ Possível saturação de ADC (valor máximo 4.095 em 2 pontos ESQ, 1 ponto DIR)
  ✗ Alta variabilidade ESQ (CV 42.20%) vs EMG (CV 24.29%)
  ✗ W stat ESQ (0.828) é mais baixo que EMG (0.917), indicando menor "fit"
  ✗ Heterogeneidade entre pernas (IQR ESQ = 2.391 vs DIR = 1.439)

═══════════════════════════════════════════════════════════════════════════════════

8️⃣ ARQUIVOS FORNECIDOS

ecg_analysis.py
  → Script Python que realiza:
    1. Conexão com banco clinic.db
    2. Extração de dados brutos de ECG (JSON)
    3. Cálculo de deltas ECG (max - min)
    4. Teste Shapiro-Wilk
    5. Geração de boxplot
    6. Exportação em Excel

analise_ecg_completa_*.xlsx
  → Relatório Excel com 4 abas:
    - Dados por Sessão (deltas para cada perna)
    - Estatísticas Esquerda (descritivas ECG)
    - Estatísticas Direita (descritivas ECG)
    - Shapiro-Wilk (resultados dos testes)

boxplot_deltas_ecg_*.png
  → Gráfico PNG com boxplot comparativo entre pernas
    Mostra:
    - Mediana (linha central)
    - Q1 e Q3 (caixa)
    - Whiskers (extremos)
    - Comparação visual ESQ vs DIR
    - NOTA: Observe o Q3 ESQ muito alto (4.095) indicando saturação

═══════════════════════════════════════════════════════════════════════════════════

9️⃣ COMO USAR

EXECUTAR A ANÁLISE:
  1. Abra PowerShell/Terminal
  2. Navegue até a pasta: cd analysis
  3. Execute: python ecg_analysis.py
  4. O script irá:
     - Conectar ao banco de dados
     - Calcular todos os valores
     - Gerar novo Excel
     - Gerar novo PNG (boxplot)
     - Exibir resultados no console

VER RESULTADOS:
  • Abra o arquivo .xlsx para ver tabelas detalhadas
  • Abra o arquivo .png para ver o gráfico (boxplot)
  • Leia este README_ECG.txt para entender os resultados

═══════════════════════════════════════════════════════════════════════════════════

PRÓXIMAS ANÁLISES RECOMENDADAS

1. TESTE T PAREADO:
   Questão: "Há diferença significativa entre perna ESQ e DIR?"
   Método: Comparar os 5 pares de deltas ECG
   Resultado esperado: Não significante ou marginal (alta variabilidade ESQ)

2. ANÁLISE DE SATURAÇÃO:
   Questão: "Quanto dos dados está sendo "cortado" pelo ADC de 12 bits?"
   Método: Contar pontos em 4.095 (máximo possível)
   Resultado esperado: ~20% dos dados pode estar saturado (especialmente ESQ)
   RECOMENDAÇÃO: Calibrar ganho de amplificação para menor saturação

3. CORRELAÇÃO COM ÂNGULO:
   Questão: "Maior ativação de isquiotibial está associada com flexão de joelho?"
   Método: Correlacionar deltas ECG com deltas angulares
   Resultado esperado: Correlação positiva fraca a moderada

4. COATIVAÇÃO MUSCULAR:
   Questão: "EMG e ECG são ativados simultaneamente (coativação)?"
   Método: Correlacionar deltas EMG com deltas ECG
   Resultado esperado: Correlação positiva (músculos agonistas-antagonistas)

5. ANÁLISE DE COMPENSAÇÃO:
   Questão: "Há padrão de compensação (um lado aumenta quando o outro diminui)?"
   Método: Correlação negativa entre ESQ e DIR para ECG
   Resultado esperado: Possível padrão compensatório especialmente em sessão 23

═══════════════════════════════════════════════════════════════════════════════════

🎓 GLOSSÁRIO DE TERMOS

ECG (Eletrocardiografia): Aqui, técnica que mede a atividade elétrica dos músculos
                         (não o coração, embora tecnicamente similar)
mV (Millivolts): Unidade de medida de potencial elétrico (1 mV = 10⁻³ V)
Delta (ΔSignal): Diferença entre sinal máximo e sinal mínimo em uma sessão
Isquiotibial: Grupo de 3 músculos na parte posterior da coxa (flexores de joelho)
Semitendinoso, Semimembranoso, Bíceps Femoral: Componentes do isquiotibial
Quartil: Valor que divide os dados em 4 partes iguais (Q1 = 25%, Q3 = 75%)
Mediana: Valor central que divide a distribuição no meio (50%)
Desvio Padrão: Medida de dispersão (variabilidade) dos dados
Coef. Variação: Desvio padrão dividido pela média, em percentagem
ADC: Conversor Analógico-Digital (12 bits no ESP32 = máximo 4095)
Saturação: Quando o sinal ultrapassa o máximo que o sensor pode registrar
Shapiro-Wilk: Teste estatístico para normalidade
P-value: Probabilidade de observar dados tão extremos por acaso
Parética: Afetada por paralisia (perna esquerda - pós-AVC)
Controle: Não afetada (perna direita - referência saudável)
Coativação: Ativação simultânea de músculos agonistas e antagonistas
Espasticidade: Aumento de tônus muscular involuntário, comum pós-AVC

═══════════════════════════════════════════════════════════════════════════════════

Data: 03/12/2025
Análise: Variação ECG PBL (Sessões 19-23)
Sensor: Isquiotibial (Músculo Posterior)
Status: ✓ COMPLETO
Versão: 1.0

═══════════════════════════════════════════════════════════════════════════════════
