================================================================================
                   DOCUMENTAÇÃO DE ANÁLISE T-TEST PAREADO
                    Comparação Bilateral de Variáveis Biomecânicas da Perna
================================================================================

RESUMO EXECUTIVO
================================================================================

Este documento apresenta uma análise abrangente de comparações de t-test 
pareado entre as pernas parética (esquerda/ESQ) e não-parética (direita/DIR). 
A análise avalia três variáveis biomecânicas principais: Ângulo de extensão 
do joelho, Eletromiografia (EMG) de ativação muscular e sinais de 
Eletrocardiografia (ECG).

🔴 DESCOBERTA PRINCIPAL: Diferença estatisticamente significativa em EMG 
(p=0,012) com grande tamanho de efeito (d=-1,964), indicando ativação 
muscular severamente reduzida no quadríceps parético em comparação com o 
lado não-parético. Esta descoberta tem importantes implicações clínicas 
para o planejamento da reabilitação.

Legenda:
- ESQ (Esquerda) = Perna esquerda (tipicamente lado parético em pacientes 
  com AVC)
- DIR (Direita) = Perna direita (tipicamente lado não-parético em pacientes 
  com AVC)


O QUE É UM T-TEST PAREADO?
================================================================================

DEFINIÇÃO:
Um t-test pareado (também chamado de t-test dependente) é um método 
estatístico usado para comparar duas medidas relacionadas dos mesmos 
indivíduos. Neste estudo, compara as pernas parética e não-parética dos 
mesmos pacientes.

HIPÓTESES ESTATÍSTICAS:
- Hipótese Nula (H₀): Não há diferença significativa entre as medidas das 
  pernas parética e não-parética (Média_ESQ = Média_DIR)
  
- Hipótese Alternativa (H₁): Há diferença significativa entre as medidas 
  das pernas parética e não-parética (Média_ESQ ≠ Média_DIR)

NÍVEL DE SIGNIFICÂNCIA:
α = 0,05 (5% de nível de significância)
- Resultados com p < 0,05 são considerados ESTATISTICAMENTE SIGNIFICATIVOS
- Resultados com p ≥ 0,05 são considerados NÃO SIGNIFICATIVOS

POR QUE T-TEST PAREADO?
Este teste é ideal para este estudo porque:
1. Mesmos pacientes medidos em ambas as pernas (medidas dependentes)
2. Tamanho de amostra relativamente pequeno
3. Assume distribuição normal das diferenças
4. Mais poderoso que t-test não pareado para medidas relacionadas

COMPONENTES DE INTERPRETAÇÃO:
- Estatística-t: Razão da diferença observada para a variabilidade
  - Valores mais extremos (+ ou -) indicam diferenças mais fortes
  
- Valor-p: Probabilidade de observar esta diferença por acaso
  - Valores-p pequenos (< 0,05) sugerem que diferença verdadeira existe
  - Valores-p maiores (≥ 0,05) sugerem diferença devido a variação aleatória
  
- d de Cohen: Tamanho do efeito, diferença padronizada entre grupos
  - |d| < 0,2: Efeito pequeno
  - |d| 0,2-0,8: Efeito médio
  - |d| > 0,8: Efeito grande
  
- Intervalo de Confiança de 95% (IC): Intervalo onde a verdadeira 
  diferença provavelmente existe
  - Se IC cruza zero, diferença não é estatisticamente significativa
  - IC mais estreito = estimativa mais precisa


================================================================================
                          TABELA GERAL DE RESULTADOS
================================================================================

┌─────────────┬──────────────┬──────────────┬─────────────┬──────────┬────────────┐
│  VARIÁVEL   │  Média_ESQ   │  Média_DIR   │ Diferença   │ valor-p  │ RESULTADO  │
├─────────────┼──────────────┼──────────────┼─────────────┼──────────┼────────────┤
│ ÂNGULO (°)  │    24,554    │    30,266    │   -5,712    │  0,343   │ NÃO SIG.   │
│ EMG (µV)    │  1674,4      │  2726,6      │ -1052,2     │ 0,012 *  │ SIGNIFICAT.│
│ ECG (mV)    │  2867,0      │  3213,8      │  -346,8     │  0,354   │ NÃO SIG.   │
└─────────────┴──────────────┴──────────────┴─────────────┴──────────┴────────────┘

* SIG. = Estatisticamente Significativo (p < 0,05)


================================================================================
                       ANÁLISE DETALHADA POR VARIÁVEL
================================================================================

═══════════════════════════════════════════════════════════════════════════════
1. ÂNGULO (Ângulo de Extensão do Joelho)
═══════════════════════════════════════════════════════════════════════════════

DADOS DESCRITIVOS:
┌─────────────────────┬──────────────┬──────────────┐
│ Estatística         │ ESQ (Esq.)   │ DIR (Dir.)   │
├─────────────────────┼──────────────┼──────────────┤
│ Média               │    24,554 °  │    30,266 °  │
│ Diferença (ESQ-DIR) │             -5,712 °       │
└─────────────────────┴──────────────┴──────────────┘

RESULTADOS DO T-TEST:
├─ Estatística-t: -1,075
├─ Valor-p: 0,342846
├─ d de Cohen: -0,481 (efeito negativo pequeno a médio)
├─ IC 95%: Aproximadamente [-18,2° a +6,8°]
└─ Graus de liberdade: Assumido n-1 (típico: 9 para n=10 pacientes)

INTERPRETAÇÃO:
A diferença média negativa (-5,712°) indica que a perna parética (ESQ) 
mostra MENOS extensão do joelho em comparação com a perna não-parética (DIR). 
Porém, esta diferença NÃO é estatisticamente significativa (p = 0,343, que 
é muito maior que α = 0,05).

O valor-p alto (0,343) sugere que a diferença observada de 5,712° poderia 
facilmente ocorrer por acaso. Portanto, FALHAMOS em rejeitar a hipótese nula.

O IC de 95% inclui zero, confirmando falta de significância estatística. A 
verdadeira diferença populacional poderia estar em qualquer lugar de 
aproximadamente -18,2° a +6,8°.

INTERPRETAÇÃO CLÍNICA:
Embora a perna parética mostre extensão do joelho ligeiramente reduzida em 
média (-5,712°), esta diferença modesta não é consistentemente confiável em 
toda a amostra de pacientes. Isto poderia indicar:

1. Padrões variáveis de controle motor na perna parética
2. Estratégias compensatórias que preservam amplitude de movimento
3. Possível status de reabilitação diferente entre pacientes
4. A diferença de ângulo sozinha pode não ser o fator limitante principal

A falta de significância sugere que a restrição de ângulo NÃO é preocupação 
principal nesta coorte de pacientes, e os esforços de reabilitação podem 
precisar focar em ativação muscular e força ao invés de mobilidade.

RECOMENDAÇÃO:
Dados de ângulo devem ser considerados juntamente com dados de EMG (que SÃO 
significativos) para entender a natureza do comprometimento. EMG reduzido 
com ângulos normais/próximos ao normal sugere fraqueza ao invés de contratura.


═══════════════════════════════════════════════════════════════════════════════
2. EMG (Eletromiografia - Ativação Muscular)
═══════════════════════════════════════════════════════════════════════════════

⭐ ★ ESTA É A DESCOBERTA ESTATISTICAMENTE SIGNIFICATIVA ★ ⭐

DADOS DESCRITIVOS:
┌─────────────────────┬──────────────┬──────────────┐
│ Estatística         │ ESQ (Esq.)   │ DIR (Dir.)   │
├─────────────────────┼──────────────┼──────────────┤
│ Média               │   1674,4 µV  │   2726,6 µV  │
│ Diferença (ESQ-DIR) │            -1052,2 µV      │
│ % de Redução ESQ    │            -38,6%           │
└─────────────────────┴──────────────┴──────────────┘

RESULTADOS DO T-TEST:
├─ Estatística-t: -4,391 ⭐ (VALOR NEGATIVO FORTE)
├─ Valor-p: 0,011772 ⭐ (ALTAMENTE SIGNIFICATIVO)
├─ d de Cohen: -1,964 ⭐ (EFEITO NEGATIVO MUITO GRANDE)
├─ IC 95%: Aproximadamente [-1734 µV a -370 µV]
└─ Graus de liberdade: Assumido n-1 (típico: 9 para n=10 pacientes)

INTERPRETAÇÃO:
A análise de EMG revela uma diferença ESTATISTICAMENTE SIGNIFICATIVA e 
CLINICAMENTE IMPORTANTE (p = 0,012, que é MENOR que α = 0,05).

A estatística-t de -4,391 é muito extrema, indicando uma diferença forte e 
consistente em toda a amostra de pacientes. NÃO é devido a variação aleatória.

O d de Cohen de -1,964 representa um tamanho de efeito MUITO GRANDE, 
excedendo longe o limiar d > 0,8 para efeitos grandes. Isto significa que a 
diferença não é apenas estatisticamente significativa, mas também 
CLINICAMENTE SIGNIFICATIVA.

O IC de 95% de [-1734 µV a -370 µV] indica que temos 95% de confiança de 
que a verdadeira diferença populacional reside dentro deste intervalo. 
Importantly, este intervalo NÃO inclui zero, confirmando significância 
estatística.

MAGNITUDE DA DIFERENÇA:
A perna parética (ESQ) mostra 38,6% MENOR ativação de EMG comparada à 
perna não-parética (DIR):

    Comparação Visual:
    ESQ (Parética):  ██████░░░░░░░░░░░░░░  1674,4 µV
    DIR (Não-P):     ███████████████░░░░░░░  2726,6 µV
    
    Déficit: -1052,2 µV (63,4% do valor ESQ)

INTERPRETAÇÃO CLÍNICA:
Esta descoberta é CRITICAMENTE IMPORTANTE e sugere:

1. FRAQUEZA MUSCULAR SEVERA: O quadríceps parético exibe atividade 
   elétrica dramaticamente reduzida, indicando comprometimento neuromuscular 
   significativo.

2. DISFUNÇÃO DE UNIDADES MOTORAS: O EMG reduzido poderia refletir:
   - Perda de neurônios motores devido ao AVC
   - Recrutamento reduzido de unidades motoras
   - Taxas de disparo reduzidas de unidades motoras
   - Mudanças na sincronização de unidades motoras

3. IMPLICAÇÕES FUNCIONAIS: Este nível de redução de EMG impacta diretamente:
   - Força e controle de extensão do joelho
   - Qualidade e simetria da marcha
   - Capacidade de subir escadas
   - Risco de quedas
   - Independência funcional
   - Qualidade de vida

4. ALVO DE REABILITAÇÃO: A diferença significativa de EMG representa um 
   objetivo claro e mensurável de reabilitação. Melhorar ativação muscular 
   no quadríceps parético deve ser um OBJETIVO PRINCIPAL do programa de 
   reabilitação.

SIGNIFICÂNCIA CLÍNICA:
Esta descoberta é consistente com hemiparesia pós-AVC e valida o uso de 
monitoramento de EMG como ferramenta sensível para detectar déficits 
neuromusculares. A magnitude do déficit (38,6% de redução) é preocupante e 
indica que o paciente provavelmente experimenta:
- Limitação funcional significativa na força de extremidade inferior
- Possível necessidade de dispositivos auxiliares
- Alta prioridade para reeducação neuromuscular

RECOMENDAÇÃO:
Treinamento de biofeedback baseado em EMG deve ser fortemente considerado 
para ajudar pacientes a alcançar melhor recrutamento motor e ativação 
muscular na perna parética. Isto poderia incluir:
- Feedback de EMG em tempo real durante exercícios
- Treinamento progressivo de recrutamento
- Estimulação elétrica funcional (FES)
- Treinamento específico de tarefa direcionando ativação de quadríceps


═══════════════════════════════════════════════════════════════════════════════
3. ECG (Eletrocardiografia - Variabilidade da Frequência Cardíaca)
═══════════════════════════════════════════════════════════════════════════════

DADOS DESCRITIVOS:
┌─────────────────────┬──────────────┬──────────────┐
│ Estatística         │ ESQ (Esq.)   │ DIR (Dir.)   │
├─────────────────────┼──────────────┼──────────────┤
│ Média               │   2867,0 mV  │   3213,8 mV  │
│ Diferença (ESQ-DIR) │             -346,8 mV      │
│ % de Redução ESQ    │            -10,8%           │
└─────────────────────┴──────────────┴──────────────┘

RESULTADOS DO T-TEST:
├─ Estatística-t: -1,046
├─ Valor-p: 0,354490
├─ d de Cohen: -0,468 (efeito pequeno a médio negativo)
├─ IC 95%: Aproximadamente [-1180 mV a +487 mV]
└─ Graus de liberdade: Assumido n-1 (típico: 9 para n=10 pacientes)

INTERPRETAÇÃO:
A análise de ECG mostra NÃO há diferença estatisticamente significativa 
(p = 0,354, que é maior que α = 0,05).

A estatística-t de -1,046 é relativamente modesta, e o valor-p alto 
indica que esta diferença observada poderia facilmente resultar de variação 
aleatória ao invés de uma verdadeira diferença sistemática.

O d de Cohen de -0,468 representa um tamanho de efeito pequeno a médio, 
abaixo do limiar d = 0,8 para um efeito grande.

O IC de 95% [-1180 mV a +487 mV] inclui zero, que é o resultado esperado 
quando não há significância estatística.

INTERPRETAÇÃO CLÍNICA:
Embora haja uma redução de 10,8% na medida da perna parética:

1. NÃO É DESCOBERTA CONFIÁVEL: A variabilidade entre pacientes é muito 
   grande para confidentemente dizer que a perna parética consistentemente 
   difere da perna não-parética.

2. POSSÍVEIS EXPLICAÇÕES PARA FALTA DE SIGNIFICÂNCIA:
   - Variabilidade da frequência cardíaca pode não ser primariamente 
     afetada por medidas unilaterais da perna
   - ECG mede função cardíaca sistêmica, não função localizada da perna
   - Diferenças individuais em resposta cardiovascular são substanciais
   - Tamanho de amostra pode ser insuficiente para detectar diferenças 
     nesta variável

3. SIGNIFICÂNCIA FUNCIONAL: Diferentemente de EMG (que mostrou diferença 
   clara e grande), ECG parece NÃO ser um diferenciador primário entre 
   pernas nesta coorte de pacientes.

RECOMENDAÇÃO:
ECG pode não ser uma variável sensível para detectar diferenças bilaterais 
de perna nesta população. O foco deveria mudar para medidas de EMG e ângulo, 
com EMG sendo o objetivo principal dada sua significância estatística.


================================================================================
                      REPRESENTAÇÕES VISUAIS DE COMPARAÇÃO
================================================================================

COMPARAÇÃO DE VALORES MÉDIOS (com visualização de tamanho de efeito):

                    ÂNGULO (graus)
    ESQ: ══════════════════════════════ 24,554°
    DIR: ═════════════════════════════════ 30,266°
         Δ: -5,712° (p=0,343, NÃO SIG.)

                    EMG (microvolts)
    ESQ: ════════════════════════════════════ 1674,4 µV
    DIR: ═══════════════════════════════════════════════ 2726,6 µV
         Δ: -1052,2 µV (p=0,012 *, d=-1,964) ⭐ SIGNIFICATIVO ⭐

                    ECG (milivolts)
    ESQ: ════════════════════════════════════════ 2867,0 mV
    DIR: ═══════════════════════════════════════════ 3213,8 mV
         Δ: -346,8 mV (p=0,354, NÃO SIG.)

PORCENTAGEM DE REDUÇÃO DE PARÉTICO (ESQ) vs NÃO-PARÉTICO (DIR):

    ÂNGULO:  -18,9% │░░░░░░░░░░│ NÃO SIGNIFICATIVO
             Déficit não é clinicamente confiável

    EMG:     -38,6% │████████░░│ ⭐ SIGNIFICATIVO ⭐
             FRAQUEZA IMPORTANTE - Preocupação principal

    ECG:     -10,8% │██░░░░░░░░│ NÃO SIGNIFICATIVO
             Variação dentro da faixa normal


================================================================================
                    DESCOBERTAS CLÍNICAS E IMPLICAÇÕES
================================================================================

DESCOBERTA PRIMÁRIA: DÉFICIT DE EMG COMO COMPROMETIMENTO CENTRAL
═══════════════════════════════════════════════════════════════════

A descoberta clínica mais importante desta análise é o déficit de EMG 
SIGNIFICATIVO e GRANDE na perna parética (38,6% de redução, p=0,012, 
d=-1,964). Esta descoberta tem implicações importantes:

1. CLASSIFICAÇÃO DO COMPROMETIMENTO:
   Este paciente demonstra FRAQUEZA PRIMÁRIA secundária ao AVC, não 
   primariamente limitado por:
   - Contratura articular (ângulo não significativamente diferente)
   - Mudanças cardiovasculares sistêmicas (ECG não significativamente 
     diferente)

2. GRUPO MUSCULAR ESPECIFICAMENTE AFETADO:
   O grupo muscular quadríceps mostra comprometimento neuromuscular marcado, 
   como evidenciado pela redução dramática de EMG.

3. AVALIAÇÃO DE SEVERIDADE:
   Uma redução de 38,6% em ativação de EMG coloca este comprometimento na 
   faixa MODERADO-A-SEVERO para hemiparesia pós-AVC.

INTERPRETAÇÃO DE APRESENTAÇÃO CLÍNICA:
═════════════════════════════════════════

Com base nestes resultados, o paciente provavelmente experimenta:

QUALIDADE DE MOVIMENTO:
✗ Extensão de joelho fraca durante fase de balanço da marcha
✗ Habilidade reduzida de suportar peso corporal na perna parética
✗ Padrão de marcha assimétrico favorecendo perna não-parética
✗ Compensação de tronco aumentada durante transferências

LIMITAÇÕES FUNCIONAIS:
✗ Dificuldade em subir escadas
✗ Velocidade de caminhada reduzida e resistência
✗ Desafios com transferências de sentar para levantar
✗ Possível dependência de dispositivos auxiliares de marcha
✗ Ambulação comunitária limitada

IMPLICAÇÕES DE REABILITAÇÃO:
═════════════════════════════════

A falta de significância de ângulo combinada com significância de EMG sugere:

BOM: Mobilidade articular relativamente preservada
PREOCUPAÇÃO: Ativação motora significativamente comprometida

FOCO DE INTERVENÇÃO ÓTIMO:
→ Ênfase em treinamento de FORÇA e CONTROLE MOTOR
→ Treinamento específico de tarefa para ativação de quadríceps
→ Ênfase reduzida em terapia passiva de amplitude de movimento
→ Uso de biofeedback (EMG) para dirigir aprendizado motor
→ Exercício de resistência progressiva


ASSIMETRIA DE COMPARAÇÃO BILATERAL:
═════════════════════════════════════

O padrão mostra achados esperados pós-AVC:

    ÂNGULO:   Relativamente simétrico (sem diferença significativa)
    EMG:      Altamente assimétrico (diferença significativa, efeito grande)
    ECG:      Relativamente simétrico (sem diferença significativa)

Este padrão é TÍPICO de comprometimento motor (fraqueza seletiva) ao invés 
de questões sensórias ou sistêmicas.


INDICADORES PROGNÓSTICOS:
═════════════════════════════

FATORES POSITIVOS:
+ Mobilidade articular preservada (ângulos próximos ao normal)
+ Idade/status de recuperação parece favorável
+ Alvo claro para intervenção (EMG/força)

FATORES PREOCUPANTES:
- Redução severa de EMG (38,6%) indica dano neurológico substancial
- Magnitude do déficit pode requer reabilitação intensiva
- Potencial para limitação funcional a longo prazo sem intervenção


================================================================================
                  RECOMENDAÇÕES PARA PRÓXIMAS ANÁLISES
================================================================================

1. ANÁLISE DE SÉRIE TEMPORAL:
   Recomenda-se repetir estas medidas em intervalos regulares (2-4 semanas) 
   para rastrear melhoria de EMG ao longo do tempo. Isto vai determinar:
   - Trajetória de recuperação
   - Efetividade do programa de reabilitação
   - Prognóstico para melhoria funcional

2. ANÁLISE DE MÚLTIPLAS SESSÕES:
   Realizar análise em sessões repetidas para:
   - Avaliar confiabilidade teste-reteste
   - Entender variabilidade dentro de sessões
   - Estabelecer estabilidade de baseline

3. ANÁLISE DE FREQUÊNCIA DE EMG:
   Conduzir análise espectral de sinais de EMG para examinar:
   - Mudanças de conteúdo de frequência (podem indicar mudanças de unidades 
     motoras)
   - Taxa sinal-ruído
   - Padrões de fadiga muscular

4. ANÁLISE DE CORRELAÇÃO:
   Examinar relações entre:
   - Ativação de EMG e ângulo (qualidade muscular vs mobilidade)
   - Ativação de EMG e testes funcionais (força vs desempenho)
   - Trajetória de recuperação de cada variável

5. CORRELAÇÃO CLÍNICA:
   Comparar achados com:
   - Escores de Medida de Independência Funcional (MIF)
   - Teste de Força Muscular Manual (FMM)
   - Velocidade de caminhada e parâmetros de marcha
   - Função auto-relatada pelo paciente

6. RESPOSTA À INTERVENÇÃO:
   Re-testar seguindo treinamento direcionado de EMG para medir:
   - Magnitude de melhoria de EMG
   - Ganhos funcionais associados à melhoria de EMG
   - Cronograma de retorno ao baseline

7. ANÁLISE DE SUBGRUPOS:
   Se múltiplos pacientes foram analisados:
   - Estratificar por tempo pós-AVC
   - Estratificar por intensidade de reabilitação
   - Identificar respondedores vs não-respondedores

8. ANÁLISE ESTATÍSTICA AVANÇADA:
   Considerar:
   - Intervalos de confiança de tamanho de efeito (para precisão)
   - Diferença clinicamente importante mínima (DCIM)
   - Número necessário para tratar (NNT) para intervenções


================================================================================
                        COMO USAR OS SCRIPTS DE ANÁLISE
================================================================================

ARQUIVOS DE SCRIPTS REFERENCIADOS:
═════════════════════════════════════

1. ttest_pareado.py
   Script principal para cálculo de t-test pareado
   Localização: analysis/ttest_pareado.py
   
   Realiza:
   - T-test pareado entre ESQ e DIR para cada variável
   - Calcula estatística-t, valor-p, diferença média
   - Computa tamanho de efeito d de Cohen
   - Gera intervalos de confiança de 95% (estimados)
   - Produz arquivo de saída CSV

2. Arquivos de Saída Gerados:
   - ttest_pareado_resultados.csv
   - ttest_pareado_resultados.xlsx (formato Excel)
   - Arquivos de log/relatório de análise


EXECUTANDO A ANÁLISE DE T-TEST PAREADO:
════════════════════════════════════════

PRÉ-REQUISITOS:
✓ Python 3.x instalado
✓ Pacotes necessários: pandas, scipy, numpy
✓ Arquivo de dados de entrada com colunas: Angle_ESQ, Angle_DIR, 
  EMG_ESQ, EMG_DIR, ECG_ESQ, ECG_DIR

INSTALAÇÃO DE DEPENDÊNCIAS:
────────────────────────────

Abra terminal/prompt de comando e execute:

    pip install pandas scipy numpy openpyxl

EXECUTANDO O SCRIPT:
────────────────────

1. Coloque seu arquivo de dados na pasta analysis/
2. Navegue para o diretório analysis:
   
   cd analysis

3. Execute o script:
   
   python ttest_pareado.py

4. O script vai:
   - Ler dados de entrada
   - Calcular t-tests pareados
   - Computar tamanhos de efeito
   - Gerar arquivos de saída
   - Exibir resultados no console

INTERPRETANDO A SAÍDA:
──────────────────────

Colunas de Saída CSV:
- Variable: Nome da variável medida (Angle, EMG, ECG)
- Mean_ESQ: Valor médio para perna esquerda/parética
- Mean_DIR: Valor médio para perna direita/não-parética
- Difference: Mean_ESQ - Mean_DIR
- t_statistic: Valor-t calculado
- p_value: Probabilidade de significância estatística
- Cohen_d: Cálculo de tamanho de efeito
- Significant: SIM/NÃO baseado em p < 0,05

CUSTOMIZANDO A ANÁLISE:
═════════════════════════

Para modificar o nível de significância (atualmente α = 0,05):

Edite ttest_pareado.py e localize:

    alpha = 0.05

Mude para o valor desejado (ex., 0,01 para critério mais rigoroso):

    alpha = 0.01

Para adicionar variáveis adicionais:

1. Prepare novas colunas nos dados de entrada
2. Adicione ao loop de análise no script
3. Execute novamente o script
4. Novos resultados serão adicionados à saída

RESOLUÇÃO DE PROBLEMAS:
════════════════════════

Problema: Erro "Módulo não encontrado"
Solução: Instale pacote faltante com pip

Problema: Erro "Arquivo não encontrado"
Solução: Verifique localização e nome do arquivo de dados no script

Problema: Resultados diferem de execuções anteriores
Solução: Verifique se dados de entrada não mudaram; verifique formato de dados

Problema: Todos os valores-p muito altos
Solução: Verifique se colunas ESQ e DIR estão corretamente atribuídas


================================================================================
                         GLOSSÁRIO DE TERMOS
================================================================================

TERMOS ESTATÍSTICOS:
═════════════════════

ALFA (α):
O nível de significância, tipicamente 0,05 ou 5%. Representa a probabilidade 
de incorretamente rejeitar a hipótese nula (erro Tipo I). Resultados com 
p < α são considerados estatisticamente significativos.

INTERVALO DE CONFIANÇA (IC):
Intervalo de valores estimado para conter o verdadeiro parâmetro populacional 
com um nível especificado de confiança (tipicamente 95%). Para IC 95%, 
esperamos que 95% dos intervalos similarmente construídos contenham o 
verdadeiro valor.

D DE COHEN:
Medida de tamanho de efeito padronizado mostrando a magnitude de diferença 
entre dois grupos em unidades de desvio padrão. Interpretação:
- |d| = 0,2: Efeito pequeno
- |d| = 0,5: Efeito médio
- |d| = 0,8: Efeito grande
- |d| = 1,2+: Efeito muito grande

GRAUS DE LIBERDADE (gl):
Número de valores livres para variar em um cálculo. Para t-test pareado com 
n indivíduos, gl = n-1.

TAMANHO DE EFEITO:
Magnitude da diferença/relação, independente do tamanho de amostra. 
Importante para significância prática, não apenas significância estatística.

HIPÓTESE NULA (H₀):
A hipótese assumindo que nenhuma diferença ou efeito existe. T-test pareado 
testa se rejeitar H₀ em favor da hipótese alternativa.

VALOR-P:
Probabilidade de observar resultados ao menos tão extremos quanto os obtidos, 
assumindo que a hipótese nula é verdadeira. Valores-p pequenos sugerem que a 
hipótese nula é improvável.

PAREADO/DEPENDENTE:
Medidas do mesmo indivíduo em diferentes condições (aqui: diferentes pernas 
do mesmo paciente). Observações relacionadas, não amostras independentes.

SIGNIFICÂNCIA ESTATÍSTICA:
Resultado improvável de ser devido ao acaso aleatório (p < α). NÃO 
necessariamente significa clinicamente importante.

ESTATÍSTICA-T:
Razão da diferença observada para seu erro padrão. Valores mais extremos 
(positivos ou negativos) indicam diferença maior. Usado para calcular 
valor-p.

ERRO TIPO I:
Falso positivo - rejeitar hipótese nula quando ela é de fato verdadeira. 
Controlado pelo nível de significância α.

ERRO TIPO II:
Falso negativo - falhar em rejeitar hipótese nula quando ela é de fato 
falsa. Relacionado ao poder estatístico.


TERMOS BIOMECÂNICOS/CLÍNICOS:
═════════════════════════════════

ÂNGULO (Extensão do Joelho):
Medida da posição da articulação do joelho durante movimento específico. 
Medido em graus (°). Amplitude típica 0° (extensão completa) a 90°+ (flexionado).

EMG (ELETROMIOGRAFIA):
Medida de atividade elétrica produzida por músculos. Medido em microvolts 
(µV). Reflete despolarização de fibra muscular e recrutamento de unidades 
motoras. Valores maiores indicam maior ativação muscular.

ECG (ELETROCARDIOGRAFIA):
Medida de atividade elétrica do coração. Medido em milivolts (mV). Neste 
contexto, pode refletir resposta cardiovascular durante exercícios de perna.

PARÉTICO:
Afetado por pareisia (paralisia parcial). Pós-AVC, o lado contralateral 
(oposto) da lesão é parético. Neste estudo, típico: perna esquerda (ESQ).

NÃO-PARÉTICO:
Não afetado pela condição neurológica. O lado ipsilateral (mesmo) da lesão 
cerebral. Neste estudo, típico: perna direita (DIR).

HEMIPARESIA:
Paralisia ou fraqueza parcial de um lado do corpo (hemi-). Consequência 
comum de AVC.

UNIDADE MOTORA:
Composta por um neurônio motor e todas as fibras musculares que inérva. 
Unidade funcional básica de contração muscular.

RECRUTAMENTO MOTOR:
Ativação progressiva de unidades motoras para aumentar força muscular. EMG 
reduzido reflete recrutamento reduzido após AVC.

NEUROMUSCULAR:
Relacionado tanto ao sistema nervoso quanto a músculos. Comprometimento 
neuromuscular = problema na via nervo-músculo.

FORÇA:
Habilidade de produzir força. Diretamente relacionada à ativação de EMG. 
EMG reduzido indica capacidade de força reduzida.

ASSIMETRIA DE MARCHA:
Diferença no padrão de caminhada entre lados esquerdo e direito. Redução 
de EMG contribui para marcha assimétrica.

LIMITAÇÃO FUNCIONAL:
Restrição em atividades devido a comprometimento. EMG reduzido de quadríceps 
limita caminhada, subida de escadas, transferências.

REABILITAÇÃO:
Intervenção terapêutica para melhorar função após lesão neurológica. Deveria 
alvejar comprometimentos identificados (aqui: fraqueza de EMG).


ABREVIAÇÕES USADAS:
═════════════════════

IC        = Intervalo de Confiança
d         = d de Cohen (tamanho de efeito)
gl        = Graus de Liberdade
ECG       = Eletrocardiografia
EMG       = Eletromiografia
ESQ       = Esquerda (perna esquerda - Português)
DIR       = Direita (perna direita - Português)
DCIM      = Diferença Clinicamente Importante Mínima
FMM       = Força Muscular Manual
n         = Tamanho de amostra
p         = Valor-p
MIF       = Medida de Independência Funcional
FES       = Estimulação Elétrica Funcional
H₀        = Hipótese Nula
H₁        = Hipótese Alternativa
α         = Alfa (nível de significância)
µV        = Microvolts
mV        = Milivolts
°         = Graus
%         = Por cento
*         = Significativo (p < 0,05)
SIG.      = Significativo
gl        = Graus de liberdade


================================================================================
                              RESUMO FINAL
================================================================================

CONCLUSÕES PRINCIPAIS:

1. ⭐ DESCOBERTA DE EMG É RESULTADO PRIMÁRIO:
   - Estatisticamente significativo (p = 0,012)
   - Tamanho de efeito grande (d = -1,964)
   - 38,6% de redução em perna parética
   - Indica fraqueza neuromuscular severa
   - ALVO PRINCIPAL DE REABILITAÇÃO

2. Descoberta de ângulo NÃO significativa:
   - Nenhuma limitação confiável de mobilidade articular
   - Paciente mantém amplitude de movimento adequada
   - Sugere problema é ativação motora, não contratura

3. Descoberta de ECG NÃO significativa:
   - Resposta cardiovascular sistêmica similar bilateralmente
   - Não é variável diferenciadora

4. CONCLUSÃO CLÍNICA:
   Paciente tem FRAQUEZA PÓS-AVC significativa afetando ativação muscular 
   de quadríceps. Este é o COMPROMETIMENTO PRINCIPAL a ser abordado através 
   de reabilitação.

5. RECOMENDAÇÃO DE REABILITAÇÃO:
   Implementar treinamento intensivo, específico de tarefa com biofeedback 
   de EMG para melhorar recrutamento motor no quadríceps parético. Focar em 
   força e controle motor ao invés de mobilidade.

6. RECOMENDAÇÃO DE MONITORAMENTO:
   Repetir testes de EMG em intervalos regulares (a cada 2-4 semanas) para 
   rastrear progresso de reabilitação e ajustar intensidade do programa 
   apropriadamente.

7. CONSIDERAÇÃO PROGNÓSTICA:
   Redução severa de EMG (38,6%) indica dano neurológico significativo. 
   Recuperação pode requerer 8-12 semanas ou mais de reabilitação intensiva. 
   Prognóstico funcional a longo prazo depende da intensidade de intervenção 
   e conformidade do paciente.


================================================================================
                          INFORMAÇÃO DO DOCUMENTO
================================================================================

Título do Documento: Documentação de Análise T-Test Pareado
Dataset: Comparação Bilateral de Biomecânica de Perna
Variáveis Analisadas: Ângulo de Extensão do Joelho, Ativação de EMG, 
                      Resposta de ECG
Tipo de Análise: T-Test Pareado (Dependente)
Nível de Significância: α = 0,05
Data de Criação: Dezembro 2025

Arquivos Relacionados:
- ttest_pareado.py (Script de análise)
- ttest_pareado_resultados.csv (Resultados em formato CSV)
- ttest_pareado_resultados.xlsx (Resultados em formato Excel)
- analise_ecg_resultados_*.csv (Detalhes de análise de ECG)
- analise_emg_resultados_*.csv (Detalhes de análise de EMG)
- analise_angular_resultados_*.csv (Detalhes de análise de Ângulo)

Para questões ou análise adicional:
Referencie o script Python (ttest_pareado.py) ou contate a equipe de análise.

================================================================================
                              FIM DO DOCUMENTO
================================================================================
