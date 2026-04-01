A função transformar_dados recebe um DataFrame com os dados extraídos e cria uma cópia para não modificar o original. Em seguida, ela adiciona uma nova coluna chamada mensagem usando df.apply(gerar_mensagem, axis=1), ou seja, aplica a função gerar_mensagem em cada linha do DataFrame. Por fim, retorna somente as colunas necessárias: Nome, Conta, Cartão e mensagem.

A função carregar_dados recebe o DataFrame transformado e grava o resultado em um arquivo CSV. O nome do arquivo de saída é clientes_mensagens.csv por padrão, mas pode ser alterado ao chamar a função. O parâmetro index=False garante que o índice do DataFrame não seja salvo como coluna extra no arquivo. Após a escrita, ela imprime uma mensagem confirmando o caminho do arquivo gerado.

O bloco if __name__ == "__main__": é o ponto de entrada do script quando ele é executado diretamente. Ele chama as três etapas do fluxo ETL: extração (extrair_dados()), transformação (transformar_dados(df_bruto)) e carga (carregar_dados(df_transformado)). Dessa forma, o script lê os dados de entrada, constrói as mensagens personalizadas e salva o resultado final em disco.


