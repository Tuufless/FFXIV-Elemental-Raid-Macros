---
layout: default
title: P7S
parent: Savage Raids
nav_order: "07"
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/savage_raids/p7s/
---

# Abyssos: The Seventh Circle (Savage)

PF uses [Shinosho's strat](https://youtu.be/JOMBTuWf-j8) as a base, but uses
[Sleepo's Inviolate Purgation strat](https://ff14.toolboxgaming.space/?id=339073562612661&preview=1)
and [Inumaru's War's Harvest strat](#wars-harvest-inumaru).

Nukemaru has made a guide aggregating all the strats together:

{% include youtube.html id="iaxDpAfkTIA" %}

### Things to check on Party Finder

- **Japanese** parties prefer to:
  - Inviolate Bonds: Have the first stack in the center of the arena, but do
    the second stack where the island meets the bridge.
  - Forbidden Fruit #5: Take the bird tethers clockwise.
- **English** parties prefer to:
  - Inviolate Bonds: Resolve both stacks in the middle of the islands.
  - Forbidden Fruit #5: Stretch the tethers across the arena.

## Japanese

The following is [Game8.jp's macro](https://game8.jp/ff14/479465):

{% include_relative macros/p7s.jp.md %}


## English

{% include_relative macros/p7s.en.md %}

## Markers (Game8)

These are the markers as promoted on Game8's website.

All markers are used for Sleepo's Purgation. Of note, the spread position for
the outer-left positions (`B` and `2`) are directly *west/east* of the markers.

![]({{site.baseurl}}/images/6.0_endwalker/p7s/markers_game8.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"P7S (Game8)",
  "MapID":877,
  "A":{"X":114.29,"Y":0.0,"Z":86.151,"ID":0,"Active":true},
  "B":{"X":119.543,"Y":0.0,"Z":96.25,"ID":1,"Active":true},
  "C":{"X":114.29,"Y":0.0,"Z":100.75,"ID":2,"Active":true},
  "D":{"X":114.29,"Y":0.0,"Z":91.75,"ID":3,"Active":true},
  "One":{"X":85.71,"Y":0.0,"Z":86.151,"ID":4,"Active":true},
  "Two":{"X":80.457,"Y":0.0,"Z":96.25,"ID":5,"Active":true},
  "Three":{"X":85.71,"Y":0.0,"Z":100.75,"ID":6,"Active":true},
  "Four":{"X":85.71,"Y":0.0,"Z":91.75,"ID":7,"Active":true}
}
```

</details>

## Markers (Sleepo)

These set of markers can only be placed in-game after you have cleared the
fight (the arena with expand after clearing, where you can then place the
markers).

If you haven't cleared the fight, you will need to copy the markers from
someone who does.

All markers are used for Sleepo's Purgation.

- `2` and `B`: Stack positions.
- All other markers are the spread positions.

![]({{site.baseurl}}/images/6.0_endwalker/p7s/markers_sleepo.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"P7S (Sleepo)",
  "MapID":877,
  "A":{"X":114.29,"Y":0.0,"Z":82.75,"ID":0,"Active":true},
  "B":{"X":122.084,"Y":0.0,"Z":87.25,"ID":1,"Active":true},
  "C":{"X":122.0842,"Y":0.0,"Z":96.25,"ID":2,"Active":true},
  "D":{"X":114.29,"Y":0.0,"Z":100.75,"ID":3,"Active":true},
  "One":{"X":85.71,"Y":0.0,"Z":82.75,"ID":4,"Active":true},
  "Two":{"X":77.915,"Y":0.0,"Z":87.25,"ID":5,"Active":true},
  "Three":{"X":77.915,"Y":0.0,"Z":96.25,"ID":6,"Active":true},
  "Four":{"X":85.71,"Y":0.0,"Z":100.75,"ID":7,"Active":true}
}
```

</details>

## Timeline
![](https://preview.redd.it/gvazt7d9ngm91.png?width=1718&format=png&auto=webp&s=c04fcb786ac3df24733e4136cda2e927cf2727ce)
*(Credit: [u/ExiaKuromonji](https://www.reddit.com/r/ffxiv/comments/x891mn/p7s_timeline/))*

## Inviolate Purgation (Sleepo)

This is a strat to resolve Inviolate Purgation that involves alternating all
eight players between the two front islands.

[Sleepo Purgation Toolbox](https://ff14.toolboxgaming.space/?id=339073562612661&preview=1)

## Famine's Harvest

The group tethered to minotaurs need to cross tethers to avoid hitting one another.

![]({{site.baseurl}}/images/6.0_endwalker/p7s/famines_harvest.jpg)

## Death's Harvest (fixed positions, tank invuln)

One of the three platforms has an add; use this platform as North, and then all
(non-tank) players have fixed assigned positions as shown below, regardless of
which Behemoth they're tethered to.

Tanks stack on the empty bridge and invuln.

![]({{site.baseurl}}/images/6.0_endwalker/p7s/deaths_harvest.jpg)

## War's Harvest (Inumaru)

Note that the minotaur tethers will *not* be stretched out enough to turn
purple. As a result, **shields and mitigations are required** for the two
minotaur players to survive.

![]({{site.baseurl}}/images/6.0_endwalker/p7s/wars_harvest.jpg)

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
