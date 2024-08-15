# Desafio de Estimativa de Fretes
![capa](img/wallpaper.png)

# Contexto do Negócio
Este projeto envolve a análise e previsão de custos de frete rodoviário para o estado do Mato Grosso. A base de dados principal é composta por duas tabelas:

**freight_costs.csv:** Contém um subconjunto de cotações de frete com origem no estado do Mato Grosso e destinos variados.

**distances.csv:** Inclui as distâncias rodoviárias entre os municípios do Mato Grosso e todos os outros municípios do Brasil.

As colunas id_city_origin e id_city_destination identificam, respectivamente, os municípios de origem e destino das cargas, utilizando códigos padronizados pelo IBGE.

# 🎯 Objetivos
**Output 1:** Gerar uma base de dados histórica em formato CSV contendo cotações de frete de todos os municípios do Mato Grosso para destinos específicos (códigos: 1501303, 1506807, 3205309, 3548500, 4118204, 4207304, 4216206, 4315602).

**Output 2:** Estimar e gerar uma base de dados em formato CSV com as cotações de frete para as próximas 52 semanas para os mesmos trajetos.

# 📋 Qual o meu plano para resolver o problema?
Meu planejamento é terminar o primeiro ciclo end-to-end de maneira rápida com os dados disponíveis para mapear todos os problemas que podem estar em diferentes etapas do projeto e entregar valor rápido para o stakeholder. No primeiro ciclo, estou mais preocupado com a estrutura do projeto e fazer o modelo funcionar do início até a previsão, no próximo ciclo pretendo aumentar a complexidade da solução.                                                                                           |

# 📖 Dicionário dos Dados

| Coluna                | Descrição                                                                                   |
|-----------------------|---------------------------------------------------------------------------------------------|
| **id_city_origin**    | Representa o código IBGE do município de origem da carga.                                    |
| **id_city_destination** | Representa o código IBGE do município de destino da carga, presente nas bases de cotações e distâncias. |
| **distance**          | Distância rodoviária entre o município de origem e o município de destino, em quilômetros.   |
| **freight_cost**      | Custo do frete para o transporte da carga entre os municípios de origem e destino.           |

# Premissas assumidas
1. Custos fixos: Os custos de frete variam de acordo com a distância, mas outras variáveis como peso da carga e tipo de mercadoria foram consideradas constantes.
2. Normalidade dos Dados: Assumi que as distribuições de probabilidade do custo do frete e distâncias seguem uma distribuição mais próxima da gaussiana, o que permite a modelagem de regressão sem a necessidade de transformações complexas dos dados.
3. Estabilidade dos Fatores Externos: Não levei em conta política de transporte, tarifas adicionais e regulamentações.

# 🛠️ Ferramentas Utilizadas

## Modelagem de Dados e treinamento do algoritmo
- **Scikit-learn:** Biblioteca de machine learning em Python usada para pré processamento de dados e implementação de algoritmos de aprendizado supervisionado e não supervisionado.
- **XGBoost Regressor:** Implementação avançada do algoritmo Gradient Boosting, otimizada para problemas de regressão, conhecida pela alta precisão e eficiência.

## Desenvolvimento e controle de versão
- **Git:** Sistema de controle de versão amplamente utilizado para gerenciar o código-fonte.
- **Anaconda:** Programa de gerenciamento de ambientes virtuais no Windows, facilitando a gestão de pacotes e dependências.

# Configuração

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Ceritique-se de que os dados estão em `data/freight_costs.csv` e `data/distances.csv`

## Execução

- Execute o script principal

# 🚚 Conclusão 
Meu modelo cumpre o objetivo de fornecer previsões de cotações de frete para o estado do Mato Grosso para as próximas 52 semanas usando XGBoost.

# 🔎 Próximos Passos
-

