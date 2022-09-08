
### 在 Pipeline 中想要 clone submodule 怎麼做
```
1. .gitsubmodule 格式為
[submodule "proto"]
  path = proto
  url = ../proto.git

2. bitbucket-pipelines.yml
- step:
  name: testing
  script:
    - apk update && apk upgrade && apk add --no-cache bash git openssh
    - git submodule update --init proto
    - cp .env.example ./test/.env
    - sh ./scripts/alpine_setup.sh
    - sh ./scripts/integration_testing.sh

3. 在想要 clone submodule 的 repo 設定中產生 SSH key
  Repository settings > PIPELINES > SSH Keys > Generate key > Copy it
 
4. 在 submodule repo 中設定 Access key
  Repository settings > GENERAL > Access keys > Add key

// https://stackoverflow.com/questions/53121955/how-to-use-git-submodules-with-bitbucket-pipelines
```