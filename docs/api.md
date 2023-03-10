# Exemplos de utilização

### Buscando por um código NCM único

Mesmo a API encontrando um único valor correspondente do NCM ela irá retornar uma lista com um objeto JSON dentro.

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

### Buscando por um grupo de NCM's

Utilizando a mesma rota nós podemos buscar por um código de NCM mais abrangente, de forma a retornar todos os casos que estejam "dentro" da classificação pesquisada.

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
