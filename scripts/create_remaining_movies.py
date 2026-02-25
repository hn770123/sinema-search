import os

movies_data = [
    {
        "todo_title": "パプリカ",
        "title": "パプリカ",
        "original_title": "Paprika",
        "filename": "Paprika.md",
        "director": "今敏",
        "country": "日本",
        "release_year": 2006,
        "genre": ["アニメーション", "SF", "サスペンス"],
        "rating_child": 3,
        "has_sexual_content": True,
        "has_violence": True,
        "sf_rating": 5,
        "synopsis": "他人の夢に入り込んで治療を行う精神医療機器「DCミニ」が盗まれた。夢探偵パプリカは、現実と夢が混ざり合う危険な世界に飛び込み、犯人を追う。",
        "recommendation": "夢の中のお祭りのシーンがカラフルですごい！でもちょっと怖くて意味がわからないところもあるかも。",
        "content_warning": "夢の中でお人形が壊れたり、少し怖いシーンがある。",
        "sf_review": "夢を共有する技術というSF設定と、悪夢のような映像美が融合した傑作。"
    },
    {
        "todo_title": "スパイダーマン：スパイダーバース",
        "title": "スパイダーマン：スパイダーバース",
        "original_title": "Spider-Man: Into the Spider-Verse",
        "filename": "SpiderManIntoTheSpiderVerse.md",
        "director": "ボブ・ペルシケッティ 他",
        "country": "アメリカ",
        "release_year": 2018,
        "genre": ["アニメーション", "アクション", "ヒーロー"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 4,
        "synopsis": "突然スパイダーマンの力を手に入れた中学生マイルス。異次元からやってきた様々なスパイダーマンたちと出会い、共に敵に立ち向かいながら成長していく。",
        "recommendation": "コミックがそのまま動いているみたいでおしゃれ！色んなスパイダーマンが出てきて楽しい。",
        "content_warning": "特になし。",
        "sf_review": "マルチバース（多元宇宙）を扱ったSFアニメーションの金字塔。"
    },
    {
        "todo_title": "カンフー・パンダ",
        "title": "カンフー・パンダ",
        "original_title": "Kung Fu Panda",
        "filename": "KungFuPanda.md",
        "director": "マーク・オズボーン, ジョン・スティーヴンソン",
        "country": "アメリカ",
        "release_year": 2008,
        "genre": ["アニメーション", "アクション", "コメディ"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "カンフーオタクの太っちょパンダ、ポー。ひょんなことから伝説の「龍の戦士」に選ばれてしまい、厳しい修行を経て、最強の敵に立ち向かう。",
        "recommendation": "ポーがドジだけど一生懸命で応援したくなる！カンフーのアクションもかっこいい。",
        "content_warning": "特になし。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "ペット",
        "title": "ペット",
        "original_title": "The Secret Life of Pets",
        "filename": "TheSecretLifeOfPets.md",
        "director": "クリス・ルノー",
        "country": "アメリカ",
        "release_year": 2016,
        "genre": ["アニメーション", "コメディ", "ファミリー"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "飼い主が留守の間、ペットたちは何をしているのか？小型犬のマックスと、新しくやってきた大型犬デュークが、ニューヨークの街で大冒険を繰り広げる。",
        "recommendation": "わんちゃんやねこちゃんが可愛くて癒される！動物たちが喋るのが面白い。",
        "content_warning": "特になし。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "エイリアン",
        "title": "エイリアン",
        "original_title": "Alien",
        "filename": "Alien.md",
        "director": "リドリー・スコット",
        "country": "アメリカ, イギリス",
        "release_year": 1979,
        "genre": ["SF", "ホラー"],
        "rating_child": 1,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 5,
        "synopsis": "宇宙貨物船ノストロモ号は、謎の信号を受信して未知の惑星に降り立つ。そこで乗組員の一人に異星生物が寄生し、船内で次々と仲間を襲い始める。",
        "recommendation": "宇宙人が気持ち悪くて怖すぎるので、絶対に見ない方がいい。",
        "content_warning": "お腹からエイリアンが出てくるシーンがトラウマレベル。",
        "sf_review": "宇宙船内の閉鎖空間での恐怖を描いたSFホラーの傑作。"
    },
    {
        "todo_title": "アルマゲドン",
        "title": "アルマゲドン",
        "original_title": "Armageddon",
        "filename": "Armageddon.md",
        "director": "マイケル・ベイ",
        "country": "アメリカ",
        "release_year": 1998,
        "genre": ["SF", "アクション", "パニック"],
        "rating_child": 3,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 4,
        "synopsis": "巨大な小惑星が地球に接近。人類滅亡を阻止するため、石油掘削のプロフェッショナルたちが宇宙へ飛び、小惑星の深部で核爆弾を爆発させるという危険なミッションに挑む。",
        "recommendation": "お父さんが娘のために頑張る姿に感動して泣いちゃうかも。",
        "content_warning": "人が死ぬシーンがある。",
        "sf_review": "宇宙空間での掘削作業やスペースシャトルの描写など、壮大なSF設定。"
    },
    {
        "todo_title": "グレムリン",
        "title": "グレムリン",
        "original_title": "Gremlins",
        "filename": "Gremlins.md",
        "director": "ジョー・ダンテ",
        "country": "アメリカ",
        "release_year": 1984,
        "genre": ["SF", "コメディ", "ホラー"],
        "rating_child": 3,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 2,
        "synopsis": "発明家の父親から不思議な生き物「モグワイ」をプレゼントされたビリー。しかし、飼育のルールを破ってしまったことで、モグワイから凶暴な怪物「グレムリン」が誕生し、町中が大パニックになる。",
        "recommendation": "ギズモは可愛いけど、悪いグレムリンたちが暴れるのが怖くて気持ち悪い。",
        "content_warning": "グレムリンが電子レンジで爆発したりするシーンがグロテスク。",
        "sf_review": "不思議な生物の生態を描いたSFファンタジー要素がある。"
    },
    {
        "todo_title": "シザーハンズ",
        "title": "シザーハンズ",
        "original_title": "Edward Scissorhands",
        "filename": "EdwardScissorhands.md",
        "director": "ティム・バートン",
        "country": "アメリカ",
        "release_year": 1990,
        "genre": ["ファンタジー", "ロマンス"],
        "rating_child": 3,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 2,
        "synopsis": "丘の上の屋敷に住む、両手がハサミの人造人間エドワード。ある日、化粧品セールスの女性に連れられて町に降りるが、そのハサミのせいで人々を傷つけ、誤解されてしまう。",
        "recommendation": "手がハサミで不便そうだけど、優しいエドワードが可哀想で切なくなる。",
        "content_warning": "ハサミで顔を切ってしまったりするシーンがある。",
        "sf_review": "人造人間という設定だが、寓話的なファンタジー色が強い。"
    },
    {
        "todo_title": "ターミネーター",
        "title": "ターミネーター",
        "original_title": "The Terminator",
        "filename": "TheTerminator.md",
        "director": "ジェームズ・キャメロン",
        "country": "アメリカ",
        "release_year": 1984,
        "genre": ["SF", "アクション"],
        "rating_child": 2,
        "has_sexual_content": True,
        "has_violence": True,
        "sf_rating": 5,
        "synopsis": "未来で機械軍のリーダーとなるジョン・コナーを抹殺するため、未来から殺人サイボーグ「ターミネーター」が送り込まれる。ジョンの母となるサラ・コナーは、同じく未来から来た戦士カイルと共に逃走する。",
        "recommendation": "ターミネーターがとにかく怖くて、夢に出てきそう。",
        "content_warning": "激しい銃撃戦や、自分で目を手術するシーンなどが痛々しい。",
        "sf_review": "タイムトラベルと殺人ロボットというSFアクションの金字塔。"
    },
    {
        "todo_title": "ロッキー",
        "title": "ロッキー",
        "original_title": "Rocky",
        "filename": "Rocky.md",
        "director": "ジョン・G・アヴィルドセン",
        "country": "アメリカ",
        "release_year": 1976,
        "genre": ["ドラマ", "スポーツ"],
        "rating_child": 3,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "フィラデルフィアの三流ボクサー、ロッキー。ある日、世界チャンピオンのアポロから対戦相手に指名される。ロッキーは愛する女性エイドリアンのために、過酷なトレーニングに挑みリングに立つ。",
        "recommendation": "ボクシングの試合で殴り合うのが痛そう。でも頑張る姿はかっこいい。",
        "content_warning": "ボクシングの試合で顔が腫れ上がったり血が出たりする。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "スピード",
        "title": "スピード",
        "original_title": "Speed",
        "filename": "Speed.md",
        "director": "ヤン・デ・ボン",
        "country": "アメリカ",
        "release_year": 1994,
        "genre": ["アクション", "サスペンス"],
        "rating_child": 3,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "ロサンゼルスを走る路線バスに爆弾が仕掛けられた。時速80キロを下回ると爆発するという罠の中、SWAT隊員のジャックは乗客を救うためにバスに乗り込む。",
        "recommendation": "バスが止まれなくてハラハラドキドキしっぱなし！",
        "content_warning": "爆発シーンや暴力シーンがある。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "グラディエーター",
        "title": "グラディエーター",
        "original_title": "Gladiator",
        "filename": "Gladiator.md",
        "director": "リドリー・スコット",
        "country": "アメリカ, イギリス",
        "release_year": 2000,
        "genre": ["アクション", "ドラマ", "歴史"],
        "rating_child": 2,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "古代ローマ帝国。皇帝の息子に家族を殺され、奴隷に身を落とした将軍マキシマス。彼は剣闘士（グラディエーター）としてコロッセオで戦いながら、皇帝への復讐を誓う。",
        "recommendation": "戦いのシーンが怖くて血がいっぱい出るので、小学生にはおすすめできない。",
        "content_warning": "首が飛んだり腕が切れたりと、残酷なシーンが多い。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "シンドラーのリスト",
        "title": "シンドラーのリスト",
        "original_title": "Schindler's List",
        "filename": "SchindlersList.md",
        "director": "スティーヴン・スピルバーグ",
        "country": "アメリカ",
        "release_year": 1993,
        "genre": ["ドラマ", "歴史", "戦争"],
        "rating_child": 1,
        "has_sexual_content": True,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "第二次世界大戦中、ナチス・ドイツによるユダヤ人虐殺が進むポーランド。ドイツ人実業家オスカー・シンドラーは、自分の工場でユダヤ人を雇うことで、多くの命を救おうとする。",
        "recommendation": "白黒映画だし、人がたくさん殺されて悲しいので、小学生にはまだ早いかも。",
        "content_warning": "虐殺シーンが非常に残酷でショッキング。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "パラサイト 半地下の家族",
        "title": "パラサイト 半地下の家族",
        "original_title": "Parasite",
        "filename": "Parasite.md",
        "director": "ポン・ジュノ",
        "country": "韓国",
        "release_year": 2019,
        "genre": ["ドラマ", "スリラー", "ブラックコメディ"],
        "rating_child": 1,
        "has_sexual_content": True,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "全員失業中の貧しいキム一家。長男が裕福なパク家の家庭教師になったことをきっかけに、家族全員が他人を装ってパク家に「寄生」し始めるが、予想外の事件が起きる。",
        "recommendation": "最初は面白いけど、だんだん怖くなって最後は衝撃的。小学生にはおすすめできない。",
        "content_warning": "暴力シーンや性的なシーンがある。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "トゥルーマン・ショー",
        "title": "トゥルーマン・ショー",
        "original_title": "The Truman Show",
        "filename": "TheTrumanShow.md",
        "director": "ピーター・ウィアー",
        "country": "アメリカ",
        "release_year": 1998,
        "genre": ["ドラマ", "コメディ", "SF"],
        "rating_child": 3,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 3,
        "synopsis": "トゥルーマンは平凡な人生を送っていたが、実は彼の生活はすべてテレビ番組として世界中に放送されていた。家族も友人も全員俳優。真実に気づいた彼は、外の世界への脱出を試みる。",
        "recommendation": "自分の生活が全部ニセモノだったらと思うと怖い。ちょっと考えさせられるお話。",
        "content_warning": "特になし。",
        "sf_review": "巨大なセットで作られた人工世界というSF的設定。"
    },
    {
        "todo_title": "羊たちの沈黙",
        "title": "羊たちの沈黙",
        "original_title": "The Silence of the Lambs",
        "filename": "TheSilenceOfTheLambs.md",
        "director": "ジョナサン・デミ",
        "country": "アメリカ",
        "release_year": 1991,
        "genre": ["サスペンス", "ホラー", "スリラー"],
        "rating_child": 1,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "連続殺人事件の捜査協力を求めるため、FBI訓練生のクラリスは、収監中の天才精神科医で人食い殺人鬼のレクター博士と面会する。博士は捜査に協力する代わり、クラリス自身の過去を語らせる。",
        "recommendation": "レクター博士が何を考えているかわからなくて怖い。絶対に小学生は見ないでね。",
        "content_warning": "死体の損壊や、顔の皮を剥ぐなどの猟奇的なシーンがある。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "セッション",
        "title": "セッション",
        "original_title": "Whiplash",
        "filename": "Whiplash.md",
        "director": "デイミアン・チャゼル",
        "country": "アメリカ",
        "release_year": 2014,
        "genre": ["ドラマ", "音楽"],
        "rating_child": 2,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "名門音楽学校に入学したドラマーのニーマン。伝説の鬼教師フレッチャーの指導を受けることになるが、そのレッスンは罵倒や暴力が飛び交う常軌を逸したものだった。",
        "recommendation": "先生が怖すぎて見ていて辛くなる。ドラムはすごいけど…。",
        "content_warning": "先生が暴言を吐いたり、手を怪我して血だらけになるシーンがある。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "グッド・ウィル・ハンティング/旅立ち",
        "title": "グッド・ウィル・ハンティング/旅立ち",
        "original_title": "Good Will Hunting",
        "filename": "GoodWillHunting.md",
        "director": "ガス・ヴァン・サント",
        "country": "アメリカ",
        "release_year": 1997,
        "genre": ["ドラマ"],
        "rating_child": 3,
        "has_sexual_content": True,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "数学の天才的な才能を持ちながら、過去のトラウマから心を閉ざし、清掃員として働くウィル。最愛の妻を亡くした心理学者ショーンとの対話を通じて、少しずつ未来へと歩き出す。",
        "recommendation": "お話はいいけど、難しい言葉がいっぱい出てくるので小学生には退屈かも。",
        "content_warning": "喧嘩のシーンや汚い言葉遣いがある。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "リトル・ミス・サンシャイン",
        "title": "リトル・ミス・サンシャイン",
        "original_title": "Little Miss Sunshine",
        "filename": "LittleMissSunshine.md",
        "director": "ジョナサン・デイトン, ヴァレリー・ファリス",
        "country": "アメリカ",
        "release_year": 2006,
        "genre": ["ドラマ", "コメディ", "ロードムービー"],
        "rating_child": 3,
        "has_sexual_content": True,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "個性的な家族が、娘オリーヴの美少女コンテスト出場のために、オンボロバスに乗ってカリフォルニアを目指す旅に出る。トラブル続きの旅の中で、崩壊寸前の家族の絆が再生していく。",
        "recommendation": "変な家族がドタバタしてて面白いけど、最後はちょっと感動する。",
        "content_warning": "おじいちゃんが変なことを言ったり、少し下品な話がある。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "レインマン",
        "title": "レインマン",
        "original_title": "Rain Man",
        "filename": "RainMan.md",
        "director": "バリー・レヴィンソン",
        "country": "アメリカ",
        "release_year": 1988,
        "genre": ["ドラマ", "ロードムービー"],
        "rating_child": 3,
        "has_sexual_content": True,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "自由奔放な青年チャーリーは、父の死後、存在さえ知らなかった自閉症の兄レイモンドと出会う。遺産目当てで兄を施設から連れ出したチャーリーだが、旅を通じて兄弟の絆を取り戻していく。",
        "recommendation": "お兄さんの計算がすごくてびっくり。兄弟の旅が素敵。",
        "content_warning": "特になし。",
        "sf_review": "SF要素はない。"
    }
]

def create_movie_file(movie):
    filepath = os.path.join("Movie", movie["filename"])
    if os.path.exists(filepath):
        print(f"File already exists: {filepath}")
        return

    content = f"""---
title: "{movie['title']}"
original_title: "{movie['original_title']}"
director: "{movie['director']}"
country: "{movie['country']}"
release_year: {movie['release_year']}
genre: {str(movie['genre']).replace("'", '"')}
rating_child: {movie['rating_child']}
has_sexual_content: {str(movie['has_sexual_content']).lower()}
has_violence: {str(movie['has_violence']).lower()}
sf_rating: {movie['sf_rating']}
---

## あらすじ
{movie['synopsis']}

## おすすめポイント（小学生女児基準）
{movie['recommendation']}

## エロ/グロ表現（小学生女児基準）
{movie['content_warning']}

## SF的な要素とその評価
{movie['sf_review']}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {filepath}")

def update_todo(movies):
    todo_path = "TODO.md"
    with open(todo_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    updated_count = 0

    # Create a set of processed titles for quick lookup
    processed_titles = {m["todo_title"] for m in movies}

    for line in lines:
        stripped = line.strip()
        matched = False
        if "[ ]" in stripped:
            title_part = stripped.split("]")[1].strip()
            # Remove trailing spaces
            if title_part in processed_titles:
                new_lines.append(line.replace("[ ]", "[x]"))
                updated_count += 1
                matched = True

        if not matched:
            new_lines.append(line)

    with open(todo_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"Updated TODO.md: {updated_count} items marked as checked.")

def main():
    # Ensure Movie directory exists
    if not os.path.exists("Movie"):
        os.makedirs("Movie")

    for movie in movies_data:
        create_movie_file(movie)
    update_todo(movies_data)

if __name__ == "__main__":
    main()
