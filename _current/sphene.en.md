---
layout: default
title: Sphene EX
nav_order: 3
permalink: /7.0_dawntrail/extreme_trials/sphene/
---

# The Minstrel's Ballad: Sphene's Burden

[Game8](https://game8.jp/ff14/641571) has gone with Hamkatsu's strategy.

{% include youtube.html id="UEQrzXo_zbo" %}

## English

{% include_relative macros/sphene.en.md %}

## Japanese

{% include_relative macros/sphene.jp.md %}

---

## Markers

The markers are where the party stands during *Coronation*. They are also
colour-coded to indicate where each beam should be placed (i.e: between the
`1A`, `2B`, `3C`, and `4D` markers).

![]({{site.baseurl}}/images/7.0_dawntrail/sphene/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"Sphene EX",
  "MapID":1017,
  "A":{"X":100.0,"Y":0.0,"Z":81.125,"ID":0,"Active":true},
  "B":{"X":118.875,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":118.875,"ID":2,"Active":true},
  "D":{"X":81.125,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":118.875,"Y":0.0,"Z":81.125,"ID":4,"Active":true},
  "Two":{"X":118.875,"Y":0.0,"Z":118.875,"ID":5,"Active":true},
  "Three":{"X":81.125,"Y":0.0,"Z":118.875,"ID":6,"Active":true},
  "Four":{"X":81.125,"Y":0.0,"Z":81.125,"ID":7,"Active":true}
}
```

</details>

---

## Timeline
![](https://preview.redd.it/spoiler-7-1-ex3-timeline-v0-i330ioksqq0e1.png?width=1684&format=png&auto=webp&s=60dd46440cce5f601eefbbe5c39821d4130b6e3a)
*(Credit: [u/ExiaKuromonji](https://www.reddit.com/r/ffxiv/comments/1gqk8l3/spoiler_71_ex3_timeline/))*

---

## Frequently Asked Questions

<details markdown=block>
<summary>
  <b>[Aethertithe]</b> Do the tanks have to stand in front for the beams?
</summary>
<table>
  <tr>
    <td>
      <p>No, the beams split their damage between all players hit, with no 
      consideration to who is in front.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Laws of Ice 2]</b> When should the tanks use their invulns?
</summary>
<table>
  <tr>
    <td>
      <p>The stack marker will pulse six times before resolving.</p>
      <p>The tanks should use their invulns <b>at the fifth pulse</b> to cover
      the last two hits.</p>
    </td>
  </tr>
</table>
</details>

---

## Troubleshooting

<details markdown=block>
<summary>
  <b>[Authority Eternal]</b> How are we dying to the P1 enrage?
</summary>
<table>
  <tr>
    <td>
      <p>The mechanic sequence after the Virtual Shift (Ice) phase goes:</p>
      <ol>
        <li><em>Prosecution of War</em> (tankbusters)</li>
        <li><em>Royal Domain</em> (raid-wide damage)</li>
        <li><em>Legitimate Force</em> (half-room E/W cleaves)</li>
        <li><em>Royal Domain</em> (raid-wide damage)</li>
        <li><em>Authority Eternal</em> (P1 enrage)</li>
      </ol>
      <p>This whole sequence lasts a minute- <b>however, this is interrupted,
      and goes straight to Authority Eternal when the boss goes below 2.0% HP.</b></p>
      <p>The danger is that <em>Authority Eternal</em> is pushed, but the 
      party has weakened members, or doesn't have the ability to burst down 
      the boss's HP to 0.1% before <em>Authority Eternal</em> resolves, 
      leading to a wipe.</p>
      <p>For that reason, if the party was struggling earlier, it may be 
      worth considering holding damage or building resources for 
      <em>Authority Eternal</em>. Also note that if the boss's is pushed below
      2.0% HP in the middle of a mechanic, the mechanic will complete before 
      starting <em>Authority Eternal</em>.</p>
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
