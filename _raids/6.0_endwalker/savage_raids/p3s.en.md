---
layout: default
title: P3S
parent: Savage Raids
nav_order: "03"
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/savage_raids/p3s/
---

# Asphodelos: The Third Circle (Savage)

PF uses [Inumaru's strat](https://youtu.be/BHMjrxpZb7k) as a base, but puts
Darkened Fires (闇の炎) on intercardinal positions (Shinosho), and replaces
Fountain of Fire (霊泉) with Mr. Happy's strat (see below).

English parties replace Firestorms of Asphodelos (FoA) with "my" strat (see
below).

### Things to check on Party Finder

- Check the positions for the transition *(older macros may have different
  positioning)*

---

## English

This is the macro often used in **English** parties. In particular, Firestorms
of Asphodelos is, er, ["my" strat](#firestorms-of-asphodelos).

{% include_relative macros/p3s_tuufless.en.md %}

<details markdown=block>
<summary>Japanese translation</summary>

{% include_relative macros/p3s_tuufless.jp.md %}

</details>

## Japanese

This is the [Game8.jp macro](https://game8.jp/ff14/421350) often used by
**Japanese** parties.

{% include_relative macros/p3s_inumaru.jp.md %}

<details markdown=block>
<summary>English translation</summary>

{% include_relative macros/p3s_inumaru.en.md %}

</details>

---

## Markers

- `ABCD` are for orientation, and for the transition stacks (if applicable).
- `1234` are for:
  - Resolving the "Limit Cut" dice during Darkened Fires
  - Placing the eye thingies during Fledgling Flight.

![]({{site.baseurl}}/images/6.0_endwalker/p3s/markers.jpg)

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

---

## Experimental Gloryplume

```
【Experimental Gloryplume - Spread】
　　　MT　ST　　※ Melee (N/W), Ranged (S/E)
　　D1　▲　D2　※ Explosions-Relative:
　　D3　　　D4　　1st→D1D4　　2nd→MTH2
　　　H1　H2　　　3rd→STH1　　4th→D2D3
```

The first Experimental Gloryplume always starts with the four explosions around
the outside of the arena. We use these four explosions to determine where
everyone is spreading.

For example, if the first two explosions were the ones below (east and west),
then the final spread positions for the black orbs spread would look like:

```
    3             ST
 2     4       MT    D2
1       1  →  D1      D4
 4     2       D3    H2
    3             H1
```

---

## Firestorms of Asphodelos

There are two main ways of doing Firestorms of Asphodelos (FoA) in PF.

### Firestorms of Asphodelos (Inumaru)

**Japanese** parties will follow Inumaru's strat. Inumaru's strat maintains the
pairs from the earlier Experimental Gloryplume:

- **Tanks** + Melee north
- **Healers** + Ranged south

<table>
  <tr>
    <td><p><b>Experimental Ashplume (Spread)</b></p>
    <p>Dodge the "pizza" AoEs, followed by stacking or spreading as required.</p>
    <p>If the party needs to spread, follow this formation.</p></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p3s/foa_inumaru_01.jpg"></td>
  </tr>
  <tr>
    <td><p><b>Storms of Asphodelos</b></p>
    <p>Dodge the "pizza" AoEs, and move into position:</p>
    <ul>
      <li><b>Tanks:</b> Take the tethers, stand outside the boss's target
      circle to the NW and NE.</li>
      <li><b>H1, H2, D3:</b> Bait the fire tornadoes.</li>
      <li><b>D1, D2, D4:</b> Fan out along the south side, inside the boss's
      target circle. Use the floor markings to help with positioning.</li>
      </ul>
    </td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p3s/foa_inumaru_02.jpg"></td>
  </tr>
  <tr>
    <td><p><b>Darkblaze Twister (Spread)</b></p>
    <p>Start from the black tornado, move clockwise around the boss to bait
    five sets of AoEs before getting knocked back. Stay close to the other
    tornados to dodge the donut AoEs before stacking or spreading as needed.</p>
    <p>Using the black tornado as north:</p>
    <ul>
      <li><b>Tanks + Melee:</b> Knockback bottom-left</li>
      <li><b>Healers + Ranged:</b> Knockback bottom-right</li>
    </ul>
    <p>If the party needs to spread, take up this formation.</p></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p3s/foa_inumaru_03.jpg"></td>
  </tr>
</table>

### Firestorms of Asphodelos (Tuufless)

**English** parties will do ["my" strat](https://na.finalfantasyxiv.com/lodestone/character/10898230/blog/4933610/)
instead. The pairings for Firestorms of Asphodelos are different:

- **Healers** + Melee north
- **Tanks** + Ranged south.

{% include youtube.html id="ETQ-lHv57n0" %}

<table>
  <tr>
    <td><p><b>Experimental Ashplume (Spread)</b></p>
    <p>Dodge the "pizza" AoEs, followed by stacking or spreading as required.</p>
    <p>If the party needs to spread, follow this formation.</p></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p3s/foa_tuufless_01.jpg"></td>
  </tr>
  <tr>
    <td><p><b>Storms of Asphodelos</b></p>
    <p>Dodge the "pizza" AoEs, and move into position:</p>
    <ul>
      <li><b>Tanks:</b> Take the tethers, stand inside the boss's target
      circle to the south, and invuln.</li>
      <li><b>D1, D2, H1:</b> Stack NE of the boss, outside the target circle.</li>
      <li><b>D3, D4, H2:</b> Bait the fire tornadoes.</li></ul>
      <p>In the event any of the ranged players are dead, H1 (followed by D2)
      goes and takes their position instead.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p3s/foa_tuufless_02.jpg"></td>
  </tr>
  <tr>
    <td><p><b>Darkblaze Twister (Spread)</b></p>
    <p>Start from the black tornado, move clockwise around the boss to bait
    five sets of AoEs before getting knocked back. Stay close to the other
    tornados to dodge the donut AoEs before stacking or spreading as needed.</p>
    <p>Using the black tornado as north:</p>
    <ul>
      <li><b>Healers + Melee:</b> Knockback bottom-left</li>
      <li><b>Tanks + Ranged:</b> Knockback bottom-right</li>
    </ul>
    <p>If the party needs to spread, take up this formation.</p></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p3s/foa_tuufless_03.jpg"></td>
  </tr>
</table>

---

## Timeline

![](https://preview.redd.it/zni62rkskmb81.png?width=3200&format=png&auto=webp&s=778db6ee45958802800f16e5f9c59bedcc5b3dd3)
*(Credit: [u/Syldris](https://www.reddit.com/r/ffxiv/comments/s3on6c/p3s_rotation_and_timeline/))*

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
