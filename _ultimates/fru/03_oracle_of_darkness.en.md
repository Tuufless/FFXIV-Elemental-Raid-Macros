---
layout: default
title: 3. Oracle of Darkness (WIP)
parent: Lv 100. FRU (WIP)
nav_order: 3
has_children: false
has_toc: false
permalink: /ultimates/fru/03_oracle_of_darkness/
---

# Oracle of Darkness (WIP)

<div style="background-color: #200 ; padding: 10px; border: 1px solid;">
<p style="text-align:center"><b>Details may be missing, or subject to change
until I have better first-hand experience.</b></p>
</div>

- [**Ultimate Relativity - Atobe**](#ultimate-relativity---atobe) _or_ [**Ultimate Relativity - Awk**](#ultimate-relativity---awk)
- [**Apocalypse**](#apocalypse)

The Oracle of Darkness starts south, and immediately opens with *Hell's Judgment*, which sets everyone to 1HP.

She will then teleport to the middle of the arena and prepare her first
major mechanic with a heavy raid-wide.

## Ultimate Relativity

When *Ultimate Relativity* resolves, there will be a lot of debuffs that go 
out. However, you only need to check a limited set of debuffs.

Six of the eight sets of debuffs have fixed assignments:

- Two DPS will get 10s Fire debuffs (the "short Fires").
- One tank/healer and one DPS will get 20s Fire debuffs (the "mid Fires"). 
  - The tank/healer have a 42s *Dark Eruption* debuff.
  - The DPS will also have a 42s *Dark Water III* debuff.
- Two tanks/healers will get 30s Fire debuffs (the "long Fires").

This leaves the last tank/healer and the last DPS. One of them will get a *Dark Blizzard III* debuff, and the other will get a *Dark Fire III* debuff.

- **If the Blizzard is on a DPS:** This will be a "slow Blizzard". The tank/
  healer will get a 10s Fire debuff and join the "short Fire" group.
- **If the Blizzard is on a tank/healer:** This will be a "fast Blizzard". The 
  DPS will get a 30s Fire debuff and join the "long Fire group.

The first step is to assign hourglasses to players. The basic rules are:

- **Short fires** go to **empty** spots.
- **Mid fires** go to the **purple** tethered spots.
- **Long fires** go to the **yellow** tethered spots.

After that, it's just a matter of how to assign players to hourglasses.

### Ultimate Relativity - Atobe

This is the <a href="https://twitter.com/PoneKoni/status/1862335851671560669">"Atobe" strat</a> that Nukemaru's group uses that uses a **tethers-relative** assignment.

<table>
  <tr>
    <td>
      <p><b>1.</b> Find the lone yellow tether- this will be "North" for the 
      duration of this mechanic.</p>
      <p>Take up assigned clock positions based on your Fire group:</p>
      <ul>
        <li>For the DPS short Fires, use the following priority:
          <ul>
            <li><b>NW: </b> D1 > D2 > D3 > D4 <b>:NE</b></li>
          </ul>
        </li>
        <li>For the tank/healer long Fires, use the following priority:
          <ul>
            <li><b>SW: </b> MT > ST > H1 > H2 <b>:SE</b></li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/ultimate_relativity_01.jpg">
    </td>
  </tr>
</table>

### Ultimate Relativity - Awk

This is a minor modification of the strategy that MrHappy's group used, which uses a **map-relative** assignment. We tweak it slightly to mirror *Second Sunrise* in M4S.

<table>
  <tr>
    <td>
      <p><b>1.</b> Face the map's North, and find the first hourglass for your 
      group:</p>
      <ul>
        <li><b>Tanks/Healers:</b> Start from NW, go anti-clockwise.</li>
        <li>Long fires follow the priority:
          <ul>
            <li><b>NW (going ccw): </b> MT > ST > H1 > H2 <b>:N</b></li>
          </ul>
        </li>
        <li><b>DPS:</b> Start from N, go clockwise.</li>
        <li>Short fires follow the priority:
          <ul>
            <li><b>N (going cw): </b> D1 > D2 > D3 > D4 <b>:NW</b></li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/ultimate_relativity_awk_01.jpg">
    </td>
  </tr>
</table>

Once everyone has their assigned hourglass, we can resolve the debuffs.

Each player should only need to move in a straight line from the center of the 
arena, through their assigned hourglass to the edge to resolve their debuffs.

<table>
  <tr>
    <td width="50%">
      <p><b>2.</b> First set of <em>Dark Fire III</em> and <em>Unholy 
      Darkness</em> resolve.</p>
      <ul>
        <li><b>Short Fire:</b> Go outside to resolve <em>Dark Fire III</em>.
          <ul>
            <li><b>T/H Ice:</b> Stack in the middle for <em>Unholy Darkness</em>.</li>
          </ul>
        </li>
        <li><b>Mid Fire:</b> Stack in the middle for <em>Unholy Darkness</em>.</li>
        <li><b>Long Fire:</b> Stack in the middle for <em>Unholy Darkness</em>.</li>
      </ul>
      <p><em>(This example illustrates the "slow Blizzard" case where a DPS has
      <em>Dark Blizzard III</em>.)</em></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/ultimate_relativity_02.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>3.</b> First set of records and laser baits.</p>
      <ul>
        <li><b>Short Fire:</b> Stay outside and record your position (for <em>Dark Eruption</em>).</li>
        <li><b>Mid Fire:</b> Record your position based on your debuff:
          <ul>
            <li><b>Tank/Healer:</b> Outside.</li>
            <li><b>DPS:</b> Inside (a little away from the center).</li>
          </ul>
        </li>
        <li><b>Long Fire:</b> Bait your hourglass's laser.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/ultimate_relativity_03.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>4.</b> Second set of <em>Dark Fire III</em> and <em>Unholy 
      Darkness</em> resolve. The <em>Dark Blizzard III</em> also resolves here.</p>
      <ul>
        <li><b>Short Fire:</b> Stack in the middle for <em>Unholy Darkness</em>.</li>
        <li><b>Mid Fire:</b> Go outside to resolve <em>Dark Fire III</em>.</li>
        <li><b>Long Fire:</b> Stack in the middle for <em>Unholy Darkness</em>.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/ultimate_relativity_04.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>5.</b> Second set of records and laser baits.</p>
      <ul>
        <li><b>Short Fire:</b> Bait your hourglass's laser.</li>
        <li><b>Mid Fire:</b> Move inside.</li>
        <li><b>Long Fire:</b> Stay inside and record your position (for <em>Shadoweye</em>).</li>
      </ul>
      <p>Record your position in your assigned clock spot position, <b>a 
      little away from the center</b>.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/ultimate_relativity_05.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>6.</b> Third set of <em>Dark Fire III</em> and <em>Unholy 
      Darkness</em> resolve.</p>
      <ul>
        <li><b>Short Fire:</b> Stack in the middle for <em>Unholy Darkness</em>.</li>
        <li><b>Mid Fire:</b> Stack in the middle for <em>Unholy Darkness</em>.</li>
        <li><b>Long Fire:</b> Go outside to resolve <em>Dark Fire III</em>.
          <ul>
            <li><b>DPS Ice:</b> Stack in the middle for <em>Unholy Darkness</em>.</li>
          </ul>
        </li>
      </ul>
      <p><em>(This example illustrates the "fast Blizzard" case where a T/H has
      <em>Dark Blizzard III</em>.)</em></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/ultimate_relativity_06.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>7.</b> Third set of laser baits (there are no recordings).</p>
      <ul>
        <li><b>Short Fire:</b> Stay inside.</li>
        <li><b>Mid Fire:</b> Bait your hourglass's laser.</li>
        <li><b>Long Fire:</b> Move inside.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/ultimate_relativity_07.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>8.</b> The <em>Rewind</em> will trigger just before the 42s 
      debuffs resolve.</p>
      <p>Note that your characters positions were recorded earlier, but 
      <em>not</em> your orientation.</p>
      <p>Your character's orientation just before the <em>Rewind</em> will be 
      locked throughout the <em>Rewind</em>.</p>
      <p>As a result, <b>face your character towards the outside of the
      arena</b> just before the <em>Rewind</em> resolves. <em>(i.e: if you are 
      at the NW position, face your character north-west.)</em></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/ultimate_relativity_08.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>9.</b> The <em>Rewinds</em> resolve, taking back your characters 
      to their recorded positions, which should be along their assigned clock 
      positions.</p>
      <ul>
        <li>All the players with <em>Dark Eruption</em> (the short Fires and
        the tank/healer mid Fire) should have recorded their positions on the 
        outside.</li>
        <li>The player with <em>Dark Water III</em> (the DPS mid Fire) 
        should have recorded their position on the inside.</li>
        <li>All the players with <em>Shadoweye</em> (the long Fires) should 
        have recorded their positions on the inside.</li>
      </ul>
      <p>Done correctly, the <em>Dark Eruptions</em> should not hit anyone 
      else, the <em>Shadoweye</em> players share the <em>Dark Water III</em> 
      stack, and all players are facing outside to not get gazed by the 
      <em>Shadoweye</em> attack.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/ultimate_relativity_09.jpg">
    </td>
  </tr>
</table>

After you gain control of your characters, stack up in the middle to share a 
*Shell Crusher* AoE. The hourglasses will disappear, and the boss casts a 
raid-wide *Shockwave Pulsar*. The boss will then target the first player in 
aggro with *Black Halo*, a two-player tankbuster cleave.

## Apocalypse

The boss will be targetable for the duration of this mechanic.

Before the cast, the Oracle of Darkness first casts *Spell-in-Waiting Refrain* 
which puts three pairs of *Dark Water III* on six different players to be 
resolved during *Apocalypse*.

This effectively creates four pairs of players (including the two players who
did not get any *Water III*).

We need to sort out the party into two groups of four, such that each group has
one of each debuff (nothing, 10s, 29s, 38s).

<table>
  <tr>
    <td width="50%">
      <p><b>10.</b> Group up with tanks/healers on the West, and DPS on the East.</p>
      <p>When <em>Water III</em> debuffs come out, look within your group for
      duplicates (nothing, 10s, 29s, 38s).</p>
      <ul>
        <li><b>If there are duplicates within a group:</b> The player with the
        higher priority swaps to the other group:
          <ul>
            <li><b>Swap:</b> MT > ST > H1 > H2 <b>:Stay</b></li>
            <li><b>Swap:</b> D1 > D2 > D3 > D4 <b>:Stay</b></li>
          </ul>
        </li>
      </ul>
      <p><em>(In this example, H1 + H2 have the 10s Water, and D1 + D2 have no
      debuff, so H1 and D1 will switch sides.)</em></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_01.jpg">
    </td>
  </tr>
</table>

**UNDER CONSTRUCTION**

The boss casts *Memory's End* as the enrage, and must be brought down to under 
20.0% HP to survive the cast.
