---
layout: default
title: P6S
parent: Savage Raids
nav_order: "06"
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/savage_raids/p6s/
---

# Abyssos: The Sixth Circle (Savage)

The following macros are from [Game8.jp](https://game8.jp/ff14/479307), which uses
Nukemaru's strat:

{% include youtube.html id="pibChZ8AjZ8" %}

*Some* parties will replace Nukemaru's *Cachexia* 1 with ZizieZip's method (see
below).

## Japanese

*(Nukemaru's Cachexia 1)*
{% include_relative macros/p6s_nukemaru.jp.md %}

## English

*(Nukemaru's Cachexia 1)*
{% include_relative macros/p6s_nukemaru.en.md %}

**English** parties will replace Nukemaru's Cachexia 1 strat with
[ZizieZip's Cachexia 1 strat](https://twitter.com/ZizieZip/status/1564991162775060480).


## English

*(ZizieZip's Cachexia 1)*
{% include_relative macros/p6s_ziziezip.en.md %}

## Japanese

*(ZizieZip's Cachexia 1)*
{% include_relative macros/p6s_ziziezip.jp.md %}

## Markers (Nukemaru)

These markers are for Nukemaru's Cachexia 1:

- `1` and `A`: 8 seconds
- `2` and `B`: 12 seconds
- `3` and `C`: 16 seconds
- `4` and `D`: 20 seconds

Players rotate moving "down" in the markers (i.e: 4→3→2→1→4 and D→C→B→A→D)

![]({{site.baseurl}}/images/6.0_endwalker/p6s/markers_nukemaru.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"P6S (Nukemaru)",
  "MapID":881,
  "A":{"X":108.7,"Y":0.0,"Z":91.3,"ID":0,"Active":true},
  "B":{"X":115.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":108.7,"Y":0.0,"Z":108.7,"ID":2,"Active":true},
  "D":{"X":104.5,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":91.3,"Y":0.0,"Z":91.3,"ID":4,"Active":true},
  "Two":{"X":85.0,"Y":0.0,"Z":100.0,"ID":5,"Active":true},
  "Three":{"X":91.3,"Y":0.0,"Z":108.7,"ID":6,"Active":true},
  "Four":{"X":95.5,"Y":0.0,"Z":100.0,"ID":7,"Active":true}
}
```

</details>

## Markers (ZizieZip)

These markers are for ZizieZip. The markers are colour-coded in each corner to
make callouts easier.

In addition, the "purple-ish" markers are on the west side, and the "green-ish"
markers (blue + yellow) are on the east side to help remember which side the
purple/green debuffs go.

Letters are N/S, while numbers are E/W to also help with that grouping when
dodging the fan AoEs.

![]({{site.baseurl}}/images/6.0_endwalker/p6s/markers_ziziezip.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"P6S (ZizieZip)",
  "MapID":881,
  "A":{"X":95.0,"Y":0.0,"Z":88.333,"ID":0,"Active":true},
  "B":{"X":105.0,"Y":0.0,"Z":88.333,"ID":1,"Active":true},
  "C":{"X":105.0,"Y":0.0,"Z":111.666,"ID":2,"Active":true},
  "D":{"X":95.0,"Y":0.0,"Z":111.666,"ID":3,"Active":true},
  "One":{"X":88.333,"Y":0.0,"Z":95.0,"ID":4,"Active":true},
  "Two":{"X":111.666,"Y":0.0,"Z":95.0,"ID":5,"Active":true},
  "Three":{"X":111.666,"Y":0.0,"Z":105.0,"ID":6,"Active":true},
  "Four":{"X":88.333,"Y":0.0,"Z":105.0,"ID":7,"Active":true}
}
```

</details>

## Timeline
![](https://preview.redd.it/8x9fj1dkn9m91.png?width=1725&format=png&auto=webp&s=a31c4670ce294596a5c19307835088361ce47048)
*(Credit: [u/ExiaKuromonji](https://www.reddit.com/r/ffxiv/comments/x49kry/p6s_timeline/))*

## Aetheric Polynominoids

![]({{site.baseurl}}/images/6.0_endwalker/p6s/polynominoids.jpg)
*(Credit: Yuexi Siohre)*

## Cachexia 1

English PFs will use ZizieZip's strat to resolve Cachexia 1.

<blockquote class="twitter-tweet">
  <p lang="ja" dir="ltr">煉獄零式2層：カヘキシー(緑紫デバフ)<br>ぐるぐる回らなくても、少しの移動だけで処理できそう。<br>デバフの残り秒数に関係なく「北T-H-D4321南」順に並べばめちゃくちゃ簡単。<br>基本の立ち位置に各マーカー、順番にタゲサをちょっと踏み越えるだけでOKです。<a href="https://t.co/VMWjsPhUFb">https://t.co/VMWjsPhUFb</a> <a href="https://t.co/CF32Zq8a1U">pic.twitter.com/CF32Zq8a1U</a></p>&mdash; ジジー･ジップ🐥 (@ZizieZip) <a href="https://twitter.com/ZizieZip/status/1564991162775060480?ref_src=twsrc%5Etfw">August 31, 2022</a>
</blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Note that there are two versions of the strat going around:

1. One based on roles (this is the one used in the macro)
2. One based on timers (we aren't using this)

The two players with the 20s debuffs start a little under the boss. All other
players can wait for their vulnerability debuff to wear off before then
stepping inside the boss's hitbox.

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
