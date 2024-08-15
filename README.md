# Desafio de Estimativa de Fretes
![capa](img/wallpaper.png)

# 💼 Contexto do Negócio
Este projeto foi desenvolvido para uma empresa de Inteligência em Agronegócio que utiliza Data Science Aplicada em suas soluções. As principais áreas de atuação são logística, crédito, mercados agrícolas, sementes/defensivos e fertilizantes. O principal desafio da empresa é auxiliar seus clientes na tomada de decisões no mercado de commodities agrícolas por meio soluções com Forecast e Inteligência de mercado.

O agronegócio é um dos setores fundamentais da economia brasileira, seu PIB foi de R$ 2,45 trilhões no primeiro trimestre de 2024, segundo relatório da [Cepea/Esalq/USP e CNA](https://www.cepea.esalq.usp.br/br/pib-do-agronegocio-brasileiro.aspx).

O desafio central deste projeto é a previsão de cotações de frete rodoviário para o estado do Mato Grosso. Pretendo fornecer insights acionáveis e previsões precisas para as próximas 52 semanas, permitindo que produtos e empresas de logística consigam otimizar suas operações, planejamento financeiro e gestão de riscos.

A base de dados é composta por duas tabelas:

**freight_costs.csv:** Contém um subconjunto de cotações de frete com origem no estado do Mato Grosso e destinos variados.

**distances.csv:** Inclui as distâncias rodoviárias entre os municípios do Mato Grosso e todos os outros municípios do Brasil.

As colunas "id_city_origin" e "id_city_destination" identificam, respectivamente, os municípios de origem e destino das cargas, utilizando códigos padronizados pelo IBGE.

# 🎯 Objetivos
**Output 1:** Gerar uma base de dados histórica em formato CSV contendo cotações de frete de todos os municípios do Mato Grosso para destinos específicos (códigos: 1501303, 1506807, 3205309, 3548500, 4118204, 4207304, 4216206, 4315602).

**Output 2:** Estimar e gerar uma base de dados em formato CSV com as cotações de frete para as próximas 52 semanas para os mesmos trajetos.

# 📋 Qual o meu plano para resolver o problema?
Meu planejamento é terminar o primeiro ciclo end-to-end de maneira rápida com os dados disponíveis para mapear todos os problemas que podem estar em diferentes etapas do projeto e entregar valor rápido para o stakeholder. No próximo ciclo pretendo aumentar a complexidade da solução.                                                                                           

# 📖 Dicionário dos Dados

| Coluna                | Descrição                                                                                   |
|-----------------------|---------------------------------------------------------------------------------------------|
| **id_city_origin**    | Representa o código IBGE do município de origem da carga.                                    |
| **id_city_destination** | Representa o código IBGE do município de destino da carga, presente nas bases de cotações e distâncias. |
| **distance**          | Distância rodoviária entre o município de origem e o município de destino, em quilômetros.   |
| **freight_cost**      | Custo do frete para o transporte da carga entre os municípios de origem e destino.           |
| **dt_reference** | Data de referência do custo do frete                                                             |


# ❗ Premissas assumidas
**1. Custos fixos:** Os custos de frete variam de acordo com a distância, mas outras variáveis como peso da carga e tipo de mercadoria foram consideradas constantes.

**2. Normalidade dos Dados:** Assumi que as distribuições de probabilidade do custo do frete e distâncias seguem uma distribuição mais próxima da gaussiana, o que permite a modelagem de regressão sem a necessidade de transformações complexas das features.

**3. Estabilidade dos Fatores Externos:** Não levei em conta política de transporte, tarifas adicionais e regulamentações.

**4. Custo Monetário:** Assumi que as cotações de frete estão em Reais (R$)

# 🛠️ Ferramentas Utilizadas

## Linguagem de programação
- **Python 3.11.9:** Linguagem de programação utilizada para desenvolvimento do código.

## Modelagem de Dados e treinamento do algoritmo
- **Scikit-learn:** Biblioteca de machine learning em Python usada para pré processamento de dados e implementação de algoritmos de aprendizado supervisionado e não supervisionado.
- **XGBoost Regressor:** Implementação avançada do algoritmo Gradient Boosting, otimizada para problemas de regressão, conhecida pela alta precisão e eficiência.
- **Random Search:** Técnica de otimização de hiperparâmetros que seleciona combinações aleatórias dentro de um espaço de busca definido.
- **Feature Importance:** Método para avaliar a relevância de cada variável no modelo. Utilizando permutation importance, medi o impacto na performance do modelo ao permutar aleatoriamente os valores de cada feature. Features que causam maior queda na performance quando permutadas são consideradas mais importantes.

## Desenvolvimento e controle de versão
- **Git:** Sistema de controle de versão amplamente utilizado para gerenciar o código-fonte.
- **Anaconda:** Programa de gerenciamento de ambientes virtuais no Windows, facilitando a gestão de pacotes e dependências.

## Métricas de avaliação do modelo
- **Root Mean Squared Error (RMSE)** Métrica muito utilizada em problemas de regressão, ela mede a diferença entre valores previstor pelo modelo e valores reais. É calculada como a raiz
quadrada da média dos erros quadráticos. Quanto menor o valor do RMSE, melhor é a performance do modelo, porque mostra que as previsões tem um baixo erro.
- **Mean Absolute Percentage Error (MAPE)** Métrica que avalia a precisão das previsões em termos percentuais. Ela é calculada como a média do erro absoluto percentual entre o valor previsto e o valor real. Quanto menor o MAPE, melhor a precisão do modelo, pois indica que as previsões estão mais próximas dos valores reais em termos percentuais.

![resultado](img/resultado.png)


# 💲 Business Performance

O modelo de previsão de fretes tem uma margem de erro média de 11,23%. Para exemplificar, coloquei abaixo uma análise de cenários, com um exemplo de cotação de R$ 1.000,00

| Cenário         | Valor do Frete     | Impacto para Produtores | Impacto para Empresas de Logística |
|-----------------|--------------------|---------------------------------|------------------------------------|
| Previsão Base   | R$ 1.000,00        | Neutro                          | Neutro                             |
| Previsão abaixo | R$ 887,70          | Favorável                       | Desfavorável                       |
| Previsão acima | R$ 1.112,30        | Desfavorável                    | Favorável                          |

Abaixo, trouxe alguns Insights que ajudam a solucionar as dores dos clientes:

**1. Competitividade logística:** Com um erro médio de 11,23%, o cliente conta com uma ferramenta que possui mais precisão nas cotações para estimar custos ou receitas de frete, dependendo de sua posição na cadeia logística.

**2. Planejamento:** As previsões permitem que produtores e empresas de logística planejem suas operações e negociações com base em uma variação conhecida.

**3. Gestão de riscos:** O modelo auxilia na quantificação dos riscos associados às flutuações de preços de frete, permitindo que o cliente tenha mais segurança financeira.

**4. Otimização logística:** O cliente pode focar em otimizar rotas e operações onde o impacto financeiro é menor e investigar onde o impacto está tendo maior variação.

O modelo de previsão ajuda os clientes a tomarem decisões mais velozes e assertivas sobre precificação, orçamento e estratégias logísticas para as próximas 52 semanas, considerando diferentes cenários baseados na margem de erro médio de 11,23%.

# Configuração e execução

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Ceritique-se de que os dados estão em `data/freight_costs.csv` e `data/distances.csv`
4. Execute o script principal ( python main.py )

# 🔎 Conclusão e próximos passos
Meu modelo cumpre o objetivo de fornecer previsões de cotações de frete para o estado do Mato Grosso para as próximas 52 semanas usando XGBoost. A Métrica utilizada para calcular a performance do modelo foi o RMSE, mas utilizei o MAPE para mostrar a peformance financeira pela facilidade de entendimento.
### Impacto no Negócio:

- O modelo permite que clientes antecipem flutuações nos cotações de frete.
- Oferece uma vantagem competitiva para empresas de logística na precificação de serviços.
- Auxilia na gestão de riscos financeiros.


### Como próximos passos listei abaixo o que pretendo fazer:

- Tentar implementar uma transformação de natureza com base na coluna dt_reference para captar comportamento cíclico.
- Tentar criar novas features que talvez expliquem melhor o fenômeno, a partir dessa transformação de natureza.
