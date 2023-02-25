# Rotas

> #### GET
>
> Retorna somente um NCM específico
>
> ```text
> .../api/ncm/<numero_do_ncm>
> ```


> #### GET
>
> Retorna todos os dados dos produtos registrados na TIPI
>
> ```text
> .../api/ncm/all
> ```

# Exemplos

> #### GET
>
> ```text
> .../api/ncm/9011.20.1
> ```
>
> Retorno
> ```json
> [
>   {
>     "NCM": "9011.20.10",
>     "EX": null,
>     "DESCRIÇÃO": "Para fotomicrografia",
>     "ALÍQUOTA(%)": 3.25
>   }
> ]
> ```

> #### GET
>
> ```text
> .../api/ncm/1.03
> ```
>
> Retorno
> ```json
> [
>  {
>    "NCM": "1.03",
>    "EX": null,
>    "DESCRIÇÃO": "Animais vivos da espécie suína.",
>    "ALÍQUOTA(%)": null
>  },
>  {
>    "NCM": "0103.10.00",
>    "EX": null,
>    "DESCRIÇÃO": "Reprodutores de raça pura",
>    "ALÍQUOTA(%)": 0
>  },
>  {
>    "NCM": "103.9",
>    "EX": null,
>    "DESCRIÇÃO": "Outros",
>    "ALÍQUOTA(%)": null
>  },
>  {
>    "NCM": "0103.91.00",
>    "EX": null,
>    "DESCRIÇÃO": "De peso inferior a 50 kg",
>    "ALÍQUOTA(%)": 0
>  },
>  {
>    "NCM": "0103.92.00",
>    "EX": null,
>    "DESCRIÇÃO": "De peso igual ou superior a 50 kg",
>    "ALÍQUOTA(%)": 0
>  }
>]
> ```
