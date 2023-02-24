# ⚙️ Rotas

> **GET**
>
> Retorna somente um NCM específico
>
> ```text
> .../api/ncm/<numero_do_ncm>
> ```


> **GET**
>
> Retorna todos os dados dos produtos registrados na TIPI
>
> ```text
> .../api/ncm/all
> ```

## 🌐Template

> **GET**
>
> Renderiza uma página HTML com todos os dados da tabela TIPI
>
> ```text
> .../
> ```

# Exemplos

> **GET**
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
>     "EX": "",
>     "DESCRIÇÃO": "Para fotomicrografia",
>     "ALÍQUOTA(%)": 3.25
>   }
> ]
> ```

> **GET**
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
>     "EX": "",
>     "DESCRIÇÃO": "Para fotomicrografia",
>     "ALÍQUOTA(%)": 3.25
>   }
> ]
> ```

> **GET**
>
> ```text
> .../api/ncm/9011.20.1
> ```
>
> Retorno
> ```json
> [
>  {
>    "NCM": "0105.11",
>    "EX": "",
>    "DESCRIÇÃO": "Aves da espécie Gallus domesticus",
>    "ALÍQUOTA(%)": null
>  },
>  {
>    "NCM": "0105.11.10",
>    "EX": "",
>    "DESCRIÇÃO": "De linhas puras ou híbridas, para reprodução",
>    "ALÍQUOTA(%)": 0
>  },
>  {
>    "NCM": "0105.11.90",
>    "EX": "",
>    "DESCRIÇÃO": "Outros",
>    "ALÍQUOTA(%)": 0
>  }
>]
> ```
