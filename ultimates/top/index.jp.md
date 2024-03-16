---
layout: default
title: Lv 90. 絶オメガ
parent: Ultimates
nav_order: 5
has_children: true
has_toc: false
permalink: /ultimates/jp/top/
---

# 絶オメガ検証戦

Elemental's TOP PF strat can be broken down as follows:

- [**(Beetle) Omega**](01_omega.en.md): HTDH priority, NW/SE Pantokrator
- [**Omega M/F**](02_omega_mf.en.md): 1234 (〇×▽□)-4231
- [**(Final) Omega**](03_omega_reconfigured.en.md): Astoh monitors
- [**Blue Screen**](04_blue_screen.en.md): TRHM, melee adjust
- **Run: Dynamis**
  - [**Delta**](05a_run_dynamis_delta.en.md): Awk
  - [**Sigma**](05b_run_dynamis_sigma.en.md): Waymark towers
  - [**Omega**](05c_run_dynamis_omega.en.md)
- [**Alpha Omega**](06_alpha_omega.en.md): Clock spread, Wave Cannon stack east

エレDCと[Lily Dollさん](https://jp.finalfantasyxiv.com/lodestone/character/34120564/blog/5178791/)の処理法の違いは以下の通り。

P1:
  - パンクラのグループ分け法が異なる。
  - 波動砲の散開位置はヒーラーと遠隔DPSが入れ替わる。
P2:
  - ファー散開位置が一番上と下しか入れ替わりません。
  - 連携プログラムLBの線取りが異なる（南北で取ります）。
P3:
  - 検知式波動砲の優先はTDHではなく、HTDになる。
デルタ：
  - 内周の青線が短い。
  - 内周の青線がオメガMのシールドバッシュを誘導する。
  - ハロワの立ち位置が異なる。
シグマ：
  - オメガMが北として、南中央で並ぶ。
  - デバフなしの線引っ張る位置が逆（上の方は左上へ）。
  - 塔踏みマーカーが異なる。
P6:
  - ８方向散開は全てMTD3入れ替わる。

### BiS Notes

- The Omega Protocal is a current Ultimate, and is **not** outgeared yet.
    - BiS will be a mix of i630 gear, and i635 gear from The Lunar Subterrane.

Looking towards the future:

- The Omega Protocol will not be outgeared until **i760** gear is available.
- Relic weapons (when they arrive) will have their substats capped at **287**.

![]({{site.baseurl}}/assets/images/ultimates/top/top_cheatsheet_jp.jpg)
*(Full-size image: [English]({{site.baseurl}}/assets/images/ultimates/top/top_cheatsheet.jpg), [日本語]({{site.baseurl}}/assets/images/ultimates/top/top_cheatsheet_jp.jpg))*

---

## 各ロール視点

Here are some clear PoVs that I've been collecting.

- [MT PoV (WAR)](https://youtube.com/live/ddu61i9cG6Q)
- [ST PoV (PLD)](https://youtube.com/live/sn_3cjm2vIo)
- [H1 PoV (WHM)](https://youtube.com/live/4OtrT1IDH5c)
- [H2 PoV (SGE)](https://youtube.com/live/wklF6mteicY)
- [D1 PoV (SAM)](https://youtube.com/live/_zxDr1mJLbo)
- [D2 PoV (NIN)](https://youtube.com/live/IWayItot1o8)
- [D3 PoV (BRD)](https://youtube.com/live/mtfT3oWXe3Y)
- [D4 PoV (BLM)](https://youtube.com/live/bB3v9ev093I)

---

## Things to note

- Using automarkers to mark players for the transition to P3, and to mark player positions in Delta, Sigma, and Omega is considered the norm (*use at your own risk*).

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
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

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
<summary><b>[Damage Down]</b> How strong is the damage down debuff in this fight?</summary>
<table>
  <tr><td><p>The Damage Down debuff in this phase lowers a player's damage by <b>90%</b>.</p>
  <p><em>(Yes, this is </em>worse<em> than double-weakness!)</em></p></td></tr>
</table>
</details>