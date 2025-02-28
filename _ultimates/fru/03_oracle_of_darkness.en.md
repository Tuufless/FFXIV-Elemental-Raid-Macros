---
layout: default
title: 3. Oracle of Darkness
parent: Lv 100. FRU (Mana)
nav_order: 3
has_children: false
has_toc: false
permalink: /ultimates/fru/03_oracle_of_darkness/
---

# Oracle of Darkness（闇の巫女）

The Oracle of Darkness starts south, and immediately opens with *Hell's
Judgment*, which sets everyone to 1HP.

She will then teleport to the middle of the arena and prepare her first
major mechanic with a heavy raid-wide.

## Ultimate Relativity（時間圧縮・絶）- Poni Kone

When *Ultimate Relativity* resolves, there will be a lot of debuffs that go 
out. However, you only need to check a limited set of debuffs.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Ultimate Relativity debuffs</b></summary>
<p>The following debuffs all resolve before <em>Return</em> resolves.</p>
<table>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/dark_blizzard.png">
    </td>
    <td>
      <p><b>Spell-in-Waiting: Dark Blizzard III</b></p>
      <p>One player will get this debuff, and it will always be 20s.</p>
      <ul>
        <li>When the timer expires, a donut AoE centered on the player resolves.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/dark_fire.png">
    </td>
    <td>
      <p><b>Spell-in-Waiting: Dark Fire III</b></p>
      <p>Seven players will get this debuff, but with different durations.</p>
      <ul>
        <li>Two DPS and one tank/healer will have a 10s duration (the "short
        Fires")</li>
        <li>One tank/healer and one DPS will have a 20s duration (the "mid 
        Fires")</li>
        <li>Two tank/healers and one DPS will have a 30s duration (the "long
        Fires")</li>
        <li>When the timer expires, a point-blank AoE centered on the player
        resolves (8 yalm radius).</li>
      </ul>
      <p>However, either the 10s tank/healer <em>Dark Fire III</em> or the 30s
      DPS <em>Dark Fire III</em> will be replaced with a 20s <em>Dark Blizzard
      III</em> instead.</p>
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/unholy_darkness.png">
    </td>
    <td>
      <p><b>Spell-in-Waiting: Unholy Darkness</b></p>
      <p>Three players will get this debuff, at 10s, 20s, and 30s.</p>
      <ul>
        <li>When the timer expires, a stack AoE centered on the player resolves
        (6 yalm radius).</li>
        <li>If there are less than <b>five</b> players in the stack, the
        players in the stack each get a stack of <em>Mark of Mortality</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/spell_in_waiting_return.png">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/return.png">
    </td>
    <td>
      <p><b>Spell-in-Waiting: Return</b></p>
      <p>All players will get this debuff, but with different durations.</p>
      <ul>
        <li>When the debuff resolves, the player's current position is recorded, and this debuff turns into <em>Return</em></li>
      </ul>
      <p><b>Return</b></p>
      <p><em>Spell-in-Waiting: Return</em> turns into this debuff when it 
      expires. The total duration of <em>Spell-in-Waiting: Return</em> and 
      <em>Return</em> add up to 39s (so will resolve just before the 42s 
      debuffs resolve.)</p>
      <ul>
        <li>When the debuff resolves, the player is stunned, and brought back
        to their previously recorded position.</li>
        <li>Although the player position is recorded, the player 
        <em>orientation</em> is not- the direction you face before 
        <em>Return</em> resolves stays constant throughout.</li>
      </ul>
    </td>
  </tr>
</table>
<p>The following debuffs all resolve <em>after Return</em>, so will determine 
where players record their positions.</p>
<table>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/dark_eruption.png">
    </td>
    <td>
      <p><b>Spell-in-Waiting: Dark Eruption</b></p>
      <p>3-4 players will get this debuff, and it will always be 42s (resolves 
      after <em>Return</em>).</p>
      <ul>
        <li>When the timer expires, a point-blank AoE centered on the player
        resolves (6 yalm radius).</li>
        <li>All short Fire players will get this debuff, and <em>possibly</em>
        the mid Fire tank/healer.</li>
        <li>Players with this debuff need to record their positions just
        behind their assigned hourglass (towards the center of the arena).</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/dark_water.png">
    </td>
    <td>
      <p><b>Spell-in-Waiting: Dark Water III</b></p>
      <p>The DPS mid Fire will get this debuff, and it will always be 42s 
      (resolves after <em>Return</em>).</p>
      <ul>
        <li>When the timer expires, a stack AoE centered on the player resolves
        (6 yalm radius).</li>
        <li>If there are less than <b>four</b> players in the stack, the
        players in the stack each get a stack of <em>Mark of Mortality</em>.</li>
        <li>The player with this debuff records their position just a little
        off the center of the arena (one step towards their assigned
        hourglass).</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/shadoweye.png">
    </td>
    <td>
      <p><b>Spell-in-Waiting: Shadoweye</b></p>
      <p>3-4 players will get this debuff, and it will always be 42s (resolves 
      after <em>Return</em>).</p>
      <ul>
        <li>When the timer expires, anyone looking at the affected player gets
        a <em>Doom</em> debuff, which will kill them after a few seconds.</li>
        <li>All long Fire players will get this debuff, and <em>possibly</em>
        the mid Fire tank/healer.</li>
        <li>Players with this debuff records their position just a little off
        the center of the arena (one step towards their assigned hourglass).</li>
      </ul>
    </td>
  </tr>
</table>

</details>
</div>

The party can be split up into three groups based off the duration of each 
player's *Dark Fire III* debuff.

- Three players (two DPS and one tank/healer) will get 10s Fire debuffs (the "short Fires").
- Two players (one tank/healer and one DPS) will get 20s Fire debuffs (the "mid Fires"). 
- Three players (two tanks/healers and one DPS) will get 30s Fire debuffs (the "long Fires").

Either the tank/healer short Fire, or the DPS long Fire will have their *Dark 
Fire III* debuff replaced with *Dark Blizzard III*.

The first step is to assign hourglasses to players. The basic rules are:

- **Short fires** go to **empty** spots.
- **Mid fires** go to the **purple** tethered spots.
- **Long fires** go to the **yellow** tethered spots.

This is a *tethers-relative* assigment.

Each player is expected to carry a set of macros that do two things:

- Mark themselves with the appropriate marker based on whether you're short,
  mid, or long Fire.
- Dump the sequence of mechanics (in order) in `/echo` chat.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Ultimate Relativity macros</b></summary>
<p>Tank/Healer short Fire/Blizzard:</p>
```
/micon attack3 marking
/mk attack3 <me>
/echo >---- T/H Short Fire/Blizzard: South ---- <
/echo Out for Fire (mid if Blizzard)
/echo Record at hourglass
/echo Stack (Blizzard)
/echo Bait laser
/echo Stack
/echo Face outside
/echo >----------------------<
```
<p>Tank/Healer Mid Fire:</p>
```
/micon ignore1 marking
/mk ignore1 <me>
/echo >---- T/H Mid Fire: West ---- <
/echo Stack
/echo Record at hourglass
/echo Out for Fire
/echo Wait in Mid
/echo Stack
/echo Bait laser → Dodge + face out
/echo >----------------------<
```
<p>Tank/Healer Long Fire:</p>
```
/micon bind1 marking
/mk bind <me>
/echo >---- T/H Long Fire: SW/SE ---- <
/echo Stack
/echo Bait laser
/echo Stack
/echo Record position
/echo Out for Fire
/echo Mid + face outside
/echo >----------------------<
```
<p>DPS short Fire:</p>
```
/micon attack1 marking
/mk attack <me>
/echo >---- DPS Fast Fire: NW/NE ---- <
/echo Out for Fire
/echo Record at hourglass
/echo Stack
/echo Bait laser
/echo Stack
/echo Mid + face outside
/echo >----------------------<
```
<p>DPS mid Fire:</p>
```
/micon stop2 marking
/mk stop2 <me>
/echo >---- DPS Mid Fire: East ---- <
/echo Stack
/echo Record at mid
/echo Out for Fire
/echo Wait
/echo Stack
/echo Bait laser → Dodge + face out
/echo >----------------------<
```
<p>DPS Long Fire:</p>
```
/micon bind3 marking
/mk bind3 <me>
/echo >---- DPS Long Fire/Blizzard: South ---- <
/echo Stack
/echo Bait laser
/echo Stack (Blizzard)
/echo Record at mid
/echo Out for Fire
/echo Mid + face outside
/echo >----------------------<
```
</details>
</div>

<table>
  <tr>
    <td>
      <p>The tethers make a shape like the kanji character 大, with a single
      yellow tether pointing upwards. Find the 大 and orient to it with the
      single yellow tether as North.</p>
      <p>Take up assigned clock positions based on your Fire group.</p>
    </td>
  </tr>
  <tr>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/ultimate_relativity_01.jpg">
    </td>
  </tr>
</table>

Once you have your assigned hourglass, you can resolve everything by staying 
in the center, only moving out to resolve specific debuffs.

- When it's your turn to resolve *Dark Fire III*, do so outside.
- When it's your turn to record:
  - Short and Mid Fires do so *just* behind their hourglass.
  - Long Fires do so in the center, *just* towards their hourglass.
- When your hourglass starts spinning, go bait the laser beam.

<table>
  <tr>
    <td width="50%">
      <p>A good trick to use when baiting your hourglass's laser is to position 
      yourself such that the hourglass frame covers the black dot in the center 
      of the "Spell-in-Waiting" icon above your character (when your camera
      faces towards the outside).</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/hourglass_bait.jpg">
    </td>
  </tr>
</table>

You can either refer to the macros above that dump the order of events in
`/echo` chat, or just read off what you're supposed to do next from the next
debuff that's expiring. Every 5 seconds, *something* happens (stack in mid if
you don't have a debuff that's about to resolve, and your hourglass isn't
spinnning).

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
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/ultimate_relativity_02.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>3.</b> First set of records and laser baits <em>(Sinbound
      Meltdown)</em>.</p>
      <ul>
        <li><b>Short Fire:</b> Record your position just behind your hourglass
        (for <em>Dark Eruption</em>).</li>
        <li><b>Mid Fire:</b> Record your position depending on your role:
          <ul>
            <li><b>Tank/Healer:</b> Just behind your hourglass.</li>
            <li><b>DPS:</b> Center (a little towards your hourglass).</li>
          </ul>
        </li>
        <li><b>Long Fire:</b> Bait your hourglass's laser.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/ultimate_relativity_03.jpg">
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
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/ultimate_relativity_04.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>5.</b> Second set of records and laser baits.</p>
      <ul>
        <li><b>Short Fire:</b> Bait your hourglass's laser.</li>
        <li><b>Mid Fire:</b> Move inside.</li>
        <li><b>Long Fire:</b> Center (a little towards your hourglass for 
        <em>Shadoweye</em>).</li>
      </ul>
      <p>Record your position in your assigned clock spot position, <b>a 
      little away from the center</b>.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/ultimate_relativity_05.jpg">
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
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/ultimate_relativity_06.jpg">
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
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/ultimate_relativity_07.jpg">
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
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/ultimate_relativity_08.jpg">
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
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/ultimate_relativity_09.jpg">
    </td>
  </tr>
</table>

After you gain control of your characters, stack up in the middle to share a 
*Shell Crusher* AoE. The hourglasses will disappear, and the boss casts a 
raid-wide *Shockwave Pulsar*. The boss will then target the first player in 
aggro with *Black Halo*, a two-player tankbuster cleave.

## Apocalypse（アポカリプス） - Permaswap, Coloured Apocalypse

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

This variant makes the party adjust just once at the start of the mechanic, and
keeps the groups that way until the end.

However, *in exchange*, all players (other than H2 and D4) will need to be 
comfortable with dodging the Apocalypse AoEs from different positions. There is 
also a chance of melee downtime (although this can be mitigated by giving it to
a tank).

<table>
  <tr>
    <td width="50%">
      <p><b>10.</b> Group up with tanks/healers NNW, and DPS SSE, and
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
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_00.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>11.</b> These will be your groups for the duration of this
      mechanic.</p>
      <p>Following the letter "Z", each group has their assigned position:</p>
      <ul>
        <li><b>Top-left:</b> D1 D2 MT ST D3 H1 D4 H2 <b>:Bottom-right</b></li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_01.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>12.</b> The Oracle of Darkness will cast <em>Apocalypse</em>,
      which changes the arena slightly, and the first pair of <em>Dark Water
      III</em> stacks resolve.</p>
      <p>Three points on the arena; one center and two opposite cardinal/
      intercardinals will pulse white. This is a telegraph for where the later 
      AoEs will appear.</p>
      <p>A white streak also originates from each point and follows the line
      around the arena clockwise or anti-clockwise.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_02.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>13.</b> While the Water stacks are resolving, determine your future
      safe spots.</p>
      <p>Look at the outside lights- these will be each group's reference
      points in their half of the arena:</p>
      <ul>
        <li><b>W to NE:</b> Tank/healers (after any swaps).</li>
        <li><b>SW to E:</b> DPS group (after any swaps).</li>
      </ul>
      <p><em>(N.B: Your final spread positions are </em>not necessarily<em> in
      these sectors!)</em></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_02b.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>14.</b> Then, from your assigned outside lights, look 45 degrees in
      the <b>opposite direction</b> that the lights are travelling in.</p>
      <p>From these reference points, there are four more positions to take
      note of (marked with yellow arrows):</p>
      <ol>
        <li>The near position (towards the center).</li>
        <li>The near position <em>another</em> 45 degrees.</li>
        <li>The two far positions at the edge, 2.5 tick marks on either side of
        the cardinal/intercardinal mark.</li>
      </ol>
      <p>These will be your spread positions later.</p>
      <p><em>(In this example, the lights start W and E and go clockwise, so
      the "base T/H" group references W, and the "base DPS" group references
      E. Rotating 45 degrees in the opposite direction means the "base T/H"
      group goes SW, and the "base DPS" group goes NE.)</em></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_02c.jpg">
    </td>
  </tr>
</table>

This might take a little bit of getting used to, so here are all eight
possible configurations:

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] All Apocalypse configurations</b></summary>
<p>The following diagrams show the <em>initial</em> Apocalypse
positions/directions, and the party's base spread positions (without any
swaps).</p>
<table>
  <tr>
    <td width="50%" style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_ex1a.jpg">
    </td>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_ex1b.jpg">
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_ex2a.jpg">
    </td>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_ex2b.jpg">
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_ex3a.jpg">
    </td>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_ex3b.jpg">
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_ex4a.jpg">
    </td>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_ex4b.jpg">
    </td>
  </tr>
</table>

</details>
</div>

Now that the spread spots have been determined, we continue with the rest of
the mechanic.

<table>
  <tr>
    <td width="50%">
      <p><b>15.</b> While the water stacks were resolving, the boss also 
      readies <em>Spirit Taker</em>- the boss will jump on a random target
      with an AoE attack that knocks anyone else hit out of the arena.</p>
      <p>After the water stacks resolve, quickly spread out for <em>Spirit 
      Taker</em> in the earlier box formation.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_03.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>16.</b> The boss's <em>Spirit Taker</em> resolves.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_04.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>17.</b> The boss will return to the center.</p>
      <p>The trails will continue for a total of six pulses (indicating six 
      upcoming sets of AoEs) and end up in this formation relative to the 
      first set of pulses.</p>
      <p>All party members will get a spread marker. Just like before, spread
      out in your previous box formation in the positions at Step 14.</p>
      <p>There will be a large white circle on the floor- the front positions
      should stand on the edge of this circle to avoid the center Apocalypse.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_05.jpg">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_05a.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>18.</b> The AoEs now resolve for real.</p>
      <p>The AoEs will appear at the points that pulsed earlier for a total
      of six waves.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_06.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>19.</b> The second set of AoEs resolve together with the party's 
      spread markers.</p>
      <p>Move as soon as the spread AoEs resolve.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_07.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>20.</b> Quickly move to the center while avoiding the third set of 
      AoEs.</p>
      <ul>
        <li>Players towards the center can simply walk in.</li>
        <li>Players at the edge will want to collapse on the narrow safe path
        that leads in to the middle.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_08.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>21.</b> Fourth set of AoEs.</p>
      <p>There will be a white circle in the center of the arena.</p>
      <p>Use this circle as a guide to both not get hit by the Apocalypse AoEs,
      but also to stay far enough apart to not overlap the upcoming <em>Dark 
      Water III</em> stacks.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_09.jpg">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_09a.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>22.</b> The second set of <em>Dark Water III</em> stacks resolve
      together with the fifth set of AoEs.</p>
      <p>The ST moves out 90 degrees from where the first set of lights pulsed.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_10.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>23.</b> The boss then uses <em>Darkest Dance</em> (暗夜の舞踏技), which
      targets the furthest player (which should be a tank) with an AoE
      tankbuster.</p>
      <p>The <em>Darkest Dance</em> is also usually invulned, with the priority
      PLD > ST.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_11.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>24.</b> The tank that baited <em>Darkest Dance</em> rejoins their 
      group.</p>
      <p>Everyone moves towards the boss, and positions to prepare from a
      knockback from the boss in their groups.</p>
      <ul>
        <li><b>Boss's back-left:</b> Base T/H group.</li>
        <li><b>Boss's back-right:</b> Base DPS group.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_12.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>25.</b> The boss does a knockback.</p>
      <p>Use a shallow angle to avoid getting knocked out of the sides of the 
      arena.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_13.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>26.</b> The third set of <em>Dark Water III</em> stacks resolve.</p>
      <p>Resolve these near the boss- melee can use their gap closers, but will
      need to back out a little bit to meet up with the healers and ranged.</p>
      <ul>
        <li><b>Base T/H group:</b> Boss's back-left.</li>
        <li><b>Base DPS group:</b> Boss's back-right.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/apocalypse_14.jpg">
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
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/dark_water.png">
      <img src="{{site.baseurl}}/images/ultimates/fru_mana/03/unholy_darkness.png">
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Apocalypse]</b> Are there cases where more than one pair needs to swap?
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
  <b>[Darkest Dance]</b> How do tank invulns here interact with the rest of the 
  fight?
</summary>
<table>
  <tr>
    <td>
      <p>Some important relations to keep in mind are:</p>
      <ul>
        <li><b>WAR</b> and <b>DRK</b> can both invuln <em>Darkest Dance</em>,
        and have <em>Holmgang/Living Dead</em> back in time for the first 
        <em>Wings Dark and Light</em> in the final phase.</li>
        <li><b>GNB</b> and <b>PLD</b> can both invuln <em>Darkest Dance</em>. If 
        they do, their invuln will <em>not</em> be available for the first 
        <em>Wings Dark and Light</em> in the final phase (but it will be 
        available for the second).</li>
      </ul>
      <p>However, PLD is the only tank that cannot invuln <em>Somber Dance</em> 
      in P4 and have it available for either <em>Wings Dark and Light</em> in
      the final phase, so prioritize letting PLD bait <em>Darkest Dance</em> 
      with <em>Hallowed Ground</em> in this phase to extract the most out of
      your tank invulns.</p>
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
