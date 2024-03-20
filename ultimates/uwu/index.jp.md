---
layout: default
title: Lv 70. 絶アルテマ
parent: 絶シリーズ
nav_order: 2
has_children: false
has_toc: false
permalink: /ultimates/jp/uwu/
---

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
日本語が母国語じゃないし、記事をすべて日本語で詳しくできないと思います。添削してくれたら感謝します！</div>

# 絶アルテマウェポン破壊作戦

Elemental DCの野良絶アルテマのやり方は基本[Cleesさんの処理法](https://www.icy-veins.com/ffxiv/the-weapons-refrain-ultimate-guides-ultima)です。

- [**ガルーダ**](01_garuda.en.md): ガルーダ中央
- [**イフリート**](02_ifrit.en.md): 逆Z字
- [**タイタン**](03_titan.en.md): マラソン
- [**追撃**](04a_predation.en.md)
- [**爆撃**](04b_annihilation.en.md): 2211玉処理
- [**乱撃**](04c_suppression.en.md): 扇式
- [**蛮神召喚履行**](04d_primal_roulette.en.md)

### 最適装備

- **IL500**以上の装備で、サブステが上限に設定される。
- レリックウェポンのサブステの上限は**136**です。
- **幻薬G4**以上の薬が上限に設定される。

---

## 注意点

- タイタンに外部ツールでプレイヤーをマークするのはよくあります。**外部ツールは自己責任でご利用ください。。**
- イフリートの突進を飛ぶ可能性があるし、ナイトとガンブレがいったら注意ところがある。
	- 突進を飛ぶと、イフリートの最初の強攻撃から追撃後の「誘導レーザー」までは約6分30秒です（ナイトは両方無敵受けられません。）
  - 突進を飛ばないと、イフリートの最終の強攻撃から追撃後の「誘導レーザー」までは約5分40秒です（ナイトとガンブレもは両方無敵受けられません。）

---

## マクロ

```
{% include_relative macros/uwu.jp.txt %}
```

<details markdown=block>
<summary>English</summary>


```
{% include_relative macros/uwu.en.txt %}
```

</details>

---

## マーカー

- `ABCD`：東西南北

**ガルーダ：**
- `4`：ミストラルの時に集合ところ

**イフリート：**
- `ABCD`：東西南北（突進１回目を避けるため）

**タイタン：**
- `ABCD`と`1`：ジェイル

**アルテマ：**
- `3`:「爆撃」と「蛮神召喚履行フェーズ」にイフリートの突進を避けるため
- `4`: 乱撃のジェイル
- `B`: 乱撃のファイアボール

![]({{site.baseurl}}/assets/images/ultimates/uwu/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin の座標</summary>

```json
{
  "Name":"UWU",
  "MapID":539,
  "A":{"X":100.0,"Y":0.0,"Z":93.3,"ID":0,"Active":true},
  "B":{"X":106.7,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":106.7,"ID":2,"Active":true},
  "D":{"X":93.3,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":100.0,"Y":0.0,"Z":100.0,"ID":4,"Active":true},
  "Two":{"X":107.3,"Y":0.0,"Z":107.3,"ID":5,"Active":true},
  "Three":{"X":100.0,"Y":0.0,"Z":81.0,"ID":6,"Active":true},
  "Four":{"X":87.0,"Y":0.0,"Z":87.0,"ID":7,"Active":true}
}
```

</details>
