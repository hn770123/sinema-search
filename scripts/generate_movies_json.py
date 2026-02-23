"""
映画データのJSONファイルを生成するスクリプト。

Movie/ ディレクトリ内のMarkdownファイルを走査し、
YAML Frontmatterのメタデータを抽出して movies.json を生成します。
"""
import os
import json
import frontmatter

MOVIE_DIR = 'Movie'
OUTPUT_FILE = 'movies.json'

def main():
    """
    メイン処理。
    Markdownファイルを読み込み、JSONファイルを出力します。
    """
    movies = []
    # ディレクトリの存在確認
    if not os.path.exists(MOVIE_DIR):
        print(f"ディレクトリ {MOVIE_DIR} が存在しません。")
        return

    # ディレクトリ内のファイルを走査
    for filename in os.listdir(MOVIE_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(MOVIE_DIR, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    # Frontmatterをパース
                    post = frontmatter.load(f)
                    metadata = post.metadata
                    # IDとしてファイル名（拡張子なし）を追加
                    metadata['id'] = os.path.splitext(filename)[0]
                    # Markdown本文を追加
                    metadata['content'] = post.content
                    movies.append(metadata)
            except Exception as e:
                print(f"ファイル {filename} の処理中にエラーが発生しました: {e}")

    # ID順でソート（一覧表示の並び順を安定させるため）
    movies.sort(key=lambda x: x.get('id', ''))

    # JSONファイルとして出力
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)

    print(f"{OUTPUT_FILE} を生成しました。件数: {len(movies)}")

if __name__ == "__main__":
    main()
