---
layout: default
title: P3S
parent: Savage Raids
nav_order: "03"
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/savage_raids/p3s/
---

# Asphodelos: The Third Circle (Savage)

PF uses [Inumaru's strat](https://youtu.be/BHMjrxpZb7k) as a base, but puts Darkened Fires (闇の炎) on intercardinal positions (Shinosho), and replaces Fountain of Fire (霊泉) with Mr. Happy's strat (see below).

English parties replace Firestorms of Asphodelos (FoA) with "my" strat (see below).

### Things to check on Party Finder

- Check the positions for the transition *(older macros may have different positioning)*

## English

This is the macro often used in **English** parties. In particular, Firestorms of Asphodelos is, er, ["my" strat](#firestorms-of-asphodelos).
```
{% include_relative macros/p3s_tuufless.en.txt %}
```

<details markdown=block>
<summary>Japanese translation</summary>

```
{% include_relative macros/p3s_tuufless.jp.txt %}
```

</details>

## Japanese

This is the [game8 macro](https://game8.jp/ff14/421350) often used by **Japanese** parties.
```
{% include_relative macros/p3s_inumaru.jp.txt %}
```

<details markdown=block>
<summary>English translation</summary>

```
{% include_relative macros/p3s_inumaru.en.txt %}
```

</details>

## Markers

- `ABCD` are for orientation, and for the transition stacks (if applicable).
- `1234` are for:
	- Resolving the "Limit Cut" dice during Darkened Fires
	- Placing the eye thingies during Fledgling Flight.

![](images/markers.jpg)

<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"P3S",
  "MapID":807,
  "A":{"X":100.0,"Y":0.0,"Z":81.5,"ID":0,"Active":true},
  "B":{"X":118.5,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":118.5,"ID":2,"Active":true},
  "D":{"X":81.5,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":100.0,"Y":0.0,"Z":94.0,"ID":4,"Active":true},
  "Two":{"X":106.0,"Y":0.0,"Z":100.0,"ID":5,"Active":true},
  "Three":{"X":100.0,"Y":0.0,"Z":106.0,"ID":6,"Active":true},
  "Four":{"X":94.0,"Y":0.0,"Z":100.0,"ID":7,"Active":true}
}
```

</details>

## Experimental Gloryplume

```
【Experimental Gloryplume - Spread】
　　　MT　ST　　※ Melee (N/W), Ranged (S/E)
　　D1　▲　D2　※ Explosions-Relative:
　　D3　　　D4　　1st→D1D4　　2nd→MTH2
　　　H1　H2　　　3rd→STH1　　4th→D2D3
```
The first Experimental Gloryplume always starts with the four explosions around the outside of the arena. We use these four explosions to determine where everyone is spreading.

For example, if the first two explosions were the ones below (east and west), then the final spread positions for the black orbs spread would look like:

```
    3             ST
 2     4       MT    D2
1       1  →  D1      D4
 4     2       D3    H2
    3             H1
```

## Firestorms of Asphodelos

There are two main ways of doing Firestorms of Asphodelos (FoA) in PF.

- **Japanese** parties will do follow Inumaru's strat. ([Inumaru FoA](https://imgur.com/a/V0UWZym))
  - **Tanks** + Melee north
  - **Healers** + Ranged south

- **English** parties will do "my" strat instead. ([Tuufless FoA](https://imgur.com/a/yCdVkTW))
  - Explanations [in English](https://ffxiv.link/061500) and [in Japanese](https://ffxiv.link/062054)
  - **Healers** + Melee north
  - **Tanks** + Ranged south.

## Timeline

![](https://preview.redd.it/zni62rkskmb81.png?width=3200&format=png&auto=webp&s=778db6ee45958802800f16e5f9c59bedcc5b3dd3)
*(Credit: [u/Syldris](https://www.reddit.com/r/ffxiv/comments/s3on6c/p3s_rotation_and_timeline/))*