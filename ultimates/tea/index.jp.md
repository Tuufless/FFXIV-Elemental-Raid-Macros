---
layout: default
title: Lv 80. 絶アレキ
parent: 絶シリーズ
nav_order: 3
has_children: false
has_toc: false
permalink: /ultimates/jp/tea/
---

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
日本語が母語ではないので記事をすべて日本語するのは難しいと思います。添削をしてくださると嬉しいです。</div>

# 絶アレキサンダー討滅戦

Elemental DCの野良絶処理法は以下の通りです。

- [**リキッド**](01_living_liquid.en.md): セパレ式改
- [**サイコロ**](02a_limit_cut.en.md): 1211か1256
- [**２体フェーズ**](02b_bjcc.en.md): Tollgate（エレDC特有の処理法）
- [**アレキザンダープライム**](03_alex_prime.en.md): ハムカツ34固定式
- [**Pアレキ**](04_perfect_alex.en.md)

### 確認しておくこと

- リキッドフェーズのエスナの優先順
- サイコロの処理法（1211か1256）

### 最適装備

- **IL595**以上の装備で、サブステが上限に設定される。
- レリックウエポンのサブステの上限は**184**です。
- **幻薬G6**以上の薬が上限に設定される。

![]({{site.baseurl}}/assets/images/ultimates/tea/tea_cheatsheet_jp.jpg)
*(フルサイズ： [日本語]({{site.baseurl}}/assets/images/ultimates/tea/tea_cheatsheet_jp.jpg)、[English]({{site.baseurl}}/assets/images/ultimates/tea/tea_cheatsheet.jpg))*

---

## 各ロール視点

英語版ですが、各ロール視点を撮影しまいた。

- [MT視点 (戦)](https://youtu.be/uJVHsrhHsJ8)
- [ST視点 (ナ)](https://youtu.be/leQ9t61W4OY)
- [H1視点 (白)](https://youtu.be/IqcxKunPY5Q)
- [H2視点 (賢)](https://youtu.be/Q80yoHMcxhg)
- [D1視点 (侍)](https://youtu.be/RCkbxPT3prI)
- [D2視点 (忍)](https://youtu.be/yb9oLIlwiCM)
- [D3視点 (踊)](https://youtu.be/ToaYJdOdUcA)
- [D4視点 (赤)](https://youtu.be/coE2xYyd23A)

---

## マクロ

```
{% include_relative macros/tea.jp.txt %}
```

<details markdown=block>
<summary>English</summary>

```
{% include_relative macros/tea.en.txt %}
```

</details>

---

## マーカー

- `ABCD`：東西南北

**サイコロ：**
- `1234`数字マーカーはサイコロギミックのフィールドを分けるために活用します。
	- 1211式をすれば、マーカー無い方の最初の爆発から走る。
	- 1256式をすれば、1256グループはマーカー無い方から走る。3478グループはマーカー有り方から走る。
	
**２体フェーズ：**
- `A`：水１回目
- `C`：水２回目
- `3`：水３回目

**アレキザンダープライム：**
- `4`：時空潜行のマーチの後半の退避場所（ST、接近禁止だったDPS、ヒーラー２人以外）。

**Pアレキ**
- `B`：闇の親
- `1234`：大審判

![]({{site.baseurl}}/assets/images/ultimates/tea/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin の座標</summary>

```json
{
  "Name":"TEA",
  "MapID":694,
  "A":{"X":100.0,"Y":0.0,"Z":88.0,"ID":0,"Active":true},
  "B":{"X":114.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":116.0,"ID":2,"Active":true},
  "D":{"X":84.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":92.2,"Y":0.0,"Z":107.8,"ID":4,"Active":true},
  "Two":{"X":100.0,"Y":0.0,"Z":107.8,"ID":5,"Active":true},
  "Three":{"X":107.8,"Y":0.0,"Z":107.8,"ID":6,"Active":true},
  "Four":{"X":107.8,"Y":0.0,"Z":100.0,"ID":7,"Active":true}
}
```

</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>