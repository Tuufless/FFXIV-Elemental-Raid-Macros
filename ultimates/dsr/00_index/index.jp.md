---
layout: default
title: レベル90. 絶竜詩
parent: 絶シリーズ
nav_order: 4
has_children: true
has_toc: false
permalink: /jp/ultimates/dsr/
---

# 絶竜詩戦争

エレDCの野良のやり方は以下に要約する:

- [**教皇庁フェーズ**](../01_adelphel_and_grinnaux/index.en.md): H近遠T
- [**トールダン**](../02_thordan/index.en.md): ゼフィラン基準、 ロール内で交代
- [**ニーズヘッグ**](../03_nidhogg/index.en.md): イルB スパD (東向き)
- [**邪眼**](../04_eyes/index.en.md): T/H赤, DPS青
- [**偽典トールダン**](../05_alternate_thordan/index.en.md): 死の宣告北、死の宣告固定
- [**二天竜**](../06_double_dragons/index.en.md): △, DTTMR, 竜の息吹2回目 固定位置 *か* 5-1
- [**騎竜神トールダン**](../07_dragonking_thordan/index.en.md): アク・モーン3-3-2

![](images/dsr_cheatsheet_jp.jpg)
*(リンク: [https://cutt.ly/EleDC_DSR_summary](images/dsr_cheatsheet_jp.jpg))*

# 教皇庁フェーズ

絶竜詩戦争は絶シリーズに初めてチェックポイントがあるし、マクロとマーカーが2つあります。

## マクロ
```
{% include_relative macros/dsr_1.jp.txt %}
```

## マーカー

マーカーがハイパーディメンションの直線範囲を誘導するため。

![](images/markers_1.jpg)
<details markdown=block>
<summary>XIVLauncherのWaymarkPresetPluginの座標</summary>

```json
{
  "Name":"Adelphel and Grinnaux",
  "MapID":788,
  "A":{"X":93.015,"Y":0.0,"Z":89.036,"ID":0,"Active":true},
  "B":{"X":110.964,"Y":0.0,"Z":93.015,"ID":1,"Active":true},
  "C":{"X":106.985,"Y":0.0,"Z":110.964,"ID":2,"Active":true},
  "D":{"X":89.036,"Y":0.0,"Z":106.985,"ID":3,"Active":true},
  "One":{"X":106.985,"Y":0.0,"Z":89.036,"ID":4,"Active":true},
  "Two":{"X":110.964,"Y":0.0,"Z":106.985,"ID":5,"Active":true},
  "Three":{"X":93.015,"Y":0.0,"Z":110.964,"ID":6,"Active":true},
  "Four":{"X":89.036,"Y":0.0,"Z":93.015,"ID":7,"Active":true}
}
```

</details>

# トールダン

以下がトールダン以後使ったマクロ。

## マクロ
```
{% include_relative macros/dsr_2.jp.txt %}
```

## マーカー

もし竜の息吹2回目の固定位置処理法をしたら、タンクさんが数字マーカーで安置を楽にわかって、外周マーカーをおすすめする。

![](images/markers_outer.jpg)
<details markdown=block>
<summary>XIVLauncherのWaymarkPresetPluginの座標</summary>

```json
{
  "Name":"Dragonsong's Reprise (Outer)",
  "MapID":788,
  "A":{"X":100.0,"Y":0.0,"Z":79.0,"ID":0,"Active":true},
  "B":{"X":121.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":121.0,"ID":2,"Active":true},
  "D":{"X":79.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":114.849,"Y":0.0,"Z":85.151,"ID":4,"Active":true},
  "Two":{"X":114.849,"Y":0.0,"Z":114.849,"ID":5,"Active":true},
  "Three":{"X":85.151,"Y":0.0,"Z":114.849,"ID":6,"Active":true},
  "Four":{"X":85.151,"Y":0.0,"Z":85.151,"ID":7,"Active":true}
}
```

</details>

内周マーカーも人気です。

数字マーカーは:

- 雷槍の直線範囲の限界
- ニーズヘッグの４ヵ塔に直線範囲を誘導するところ
- ２天龍のホットテールの限界

![](images/markers_inner.jpg)
<details markdown=block>
<summary>XIVLauncherのWaymarkPresetPluginの座標</summary>

```json
{
  "Name":"Dragonsong's Reprise (Inner)",
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

## 質問

<details markdown=block>
<summary><b>[ダメージ低下デバフ]</b> ダメージ低下はどれぐらいですか？</summary>
<table>
  <tr><td><p>ダメージは<b>50%</b>低下します。</p></td></tr>
</table>
</details>