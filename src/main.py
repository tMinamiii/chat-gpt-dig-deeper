import os
import random
import sys
import time
from typing import Any

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]


def completion(talk_theme: str) -> str:
    # 返答を3つ用意してランダムに一つの答えを選ぶ
    max = 3
    resp: Any = openai.Completion.create(
        engine="text-davinci-003",
        max_tokens=1000,
        prompt=talk_theme,
        n=max,
        stop=None,
        temperature=0.5,
    )

    i = random.randint(0, max - 1)
    answer = str(resp["choices"][i]["text"]).strip()
    if answer != "":
        print(talk_theme)
        print("  ->  " + answer)
    print()
    return answer


def dig_deep(talk_theme: str, suffix: str) -> str:
    theme = f"{talk_theme} {suffix}"
    return completion(theme)


def main(theme: str) -> None:
    ans = dig_deep(theme, "についてどう思いますか？")
    ask = ans
    time.sleep(1)
    suffix = ["について更に意見はありますか？", "について詳細に述べてください。", "を要約してください。"]
    for i in range(11):
        temp_ans = dig_deep(ask, suffix[i % len(suffix)])
        if temp_ans == "":
            break
        ans = temp_ans
        ask = temp_ans
        time.sleep(1)
    print(f"{theme} とは、「{ans}」 である")


if __name__ == "__main__":
    theme = sys.argv[1]
    main(theme)
