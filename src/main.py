import os
import random
import sys
import time
from typing import Any

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]


def dig_deep(talk_theme: str) -> str:
    talk_thema = f"{talk_theme} についてどう思いますか？"

    # 返答を3つ用意してランダムに一つの答えを選ぶ
    max = 3
    resp: Any = openai.Completion.create(
        engine="text-davinci-003",
        max_tokens=500,
        prompt=talk_thema,
        n=max,
        stop=None,
        temperature=0.7,
    )

    i = random.randint(0, max - 1)
    answer = str(resp["choices"][i]["text"]).strip()
    if answer != "":
        print(talk_thema)
        print("  ->  " + answer)
    print()
    return answer


def main(theme: str) -> None:
    ask = theme
    ans = ""
    for _ in range(50):
        temp_ans = dig_deep(ask)
        if temp_ans == "":
            break
        ans = temp_ans
        ask = temp_ans
        time.sleep(3)
    print(f"{theme} とは、「{ans}」 である")


if __name__ == "__main__":
    theme = sys.argv[1]
    main(theme)
