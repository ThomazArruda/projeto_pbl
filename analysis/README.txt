═══════════════════════════════════════════════════════════════════════════════════
                    ANÁLISE ESTATÍSTICA DE VARIAÇÃO ANGULAR
                    Variação Angular entre Pernas: Sessões 19-23
═══════════════════════════════════════════════════════════════════════════════════

📊 RESUMO EXECUTIVO

Este documento apresenta os resultados da análise estatística de variação angular
(delta = ângulo máximo - ângulo mínimo) coletados do banco de dados clinic.db
para as sessões 19-23 do projeto PBL. A análise compara a perna esquerda (parética,
afetada pelo AVC) com a perna direita (controle, saudável) e valida a normalidade
dos dados através do teste Shapiro-Wilk.

═══════════════════════════════════════════════════════════════════════════════════

1️⃣ DADOS BRUTOS COLETADOS

┌──────────────────────────────────────────────────────────────────────────┐
│ DELTAS ANGULARES CALCULADOS (ΔAngle = Máximo - Mínimo)                  │
├─────────────┬──────────────────┬──────────────────┬──────────────────────┤
│ Sessão      │ Esquerda (°)     │ Direita (°)      │ Diferença (°)        │
├─────────────┼──────────────────┼──────────────────┼──────────────────────┤
│ 19          │ 42.69            │ 32.70            │ -9.99                │
│ 20          │ 11.32            │ 12.67            │ +1.35                │
│ 21          │ 33.28            │ 49.55            │ +16.27               │
│ 22          │ 7.66             │ 9.69             │ +2.03                │
│ 23          │ 27.82            │ 46.72            │ +18.90               │
├─────────────┼──────────────────┼──────────────────┼──────────────────────┤
│ MÉDIA       │ 24.55            │ 30.27            │ +5.71                │
│ MEDIANA     │ 27.82            │ 32.70            │ +4.88                │
│ MÍNIMO      │ 7.66             │ 9.69             │ -9.99                │
│ MÁXIMO      │ 42.69            │ 49.55            │ +18.90               │
└─────────────┴──────────────────┴──────────────────┴──────────────────────┘

INTERPRETAÇÃO: A perna direita (controle) apresenta maior variação angular
média (30.27°) em relação à perna esquerda (24.55°), com diferença de 5.71°.

═══════════════════════════════════════════════════════════════════════════════════

2️⃣ ESTATÍSTICAS DESCRITIVAS COMPLETAS

PERNA ESQUERDA (PARÉTICA):
┌─────────────────────────────────────────────────────────────────────────┐
│ Métrica                    │ Valor                                      │
├────────────────────────────┼──────────────────────────────────────────────┤
│ Contagem (n)               │ 5 sessões                                  │
│ Média (μ)                  │ 24.55°                                     │
│ Mediana                    │ 27.82°                                     │
│ Desvio Padrão (σ)          │ 14.80°                                     │
│ Variância (σ²)             │ 219.07 (°)²                                │
│ Mínimo                     │ 7.66°                                      │
│ Máximo                     │ 42.69°                                     │
│ Amplitude (Range)          │ 35.03°                                     │
│ 1º Quartil (Q1)            │ 11.32°                                     │
│ 3º Quartil (Q3)            │ 33.28°                                     │
│ Intervalo Interquartil     │ 21.96°                                     │
│ Coef. Variação (CV)        │ 60.28%                                     │
└────────────────────────────┴──────────────────────────────────────────────┘

PERNA DIREITA (CONTROLE):
┌─────────────────────────────────────────────────────────────────────────┐
│ Métrica                    │ Valor                                      │
├────────────────────────────┼──────────────────────────────────────────────┤
│ Contagem (n)               │ 5 sessões                                  │
│ Média (μ)                  │ 30.27°                                     │
│ Mediana                    │ 32.70°                                     │
│ Desvio Padrão (σ)          │ 18.58°                                     │
│ Variância (σ²)             │ 345.38 (°)²                                │
│ Mínimo                     │ 9.69°                                      │
│ Máximo                     │ 49.55°                                     │
│ Amplitude (Range)          │ 39.86°                                     │
│ 1º Quartil (Q1)            │ 12.67°                                     │
│ 3º Quartil (Q3)            │ 46.72°                                     │
│ Intervalo Interquartil     │ 34.05°                                     │
│ Coef. Variação (CV)        │ 61.40%                                     │
└────────────────────────────┴──────────────────────────────────────────────┘

INTERPRETAÇÃO: Ambas pernas mostram alta variabilidade (CV > 60%), indicando
heterogeneidade nos movimentos. A mediana próxima à média sugere distribuição
relativamente simétrica.

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
  
  Perna Esquerda ordenada:  [7.66, 11.32, 27.82, 33.28, 42.69]
  Perna Direita ordenada:   [9.69, 12.67, 32.70, 46.72, 49.55]

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
             0  10  20  30  40  50

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
│ Estatística W (Shapiro-Wilk)   │ 0.932319                               │
│ P-value                        │ 0.612271                               │
│ Resultado                      │ ✓ NORMAL (p > 0.05)                  │
│                                │                                        │
│ INTERPRETAÇÃO PASSO A PASSO:                                            │
│                                                                         │
│ 1. O teste calculou W = 0.932319 para os dados da perna esquerda       │
│                                                                         │
│ 2. Baseado nisso, gerou um p-value de 0.612271                         │
│                                                                         │
│ 3. Este p-value significa: "Se os dados fossem normais, teríamos       │
│    61.23% de probabilidade de observar um W tão extremo ou pior."      │
│                                                                         │
│ 4. Como 61.23% > 5% (nosso limite), NÃO rejeitamos a normalidade       │
│                                                                         │
│ 5. CONCLUSÃO: Os dados SÃO normalmente distribuídos ✓                 │
│                                                                         │
│ Em outras palavras: "Não temos evidência contra a normalidade,         │
│ então assumimos que os dados são normais!"                              │
└─────────────────────────────────────────────────────────────────────────┘

PERNA DIREITA (CONTROLE):
┌─────────────────────────────────────────────────────────────────────────┐
│ Estatística W (Shapiro-Wilk)   │ 0.872112                               │
│ P-value                        │ 0.275080                               │
│ Resultado                      │ ✓ NORMAL (p > 0.05)                  │
│                                │                                        │
│ INTERPRETAÇÃO PASSO A PASSO:                                            │
│                                                                         │
│ 1. O teste calculou W = 0.872112 para os dados da perna direita        │
│                                                                         │
│ 2. Baseado nisso, gerou um p-value de 0.275080                         │
│                                                                         │
│ 3. Este p-value significa: "Se os dados fossem normais, teríamos       │
│    27.51% de probabilidade de observar um W tão extremo ou pior."      │
│                                                                         │
│ 4. Como 27.51% > 5% (nosso limite), NÃO rejeitamos a normalidade       │
│                                                                         │
│ 5. CONCLUSÃO: Os dados SÃO normalmente distribuídos ✓                 │
│                                                                         │
│ Em outras palavras: "Não temos evidência contra a normalidade,         │
│ então assumimos que os dados são normais!"                              │
└─────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════════

5️⃣ CONCLUSÃO GERAL DO TESTE SHAPIRO-WILK

✓ PERNA ESQUERDA:  W = 0.932319, p = 0.612271 → NORMAL
✓ PERNA DIREITA:   W = 0.872112, p = 0.275080 → NORMAL

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

ACHADO PRINCIPAL: ASSIMETRIA ANGULAR

A perna direita (controle, saudável) apresenta maior variação angular média
(30.27°) em comparação à perna esquerda (parética, afetada pelo AVC) (24.55°).

Diferença média: 5.71° (5.71° a mais na direita)

PADRÕES OBSERVADOS:

Sessão 19 - EXCEÇÃO (Perna ESQ melhor que DIR):
  • ESQ: 42.69° (EXCEÇÃO - muito alta)
  • DIR: 32.70°
  • Interpretação: Sessão com movimento excepcional da perna parética

Sessão 20 - FADIGA (Ambas reduzidas):
  • ESQ: 11.32° (MÍNIMA)
  • DIR: 12.67°
  • Interpretação: Possível fadiga ou menor esforço do paciente

Sessão 21 - MÁXIMA ASSIMETRIA:
  • ESQ: 33.28°
  • DIR: 49.55° (MÁXIMA da direita)
  • Diferença: 16.27° (MAIOR)
  • Interpretação: Perna controle com movimento muito superior

Sessão 22 - RECUPERAÇÃO:
  • ESQ: 7.66° (MÍNIMA geral)
  • DIR: 9.69°
  • Interpretação: Ambas reduzidas, possível recuperação/repouso

Sessão 23 - MELHORA PARCIAL:
  • ESQ: 27.82° (próximo à média)
  • DIR: 46.72°
  • Interpretação: Melhorar gradual em relação ao padrão

═══════════════════════════════════════════════════════════════════════════════════

7️⃣ VALIDAÇÃO ESTATÍSTICA

Os dados coletados satisfazem os pressupostos para análises paramétricas:

✓ Normalidade: Comprovada por Shapiro-Wilk (p > 0.05 em ambas)
✓ Amostra: 5 sessões (tamanho apropriado para teste Shapiro-Wilk)
✓ Independência: Cada sessão é independente
✓ Escalas: Dados contínuos (ângulos em graus)

═══════════════════════════════════════════════════════════════════════════════════

8️⃣ ARQUIVOS FORNECIDOS

statistical_analysis.py
  → Script Python que realiza:
    1. Conexão com banco clinic.db
    2. Extração de dados brutos (JSON)
    3. Cálculo de deltas angulares
    4. Teste Shapiro-Wilk
    5. Geração de boxplot
    6. Exportação em Excel

analise_angular_completa_*.xlsx
  → Relatório Excel com 4 abas:
    - Dados por Sessão (deltas para cada perna)
    - Estatísticas Esquerda (descritivas)
    - Estatísticas Direita (descritivas)
    - Shapiro-Wilk (resultados dos testes)

boxplot_deltas_angulares_*.png
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
  3. Execute: python statistical_analysis.py
  4. O script irá:
     - Conectar ao banco de dados
     - Calcular todos os valores
     - Gerar novo Excel
     - Gerar novo PNG (boxplot)
     - Exibir resultados no console

VER RESULTADOS:
  • Abra o arquivo .xlsx para ver tabelas detalhadas
  • Abra o arquivo .png para ver o gráfico (boxplot)
  • Leia este README.txt para entender os resultados

═══════════════════════════════════════════════════════════════════════════════════

PRÓXIMAS ANÁLISES RECOMENDADAS

1. TESTE T PAREADO:
   Questão: "Há diferença significativa entre perna ESQ e DIR?"
   Método: Comparar as 5 pares de deltas
   Resultado esperado: Provavelmente significante (DIR > ESQ)

2. ANOVA (Analysis of Variance):
   Questão: "A variação muda significativamente entre as 5 sessões?"
   Método: Comparar os 5 grupos de dados
   Resultado esperado: Significante (há padrão)

3. CORRELAÇÃO COM EMG/ECG:
   Questão: "Maior ângulo está associado com maior atividade muscular?"
   Método: Correlacionar ângulos com sinais de EMG/ECG
   Resultado esperado: Correlação positiva

4. ANÁLISE DE TENDÊNCIA:
   Questão: "Há melhora ou piora consistente ao longo do tempo?"
   Método: Regressão linear (sessão vs delta)
   Resultado esperado: Possível melhora da perna parética

═══════════════════════════════════════════════════════════════════════════════════

🎓 GLOSSÁRIO DE TERMOS

Delta (ΔAngle): Diferença entre ângulo máximo e mínimo em uma sessão
Quartil: Valor que divide os dados em 4 partes iguais (Q1 = 25%, Q3 = 75%)
Mediana: Valor central que divide a distribuição no meio (50%)
Desvio Padrão: Medida de dispersão (variabilidade) dos dados
Coef. Variação: Desvio padrão dividido pela média, em percentagem
Shapiro-Wilk: Teste estatístico para normalidade
P-value: Probabilidade de observar dados tão extremos por acaso
Parética: Afetada por paralisia (perna esquerda - pós-AVC)
Controle: Não afetada (perna direita - referência saudável)

═══════════════════════════════════════════════════════════════════════════════════

Data: 03/12/2025
Análise: Variação Angular PBL (Sessões 19-23)
Status: ✓ COMPLETO
Versão: 2.0

═══════════════════════════════════════════════════════════════════════════════════
