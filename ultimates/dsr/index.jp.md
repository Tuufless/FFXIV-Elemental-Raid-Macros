---
layout: default
title: Lv 90. 絶竜詩
parent: 絶シリーズ
nav_order: 4
has_children: false
has_toc: false
permalink: /ultimates/jp/dsr/
---

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
日本語が母語ではないので記事をすべて日本語するのは難しいと思います。添削をしてくださると嬉しいです。</div>

# 絶竜詩戦争

Elemental DC の野良処理法：

- [**教皇庁フェーズ**](01_the_holy_see.en.md): 光翼閃 H1H2 D1D2 D3D4 MTST
- [**正典トールダン**](02_thordan.en.md): 聖杖ゼフィラン基準、ロール内で交代
- [**ニーズヘッグ**](03_nidhogg.en.md): イル B スパ D（東向き）
- [**邪眼フェーズ**](04_eyes.en.md): T/H 赤、DPS 青
- [**偽典トールダン**](05_alternate_thordan.en.md): 宣告北 & 宣告固定
- [**二天竜フェーズ**](06_double_dragons.en.md): 息吹 1 三角散開、滅殺 DTTMR、息吹 2 位置固定 *または* 北 5 南 1（5-1）
- [**騎竜神トールダン**](07_dragonking_thordan.en.md): アク・モーン 3-3-2

### 最適装備

- 絶竜詩の装備は辺獄編零式のIL600と「ラピス・マナリス」のIL605装備です。

拡張パッチ後の参考までに：

- **IL730**以上の装備で、サブステが上限に設定される。
- レリックウエポンのサブステの上限は**269**です。

![]({{site.baseurl}}/assets/images/ultimates/dsr/dsr_cheatsheet_jp.jpg)
*(フルサイズ： [日本語]({{site.baseurl}}/assets/images/ultimates/dsr/dsr_cheatsheet_jp.jpg)、[English]({{site.baseurl}}/assets/images/ultimates/dsr/dsr_cheatsheet.jpg))*

---

## 各ロール視点

英語版ですが、各ロール視点を見ることができます。

- [MT視点 (戦)](https://youtube.com/live/yRJrvYChhWQ)
- [ST視点 (ナ)](https://youtube.com/live/7iFsy8xbeSc)
- [H1視点 (白)](https://youtube.com/live/UJEpzF2nJo8)
- [H2視点 (学)](https://youtube.com/live/qwVJPkc5un0)
- [D1視点 (侍)](https://youtube.com/live/2TOyLsYQlJo)
- [D2視点 (忍)](https://youtube.com/live/XOgCkE9Jdts)
- [D3視点 (踊)](https://youtube.com/live/mGSpsIZXRpc)
- [D4視点 (黒)](https://youtube.com/live/zVVuQysS9po)

---

## 注意点

- 外部ツールで「至天の陣：風槍」の雷のマーカー設置、「邪念の炎」のペアにマーカーする手法がよく用いられます。**外部ツールは自己責任でご利用ください。**

---

# 教皇庁フェーズ

絶竜詩戦争は絶シリーズ初のチェックポイントがあるため、マクロとマーカーが 2 つある。

## マクロ

```
{% include_relative macros/dsr_1.jp.txt %}
```

<details markdown=block>
<summary>English</summary>

```
{% include_relative macros/dsr_1.en.txt %}
```

</details>

## マーカー

すべてのマーカーをハイパーディメンションの誘導に使用する。

![]({{site.baseurl}}/assets/images/ultimates/dsr/markers_1.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin の座標</summary>

```json
{
  "Name":"DSR P1 - The Holy See",
  "MapID":788,
  "A":{"X":95.0,"Y":0.0,"Z":91.5,"ID":1,"Active":true},
  "B":{"X":108.5,"Y":0.0,"Z":95.0,"ID":2,"Active":true},
  "C":{"X":105.0,"Y":0.0,"Z":108.5,"ID":5,"Active":true},
  "D":{"X":91.5,"Y":0.0,"Z":105.0,"ID":6,"Active":true},
  "One":{"X":105.0,"Y":0.0,"Z":91.5,"ID":3,"Active":true},
  "Two":{"X":108.5,"Y":0.0,"Z":105.0,"ID":4,"Active":true},
  "Three":{"X":95.0,"Y":0.0,"Z":108.5,"ID":7,"Active":true},
  "Four":{"X":91.5,"Y":0.0,"Z":95.0,"ID":0,"Active":true}
}
```

</details>

---

# 正典トールダン

以下は正典トールダン以後のマクロ。

## マクロ

```
{% include_relative macros/dsr_2.jp.txt %}
```

<details markdown=block>
<summary>English</summary>

```
{% include_relative macros/dsr_2.en.txt %}
```

</details>

## マーカー

内周マーカーの数字マーカーは以下を分かりやすくする。

- 雷槍開幕の突進の安地
- ニーズヘッグの 4 塔
- 二天竜フェーズのヒートテイルの安地

![]({{site.baseurl}}/assets/images/ultimates/dsr/markers_2.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin の座標</summary>

```json
{
  "Name":"Dragonsong's Reprise",
  "MapID":788,
  "A":{"X":100.0,"Y":0.0,"Z":87.0,"ID":0,"Active":true},
  "B":{"X":113.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":113.0,"ID":2,"Active":true},
  "D":{"X":87.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":109.192,"Y":0.0,"Z":90.807,"ID":4,"Active":true},
  "Two":{"X":109.192,"Y":0.0,"Z":109.192,"ID":5,"Active":true},
  "Three":{"X":90.807,"Y":0.0,"Z":109.192,"ID":6,"Active":true},
  "Four":{"X":90.807,"Y":0.0,"Z":90.807,"ID":7,"Active":true}
}
```

</details>

---

## よくある質問

<details markdown=block>
<summary><b>[与ダメージ低下デバフ]</b> 与ダメージ低下率はどれくらいですか？</summary>
<table>
  <tr><td><p>ダメージは <b>50%</b> 低下します。</p></td></tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>