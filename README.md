# ChatGPT Dig Deeper

ChaptGPTに深堀り問答させるプログラムです。

## Usage

環境変数 `OPENAI_API_KEY` にAPI KEYを設定します

第1引数に問答させたい単語を入力すると、その単語について問答をはじめます。
ChaptGPTは答えがなくなると空文字を返すので、空文字がかえってくるまで問答させます。

## Example

```sh
$ python src/main.py 人生
人生 についてどう思いますか？
  ->  人生については、様々な価値観がありますが、私は、人生を楽しむことができる、貴重な機会と考えています。人生というのは、どんな場面でも、学び、成長、成功を目指す機会であると思っています。そして、人生の中で出会った人々や経験したことなどを、自分の人生を豊かにしていくために、活用していくことができると思います。

人生については、様々な価値観がありますが、私は、人生を楽しむことができる、貴重な機会と考えています。人生というのは、どんな場面でも、学び、成長、成功を目指す機会であると思っています。そして、人生の中で出会った人々や経験したことなどを、自分の人生を豊かにしていくために、活用していくことができると思います。 について更に意見はありますか？
  ->  人生については、それぞれの人によって異なる考え方がありますが、私の考え方としては、人生を有意義なものにしていくために、自分の人生を豊かにしていくために、挑戦し続けることが大切だと考えています。今までの経験や知識を活かし、新しい挑戦をしていくことで、自分を成長させ、さらに豊かな人生を送ることができると思います。

人生については、それぞれの人によって異なる考え方がありますが、私の考え方としては、人生を有意義なものにしていくために、自分の人生を豊かにしていくために、挑戦し続けることが大切だと考えています。今までの経験や知識を活かし、新しい挑戦をしていくことで、自分を成長させ、さらに豊かな人生を送ることができると思います。 について詳細に述べてください。
  ->  人生を有意義なものにしていくためには、自分が自分の人生を豊かにするために、挑戦し続けることが大切です。まず、自分の目標を明確にして、それに向かって努力し続けることが重要です。そして、自分が今まで習得した知識や経験を活かして、新しいことに挑戦していくことも大切です。新しいことにチャレンジし、自分を成長させていくことで、さらに豊かな人生を送ることができます。また、自分自身を磨き、新しいことを学び、自分の人生を豊かにするために、新しい環境や新しい出会いを求めて、新しい経験をしていくことも大切です。自分自身を磨き、新しい環境や新しい出会いを求めて、新しい経験をしていくことで、自分の人生をより豊かにすることができます。

人生を有意義なものにしていくためには、自分が自分の人生を豊かにするために、挑戦し続けることが大切です。まず、自分の目標を明確にして、それに向かって努力し続けることが重要です。そして、自分が今まで習得した知識や経験を活かして、新しいことに挑戦していくことも大切です。新しいことにチャレンジし、自分を成長させていくことで、さらに豊かな人生を送ることができます。また、自分自身を磨き、新しいことを学び、自分の人生を豊かにするために、新しい環境や新しい出会いを求めて、新しい経験をしていくことも大切です。自分自身を磨き、新しい環境や新しい出会いを求めて、新しい経験をしていくことで、自分の人生をより豊かにすることができます。 を要約してください。
  ->  自分の目標を明確にし、努力し続けること、新しいことに挑戦し自分を成長させること、自分自身を磨き、新しい環境や新しい出会いを求めて新しい経験をすることで、自分の人生を豊かにすることができる。

自分の目標を明確にし、努力し続けること、新しいことに挑戦し自分を成長させること、自分自身を磨き、新しい環境や新しい出会いを求めて新しい経験をすることで、自分の人生を豊かにすることができる。 について更に意見はありますか？
  ->  まず、自分の目標を明確にし、努力し続けることは、自分の人生を豊かにする上で重要なことです。そして、新しいことに挑戦し、自分を成長させることも大切です。また、自分自身を磨くことも重要です。自分の目標を達成するためには、自分自身を常に進化させていく必要があります。さらに、新しい環境や新しい出会いを求めて新しい経験をすることも大切です。新しい環境や新しい出会いを通じて、自分の視野を広げ、自分の人生を豊かにすることができます。

まず、自分の目標を明確にし、努力し続けることは、自分の人生を豊かにする上で重要なことです。そして、新しいことに挑戦し、自分を成長させることも大切です。また、自分自身を磨くことも重要です。自分の目標を達成するためには、自分自身を常に進化させていく必要があります。さらに、新しい環境や新しい出会いを求めて新しい経験をすることも大切です。新しい環境や新しい出会いを通じて、自分の視野を広げ、自分の人生を豊かにすることができます。 について詳細に述べてください。
  ->  自分の目標を達成するためには、自分自身を常に進化させていくことが不可欠です。自分自身を磨くためには、自分の弱点を克服し、自分の強みをより活かすよう努力することが重要です。また、自分のスキルを伸ばすためには、自分の興味や関心を深め、新しいことを学ぶ機会を探すことが大切です。新しい環境や新しい出会いを求めて新しい経験をすることも大切です。新しい環境や新しい出会いを通じて、自分の視野を広げ、自分の人生を豊かにすることができます。さらに、自分の人生を豊かにするためには、自分の夢を追い続けることも大切です。自分の夢を叶えるために、自分の能力を最大限に活かし、自分の目標を達成するために、全力を尽くすことが必要です。

自分の目標を達成するためには、自分自身を常に進化させていくことが不可欠です。自分自身を磨くためには、自分の弱点を克服し、自分の強みをより活かすよう努力することが重要です。また、自分のスキルを伸ばすためには、自分の興味や関心を深め、新しいことを学ぶ機会を探すことが大切です。新しい環境や新しい出会いを求めて新しい経験をすることも大切です。新しい環境や新しい出会いを通じて、自分の視野を広げ、自分の人生を豊かにすることができます。さらに、自分の人生を豊かにするためには、自分の夢を追い続けることも大切です。自分の夢を叶えるために、自分の能力を最大限に活かし、自分の目標を達成するために、全力を尽くすことが必要です。 を要約してください。
  ->  自分の目標を達成するためには、自分自身を常に進化させ、弱点を克服し、強みを活かし、スキルを伸ばし、新しい環境や出会いを求めて新しい経験を積み、夢を追い続け、能力を最大限に活かし、全力を尽くすことが必要です。

自分の目標を達成するためには、自分自身を常に進化させ、弱点を克服し、強みを活かし、スキルを伸ばし、新しい環境や出会いを求めて新しい経験を積み、夢を追い続け、能力を最大限に活かし、全力を尽くすことが必要です。 について更に意見はありますか？
  ->  まず、自分の目標を達成するためには、自分自身を積極的に動かし、チャレンジし続けることが重要です。また、自分の夢を信じ、それを追求することで、目標を達成するためのモチベーションを維持し続ける必要があります。さらに、自分の能力を最大限に活かすために、環境や出会いを求め、新しい経験を積み、スキルを伸ばし、自分の弱点を克服し、強みを活かしていく必要があります。

まず、自分の目標を達成するためには、自分自身を積極的に動かし、チャレンジし続けることが重要です。また、自分の夢を信じ、それを追求することで、目標を達成するためのモチベーションを維持し続ける必要があります。さらに、自分の能力を最大限に活かすために、環境や出会いを求め、新しい経験を積み、スキルを伸ばし、自分の弱点を克服し、強みを活かしていく必要があります。 について詳細に述べてください。
  ->  まず、自分の目標を達成するためには、自分自身を積極的に動かし、チャレンジし続けることが重要です。自分の夢を信じ、それを追求することで、目標を達成するためのモチベーションを維持し続ける必要があります。自分自身を積極的に動かすためには、日々の努力を惜しまず行うことが重要です。努力を惜しまないうちに、目標を達成するためのスキルを身につけていく必要があります。そのためには、自分の能力を最大限に活かすために、新しい環境や出会いを求め、新しい経験を積み、スキルを伸ばす必要があります。自分の弱点を克服し、強みを活かすことも重要です。また、新しい経験を積み、自分のスキルを伸ばすために、自分を挑戦することも重要です。自分の夢を信じ、それを追求することで、目標を達成するためのモチベーションを維持し続ける必要があります。

まず、自分の目標を達成するためには、自分自身を積極的に動かし、チャレンジし続けることが重要です。自分の夢を信じ、それを追求することで、目標を達成するためのモチベーションを維持し続ける必要があります。自分自身を積極的に動かすためには、日々の努力を惜しまず行うことが重要です。努力を惜しまないうちに、目標を達成するためのスキルを身につけていく必要があります。そのためには、自分の能力を最大限に活かすために、新しい環境や出会いを求め、新しい経験を積み、スキルを伸ばす必要があります。自分の弱点を克服し、強みを活かすことも重要です。また、新しい経験を積み、自分のスキルを伸ばすために、自分を挑戦することも重要です。自分の夢を信じ、それを追求することで、目標を達成するためのモチベーションを維持し続ける必要があります。 を要約してください。
  ->  自分の目標を達成するためには、自分自身を積極的に動かし、チャレンジし続けることが重要である。日々の努力を惜しまず行い、新しい環境や出会いを求め、新しい経験を積み、スキルを伸ばし、自分の弱点を克服し、強みを活かし、自分を挑戦することで、自分の夢を信じ、それを追求することで、目標を達成するためのモチベーションを維持することが重要である。

自分の目標を達成するためには、自分自身を積極的に動かし、チャレンジし続けることが重要である。日々の努力を惜しまず行い、新しい環境や出会いを求め、新しい経験を積み、スキルを伸ばし、自分の弱点を克服し、強みを活かし、自分を挑戦することで、自分の夢を信じ、それを追求することで、目標を達成するためのモチベーションを維持することが重要である。 について更に意見はありますか？
  ->  自分の目標を達成するためには、自分自身を積極的に動かすことだけでなく、他の人と協力しあうことも重要です。他の人から学び、経験を共有し、協力しあうことで、自分の目標を達成するのに役立つ知識やスキルを得ることができます。また、他の人との協力を得ることで、モチベーションを維持し、自分の目標を達成するためのインスピレーションを得ることができます。

自分の目標を達成するためには、自分自身を積極的に動かすことだけでなく、他の人と協力しあうことも重要です。他の人から学び、経験を共有し、協力しあうことで、自分の目標を達成するのに役立つ知識やスキルを得ることができます。また、他の人との協力を得ることで、モチベーションを維持し、自分の目標を達成するためのインスピレーションを得ることができます。 について詳細に述べてください。
  ->  自分の目標を達成するために、他の人と協力しあうことは重要です。他の人から学び、経験を共有することで、自分の目標を達成するための有益な情報を得ることができます。他の人と協力して、自分の目標を達成するために必要なスキルを磨くこともできます。また、他の人と協力して、自分の目標を達成するための新しいアイデアを得ることもできます。他の人と協力を得ることで、自分の目標を達成するためのモチベーションを高めることもできます。他の人と協力を得ることで、自分の目標を達成するための目標設定やプランニングを行うこともできます。他の人と協力を得ることで、自分の目標を達成するためのアクションを起こすこともできます。他の人と協力を得ることで、自分の目標を達成するためのインスピレーションを得ることもできます。

人生 とは、「自分の目標を達成するために、他の人と協力しあうことは重要です。他の人から学び、経験を共有することで、自分の目標を達成するための有益な情報を得ることができます。他の人と協力して、自分の目標を達成するために必要なスキルを磨くこともできます。また、他の人と協力して、自分の目標を達成するための新しいアイデアを得ることもできます。他の人と協力を得ることで、自分の目標を達成するためのモチベーションを高めることもできます。他の人と協力を得ることで、自分の目標を達成するための目標設定やプランニングを行うこともできます。他の人と協力を得ることで、自分の目標を達成するためのアクションを起こすこともできます。他の人と協力を得ることで、自分の目標を達成するためのインスピレーションを得ることもできます。」 である
```
