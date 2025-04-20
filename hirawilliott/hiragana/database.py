from pydantic import BaseModel


class Hiragana(BaseModel):
    character: str
    romaji: str
    word: str
    image: str


db = {
    "あ": [
        Hiragana(
            character="あ", romaji="arupaka", word="あるぱか", image="arupaka.png"
        ),
        Hiragana(
            character="あ", romaji="araiguma", word="あらいぐま", image="araiguma.png"
        ),
    ],
    "い": [Hiragana(character="い", romaji="inu", word="犬", image="inu.png")],
    "う": [
        Hiragana(character="う", romaji="uma", word="馬", image="uma.png"),
        Hiragana(character="う", romaji="usagi", word="兎", image="usagi.png"),
        Hiragana(character="う", romaji="ushi", word="牛", image="ushi.png"),
    ],
    "え": [Hiragana(character="え", romaji="ebi", word="蝦", image="ebi.png")],
    "お": [Hiragana(character="お", romaji="ookami", word="狼", image="ookami.png")],
    "か": [Hiragana(character="か", romaji="kaba", word="カバ", image="kaba.png")],
    "き": [Hiragana(character="き", romaji="kirin", word="麒麟", image="kirin.png")],
    "く": [
        Hiragana(character="く", romaji="kuma", word="熊", image="kuma.png"),
        Hiragana(character="く", romaji="kurohyou", word="黒豹", image="kurohyou.png"),
    ],
    "け": [
        Hiragana(character="け", romaji="kemushi", word="毛虫", image="kemushi.png")
    ],
    "こ": [
        Hiragana(
            character="こ", romaji="koumori", word="こうもり", image="koumori.png"
        ),
    ],
    # さ行
    "さ": [Hiragana(character="さ", romaji="sai", word="さい", image="sai.png")],
    "し": [
        Hiragana(
            character="し", romaji="shimauma", word="しまうま", image="shimauma.png"
        )
    ],
    "す": [Hiragana(character="す", romaji="suika", word="すいか", image="suika.png")],
    "せ": [
        Hiragana(character="せ", romaji="seiuchi", word="せいうち", image="seiuchi.png")
    ],
    "そ": [Hiragana(character="そ", romaji="sou", word="そう", image="sou.png")],
    "も": [
        Hiragana(character="も", romaji="mogura", word="もぐら", image="mogura.png")
    ],
    "ご": [
        Hiragana(character="こ", romaji="gorira", word="ごりら", image="gorira.png"),
    ],
    "り": [Hiragana(character="り", romaji="risu", word="りす", image="risu.png")],
    "れ": [
        Hiragana(
            character="れ",
            romaji="ressaapanda",
            word="れっさーぱんだ",
            image="ressaapanda.png",
        )
    ],
    "は": [
        Hiragana(
            character="は", romaji="hamsutaa", word="はむすたー", image="hamusutaa.png"
        )
    ],
    "ひ": [
        Hiragana(character="ひ", romaji="hitsuji", word="ひつじ", image="hitsuji.png")
    ],
    "ら": [
        Hiragana(character="ら", romaji="rakuda", word="らくだ", image="rakuda.png")
    ],
    "と": [
        Hiragana(character="と", romaji="tonakai", word="となかい", image="tonakai.png")
    ],
}
