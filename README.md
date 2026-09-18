# ci-cd-actions

Projeto fake pra testar aprovacao manual no GitHub Actions.

O job `deploy` so roda depois que alguem clica em **Review deployments -> Approve**
na pagina do run. Isso vem do `environment: production` + protection rule.

## Setup (uma vez, nao da pra fazer em YAML)

Settings -> Environments -> New environment -> `production` ->
marcar **Required reviewers** e adicionar voce mesmo -> Save.

Sem esse passo o environment existe mas nao pede aprovacao: o deploy passa direto.
