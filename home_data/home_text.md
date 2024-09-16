# Atividade Avaliativa

- Aluno: Rafael Freesz Resende Corrêa
- Disciplina: Computação Inteligênte (2024.2)
- Mestrado em Ciência da Computação

---

O presente projeto utiliza Lógica Fuzzy para solução para três problemas como segue:

### 1- Máquina de Lavar
O enunciado detalhado deste problema está presente em \[1\]

**Variáveis de entrada:**
- Sujeira ($X_1$):
    - Pouca quantidade de sujeira;
    - Média quantidade de sujeira;
    - Grande quantidade de sujeira.
- Mancha ($X_2$):
    - Sem mancha;
    - Média mancha;
    - Grande mancha.

**Matriz Associativa Fuzzy:**

| $X_1$ |    |   |    |   |
|-------|----|---|----|---|
| **PS**    | $MC$ | $M$ | $L$  |   |
| **MS**    | $C$  | $M$ | $L$  |   |
|       | **SM** | **M** | **GM** | $X_2$  |

**Variável de Saída:**
-   Tempo de Lavagem (Y):
    - Muito Longo;
    - Longo;
    - Médio;
    - Curto;
    - Muito Curto.

### 2- Central de Peças

O enunciado detalhado deste problema está presente em \[1\]

**Variáveis de entrada:**
- Tempo Médio de Espera ($m$):
    - Médio;
    - Pequeno;
    - Muito Pequeno.
- Fator de Utilização ($p$)*:
    - Alto;
    - Médio;
    - Baixo.
- Número de Funcionários ($s$)*:
    - Grande;
    - Médio;
    - Pequeno.

\* Para fins de cálculo de inferência e defuzzificação, o Fator de Utilização não foi considerado.

**Matriz Associativa Fuzzy:**

| $s$ |    |   |    |   |
|-------|----|---|----|---|
| **G**    | $MP$ | $P$ | $MP$  |   |
| **M**    | $PG$  | $PP$ | $P$  |   |
| **P**    | $MG$  | $G$ | $M$  |   |
|       | **MP** | **P** | **M** | $m$  |

**Variável de Saída:**
-   Número de Peças Extras (n):
    - Muito Grande;
    - Grande;
    - Pouco Grande;
    - Médio;
    - Pouco Pequeno;
    - Pequeno;
    - Muito Pequeno.


### 3- Ultrapassagem

O enunciado detalhado deste problema está presente em \[1\].
O problema foi modelado considerando a **velocidade** atual do veículo em relação à **distância** para o veículo à frente. Os limites de ambas variáveis foram definidos de acordo com o estudo realizado em \[2\], que apresenta a relação de velocidade e distância necessária para uma ultrapassagem segura. O Gráfico abaixo apresenta essa relação com base nos dados do autor:
