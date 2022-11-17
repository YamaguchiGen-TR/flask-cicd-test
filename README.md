# Flask サンプルアプリケーション

---

### 環境構築

- 仮想環境作成

  ```bash
  python -m venv [venvName]
  ```

- 仮想環境に入る

  ```bash
  [venvName]/Scripts/activate
  ```

- パッケージインストール

  ```bash
  pip install -r requirements.txt
  ```

---

### AWSにデプロイ

- [Zappa](https://github.com/zappa/Zappa) を利用してAPI Gateway + Lambdaにデプロイ

  ```bash
  # デプロイ実行

  zappa deploy dev

  # アプリを削除
  zappa undeploy dev

  # デプロイ済みのアプリを更新
  zappa update dev
  ```

# デプロイ時に502エラーになったら

以下を参照。

[zappaでFlaskアプリをデプロイできなくなった](https://qiita.com/marshall1987xRyuta/items/f95971f2008bf52f94f6)

---

### その他コマンド

- CloudWatchのログを表示

  ```bash
  zappa tail
  ```
  

### CI/CDにあたって

  - デプロイコマンドについて

    ※一部推測があります。

    zappaはFlaskアプリをうまいことLambdaでそのまま使えるようにzipファイルにまとめてデプロイしてくれる。
  
    Python環境のイメージ（？）を buildspec で指定すれば以下のコマンドだけでデプロイ完了するかと。

    ```bash
    pip install -r requirements.txt
    zappa deploy dev
    ```

    デプロイ済みのアプリに対して `zappa deploy dev` すると「デプロイ済みです」とエラーになってしまうので

    ```bash
    zappa update dev
    ```

    を使う必要がある。Freekeyは `zappa update dev` のみ使用していた気がする？

  - zappa_settings.jsonについて
    
    `zappa update dev` の `dev` 部分は `zappa_settings.json` の `dev` と紐づく。

    仮に `dev2` という設定を追加したら、デプロイコマンドも `zappa update dev2` のように変わる。

    ```json5
    {
      "dev": {
        "app_function": "run.app",  // Lambda起動時にrun.pyのappを実行する
        "aws_region": "ap-northeast-1",
        "profile_name": "integrated_app_dev",  // AWS CLIで使用するプロファイル
        "project_name": "app-ci-cd",  // 任意
        "runtime": "python3.9",
        "s3_bucket": "app-zappa-560333535967",  // zappaが一時的に使用するバケット
        "endpoint_configuration": [
          "REGIONAL"
        ],
        "role_name": "App-ZappaLambdaExecutionRole", // APIGateway, Lambdaに割り当てるロール
        "manage_roles": false,  // zappaが勝手にロールを作成するかどうか
        "lambda_description": "CI/CDテストアプリ",  // 任意
        "apigateway_description": "CI/CDテストアプリ",  // 任意
        "cloudwatch_log_level": "INFO", // APIGatewayのログレベル
        "cors": true  // APIGatewayのCORS設定
      }
    }
    ```
