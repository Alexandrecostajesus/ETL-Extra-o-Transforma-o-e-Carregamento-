import pandas as pd
from pandas import Series

# --- FASE 1: EXTRAÇÃO ---
def extrair_dados(arquivo_entrada: str = "clientes.csv") -> pd.DataFrame:
    return pd.read_csv(arquivo_entrada)

def gerar_mensagem(row: Series) -> str:
    return f"Olá {row['Nome']}, sua conta {row['Conta']} está registrada com o cartão {row['Cartão']}."

# --- FASE 2: TRANSFORMAÇÃO ---
def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["mensagem"] = df.apply(gerar_mensagem, axis=1)
    return df[["Nome", "Conta", "Cartão", "mensagem"]]

# --- FASE 3: CARGA ---
def carregar_dados(df: pd.DataFrame, arquivo_saida: str = "clientes_mensagens.csv") -> None:
    df.to_csv(arquivo_saida, index=False)
    print(f"Dados carregados em: {arquivo_saida}")

# --- EXECUÇÃO DO FLUXO ---
if __name__ == "__main__":
    df_bruto = extrair_dados()
    df_transformado = transformar_dados(df_bruto)
    carregar_dados(df_transformado)
