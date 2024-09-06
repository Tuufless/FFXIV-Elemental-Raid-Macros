---
layout: default
title: Endsinger EX
parent: Extreme Trials
nav_order: 3
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/extreme_trials/endsinger/
---

# The Minstrel's Ballad: The Endsinger's Aria

PF largely follows Nukemaru's guide:

{% include youtube.html id="dwZ8uVCPI80" %}

## English

{% include_relative macros/endsinger.en.md %}

## Japanese

This is the [Game8.jp macro](https://game8.jp/ff14/446913) that's being used:

{% include_relative macros/endsinger.jp.md %}

## Markers

The intercardinal `1234` markers are the impact points for all the planetary collisions.

All markers are the player positions for Flare/AoEs during Theological Fatalism (player debuffs). The center `C` marker is for the Donuts + stack (people tend to stack too far south otherwise).

You also want to mark the two healers for stacks.
![]({{site.baseurl}}/images/6.0_endwalker/endsinger/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"Endsinger EX",
  "MapID":846,
  "A":{"X":100.0,"Y":0.0,"Z":82.0,"ID":0,"Active":true},
  "B":{"X":118.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":100.0,"ID":2,"Active":true},
  "D":{"X":82.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":87.272,"Y":0.0,"Z":87.272,"ID":4,"Active":true},
  "Two":{"X":112.728,"Y":0.0,"Z":87.272,"ID":5,"Active":true},
  "Three":{"X":112.728,"Y":0.0,"Z":112.728,"ID":6,"Active":true},
  "Four":{"X":87.272,"Y":0.0,"Z":112.728,"ID":7,"Active":true}
}
```

</details>

## Theological Fatalism (5-heads)

An easy way to resolve the 5-heads mechanic is:

1. From the third donut, determine whether your current quadrant will be cleaved by the center head:
	- If it **will** get cleaved, cross over diagonally to the opposite quadrant.
	- If it **won't** get cleaved, stay in your current quadrant.
2. Check the number of rings in your current quadrant:
	- If it is **odd**, stay in your current quadrant.
	- If it is **even**, move to the other quadrant that won't get cleaved by the center head.
	
![]({{site.baseurl}}/images/6.0_endwalker/endsinger/five_head.jpg)
*(Credit: [Nukemaru](https://twitter.com/nukemarugames/status/1514278676359446528?s=20&t=olONmsjUl90VIwjrZNqbtQ))*

## 2x Fatalism

If you have LB3 available during the 2x Fatalism (quadruple planets), a Tank LB3 right after the second planet collision will allow players to survive red planet hits during the harder "blue-to-red" planet sequence.

To get the LB3 by this time, you will need a standard party setup with no duplicate jobs.

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
