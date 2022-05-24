**Um script simples desenvolvido em Python para buscar o último status de um objeto utilizando a API dos Correios.**

---

**Utilização:**

`python correios.py CódigoDoObjeto`

Exemplo: `python correios.py AA123456789BR`

---

Output:

`
Código do objeto: AA123456789BR
Tipo postal: ENCOMENDA PAC

Status: Objeto entregue ao destinatário
Data: 2022-03-22
Hora: 10:57

Status: Objeto saiu para entrega ao destinatário
Data: 2022-03-22
Hora: 09:35

Status: Objeto em trânsito - por favor aguarde
Data: 2022-03-21
Hora: 14:02

Status: Objeto em trânsito - por favor aguarde
Data: 2022-03-19
Hora: 00:47

Status: Objeto em trânsito - por favor aguarde
Data: 2022-03-16
Hora: 15:18

Status: Objeto postado
Data: 2022-03-16
Hora: 15:14
`
