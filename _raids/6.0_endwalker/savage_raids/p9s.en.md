---
layout: default
title: P9S
parent: Savage Raids
nav_order: "09"
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/savage_raids/p9s/
---

# Anabaseios: The Ninth Circle (Savage)

[Game8.jp](https://game8.jp/ff14/532345) has gone with Nukemaru's strat for P9S.

{% include youtube.html id="URo06JSGEgM" %}

### Things to check on Party Finder

- Check the Scrambled Succession ("Limit Cut 1") strat used.
  - **Japanese** parties will go with the strat that has [the party run around in a circle](#scrambled-succession-mario-kart) (known as 無職マラソン in Japanese).
  - **English** parties may do the ["Intercard" strat](#scrambled-succession-intercard) that resolves two of the Ice AoEs at one corner, before flipping the map around (known as ぶたばら式 in Japanese).

- Check the Chimeric Succession positions for players marked `1` and `2`.
  - Some macros have `1` go **west**, and `2` go **east**.
  - Some macros have `1` go **east**, and `2` go **west**.

## Nukemaru's strat (Mario Kart)

This is the preferred strat by JP that Nukemaru featured. It uses the "Mario Kart" strat for Scrambled Succession, known as 無職マラソン in Japanese.

### English (Mario Kart)

{% include_relative macros/p9s_mariokart.en.md %}

### Japanese (Mario Kart)

{% include_relative macros/p9s_mariokart.jp.md %}

### Scrambled Succession (Mario Kart)

This is the strat chosen by Game8 that involves splitting the party into two groups- players with numbers, and players without numbers.

- Non-numbered players:
  - Start at the orb numbered 1.
  - Rotate to the next wall if you do not get a blue mark.
  - Rotate **backwards** when your Ice AoE resolves.
- Numbered players:
  - Start at the orb numbered 5 (directly opposite).
  - Rotate when AoEs resolve.

<table>
  <tr>
    <td width="50%">
      <p><b>1.</b> Numbers appear. Split up into your groups.</p>
      <ul>
        <li><b>No number:</b> Go to the orb numbered 1.</li>
        <li><b>Numbered:</b> Go to the orb numbered 5 (directly opposite), and
        stay on the floor's inner-most ring.</li>
      </ul>
      <p>Identify whether the orbs are increasing in a clockwise or
      anti-clockwise order.</p>
      <ul>
        <li>The player numbered 2 can preposition at the edge, 45-degrees ahead
        of the other even-numbered players.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_nukemaru_01.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>2.</b> The first blue mark appears on a random player that did not
      have a number.</p>
      <ul>
        <li><b>No number:</b>
          <ul>
            <li><b>If you were marked:</b> Move to the wall.</li>
            <li><b>If you were not marked:</b> Rotate 90 degrees to the next
            wall (move to the orb numbered 3).</li>
          </ul>
        </li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_nukemaru_02.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>3.</b> The boss will become untargetable, teleport behind the orb
      numbered 1, and kick it across the arena.</p>
      <p>When the orb hits the wall, it will explode in an AoE and leave behind
      a tower.</p>
      <ul>
        <li><b>6:</b> Enter the tower after the orb explodes.</li>
      </ul>
      <p>A second non-numbered player will get a blue mark.</p>
      <ul>
        <li><b>If you were marked:</b> Stay at the wall.</li>
        <li><b>If you were not marked:</b> Rotate 90 degrees to the next wall.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_nukemaru_03.jpg">
    </td>
  </tr>
  <tr>
    <td><p><b>4.</b> First round of AoEs resolve together:</p><ul><li>A giant Ice AoE on the player with the blue orb</li><li>A Fire AoE on the even-numbered player.</li><li>The tower left behind by the first orb.</li></ul><p>All players rotate 90 degrees.</p>
    <ul><li>The next numbered player (4) moves 45 degrees ahead of the party.</li><li>The player that had the giant AoE rotates 90 degrees in the <b>opposite</b> direction to join the even-numbered players.</li></ul></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_nukemaru_04.jpg"></td>
  </tr>
  <tr>
    <td><p><b>5.</b> The boss will teleport behind next orb (3), and kick it across the arena.</p><ul><li><b>8:</b> Enter the tower after the orb explodes.</li></ul><p>The next non-numbered player will get a blue mark.</p>
    <ul><li><b>If you were marked:</b> Stay at the wall.</li><li><b>If you were not marked:</b> Rotate 90 degrees to the next wall.</li></ul></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_nukemaru_05.jpg"></td>
  </tr>
  <tr>
    <td><p><b>6.</b> Second round of AoEs resolve together with the tower.</p><p>All players rotate 90 degrees.</p>
    <ul><li>The next numbered player (6) moves 45 degrees ahead of the party.</li><li>The player that had the giant AoE rotates 90 degrees in the <b>opposite</b> direction to join the even-numbered players.</li></ul></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_nukemaru_06.jpg"></td>
  </tr>
  <tr>
    <td><p><b>7.</b> The boss will teleport behind next orb (5), and kick it across the arena.</p><ul><li><b>2:</b> Enter the tower after the orb explodes.</li></ul><p>The remaining non-numbered player will get a blue mark.</p>
    <ul><li><b>Last non-numbered player:</b> Stay at the wall.</li></ul></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_nukemaru_07.jpg"></td>
  </tr>
  <tr>
    <td><p><b>8.</b> Third round of AoEs resolve together with the tower.</p><p>All players rotate 90 degrees.</p>
    <ul><li>The next numbered player (8) moves 45 degrees ahead of the party.</li><li>The player that had the giant AoE rotates 90 degrees in the <b>opposite</b> direction to join the even-numbered players.</li></ul></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_nukemaru_08.jpg"></td>
  </tr>
  <tr>
    <td><p><b>9.</b> The boss will teleport behind final orb (7), and kick it across the arena.</p><ul><li><b>4:</b> Enter the tower after the orb explodes.</li></ul></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_nukemaru_09.jpg"></td>
  </tr>
  <tr>
    <td><p><b>10.</b> Final round of AoEs resolve together with the tower.</p><p>Quickly heal up, and prepare for Two Minds.</p></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_nukemaru_10.jpg"></td>
  </tr>
</table>

## Nukemaru's strat + Intercardinal Limit Cut

This is the preferred strat by EN. It takes Nukemaru's strat, but replaces
*Scrambled Succession* (Limit Cut) with the Intercard strat, known as ぶたばら式 in
Japanese.

### English (Intercard)

{% include_relative macros/p9s_intercard.en.md %}

### Japanese (Intercard/ぶたばら式)

{% include_relative macros/p9s_intercard.jp.md %}

### Scrambled Succession (Intercard)

This is the strat more favoured in EN that involves resolving the Ice/Fire twice before swapping sides. Of note, the player numbered 6 needs to pay special attention as they can potentially cause a party wipe if they are slow to move.

(N.B: This is also confusingly called the "JP strat", even though JP DCs no longer do this.)

- Start between the orbs numbered 5 and 7.
- First two iterations:
  - Ice goes between the orbs numbered 1 and 3.
  - Fire (players 2 and 4) goes between the orbs numbered 5 and 7.
- Last two iterations (swap sides):
  - Ice goes between the orbs numbered 5 and 7.
  - Fire (players 6 and 8) goes between the orbs numbered 1 and 3.

<table>
  <tr>
    <td width="50%"><p><b>1.</b> Numbers appear. All players go between the orbs numbered 5 and 7.</p>
    <ul><li><b>2:</b> You can preposition at the outer edge behind the party.</li></ul></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_intercard_01.jpg"></td>
  </tr>
  <tr>
    <td><p><b>2.</b> The first blue mark appears on a random player that did not have a number.</p>
    <ul><li><b>If you were marked:</b> Move to the opposite edge (between the orbs numbered 1 and 3).</li></ul></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_intercard_02.jpg"></td>
  </tr>
  <tr>
    <td><p><b>3.</b> The boss will become untargetable, teleport behind the orb numbered 1, and kick it across the arena.</p><p>When the orb hits the wall, it will explode in an AoE and leave behind a tower.</p><ul><li><b>6:</b> Enter the tower after the orb explodes.</li></ul><p>A second non-numbered player will get a blue mark.</p></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_intercard_03.jpg"></td>
  </tr>
  <tr>
    <td><p><b>4.</b> First round of AoEs resolve together:</p><ul><li>A giant Ice AoE on the player with the blue orb</li><li>A Fire AoE on the even-numbered player.</li><li>The tower left behind by the first orb.</li></ul>
    <p>The next pair of players (the second marked player and the player numbered 4) takes over the previous two player's positions.</p></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_intercard_04.jpg"></td>
  </tr>
  <tr>
    <td><p><b>5.</b> The boss will teleport behind next orb (3), and kick it across the arena.</p><ul><li><b>8:</b> Enter the tower after the orb explodes.</li></ul><p>The next non-numbered player will get a blue mark.</p></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_intercard_05.jpg"></td>
  </tr>
  <tr>
    <td><p><b>6.</b> Second round of AoEs resolve together with the tower.</p><p><b>All players swap sides.</b></p>
    <ul><li><p>The next numbered player (6) moves to the opposite end of the arena (between where the orbs numbered 1 and 3 were).</p><p><b>Be quick. Sprint is recommended.</b></p></li><li>The third marked player goes to the edge where the party was standing (between the two remaining orbs).</li></ul></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_intercard_06.jpg"></td>
  </tr>
  <tr>
    <td><p><b>7.</b> The boss will teleport behind next orb (5), and kick it across the arena.</p><ul><li><b>2:</b> Enter the tower after the orb explodes.</li></ul><p>The remaining non-numbered player will get a blue mark.</p></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_intercard_07.jpg"></td>
  </tr>
  <tr>
    <td><p><b>8.</b> Third round of AoEs resolve together with the tower.</p>
    <p>The next pair of players (the fourth marked player and the player numbered 8) takes over the previous two player's positions.</p></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_intercard_08.jpg"></td>
  </tr>
  <tr>
    <td><p><b>9.</b> The boss will teleport behind final orb (7), and kick it across the arena.</p><ul><li><b>4:</b> Enter the tower after the orb explodes.</li></ul></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_intercard_09.jpg"></td>
  </tr>
  <tr>
    <td><p><b>10.</b> Final round of AoEs resolve together with the tower.</p><p>Quickly heal up, and prepare for Two Minds.</p></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/p9s/lc1_intercard_10.jpg"></td>
  </tr>
</table>

## Markers

The colours indicate the pairs positions (MT/D3 are on red, etc).

![]({{site.baseurl}}/images/6.0_endwalker/p9s/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"P9S",
  "MapID":937,
  "A":{"X":100.0,"Y":0.0,"Z":86.0,"ID":0,"Active":true},
  "B":{"X":114.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":114.0,"ID":2,"Active":true},
  "D":{"X":86.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":90.101,"Y":0.0,"Z":90.101,"ID":4,"Active":true},
  "Two":{"X":109.899,"Y":0.0,"Z":90.101,"ID":5,"Active":true},
  "Three":{"X":109.899,"Y":0.0,"Z":109.899,"ID":6,"Active":true},
  "Four":{"X":90.101,"Y":0.0,"Z":109.899,"ID":7,"Active":true}
}
```

</details>

You may see the square markers rotated 90 degrees clockwise in Japanese parties.

![]({{site.baseurl}}/images/6.0_endwalker/p9s/markers2.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"P9S (JP)",
  "MapID":937,
  "A":{"X":100.0,"Y":0.0,"Z":86.0,"ID":0,"Active":true},
  "B":{"X":114.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":114.0,"ID":2,"Active":true},
  "D":{"X":86.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":109.899,"Y":0.0,"Z":90.1,"ID":4,"Active":true},
  "Two":{"X":109.899,"Y":0.0,"Z":109.899,"ID":5,"Active":true},
  "Three":{"X":90.1,"Y":0.0,"Z":109.899,"ID":6,"Active":true},
  "Four":{"X":90.1,"Y":0.0,"Z":90.1,"ID":7,"Active":true}
}
```

</details>

## Timeline
![](https://preview.redd.it/0jw482dujc3b1.png?width=1813&format=png&auto=webp&v=enabled&s=7beaeeebfb30a297fbb243c5e00fa31c0a654327)
*(Credit: [u/ExiaKuromonji](https://www.reddit.com/r/ffxiv/comments/13vzzms/spoiler_64_p9s_timeline_and_abilities/))*

## Frequently Asked Questions

<details markdown=block>
<summary><b>[Damage Down]</b> How strong is the damage down debuff in this fight?</summary>
<table>
  <tr><td><p>The Damage Down debuff in this phase lowers a player's damage by <b>25%</b>.</p></td></tr>
</table>
</details>
<details markdown=block>
<summary><b>[Chimeric Succession (Limit Cut 2)]</b> Are the numbers baitable?</summary>
<table>
  <tr><td><p>The four numbered players are the four <b>furthest</b> people from the boss, with number 1 going to the furthest player, 2 goes to the second furthest, and so on.</p></td></tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
