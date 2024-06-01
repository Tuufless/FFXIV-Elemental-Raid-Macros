---
layout: default
title: Lv 90. 絶オメガ
parent: 絶シリーズ
nav_order: 5
has_children: false
has_toc: false
permalink: /ultimates/jp/top/
---

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
日本語が母国語じゃないし、記事をすべて日本語で詳しくできないと思います。添削してくれたら感謝します！</div>

# 絶オメガ検証戦

Elemental DCの野良絶オメガのやり方は以下に要約する。

- [**(虫)オメガ**](01_omega.en.md): HTDH、北西/南東4:4分け
- [**男女オメガ**](02_omega_mf.en.md): 1234-4231 (〇×▽□)
- [**ファイナルオメガ**](03_omega_reconfigured.en.md): アスト式
- [**ブルー・スクリーン**](04_blue_screen.en.md): TRHM、近接調整
- **コードデュナミス**
  - [**デルタ**](05a_run_dynamis_delta.en.md): Awk式
  - [**シグマ**](05b_run_dynamis_sigma.en.md): マーカー判断式
  - [**オメガ**](05c_run_dynamis_omega.en.md)
- [**アルファオメガ**](06_alpha_omega.en.md): 8方向散開、頭割り東

### 最適装備

- 絶オメガの装備は煉獄編零式のIL630と「月の地下渓谷」のIL635装備です。

未来に向けて：

- **IL760**以上の装備で、サブステが上限に設定される。
- レリックウエポンのサブステの上限は**287**です。

![]({{site.baseurl}}/assets/images/ultimates/top/top_cheatsheet_jp.jpg)
*(フルサイズ： [日本語]({{site.baseurl}}/assets/images/ultimates/top/top_cheatsheet_jp.jpg)、[English]({{site.baseurl}}/assets/images/ultimates/top/top_cheatsheet.jpg))*

---

## 各ロール視点

英語版ですが、各ロール視点を撮影しまいた。

- [MT視点 (戦)](https://youtube.com/live/ddu61i9cG6Q)
- [ST視点 (ナ)](https://youtube.com/live/sn_3cjm2vIo)
- [H1視点 (白)](https://youtube.com/live/4OtrT1IDH5c)
- [H2視点 (賢)](https://youtube.com/live/wklF6mteicY)
- [D1視点 (侍)](https://youtube.com/live/_zxDr1mJLbo)
- [D2視点 (忍)](https://youtube.com/live/IWayItot1o8)
- [D3視点 (詩)](https://youtube.com/live/r-a6z9Ys4OU)
- [D4視点 (黒)](https://youtube.com/live/bB3v9ev093I)

---

## 注意点

- P3、シグマ、オメガに外部ツールでプレイヤーにマークするのはよくあります。**外部ツールは自己責任でご利用ください。**

---

## マクロ
```
{% include_relative macros/top.jp.txt %}
```

<details markdown=block>
<summary>English</summary>

```
{% include_relative macros/top.en.txt %}
```

</details>

---

## マーカー

![]({{site.baseurl}}/assets/images/ultimates/top/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin の座標</summary>

```json
{
  "Name":"TOP",
  "MapID":908,
  "A":{"X":100.0,"Y":0.0,"Z":87.0,"ID":0,"Active":true},
  "B":{"X":113.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":113.0,"ID":2,"Active":true},
  "D":{"X":87.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":109.192,"Y":0.0,"Z":90.808,"ID":4,"Active":true},
  "Two":{"X":109.192,"Y":0.0,"Z":109.192,"ID":5,"Active":true},
  "Three":{"X":90.808,"Y":0.0,"Z":109.192,"ID":6,"Active":true},
  "Four":{"X":90.808,"Y":0.0,"Z":90.808,"ID":7,"Active":true}
}
```

</details>

---

## よくある質問

<details markdown=block>
<summary><b>[与ダメージ低下デバフ]</b> 与ダメージ低下率はどれくらいですか？</summary>
<table>
  <tr>
    <td>
      <p>ダメージは <b>90%</b> 低下します。</p>
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>