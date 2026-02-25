import os

movies_data = [
    {
        "todo_title": "聲の形",
        "title": "聲の形",
        "original_title": "A Silent Voice",
        "filename": "ASilentVoice.md",
        "director": "山田尚子",
        "country": "日本",
        "release_year": 2016,
        "genre": ["アニメーション", "ドラマ", "ロマンス"],
        "rating_child": 3,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "聴覚障害を持つ少女・硝子と、かつて彼女をいじめていた少年・将也。高校生になった将也は、過去の過ちに向き合い、硝子との再会を果たす。",
        "recommendation": "友達や家族の大切さについて考えさせられる感動的なお話。",
        "content_warning": "いじめのシーンや自殺未遂の描写があり、心が痛くなるかもしれない。",
        "sf_review": "SF要素はない。現代の青春ドラマ。"
    },
    {
        "todo_title": "劇場版 ヴァイオレット・エヴァーガーデン",
        "title": "劇場版 ヴァイオレット・エヴァーガーデン",
        "original_title": "Violet Evergarden: The Movie",
        "filename": "VioletEvergardenTheMovie.md",
        "director": "石立太一",
        "country": "日本",
        "release_year": 2020,
        "genre": ["アニメーション", "ドラマ", "ファンタジー"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 2,
        "synopsis": "感情を持たない元兵士の少女ヴァイオレットは、代筆業「自動手記人形」として働きながら、かつての上官ギルベルト少佐が残した「愛してる」の意味を探し続ける。",
        "recommendation": "映像がとても綺麗で、手紙を通して人の心が繋がる様子に涙が出る。",
        "content_warning": "特になし。戦争の回想シーンが少しある。",
        "sf_review": "主人公の両腕が機械（義手）であるというスチームパンク的な要素がある。"
    },
    {
        "todo_title": "モアナと伝説の海",
        "title": "モアナと伝説の海",
        "original_title": "Moana",
        "filename": "Moana.md",
        "director": "ロン・クレメンツ, ジョン・マスカー",
        "country": "アメリカ",
        "release_year": 2016,
        "genre": ["アニメーション", "アドベンチャー", "ファンタジー"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "美しい海に囲まれた島で育った少女モアナ。島を救うため、伝説の半神マウイと共に、盗まれた女神の心を返す冒険の旅に出る。",
        "recommendation": "モアナが勇気を出して海へ旅立つ姿がかっこいい！歌も素敵。",
        "content_warning": "溶岩の怪物テ・カァが怖くて迫力がある。",
        "sf_review": "ポリネシア神話をベースにしたファンタジー。SF要素はない。"
    },
    {
        "todo_title": "ミラベルと魔法だらけの家",
        "title": "ミラベルと魔法だらけの家",
        "original_title": "Encanto",
        "filename": "Encanto.md",
        "director": "バイロン・ハワード, ジャレド・ブッシュ",
        "country": "アメリカ",
        "release_year": 2021,
        "genre": ["アニメーション", "ファンタジー", "ミュージカル"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "魔法の力を持つ不思議な家「カシータ」に住むマドリガル家。家族全員が特別な魔法のギフトを授かる中、ミラベルだけが何の力も持たなかったが、家族の危機に立ち上がる。",
        "recommendation": "魔法の家が楽しくて、家族みんなで協力するのが素敵。歌も踊りも楽しい！",
        "content_warning": "特になし。",
        "sf_review": "魔法による奇跡を描いたファンタジー。SF要素はない。"
    },
    {
        "todo_title": "マイ・エレメント",
        "title": "マイ・エレメント",
        "original_title": "Elemental",
        "filename": "Elemental.md",
        "director": "ピーター・ソーン",
        "country": "アメリカ",
        "release_year": 2023,
        "genre": ["アニメーション", "ファンタジー", "ロマンス"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "火、水、土、風のエレメント（元素）たちが暮らすエレメント・シティ。熱くなりやすい火の女の子エンバーと、涙もろい水の青年ウェイドという、正反対の二人が出会い、恋に落ちる。",
        "recommendation": "火と水という触れ合えない二人の恋にドキドキする。映像がキラキラしていて綺麗。",
        "content_warning": "特になし。",
        "sf_review": "元素を擬人化したファンタジー世界。科学的な設定というよりは魔法的。"
    },
    {
        "todo_title": "怪盗グルーの月泥棒",
        "title": "怪盗グルーの月泥棒",
        "original_title": "Despicable Me",
        "filename": "DespicableMe.md",
        "director": "ピエール・コフィン, クリス・ルノー",
        "country": "アメリカ",
        "release_year": 2010,
        "genre": ["アニメーション", "コメディ", "ファミリー"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 4,
        "synopsis": "意地悪な怪盗グルーは、月を盗むというとんでもない計画を立てる。そのために孤児の三姉妹を利用しようとするが、彼女たちとの交流を通して少しずつ心が変化していく。",
        "recommendation": "ミニオンたちがいたずら好きで面白い！グルーがだんだん優しくなるのが良い。",
        "content_warning": "特になし。",
        "sf_review": "縮小ビーム銃やロケット、奇妙な乗り物など、ユニークなガジェットが多数登場するSFコメディ。"
    },
    {
        "todo_title": "ミニオンズ",
        "title": "ミニオンズ",
        "original_title": "Minions",
        "filename": "Minions.md",
        "director": "ピエール・コフィン, カイル・バルダ",
        "country": "アメリカ",
        "release_year": 2015,
        "genre": ["アニメーション", "コメディ", "ファミリー"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 4,
        "synopsis": "最強のボスに仕えることが生きがいのミニオンたち。ボスが見つからず滅亡の危機に瀕した彼らは、新たなボスを求めて旅に出る。",
        "recommendation": "謎の言葉を話すミニオンたちがとにかく可愛い！ドジな行動に大笑いできる。",
        "content_warning": "特になし。",
        "sf_review": "様々なハイテク武器や装置が登場し、コメディながらSF的なガジェット要素が強い。"
    },
    {
        "todo_title": "シング",
        "title": "シング",
        "original_title": "Sing",
        "filename": "Sing.md",
        "director": "ガース・ジェニングス",
        "country": "アメリカ",
        "release_year": 2016,
        "genre": ["アニメーション", "コメディ", "ミュージカル"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "倒産寸前の劇場の支配人バスター・ムーンは、劇場を立て直すために歌のオーディションを開催する。個性豊かな動物たちが集まり、それぞれの夢をかけて歌声を披露する。",
        "recommendation": "知っているヒット曲がたくさん流れて楽しい！動物たちが一生懸命歌う姿に元気をもらえる。",
        "content_warning": "特になし。",
        "sf_review": "動物が人間のように暮らす世界観。SF要素はない。"
    },
    {
        "todo_title": "シュレック",
        "title": "シュレック",
        "original_title": "Shrek",
        "filename": "Shrek.md",
        "director": "アンドリュー・アダムソン, ヴィッキー・ジェンソン",
        "country": "アメリカ",
        "release_year": 2001,
        "genre": ["アニメーション", "コメディ", "ファンタジー"],
        "rating_child": 4,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "人里離れた沼に住む怪物シュレック。領主によって沼に追放されたおとぎ話のキャラクターたちを助けるため、お喋りなロバのドンキーと共に、囚われのフィオナ姫を救出する旅に出る。",
        "recommendation": "おとぎ話のパロディがたくさんあって笑える！見た目で判断しないことの大切さがわかる。",
        "content_warning": "シュレックが耳垢でろうそくを作るなど、少し汚い描写がある。",
        "sf_review": "おとぎ話をベースにしたファンタジーコメディ。SF要素はない。"
    },
    {
        "todo_title": "ヒックとドラゴン",
        "title": "ヒックとドラゴン",
        "original_title": "How to Train Your Dragon",
        "filename": "HowToTrainYourDragon.md",
        "director": "クリス・サンダース, ディーン・デュボア",
        "country": "アメリカ",
        "release_year": 2010,
        "genre": ["アニメーション", "アドベンチャー", "ファンタジー"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "ドラゴンと戦うバイキングの村。ひ弱な少年ヒックは、傷ついた伝説のドラゴン「トゥース」と出会い、秘密の友情を育むことで、村とドラゴンの関係を変えていく。",
        "recommendation": "トゥースが猫みたいで可愛い！ヒックと一緒に空を飛ぶシーンは爽快。",
        "content_warning": "特になし。ヒックが足の一部を失う描写がある。",
        "sf_review": "ドラゴンの生態や飛行具の発明など、空想科学的な面白さはあるが、基本はファンタジー。"
    },
    {
        "todo_title": "ザ・スーパーマリオブラザーズ・ムービー",
        "title": "ザ・スーパーマリオブラザーズ・ムービー",
        "original_title": "The Super Mario Bros. Movie",
        "filename": "TheSuperMarioBrosMovie.md",
        "director": "アーロン・ホーヴァス, マイケル・ジェレニック",
        "country": "アメリカ, 日本",
        "release_year": 2023,
        "genre": ["アニメーション", "アドベンチャー", "コメディ"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 2,
        "synopsis": "ニューヨークで配管工を営むマリオとルイージは、謎の土管を通って魔法の世界へ迷い込む。離れ離れになった弟を助けるため、マリオはピーチ姫やキノピオたちと協力して大魔王クッパに立ち向かう。",
        "recommendation": "ゲームの世界そのまま！マリオカートのシーンが迫力満点。",
        "content_warning": "特になし。",
        "sf_review": "カートや土管などのギミックはあるが、基本は魔法の世界のファンタジー。"
    },
    {
        "todo_title": "パイレーツ・オブ・カリビアン/呪われた海賊たち",
        "title": "パイレーツ・オブ・カリビアン/呪われた海賊たち",
        "original_title": "Pirates of the Caribbean: The Curse of the Black Pearl",
        "filename": "PiratesOfTheCaribbeanTheCurseOfTheBlackPearl.md",
        "director": "ゴア・ヴァービンスキー",
        "country": "アメリカ",
        "release_year": 2003,
        "genre": ["アクション", "アドベンチャー", "ファンタジー"],
        "rating_child": 3,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "カリブ海を舞台に、海賊ジャック・スパロウと鍛冶屋のウィルが、呪われた海賊バルボッサにさらわれた総督の娘エリザベスを救うために冒険を繰り広げる。",
        "recommendation": "ジャック・スパロウが変な人で面白いけどかっこいい！海賊船の戦いがすごい。",
        "content_warning": "月光で海賊たちが骸骨になるシーンが怖い。",
        "sf_review": "呪いや幽霊船が登場するファンタジーアクション。SF要素はない。"
    },
    {
        "todo_title": "レイダース/失われたアーク《聖櫃》",
        "title": "レイダース/失われたアーク《聖櫃》",
        "original_title": "Raiders of the Lost Ark",
        "filename": "RaidersOfTheLostArk.md",
        "director": "スティーヴン・スピルバーグ",
        "country": "アメリカ",
        "release_year": 1981,
        "genre": ["アクション", "アドベンチャー"],
        "rating_child": 3,
        "has_sexual_content": False,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "考古学者インディ・ジョーンズは、ナチス・ドイツよりも先に、神の力が宿るとされる「聖櫃（アーク）」を手に入れるため、世界中を駆け巡る冒険に出る。",
        "recommendation": "罠を抜けたり敵と戦ったり、ハラハラドキドキの連続！",
        "content_warning": "聖櫃の力でナチスの兵士たちの顔が溶けたりするシーンが怖い。",
        "sf_review": "オカルトや超常現象を扱う冒険活劇。SF要素はない。"
    },
    {
        "todo_title": "ファンタスティック・ビーストと魔法使いの旅",
        "title": "ファンタスティック・ビーストと魔法使いの旅",
        "original_title": "Fantastic Beasts and Where to Find Them",
        "filename": "FantasticBeastsAndWhereToFindThem.md",
        "director": "デヴィッド・イェーツ",
        "country": "イギリス, アメリカ",
        "release_year": 2016,
        "genre": ["ファンタジー", "アドベンチャー"],
        "rating_child": 4,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "魔法動物学者のニュート・スキャマンダーは、ニューヨークを訪れた際に、トランクから魔法動物たちを逃がしてしまう。彼は魔法使いの仲間たちと共に、動物たちの保護と街の危機に立ち向かう。",
        "recommendation": "見たこともない不思議な動物がたくさん出てきて可愛い！魔法を使うシーンがワクワクする。",
        "content_warning": "黒い影のような怪物が暴れるシーンが少し怖い。",
        "sf_review": "ハリー・ポッターシリーズの前日譚にあたる魔法ファンタジー。SF要素はない。"
    },
    {
        "todo_title": "オーシャンズ11",
        "title": "オーシャンズ11",
        "original_title": "Ocean's Eleven",
        "filename": "OceansEleven.md",
        "director": "スティーヴン・ソダーバーグ",
        "country": "アメリカ",
        "release_year": 2001,
        "genre": ["クライム", "サスペンス"],
        "rating_child": 3,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 2,
        "synopsis": "カリスマ窃盗犯ダニー・オーシャンは、仮釈放直後に仲間を集め、ラスベガスの3大カジノの金庫から1億6000万ドルを盗み出すという前代未聞の強盗計画を立てる。",
        "recommendation": "泥棒たちが鮮やかな手口でお金を盗み出すのがスカッとする！",
        "content_warning": "特になし。",
        "sf_review": "高度なセキュリティを突破するためのハイテク機器が登場する。"
    },
    {
        "todo_title": "トップガン",
        "title": "トップガン",
        "original_title": "Top Gun",
        "filename": "TopGun.md",
        "director": "トニー・スコット",
        "country": "アメリカ",
        "release_year": 1986,
        "genre": ["アクション", "ドラマ"],
        "rating_child": 3,
        "has_sexual_content": True,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "アメリカ海軍のエリートパイロット養成校「トップガン」に入隊したマーヴェリック。ライバルとの競争や教官との恋、そして親友の死を乗り越え、最高のパイロットを目指して成長していく。",
        "recommendation": "戦闘機が空を飛ぶシーンが本当にかっこいい！音楽も盛り上がる。",
        "content_warning": "キスシーンやベッドシーンがある。",
        "sf_review": "戦闘機などの軍事技術は登場するが、現代劇。"
    },
    {
        "todo_title": "レ・ミゼラブル",
        "title": "レ・ミゼラブル",
        "original_title": "Les Misérables",
        "filename": "LesMiserables.md",
        "director": "トム・フーパー",
        "country": "イギリス",
        "release_year": 2012,
        "genre": ["ミュージカル", "ドラマ"],
        "rating_child": 3,
        "has_sexual_content": True,
        "has_violence": True,
        "sf_rating": 1,
        "synopsis": "19世紀のフランス。パンを盗んだ罪で19年間投獄されたジャン・バルジャンは、仮釈放後に名前を変えて市長となるが、警部ジャベールの執拗な追跡を受ける。彼は薄幸の女性ファンティーヌの娘コゼットを育てることを誓う。",
        "recommendation": "歌がすごくて感動するけど、話がとても悲しくて重い。",
        "content_warning": "貧困や売春、革命での戦闘など、悲惨な描写が多い。",
        "sf_review": "SF要素はない。歴史ミュージカル。"
    },
    {
        "todo_title": "マンマ・ミーア！",
        "title": "マンマ・ミーア！",
        "original_title": "Mamma Mia!",
        "filename": "MammaMia.md",
        "director": "フィリダ・ロイド",
        "country": "イギリス, アメリカ",
        "release_year": 2008,
        "genre": ["ミュージカル", "コメディ", "ロマンス"],
        "rating_child": 4,
        "has_sexual_content": True,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "ギリシャの美しい島でホテルを経営するドナと、その娘ソフィ。結婚式を控えたソフィは、父親の可能性がある3人の男性をこっそり招待し、本当の父親を探そうとする。",
        "recommendation": "ABBAの曲に合わせてみんなで歌って踊るのが楽しい！ハッピーな気分になれる。",
        "content_warning": "大人の恋愛の話が多い。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "サウンド・オブ・ミュージック",
        "title": "サウンド・オブ・ミュージック",
        "original_title": "The Sound of Music",
        "filename": "TheSoundOfMusic.md",
        "director": "ロバート・ワイズ",
        "country": "アメリカ",
        "release_year": 1965,
        "genre": ["ミュージカル", "ドラマ", "ファミリー"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "修道女見習いのマリアは、7人の子供がいるトラップ家の家庭教師となる。厳格な父親によって音楽を禁じられていた子供たちに、マリアは歌うことの喜びを教える。",
        "recommendation": "ドレミの歌など、知っている曲がたくさん！マリア先生が優しくて素敵。",
        "content_warning": "ナチス・ドイツが台頭してくる後半は少し緊張感がある。",
        "sf_review": "SF要素はない。"
    },
    {
        "todo_title": "ローマの休日",
        "title": "ローマの休日",
        "original_title": "Roman Holiday",
        "filename": "RomanHoliday.md",
        "director": "ウィリアム・ワイラー",
        "country": "アメリカ",
        "release_year": 1953,
        "genre": ["ロマンス", "コメディ"],
        "rating_child": 5,
        "has_sexual_content": False,
        "has_violence": False,
        "sf_rating": 1,
        "synopsis": "ヨーロッパ親善旅行中の某国王女アンは、公務に疲れ果てて宮殿を脱走。ローマの街で新聞記者のジョーと出会い、身分を隠して一日の自由な休日を楽しむ。",
        "recommendation": "お姫様が普通の女の子として遊ぶのが楽しそう。最後は少し切ないけど素敵な映画。",
        "content_warning": "特になし。白黒映画。",
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
    if not os.path.exists("Movie"):
        os.makedirs("Movie")

    for movie in movies_data:
        create_movie_file(movie)
    update_todo(movies_data)

if __name__ == "__main__":
    main()
