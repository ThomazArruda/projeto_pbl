# Pasta de Dados

O banco SQLite `clinic.db`, utilizado pelo painel Streamlit, é gravado neste
diretório. Ele contém:

- A lista de pacientes cadastrados (`patients`).
- O histórico de sessões de cada paciente (`sessions`), com os dados da sessão
  serializados em JSON.

O arquivo `.gitignore` está configurado para ignorar automaticamente o banco de
dados e quaisquer exportações (`.json`, `.csv`) que você venha a gerar aqui, de
modo que informações sensíveis não sejam versionadas.
Arquivos JSON gerados pelo painel Streamlit são gravados neste diretório. Eles
contêm o histórico de sessões de cada paciente e não devem ser versionados. O
arquivo `.gitignore` já está configurado para ignorar automaticamente todos os
JSON armazenados aqui.
