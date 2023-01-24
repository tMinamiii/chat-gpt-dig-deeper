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


def main() -> None:
    theme = sys.argv[1]
    ans = dig_deep(theme, "についてどう思いますか？")
    time.sleep(1)
    for _ in range(10):
        temp_ans = dig_deep(ans, "について更に意見はありますか？")
        if temp_ans == "":
            break
        ans = temp_ans
        time.sleep(1)

    ans = dig_deep(theme, "を要約してください。")
    print(f"{theme} とは、「{ans}」 である")


if __name__ == "__main__":
    main()
