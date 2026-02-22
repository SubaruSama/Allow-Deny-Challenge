# Allow-Deny Challenge

Esse desafio consiste em criar duas listas:
* Denylist
* Allowlist

## Denylist

Lista de URLs que serão bloqueadas pelo camada acima. As URI schemes aceitas são:

* ``http://``
* ``https://``
* ``ftp://``

Se uma URL não conter alguma scheme da lista acima, será atribuido o scheme `http://`.

## Allowlist

Lista de URLs que serão liberadas pela camada acima. As URI schemes aceitas são:

* ``http://``
* ``https://``
* ``ftp://``

## Funcionalidades

As funcionalidades descritas nesta seção devem ser presentes nas duas entidades.

Deve gerar uma lista para cada, `denylist.txt` e `allowlist.txt`.

As URLs devem ser passadas via argumento. Ex: `bouncer.py --add-denylist http://some-phishing-site.io/id?=1`

Quando uma URL enviada não estiver dentro das schemes esperadas, retornar erro informando que não está nos padrões.

Deve gerar uma estatistica simples de quantos itens há em cada arquivo. Ex: `bouncer.py --stats`, assim retornando quantos itens há em cada lista.
  * **BONUS**: sumarizar por domínio

Devem existir testes conforme a metodologia TDD.
