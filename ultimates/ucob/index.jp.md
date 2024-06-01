---
layout: default
title: Lv 70. 絶バハ
parent: 絶シリーズ
nav_order: 1
has_children: false
has_toc: false
permalink: /ultimates/jp/ucob/
---

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
日本語が母国語じゃないし、記事をすべて日本語で詳しくできないと思います。添削してくれたら感謝します！</div>

# 絶バハムート討滅戦

Elemental DCの野良絶バハのやり方は基本[Cleesさんの処理法](https://clees.me/guides/ucob/)です。

### 最適装備

- **IL470**以上の装備で、サブステが上限に設定される。
- レリックウエポンのサブステの上限は**127**です。
- **幻薬G3**以上の薬が上限に設定される。

---

## マクロ

```
{% include_relative macros/ucob.jp.txt %}
```

<details markdown=block>
<summary>English</summary>

```
{% include_relative macros/ucob.en.txt %}
```

</details>

---

## マーカー

**タニア：**
- `123`: 拘束具

**ネール：**
- `4`: 赤熱を頭割りところ、ファイアを受けところ

**バハムート：**
- `ABCD`：連撃のシェイカー
- `123`：厄災にボス沸き所。天地のノックバークに結んだ円に乗る
- `3`：連撃の安置。シェイカー２回目を通信するため
- `4`: 黒炎と天地の集合ところ。郡龍にバハムートが東西南北にいるかどうか判断するため

**金バハムート：**
- `3`：アク・モーン１回目のタンク２人受けところ

![]({{site.baseurl}}/assets/images/ultimates/ucob/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin の座標</summary>

```json
{
  "Name":"UCoB",
  "MapID":280,
  "A":{"X":-11.472,"Y":0.0,"Z":-16.383,"ID":0,"Active":true},
  "B":{"X":11.47153,"Y":0.0,"Z":-16.383,"ID":1,"Active":true},
  "C":{"X":19.31852,"Y":0.0,"Z":5.176381,"ID":2,"Active":true},
  "D":{"X":-19.319,"Y":0.0,"Z":5.176,"ID":3,"Active":true},
  "One":{"X":-7.57,"Y":0.0,"Z":-4.38,"ID":4,"Active":true},
  "Two":{"X":7.57,"Y":0.0,"Z":-4.38,"ID":5,"Active":true},
  "Three":{"X":0.0,"Y":0.0,"Z":8.75,"ID":6,"Active":true},
  "Four":{"X":0.0,"Y":0.0,"Z":0.0,"ID":7,"Active":true}
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
