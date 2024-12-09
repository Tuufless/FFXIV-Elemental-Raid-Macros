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
<p>I'm also waiting for greater consensus on Apocalypse, so this phase will
stay WIP for another week.</p>
</div>

- **Ultimate Relativity**
  - [**Y Runytivity**](#ultimate-relativity---y-runytivity)
  - [**Awk**](#ultimate-relativity---awk)
- **Apocalypse:**
  - [**Permaswap**](#apocalypse---permaswap) _or_
  - [**Static Spreads**](#apocalypse---static-spreads)

The Oracle of Darkness starts south, and immediately opens with *Hell's
Judgment*, which sets everyone to 1HP.

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

This leaves the last tank/healer and the last DPS. One of them will get a *Dark
Blizzard III* debuff, and the other will get a *Dark Fire III* debuff.

- **If the Blizzard is on a DPS:** This will be a "slow Blizzard". The tank/
  healer will get a 10s Fire debuff and join the "short Fire" group.
- **If the Blizzard is on a tank/healer:** This will be a "fast Blizzard". The 
  DPS will get a 30s Fire debuff and join the "long Fire group.

The first step is to assign hourglasses to players. The basic rules are:

- **Short fires** go to **empty** spots.
- **Mid fires** go to the **purple** tethered spots.
- **Long fires** go to the **yellow** tethered spots.

### Ultimate Relativity - Y Runytivity

This is a *tethers-relative* assigment, with a slightly modified priority to
better match the datacenter's conventions.

<table>
  <tr>
    <td>
      <p>The yellow tethers make a "Y-shape". Find the "Y" and orient to it.</p>
      <p>Take up assigned clock positions based on your Fire group:</p>
      <ul>
        <li>For the DPS short Fires, use the following priority:
          <ul>
            <li><b>SW: </b> D1 > D2 > D3 > D4 <b>:E</b></li>
          </ul>
        </li>  
        <li>For the tank/healer long Fires, use the following priority:
          <ul>
            <li><b>W: </b> MT > ST > H1 > H2 <b>:NE</b></li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/ultimate_relativity_Y_01.jpg">
    </td>
  </tr>
</table>

### Ultimate Relativity - Awk

This is my preferred method, and is a **map-relative** assignment.

<table>
  <tr>
    <td>
      <p>Face the map's North, and find the first hourglass for your 
      group:</p>
      <ul>
        <li><b>Tanks/Healers:</b> Start from N, go anti-clockwise.</li>
        <li>Long fires follow the priority:
          <ul>
            <li><b>N (going ccw): </b> H2 > H1 > ST > MT <b>:NE</b></li>
          </ul>
        </li>
        <li><b>DPS:</b> Start from NE, go clockwise.</li>
        <li>Short fires follow the priority:
          <ul>
            <li><b>NE (going cw): </b> D4 > D3 > D2 > D1 <b>:N</b></li>
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

The good news is that once you have your assigned hourglass, you can basically
read off where you're supposed to go next from your debuffs. Every 5 seconds,
*something* happens.

- If it's your turn to resolve *Dark Fire III*, do so outside.
- If your hourglass starts spinning, go bait the laser beam.
- If it's your turn to record, do so just a little off from the center, unless 
  you are one of the short Fires or the mid Fire tank/healer, in which case 
  record *just* behind your hourglass.

Essentially, each player only needs to move in a straight line from the center 
of the arena, through their assigned hourglass to the edge to resolve their 
debuffs.

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
        <li><b>Short Fire:</b> Stay outside and record your position (for
        <em>Dark Eruption</em>).</li>
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
        <li><b>Long Fire:</b> Stay inside and record your position (for
        <em>Shadoweye</em>).</li>
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

This may necessitate one or two pairs swap around (depending on the number of 
duplicates).

After that, there is one main decision to make:

- Whether you want the Water III adjustments will be permanent **(Permaswap)**,
  *or*
- Whether you want the spreads and Apocalypse dodges to be consistent **(Static
  spreads)**.

<div style="background-color: #200 ; padding: 10px; border: 1px solid;">
<p style="text-align:center"><b>Note:</b> The diagrams below illustrate
assigning sectors based on the "First-Apoc", instead of the safespots although 
this detail is still up in the air.</p>
</div>

## Apocalypse - Permaswap

This variant makes the party adjust just once at the start of the mechanic, and
keeps the groups that way until the end.

However, *in exchange*, all players (other than H2 and D4) will need to be 
comfortable with dodging the Apocalypse AoEs from different positions. There is 
also a chance of melee downtime (although this can be mitigated by giving it to
a tank).

<table>
  <tr>
    <td width="50%">
      <p><b>10.</b> Group up with tanks/healers West, and DPS East, and
      <b>form a box</b>.</p>
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
      debuff, so H1 and D1 will be swapping sides.)</em></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_01.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>11.</b> The Oracle of Darkness will cast <em>Apocalypse</em>,
      which changes the arena slightly.</p>
      <p>Three points on the arena; one center and two opposite cardinal/
      intercardinals will pulse white. This is a telegraph for where the later 
      AoEs will appear.</p>
      <p>A white streak also originates from each point and follows the line
      around the arena clockwise or anti-clockwise.</p>
      <p>Each group references the two starting points in their half of the
      arena:</p>
      <ul>
        <li><b>SW to N:</b> North group.</li>
        <li><b>S to NE:</b> South group.</li>
      </ul>
      <p><b>Also note which direction the streaks are going.</b></p>
      <p>The first pair of <em>Dark Water III</em> stacks also resolve.</p>
      <p><em>(In this example, the reference points are North and South, and
      the streaks are travelling anti-clockwise.)</em></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_02.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>12.</b> While the water stacks were resolving, the boss also 
      readies <em>Spirit Taker</em>- the boss will jump on a random target
      with an AoE attack that knocks anyone else hit out of the arena.</p>
      <p>After the water stacks resolve, quickly spread out for <em>Spirit 
      Taker</em> in the earlier box formation.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_perma_03.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>13.</b> The boss's <em>Spirit Taker</em> resolves.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_perma_04.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>14.</b> The boss will return to the center.</p>
      <p>The trails will continue for a total of six pulses (indicating six 
      upcoming sets of AoEs) and end up in this formation relative to the 
      first set of pulses.</p>
      <p>All party members will get a spread marker. Just like before, spread
      out in your previous box formation.</p>
      <div style="background-color: #200 ; padding: 10px; border: 1px solid;">
      <b>Note:</b> The spread formation here illustrates associating markers
      with <em>the initial lights</em>.
      </div>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_perma_05.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>15.</b> The AoEs now resolve for real.</p>
      <p>The AoEs will appear at the points that pulsed earlier for a total
      of six waves.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_perma_06.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>16.</b> The second set of AoEs resolve together with the party's 
      spread markers.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_perma_07.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>17.</b> Quickly move to the center while avoiding the third set of 
      AoEs.</p>
      <p>Note that the players on the outside have a narrow safe path that
      leads in to the middle.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_perma_08.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>18.</b> Fourth set of AoEs.</p>
      <p>Use this time to gauge how far you can be from the center and still
      avoid getting hit.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_09.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>19.</b> The second set of <em>Dark Water III</em> stacks resolve
      together with the fifth set of AoEs.</p>
      <p>The player with aggro moves out 90 degrees from where the first set of 
      lights pulsed.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_10.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>20.</b> The boss then uses <em>Darkest Dance</em>, which targets
      the furthest player (which should be the tank with aggro) with an AoE 
      tankbuster.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_11.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>21.</b> The MT rejoins their group.</p>
      <p>Everyone positions to prepare from a knockback from the boss.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_12.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>22.</b> The boss does a knockback.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_13.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>23.</b> The third set of <em>Dark Water III</em> stacks resolve.</p>
      <p>Resolve these near the boss- melee can use their gap closers, but will
      need to back out a little bit to meet up with the healers and ranged.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_14.jpg">
    </td>
  </tr>
</table>

## Apocalypse - Static spreads

Players who swap will need to do so **a total of three times 
during this mechanic**.

<table>
  <tr>
    <td width="50%">
      <p><b>10.</b> Group up with tanks/healers West, and DPS East.</p>
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
      debuff, so H1 and D1 will be swapping sides.)</em></p>
      <p><b>This is the first swap (of three).</b></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_01.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>11.</b> The Oracle of Darkness will cast <em>Apocalypse</em>,
      which changes the arena slightly.</p>
      <p>Three points on the arena; one center and two opposite cardinal/
      intercardinals will pulse white. This is a telegraph for where the later 
      AoEs will appear.</p>
      <p>A white streak also originates from each point and follows the line
      around the arena clockwise or anti-clockwise.</p>
      <p>Each group references the two starting points in their half of the
      arena:</p>
      <ul>
        <li><b>SW to N:</b> North group.</li>
        <li><b>S to NE:</b> South group.</li>
      </ul>
      <p><b>Also note which direction the streaks are going.</b></p>
      <p>The first pair of <em>Dark Water III</em> stacks also resolve.</p>
      <p><em>(In this example, the reference points are North and South, and
      the streaks are travelling anti-clockwise.)</em></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_02.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>12.</b> While the water stacks were resolving, the boss also 
      readies <em>Spirit Taker</em>- the boss will jump on a random target
      with an AoE attack that knocks anyone else hit out of the arena.</p>
      <p>After the water stacks resolve, quickly spread out for <em>Spirit 
      Taker</em>.</p>
      <ul>
        <li><b>Tanks/Melee:</b> Towards the boss (MT/D1 on the left, facing
        in).</li>
        <li><b>Healers/Ranged:</b> Towards the edge (H1/D3 on the left, facing
        in).</li>
      </ul>
      <p>Players who swapped earlier can use this time to swap back to their
      original groups.</p>
      <p><b>This is the second swap (of three).</b></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_03.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>13.</b> The boss's <em>Spirit Taker</em> resolves.</p>
      <p>Players who need to swap back can now rejoin their original groups.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_04.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>14.</b> The boss will return to the center.</p>
      <p>The trails will continue for a total of six pulses (indicating six 
      upcoming sets of AoEs) and end up in this formation relative to the 
      first set of pulses.</p>
      <p>All party members will get a spread marker.</p>
      <p>Players who needed to swap back should have returned to their 
      original groups by this point.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_05.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>15.</b> The AoEs now resolve for real.</p>
      <p>The AoEs will appear at the points that pulsed earlier for a total
      of six waves.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_06.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>16.</b> The second set of AoEs resolve together with the party's 
      spread markers.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_07.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>17.</b> Quickly move to the center while avoiding the third set of 
      AoEs.</p>
      <p>Note that the players on the outside have a narrow safe path that
      leads in to the middle.</p>
      <p>Players who need to swap do so again.</p>
      <p><b>This is the third (and last) swap.</b></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_08.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>18.</b> Fourth set of AoEs.</p>
      <p>Use this time to gauge how far you can be from the center and still
      avoid getting hit.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_09.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>19.</b> The second set of <em>Dark Water III</em> stacks resolve
      together with the fifth set of AoEs.</p>
      <p>The player with aggro moves out 90 degrees from where the first set of 
      lights pulsed.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_10.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>20.</b> The boss then uses <em>Darkest Dance</em>, which targets
      the furthest player (which should be the tank with aggro) with an AoE 
      tankbuster.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_11.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>21.</b> The MT rejoins their group.</p>
      <p>Everyone positions to prepare from a knockback from the boss.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_12.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>22.</b> The boss does a knockback.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_13.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>23.</b> The third set of <em>Dark Water III</em> stacks resolve.</p>
      <p>Resolve these near the boss- melee can use their gap closers, but will
      need to back out a little bit to meet up with the healers and ranged.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru/03/apocalypse_14.jpg">
    </td>
  </tr>
</table>

The boss ends this sequence with another *Shockwave Pulsar* before casting 
*Memory's End* for the enrage. Like the previous phase, the Oracle of Darkness
must be brought down to under 20.0% HP to advance.

---

## Frequently Asked Questions

<details markdown=block>
<summary>
  <b>[Debuffs]</b> What is the difference between <em>Dark Water III</em> and
  <em>Unholy Darkness</em>? Aren't they both stacks?
</summary>
<table>
  <tr>
    <td>
      <p><em>Dark Water III</em> and <em>Unholy Darkness</em> are both stacks
      with one crucial difference:</p>
      <ul>
        <li><em>Dark Water III</em> needs at least <b>four</b> people in the
        stack to avoid the <em>Mark of Mortality</em> debuff.</li>
        <li><em>Unholy Darkness</em> needs at least <b>five</b> people in the
        stack to avoid the <em>Mark of Mortality</em> debuff.</li>
      </ul>
    </td>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru/03/dark_water.png">
      <img src="{{site.baseurl}}/images/ultimates/fru/03/unholy_darkness.png">
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Ultimate Relativity (Awk)]</b> Why do the priorities go backwards from
  North?
</summary>
<table>
  <tr>
    <td>
      <p>The boss is facing North throughout <em>Ultimate Relativity</em>.</p>
      <p>With that in mind, having the priority "backwards" gives:</p>
      <ul>
        <li>The healers the easiest positions to figure out.</li>
        <li>Melee the highest chance of getting positionals.</li>
      </ul>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Apocalypse]</b> Are these cases where more than one pair needs to swap?
</summary>
<table>
  <tr>
    <td>
      <p>Yes. It's rare (3/35 chance), but certainly possible.</p>
      <p>Consider the following example:</p>
      <ul>
        <li>Nothing: MT + ST</li>
        <li>Short Water: H1 + H2</li>
        <li>Mid Water: D1 + D3</li>
        <li>Long Water: D2 + D4</li>
      </ul>
      <p>The T/H and DPS groups each have two duplicate debuffs, so we will 
      have four players swapping groups (MT, H1, D1, D2).</p>
      <p>Most of the time, one pair will need to swap (24/35 chance). The 
      probability that <em>nobody</em> has to swap is 8/35.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Apocalypse (static spreads)]</b> Why do we have to swap three times?
</summary>
<table>
  <tr>
    <td>
      <p>Because the <em>Water III</em> debuffs are randomly distributed, we
      need a way to ensure that there are four players in each stack every 
      time they resolve.</p>
      <p>You <em>could</em> do a one-time adjustment at the very start, and use
      those groups throughout- however, the problem is that it's now not clear
      how each group should spread for <em>Spirit Taker</em>, or for <em>Dark 
      Eruption</em>.</p>
      <p>Permanently swapping this way means that not only do you need to 
      determine whether you are swapping, but also <em>who</em> you are 
      swapping with so you can take their spot when it comes time to spread 
      out.</p>
      <p>Even then, there are awkward scenarios to consider:</p>
      <ul>
        <li>What happens if a melee swaps with a healer and now the T/H group 
        has three melee? Should a tank go to the back? Which tank?</li>
        <li>What happens if two players from each group have to swap? Who 
        switches place with who?</li>
      </ul>
      <p>Arguably just as important, keeping to static positions for <em>Dark
      Eruption</em> also means that <b>every player's dodge for the
      <em>Apocalypse</em> AoEs stays consistent from run to run.</b></p>
      <p>As a result, we swap once to resolve the first Water, swap back to 
      spread out, then swap again to resolve the second Water. There are no 
      more spread mechanics after the second Water, so we can keep the groups 
      as they are to resolve the third Water.</p>
    </td>
  </tr>
</table>
</details>

---

## Troubleshooting

<details markdown=block>
<summary>
  <b>[Hell's Judgment]</b> Isn't this supposed to set your HP to 1? How did I
  die?
</summary>
<table>
  <tr>
    <td>
      <p>You had an effect that increased your maximum HP that wore off.</p>
      <p>Examples include:</p>
      <ul>
        <li><em>Food buffs</em></li>
        <li><em>Greater Nebula</em> (GNB)</li>
        <li><em>Protraction</em> (SCH)</li>
        <li><em>Thrill of Battle</em> (WAR)</li>
      </ul>
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
