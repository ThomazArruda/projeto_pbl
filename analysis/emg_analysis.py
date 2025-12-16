"""
Análise Estatística de Dados de EMG - Sessões 19-23
Script para análise da variação EMG (delta max-min) entre pernas esquerda e direita
com teste de normalidade de Shapiro-Wilk
"""

import sys
import io

# Configurar encoding para UTF-8 no Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import sqlite3
import json
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from datetime import datetime

# Configuração de estilo para gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 10

class EMGDeltaAnalyzer:
    """Classe para análise de variação EMG e teste de normalidade"""
    
    def __init__(self, db_path="../backend/clinic.db"):
        """
        Inicializa o analisador com caminho para o banco de dados
        
        Args:
            db_path: Caminho para o arquivo clinic.db
        """
        self.db_path = Path(db_path)
        self.conn = None
        self.sessions_data = {}
        self.deltas_esq = []
        self.deltas_dir = []
        self.shapiro_results = {}
        self.descriptive_stats = {}
        
    def connect_db(self):
        """Conecta ao banco de dados SQLite"""
        try:
            self.conn = sqlite3.connect(str(self.db_path))
            print(f"✓ Conectado ao banco de dados: {self.db_path}")
        except Exception as e:
            print(f"✗ Erro ao conectar ao banco de dados: {e}")
            raise
    
    def close_db(self):
        """Fecha a conexão com o banco de dados"""
        if self.conn:
            self.conn.close()
            print("✓ Conexão com banco de dados fechada")
    
    def extract_session_data(self, session_ids=[19, 20, 21, 22, 23]):
        """
        Extrai dados brutos das sessões especificadas
        
        Args:
            session_ids: Lista de IDs de sessões a processar
        """
        print(f"\n{'='*80}")
        print(f"EXTRAÇÃO DE DADOS - Sessões {session_ids[0]} a {session_ids[-1]}")
        print(f"{'='*80}")
        
        query = f"""
            SELECT id, timestamp, duration_seconds, raw_data_blob 
            FROM sessions 
            WHERE id IN ({','.join(map(str, session_ids))})
            ORDER BY id
        """
        
        try:
            df = pd.read_sql_query(query, self.conn)
            
            if df.empty:
                print(f"✗ Nenhuma sessão encontrada para IDs: {session_ids}")
                return False
            
            print(f"✓ {len(df)} sessão(ões) encontrada(s)\n")
            
            for idx, row in df.iterrows():
                session_id = row['id']
                try:
                    raw_data = json.loads(row['raw_data_blob'])
                    self.sessions_data[session_id] = {
                        'timestamp': row['timestamp'],
                        'duration': row['duration_seconds'],
                        'raw_data': raw_data
                    }
                    print(f"  Sessão {session_id}: ✓ Dados extraídos")
                except json.JSONDecodeError as e:
                    print(f"  Sessão {session_id}: ✗ Erro ao decodificar JSON: {e}")
            
            return True
            
        except Exception as e:
            print(f"✗ Erro ao extrair dados das sessões: {e}")
            raise
    
    def calculate_deltas(self):
        """
        Calcula a variação (delta) de EMG para cada sessão
        Delta = EMG_máximo - EMG_mínimo
        """
        print(f"\n{'='*80}")
        print(f"CÁLCULO DE VARIAÇÃO EMG (DELTA)")
        print(f"{'='*80}\n")
        
        for session_id, data in sorted(self.sessions_data.items()):
            try:
                raw_data = data['raw_data']
                
                # raw_data é uma lista de dicionários com timestamps e valores
                emg_esq_list = []
                emg_dir_list = []
                
                if isinstance(raw_data, list):
                    # Extrair EMG de cada ponto de dados
                    for point in raw_data:
                        if isinstance(point, dict):
                            if 'ESQ_emg' in point:
                                emg_esq_list.append(point['ESQ_emg'])
                            if 'DIR_emg' in point:
                                emg_dir_list.append(point['DIR_emg'])
                else:
                    # Fallback para dicionário (compatibilidade)
                    emg_esq_list = raw_data.get('ESQ_emg', [])
                    emg_dir_list = raw_data.get('DIR_emg', [])
                
                emg_esq = np.array(emg_esq_list)
                emg_dir = np.array(emg_dir_list)
                
                if len(emg_esq) == 0 or len(emg_dir) == 0:
                    print(f"  Sessão {session_id}: ✗ Dados de EMG incompletos")
                    continue
                
                # Calcular deltas
                delta_esq = np.max(emg_esq) - np.min(emg_esq)
                delta_dir = np.max(emg_dir) - np.min(emg_dir)
                
                self.deltas_esq.append(delta_esq)
                self.deltas_dir.append(delta_dir)
                
                print(f"  Sessão {session_id}:")
                print(f"    - Perna Esquerda: ΔEMG = {delta_esq:.2f} µV (Min: {np.min(emg_esq):.2f} µV, Max: {np.max(emg_esq):.2f} µV)")
                print(f"    - Perna Direita:  ΔEMG = {delta_dir:.2f} µV (Min: {np.min(emg_dir):.2f} µV, Max: {np.max(emg_dir):.2f} µV)")
                
            except Exception as e:
                print(f"  Sessão {session_id}: ✗ Erro ao calcular deltas: {e}")
        
        if len(self.deltas_esq) == 0 or len(self.deltas_dir) == 0:
            print("\n✗ Nenhum delta foi calculado com sucesso")
            return False
        
        print(f"\n✓ Deltas calculados: {len(self.deltas_esq)} sessões processadas")
        return True
    
    def shapiro_wilk_test(self):
        """
        Executa o teste de Shapiro-Wilk para validar normalidade dos dados
        """
        print(f"\n{'='*80}")
        print(f"TESTE DE NORMALIDADE - SHAPIRO-WILK")
        print(f"{'='*80}\n")
        
        # Teste para perna esquerda
        stat_esq, p_value_esq = stats.shapiro(self.deltas_esq)
        self.shapiro_results['ESQ'] = {
            'statistic': stat_esq,
            'p_value': p_value_esq,
            'normal': p_value_esq > 0.05
        }
        
        # Teste para perna direita
        stat_dir, p_value_dir = stats.shapiro(self.deltas_dir)
        self.shapiro_results['DIR'] = {
            'statistic': stat_dir,
            'p_value': p_value_dir,
            'normal': p_value_dir > 0.05
        }
        
        # Impressão formatada dos resultados
        print("PERNA ESQUERDA (Parética):")
        print(f"  Estatística: {stat_esq:.6f}")
        print(f"  P-value: {p_value_esq:.6f}")
        print(f"  Resultado: {'✓ NORMAL (p > 0.05)' if p_value_esq > 0.05 else '✗ NÃO NORMAL (p ≤ 0.05)'}")
        
        print("\nPERNA DIREITA (Controle):")
        print(f"  Estatística: {stat_dir:.6f}")
        print(f"  P-value: {p_value_dir:.6f}")
        print(f"  Resultado: {'✓ NORMAL (p > 0.05)' if p_value_dir > 0.05 else '✗ NÃO NORMAL (p ≤ 0.05)'}")
    
    def calculate_descriptive_stats(self):
        """
        Calcula estatísticas descritivas para ambas as pernas
        """
        print(f"\n{'='*80}")
        print(f"ESTATÍSTICAS DESCRITIVAS")
        print(f"{'='*80}\n")
        
        for perna, deltas in [('ESQ', self.deltas_esq), ('DIR', self.deltas_dir)]:
            deltas_array = np.array(deltas)
            
            stats_dict = {
                'Perna': perna,
                'Contagem': len(deltas),
                'Média': np.mean(deltas_array),
                'Mediana': np.median(deltas_array),
                'Desvio Padrão': np.std(deltas_array, ddof=1),
                'Variância': np.var(deltas_array, ddof=1),
                'Mínimo': np.min(deltas_array),
                'Q1 (25%)': np.percentile(deltas_array, 25),
                'Q3 (75%)': np.percentile(deltas_array, 75),
                'Máximo': np.max(deltas_array),
                'Amplitude': np.max(deltas_array) - np.min(deltas_array),
                'Coef. Variação (%)': (np.std(deltas_array, ddof=1) / np.mean(deltas_array)) * 100
            }
            
            self.descriptive_stats[perna] = stats_dict
            
            print(f"PERNA {perna}:")
            for key, value in stats_dict.items():
                if key != 'Perna':
                    print(f"  {key:.<30} {value:>10.4f}")
            print()
    
    def generate_plots(self, output_dir="./"):
        """
        Gera apenas o boxplot comparativo entre as pernas
        
        Args:
            output_dir: Diretório para salvar os gráficos
        """
        print(f"\n{'='*80}")
        print(f"GERAÇÃO DE GRÁFICO")
        print(f"{'='*80}\n")
        
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Criar figura com apenas o boxplot
        fig, ax = plt.subplots(figsize=(10, 6))
        
        data_box = [self.deltas_esq, self.deltas_dir]
        bp = ax.boxplot(data_box, tick_labels=['Perna Esquerda\n(Parética)', 'Perna Direita\n(Controle)'],
                        patch_artist=True, widths=0.6)
        
        for patch, color in zip(bp['boxes'], ['#FF6B6B', '#4ECDC4']):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        ax.set_ylabel('Variação EMG (µV)', fontsize=12, fontweight='bold')
        ax.set_xlabel('Pernas', fontsize=12, fontweight='bold')
        ax.set_title('Boxplot: Distribuição de Deltas EMG', fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        
        # Salvar gráfico
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        plot_file = output_path / f"boxplot_deltas_emg_{timestamp}.png"
        plt.savefig(plot_file, dpi=300, bbox_inches='tight')
        print(f"✓ Gráfico salvo em: {plot_file}")
        
        return plot_file
    
    def export_to_csv(self, output_dir="./"):
        """
        Exporta resultados consolidados em CSV de forma clara e legível
        
        Args:
            output_dir: Diretório para salvar o arquivo CSV
        """
        print(f"\n{'='*80}")
        print(f"EXPORTAÇÃO DE RESULTADOS")
        print(f"{'='*80}\n")
        
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Criar múltiplos DataFrames para melhor organização
        session_ids = sorted(self.sessions_data.keys())
        
        # DataFrame 1: Dados por sessão
        df_sessions = pd.DataFrame({
            'Sessão': session_ids,
            'Delta_Esquerda (µV)': [round(d, 2) for d in self.deltas_esq],
            'Delta_Direita (µV)': [round(d, 2) for d in self.deltas_dir],
            'Diferença_DIR-ESQ (µV)': [round(self.deltas_dir[i] - self.deltas_esq[i], 2) for i in range(len(session_ids))]
        })
        
        # DataFrame 2: Estatísticas Descritivas Esquerda
        df_stats_esq = pd.DataFrame({
            'Métrica': list(self.descriptive_stats['ESQ'].keys()),
            'Perna_Esquerda': list(self.descriptive_stats['ESQ'].values())
        })
        
        # DataFrame 3: Estatísticas Descritivas Direita
        df_stats_dir = pd.DataFrame({
            'Métrica': list(self.descriptive_stats['DIR'].keys()),
            'Perna_Direita': list(self.descriptive_stats['DIR'].values())
        })
        
        # DataFrame 4: Resultados Shapiro-Wilk
        df_shapiro = pd.DataFrame({
            'Perna': ['Esquerda', 'Direita'],
            'Estatística': [
                round(self.shapiro_results['ESQ']['statistic'], 6),
                round(self.shapiro_results['DIR']['statistic'], 6)
            ],
            'P-value': [
                round(self.shapiro_results['ESQ']['p_value'], 6),
                round(self.shapiro_results['DIR']['p_value'], 6)
            ],
            'Resultado': [
                'NORMAL (p > 0.05)' if self.shapiro_results['ESQ']['normal'] else 'NÃO NORMAL (p ≤ 0.05)',
                'NORMAL (p > 0.05)' if self.shapiro_results['DIR']['normal'] else 'NÃO NORMAL (p ≤ 0.05)'
            ]
        })
        
        # Salvar múltiplas abas em um único arquivo Excel
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        excel_file = output_path / f"analise_emg_completa_{timestamp}.xlsx"
        
        try:
            # Tentar salvar em Excel com múltiplas abas
            with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
                df_sessions.to_excel(writer, sheet_name='Dados por Sessão', index=False)
                df_stats_esq.to_excel(writer, sheet_name='Stats Esquerda', index=False)
                df_stats_dir.to_excel(writer, sheet_name='Stats Direita', index=False)
                df_shapiro.to_excel(writer, sheet_name='Shapiro-Wilk', index=False)
            print(f"✓ Resultados em Excel exportados em: {excel_file}")
        except Exception as e:
            print(f"⚠ Aviso ao salvar Excel: {e}")
        
        # Também salvar em CSV simples e consolidado
        csv_file = output_path / f"analise_emg_resultados_{timestamp}.csv"
        
        # Criar um CSV consolidado bem formatado
        with open(csv_file, 'w', encoding='utf-8') as f:
            f.write("ANÁLISE ESTATÍSTICA DE VARIAÇÃO EMG - SESSÕES 19-23\n")
            f.write("="*80 + "\n\n")
            
            f.write("DADOS POR SESSÃO\n")
            f.write("-"*80 + "\n")
            df_sessions.to_csv(f, index=False)
            
            f.write("\n\nESTATÍSTICAS DESCRITIVAS - PERNA ESQUERDA (Parética)\n")
            f.write("-"*80 + "\n")
            df_stats_esq.to_csv(f, index=False)
            
            f.write("\n\nESTATÍSTICAS DESCRITIVAS - PERNA DIREITA (Controle)\n")
            f.write("-"*80 + "\n")
            df_stats_dir.to_csv(f, index=False)
            
            f.write("\n\nTESTE DE NORMALIDADE - SHAPIRO-WILK\n")
            f.write("-"*80 + "\n")
            df_shapiro.to_csv(f, index=False)
            
            f.write("\n\nINTERPRETAÇÃO\n")
            f.write("-"*80 + "\n")
            f.write("- Perna Esquerda (Parética): Perna afetada pelo AVC\n")
            f.write("- Perna Direita (Controle): Perna saudável de referência\n")
            f.write("- Delta (ΔEMG): Variação = EMG Máximo - EMG Mínimo\n")
            f.write("- Shapiro-Wilk p-value > 0.05: Distribuição NORMAL\n")
            f.write("- Shapiro-Wilk p-value ≤ 0.05: Distribuição NÃO NORMAL\n")
        
        print(f"✓ Resultados em CSV exportados em: {csv_file}\n")
        
        return csv_file
    
    def print_summary(self):
        """
        Imprime um resumo formatado de toda a análise
        """
        print(f"\n{'='*80}")
        print(f"RESUMO FINAL DA ANÁLISE")
        print(f"{'='*80}\n")
        
        print("INFORMAÇÕES GERAIS:")
        print(f"  - Sessões analisadas: {', '.join(map(str, sorted(self.sessions_data.keys())))}")
        print(f"  - Total de sessões: {len(self.sessions_data)}")
        print(f"  - Período: Sessões 19 a 23\n")
        
        print("RESUMO DOS DELTAS EMG:")
        print(f"  Perna Esquerda (Parética):")
        print(f"    - Média de variação: {np.mean(self.deltas_esq):.2f} µV")
        print(f"    - Desvio padrão: {np.std(self.deltas_esq, ddof=1):.2f} µV")
        print(f"    - Intervalo: [{np.min(self.deltas_esq):.2f} µV, {np.max(self.deltas_esq):.2f} µV]")
        
        print(f"\n  Perna Direita (Controle):")
        print(f"    - Média de variação: {np.mean(self.deltas_dir):.2f} µV")
        print(f"    - Desvio padrão: {np.std(self.deltas_dir, ddof=1):.2f} µV")
        print(f"    - Intervalo: [{np.min(self.deltas_dir):.2f} µV, {np.max(self.deltas_dir):.2f} µV]")
        
        print(f"\n  Diferença Média (DIR - ESQ): {np.mean(self.deltas_dir) - np.mean(self.deltas_esq):.2f} µV\n")
        
        print("TESTE DE NORMALIDADE (SHAPIRO-WILK):")
        print(f"  Perna Esquerda:")
        print(f"    - Estatística: {self.shapiro_results['ESQ']['statistic']:.6f}")
        print(f"    - P-value: {self.shapiro_results['ESQ']['p_value']:.6f}")
        print(f"    - Distribuição: {'✓ NORMAL (p > 0.05)' if self.shapiro_results['ESQ']['normal'] else '✗ NÃO NORMAL (p ≤ 0.05)'}")
        
        print(f"\n  Perna Direita:")
        print(f"    - Estatística: {self.shapiro_results['DIR']['statistic']:.6f}")
        print(f"    - P-value: {self.shapiro_results['DIR']['p_value']:.6f}")
        print(f"    - Distribuição: {'✓ NORMAL (p > 0.05)' if self.shapiro_results['DIR']['normal'] else '✗ NÃO NORMAL (p ≤ 0.05)'}")
        
        print(f"\n{'='*80}\n")
    
    def run_analysis(self, session_ids=[19, 20, 21, 22, 23], output_dir="./"):
        """
        Executa a análise completa
        
        Args:
            session_ids: Lista de IDs de sessões a analisar
            output_dir: Diretório para salvar arquivos de saída
        """
        try:
            self.connect_db()
            
            # Executar todas as etapas da análise
            if not self.extract_session_data(session_ids):
                return False
            
            if not self.calculate_deltas():
                return False
            
            self.shapiro_wilk_test()
            self.calculate_descriptive_stats()
            self.generate_plots(output_dir)
            self.export_to_csv(output_dir)
            self.print_summary()
            
            print("✓ Análise completada com sucesso!")
            return True
            
        except Exception as e:
            print(f"\n✗ Erro durante a análise: {e}")
            return False
        
        finally:
            self.close_db()


def main():
    """Função principal para executar a análise"""
    
    print("\n" + "="*80)
    print("ANÁLISE ESTATÍSTICA DE VARIAÇÃO EMG - PROJETO PBL")
    print("="*80 + "\n")
    
    # Inicializar analisador
    analyzer = EMGDeltaAnalyzer(db_path="../backend/clinic.db")
    
    # Executar análise para sessões 19-23
    output_dir = "./"
    analyzer.run_analysis(session_ids=[19, 20, 21, 22, 23], output_dir=output_dir)


if __name__ == "__main__":
    main()
