# 映画データベース (Movie Database)

映画データをMarkdown形式で管理し、自動的にJSONインデックスを生成するプロジェクトです。

## ディレクトリ構成
- `Movie/`: 映画ごとのMarkdownファイルが格納されています。
- `scripts/`: JSON生成スクリプトなどのツールが格納されています。
- `movies.json`: 自動生成される映画データのインデックスファイルです。

## 映画データの追加方法
1. `Movie/` ディレクトリに新しい `.md` ファイルを作成します（例: `Movie/Title.md`）。
2. 以下のフォーマットに従って YAML Frontmatter を記述し、本文にあらすじなどを書きます。

```markdown
---
title: "映画タイトル"
original_title: "Original Title"
director: "監督名"
country: "制作国"
release_year: 2024
genre: ["ジャンル1", "ジャンル2"]
rating_child: 5
has_sexual_content: false
has_violence: false
sf_rating: 3
---

## あらすじ
あらすじを記述...
```

3. GitHubにプッシュすると、自動的に `movies.json` が更新されます。

## 自動化について
GitHub Actions (`.github/workflows/update_movies.yml`) により、`Movie/` ディレクトリ内の変更を検知して `scripts/generate_movies_json.py` が実行され、`movies.json` が更新されます。
