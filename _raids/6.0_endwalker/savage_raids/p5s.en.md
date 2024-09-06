---
layout: default
title: P5S
parent: Savage Raids
nav_order: "05"
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/savage_raids/p5s/
---

# Abyssos: The Fifth Circle (Savage)

This is [Game8.jp's macro](https://game8.jp/ff14/464675)

{% include youtube.html id="GRrZvJT1fXM" %}

## English

{% include_relative macros/p5s.en.md %}

## Japanese

{% include_relative macros/p5s.jp.md %}

## Markers

There aren't any real fixed set of markers used for this fight- this set places
markers on the potential poison puddle positions:

- `ABCD` are used for orientation.
- `1234` are useful when calling out where to move during Ruby Glow 3.

![]({{site.baseurl}}/images/6.0_endwalker/p5s/markers_1.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"P5S (Towers)",
  "MapID":873,
  "A":{"X":100.0,"Y":-300.0,"Z":92.9,"ID":0,"Active":true},
  "B":{"X":107.1,"Y":-300.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":-300.0,"Z":107.1,"ID":2,"Active":true},
  "D":{"X":92.9,"Y":-300.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":110.7,"Y":-300.0,"Z":89.3,"ID":4,"Active":true},
  "Two":{"X":110.7,"Y":-300.0,"Z":110.7,"ID":5,"Active":true},
  "Three":{"X":89.3,"Y":-300.0,"Z":110.7,"ID":6,"Active":true},
  "Four":{"X":89.3,"Y":-300.0,"Z":89.3,"ID":7,"Active":true}
}
```

</details>

This set of markers simply puts everything in a circle.

- `ABCD` are used for orientation.
- `1234` are useful when calling out where to move during Ruby Glow 3.

![]({{site.baseurl}}/images/6.0_endwalker/p5s/markers_2.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"P5S (Circle)",
  "MapID":873,
  "A":{"X":100.0,"Y":-300.0,"Z":90.0,"ID":0,"Active":true},
  "B":{"X":110.0,"Y":-300.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":-300.0,"Z":110.0,"ID":2,"Active":true},
  "D":{"X":90.0,"Y":-300.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":92.929,"Y":-300.0,"Z":92.929,"ID":4,"Active":true},
  "Two":{"X":107.07,"Y":-300.0,"Z":92.929,"ID":5,"Active":true},
  "Three":{"X":107.07,"Y":-300.0,"Z":107.07,"ID":6,"Active":true},
  "Four":{"X":92.929,"Y":-300.0,"Z":107.07,"ID":7,"Active":true}
}
```

</details>

## Timeline
![](https://preview.redd.it/byylqr56ugl91.png?width=1741&format=png&auto=webp&s=9dd4e24d2df98e9b753cfc3a49c63c6956ad709e)
*(Credit: [u/ExiaKuromonji](https://www.reddit.com/r/ffxiv/comments/x1sj4y/p5s_timeline/))*

## Ruby Glow 5

The way Game 8 chose to resolve Ruby Glow 5 is to assign the MT group to the
north-side **poison** quadrant, and the ST group to the south side **poison**
quadrant.

Once you've identified your quadrant, move to the side **without** the poison
crystal (this will always be next to the yellow crystal that will explode).

The four possible outcomes are as follows:

<table>
  <tr>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p5s/ruby_5_1.jpg"></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p5s/ruby_5_2.jpg"></td>
  </tr>
  <tr>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p5s/ruby_5_3.jpg"></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p5s/ruby_5_4.jpg"></td>
  </tr>
</table>


## Frequently Asked Questions

<details markdown=block>
<summary>
  <b>[Ruby Glow 5]</b> Some groups refer to a N/W and S/E strat- how is that
  different?
</summary>
<table>
  <tr>
    <td colspan="2">
      <p>This refers to a different method of assigning quadrants that some EN
      groups do. The main difference is what the party pays attention to.</p>
      <p>Game8 unfortunately chose the strat that focuses on the <b>poison
      crystals</b>, which leads to a somewhat counterintuitive case 1/4 of the
      time.</p>
      <p>This strat assigns the light parties based on the <b>yellow
      crystals</b> instead, which keeps to the "MT group N/W", "ST group S/E"
      convention.</p>
      <p>The problem, of course, is that both methods work out to the same
      outcome in 3/4 of the cases, but not the last 1/4.</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="{{site.baseurl}}/images/6.0_endwalker/p5s/ruby_5_1_yellow.jpg">
    </td>
    <td>
      <img src="{{site.baseurl}}/images/6.0_endwalker/p5s/ruby_5_2_yellow.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <img src="{{site.baseurl}}/images/6.0_endwalker/p5s/ruby_5_3_yellow.jpg">
    </td>
    <td>
      <img src="{{site.baseurl}}/images/6.0_endwalker/p5s/ruby_5_4_yellow.jpg">
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
