---
layout: default
title: 6. Double Dragons
parent: Lv 90. DSR (Mana)
nav_order: 7
has_children: false
has_toc: false
permalink: /mana/dsr/06_double_dragons/
---

# Double Dragons

As far as progression goes, reaching this phase for the first time marks
roughly the half-way point. The mechanics in this phase are not particularly 
difficult, but this phase is unforgiving.

The structure of this phase can be broken down as follows:

- First half
  - [Wyrmsbreath #1](#wyrmsbreath-1)
  - [Akh Afah #1](#akh-afah-1)
  - [Hallowed Wings #1](#hallowed-wings-1)
- [Wroth Flames](#wroth-flames)
- Second half
  - [Akh Afah #2](#akh-afah-2)
  - [Hallowed Wings #2](#hallowed-wings-2)
  - [Wyrmsbreath #2](#wyrmsbreath-2-5-1)
- [Cauterize](#cauterize)
- [Alternative End](#alternative-end)

### Enrage conditions

Each dragon also has their own enrage condition. Causing either dragon to break 
their vow will result in their attacks one-shotting anyone hit (including 
tanks), and lower their damage taken.

- **Solemn Vow:** Hraesvelgr will enrage if he kills *any* player.
- **Mortal Vow:** Nidhogg will enrage if *Mortal Vow* is not passed.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Mortal Vow breakdown</b></summary>
<table>
  <tr>
    <td>
      <p>After Wyrmsbreath #1, Nidhogg will give a random DPS a <em>Mortal
      Vow</em> debuff. This debuff:</p>
      <ul>
        <li>Applies a light DoT on the player.</li>
        <li>Significantly <em>reduces</em> that player's healing potency.</li>
      </ul>
      <p>When the debuff expires, it explodes in a small AoE, and the player
      that had <em>Mortal Vow</em> will now get a <em>Mortal Atonement</em>
      debuff that prevents them from getting <em>Mortal Vow</em> again.</p>
      <p><em>Mortal Vow</em> transfers onto a random player that was hit by the
      AoE that does not have <em>Mortal Atonement</em>. (If additional players
      are hit, they get a <em>Suppuration</em> debuff that halves their max HP.</p>
      <p>Thus, when passing <em>Mortal Vow</em>, we need <b>exactly two</b>
      players to stack- the player that has the debuff, and the player that is
      about to receive it.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/mortal_vow.jpg"></td>
  </tr>
</table>
</details>
</div>

There are *four Mortal Vow* passes in this phase.

1. After Hallowed Wings #1
2. After Wroth Flames (this pass is *quick*)
3. After Hallowed Wings #2
4. After Cauterize → Touchdown

We pass "DTTMR", or in other words:

**DPS → MT → ST → D1/D2 → D3**

All passes happen in the center of the arena, except for the final pass after
Touchdown (which is just done at the edge).

---

## First half

This first part cycles through the three main mechanics of the fight.

As there are HP checks in this phase, we assign four players to each dragon as
a base:

- **MT, H1, D1, D3** → Prioritize Nidhogg
- **ST, H2, D2, D4** → Prioritize Hraesvelgr

### Wyrmsbreath 1

Each dragon will tether to three non-tank players that need to be sufficiently
stretched to lower their damage.

The tethers will also apply Fire or Ice-aspected debuffs that cancel each
other, so each non-tank player needs to get hit by a tether from *each* dragon.

The tanks also have their own mechanic- either one, or both dragon's mouths
will glow.

- If one dragon's mouth glows, the dragon whose mouth *doesn't* glow targets
  the person with hate for a giant AoE tankbuster.
- If both dragon's mouths glow, they will each target the person with hate for
  a Light or Dark-aspected AoE tankbuster. Like the tethers, these will cancel
  each other out.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Wyrmsbreath debuffs</b></summary>
<p><b>Fire-aspected debuffs</b></p>
<p>Getting hit by Nidhogg's <em>Flame Breath</em> during <em>Wyrmsbreath</em>
will apply the <em>Boiling</em> debuff.</p>
<p>The fire-aspected debuffs:</p>
<ul>
  <li><b>Are cleansed by getting hit with Ice-aspected damage from 
  Hraesvelgr</b>, as part of <em>Wyrmsbreath</em>, or <em>Cauterize</em>.</li>
  <li>Greatly increases Fire-aspected damage taken.</li>
</ul>
<table>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/dsr/06/debuffs/boiling.png">
    </td>
    <td>
      <p><b>Boiling</b></p>
      <p><em>Body is slowly heating up. Will become Pyretic when this effect 
      expires.</em></p>
      <ul>
        <li>Turns into <em>Pyretic</em> when the duration (12 seconds) expires.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/dsr/06/debuffs/pyretic.png">
    </td>
    <td>
      <p><b>Pyretic</b></p>
      <p><em>Fire-aspected damage is taken with every action.</em></p>
      <ul>
        <li>Ticks for about 40-45k damage if an action is taken, including 
        auto-attacks.</li>
        <li>Lasts 30 seconds.</li>
      </ul>
    </td>
  </tr>
</table>
<p><b>Ice-aspected debuffs</b></p>
<p>Getting hit by Hraesvelgr's <em>Ice Breath</em> during <em>Wyrmsbreath</em>
will apply the <em>Freezing</em> debuff.</p>
<p>The ice-aspected debuffs:</p>
<ul>
  <li><b>Are cleansed by getting hit with Fire-aspected damage from
  Nidhogg</b>, either as part of <em>Wyrmsbreath</em>, or <em>Cauterize</em>.</li>
  <li>Greatly increases Ice-aspected damage taken.</li>
</ul>
<table>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/dsr/06/debuffs/freezing.png">
    </td>
    <td>
      <p><b>Freezing</b></p>
      <p><em>Body is slowly turning to ice. Will become Deep Freeze when this 
      effect expires.</em></p>
      <ul>
        <li>Turns into <em>Deep Freeze</em> when the duration (12 seconds) 
        expires. Moving when the effect expires does not prevent this.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/dsr/06/debuffs/deep_freeze.png">
    </td>
    <td>
      <p><b>Deep Freeze</b></p>
      <p><em>Frozen solid and unable to execute actions.</em></p>
      <ul>
        <li>Players will be unable to move, attack, or execute any action.</li>
        <li>Lasts 30 seconds.</li>
      </ul>
    </td>
  </tr>
</table>
</details>
</div>

<table>
  <tr>
    <td width="50%">
      <p><b>1.</b> Have everyone preposition to prepare for the upcoming
      mechanic.</p>
      <ul>
        <li><b>Center:</b> D1, D2</li>
        <li><b>Bottom-left:</b> H1, D3</li>
        <li><b>Bottom-right:</b> H2, D4</li>
      </ul>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr_mana/06/wyrmsbreath_01_01.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>2.</b> More precisely, these are the anchor (D1, H1, D4)
      positions.</p>
      <p><b>None of these positions are in melee range.</b></p>
      <p><em>(Note the white tile that can be used as reference for the center
      position.)</em></p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/tethers_01.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>3.</b> Fire and Ice-aspected tethers appear. The goal is to get hit
      by one tether of each, canceling their associated debuffs.</p>
      <ul>
        <li><b>D2, D3, H2:</b> If your pair has the same-coloured tether, swap
        with the other pair that also has two tethers of the opposite colour.</li>
        <li><b>D1, H1, D4:</b> Does not move.</li>
      </ul>
      <p><em>(In this example, D1 and D3 will swap positions.)</em></p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr_mana/06/wyrmsbreath_01_02.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>4.</b> Mechanics resolve.</p>
      <ul>
        <li>
          <p><b>MT, ST:</b> If your dragon's mouth is <b>not</b> glowing, you
          have a single-target tankbuster.</p>
          <p>If <b>both</b> dragon's mouths are glowing, stack towards the
          middle, for a shared tankbuster.</p>
        </li>
      </ul>
      <p><em>In the first example, Nidhogg's mouth is glowing, while
      Hraesvelgr's is not, so the ST has a single-target tankbuster.</em></p>
      <p><em>In the second example, both mouths are glowing, so the tanks
      stack together for a shared tankbuster.</em></p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/dsr_mana/06/wyrmsbreath_01_03a.jpg">
      <img src="{{site.baseurl}}/images/ultimates/dsr_mana/06/wyrmsbreath_01_03b.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>5. Mortal Vow</b></p>
      <p>DPS spread out- Nidhogg will target a random DPS for the first Mortal
      Vow (in an AoE around that player).</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/mortal_vow_01.jpg"></td>
  </tr>
</table>

### Akh Afah #1

<table>
  <tr>
    <td width="50%">
      <p><b>6.</b> 4-man shared AoEs on the two healers. Nidhogg and
      Hraesvelgr's HP <b>must be within 3%</b> or their Akh Afah will kill all
      players in the stack.</p>
      <p>If the HP difference is too large, a tether will appear connecting
      both bosses:</p>
      <ul>
        <li><b>No tether:</b> Both dragons' HP is within 3%.</li>
        <li><b>Purple tether:</b> Nidhogg's HP is too high.</li>
        <li><b>White tether:</b> Hraesvelgr's HP is too high.</li>
      </ul>  
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/akh_afah.jpg"></td>
  </tr>
</table>

### Hallowed Wings #1

Three things resolve simultaneously:

1. Nidhogg will disappear and appear along either the North or South edge. Nidhogg
   will then *Cauterize* down either the west or east, cutting off half the arena.
2. Either Hraesvelgr's left or right wing will glow, cleaving either the north or
   south half of the arena, leaving just one safe quadrant to work with.
3. Hraesvelgr will raise or lower his head and will hit the two furthest (head
   up) or two closest (head down) players with a large AoE tankbuster.

<table>
  <tr>
    <td width="50%">
      <p><b>7.</b> Turn to face Hraesvelgr.</p>
      <p>Avoid Hraesvelgr's Hallowed Wings and Nidhogg's Cauterize, and then
      position yourselves based on whether <b>Hraesvelgr's head is up or
      down</b>.</p>
      <ul>
        <li><b>Head up:</b> Party near, tanks far.</li>
        <li><b>Head down:</b> Tanks near, party far.</li>
        <li><b>MT:</b> Edge (either North or South edge)</li>
        <li><b>ST:</b> Mid (towards the equator)</li>
      </ul>
      <p><em>(In this example, Hraesvelgr's head is down.)</em></p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/hallowed_wings_01_01.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>8. Mortal Vow pass #1</b></p>
      <p>The DPS that Nidhogg targeted with Mortal Vow passes it to the MT in
      the middle of the arena.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/mortal_vow_02.jpg"></td>
  </tr>
</table>

Here are some other potential configurations to consider:

<details>
<summary><b>[Hallowed Wings #1]</b> NE quadrant safe, head up</summary>
<table>
  <tr>
    <td width="50%">
      <p>Heads up means tanks far, party near.</p>
      <p>The MT takes the northern-most position.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/hallowed_wings_01_02.jpg"></td>
  </tr>
</table>
</details>

<details>
<summary><b>[Hallowed Wings #1]</b> SW quadrant safe, head down</summary>
<table>
  <tr>
    <td width="50%">
      <p>Heads down means tanks near, party far.</p>
      <p>The MT takes the southern-most position.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/hallowed_wings_01_03.jpg"></td>
  </tr>
</table>
</details>

<details>
<summary><b>[Hallowed Wings #1]</b> SW quadrant safe, head up</summary>
<table>
  <tr>
    <td width="50%">
      <p>Heads up means tanks far, party near.</p>
      <p>The MT takes the southern-most position.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/hallowed_wings_01_04.jpg"></td>
  </tr>
</table>
</details>

The party should continue to **attack Hraesvelgr** during this whole sequence,
even after Nidhogg returns.

After the *Mortal Vow* pass, Nidhogg will cast *Wroth Flames*, and Hraesvelgr
will leave the arena.

---

## Wroth Flames

Wroth Flames is the half-way point of this phase, separating the first and
second iteration of each of the looped mechanics.

- Hraesvelgr will become untargetable, and respawn on one of three positions  
  along either the North or South edge to *Cauterize* half the arena.
  *(this gives a 2/3 chance that the party will have melee uptime on Nidhogg*
  *during this mechanic.)*
- Nidhogg will cast *Akh Morn*, which is a party stack that hits four times.
  Each hit also leaves behind a puddle that will inflict a bleed on any player
  that stays inside for too long, killing that player.
- Three sets of *Sable Price* eyes will also spawn in sequence. Each set
  will explode in order, dealing damage along their row and column. The center
  set will always spawn first, followed by two more sets on opposite corners.
- Finally, the party will be affected by a variety of spread and stack debuffs 
  that will resolve at the end together with either *Hot Wing* or *Hot Tail* 
  from Nidhogg.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Wroth Flames debuffs</b></summary>
<table>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/dsr/06/debuffs/spreading_flames.png">
    </td>
    <td>
      <p><b>Spreading Flames</b></p>
      <p><em>Powerless against Nidhogg's desire for vengeance.</em></p>
      <p>Four players will be targeted with this debuff.</p>
      <ul>
        <li>When the timer expires, or when the debuffed player dies, a
        point-blank <em>Spreading Flames</em> AoE centered on the player
        resolves.</li>
        <li>Your own <em>Spreading Flames</em> will not affect you (it won't
        even do damage), but getting hit by <em>another</em> player's
        <em>Spreading Flames</em> will apply a <em>Damage Down</em> debuff and
        have a large knockback effect.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/dsr/06/debuffs/entangled_flames.png">
    </td>
    <td>
      <p><b>Entangled Flames</b></p>
      <p><em>Powerless against Nidhogg's desire that another share his
      suffering.</em></p>
      <p>Two players will be targeted with this debuff (which leaves two players
      without any debuffs).</p>
      <ul>
        <li>When the timer expires, a two-man stack AoE centered on the player
        resolves.
        <ul>
          <li>Each player with an <em>Entangled Flames</em> debuff will pair 
          together with a player that does not have any debuff to share this AoE.</li>
        </ul>
        </li>
        <li>Each player hit by the stack will also get a <em>Fire Resistance
        Down II</em> debuff (so you cannot overlap stacks).</li>
        <li>If the debuffed player dies, or there are not enough players alive
        to assign the debuff to, it explodes with <em>Entangled Pyre</em>,
        dealing damage, and applying both <em>Damage Down</em> and <em>Fire 
        Resistance Down II</em> to the entire party instead, quickly leading to
        a wipe.</li>
      </ul>
    </td>
  </tr>
</table>
</details>
</div>

When dropping *Akh Morns*, the most efficient movement (geometrically) is to
move **perpendicular from the wall in a straight line**, and then curve in
after the third Akh Morn.

<table>
  <tr>
    <td width="50%">
      <p><b>1.</b> Hraesvelgr appears along either the North or South edge
      together with the first set of <em>Sable Price</em> eyes (that will
      always spawn center).</p>
      <p>Move to the East or West edge to avoid Hraesvelgr's Cauterize
      <em>(this will be West, next to Nidhogg 2 out of 3 times)</em></p>
      <p><em>(In this example, Hraesvelgr's Cauterize will hit the east half,
      so the party moves West next to Nidhogg.)</em></p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_01_01.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>2.</b> The second set of eyes spawn.</p>
      <p>Move to the North or South corner, whichever is further from the
      second set of eyes.</p>
      <p><em>(In this example, moving South to the SW corner puts the party the 
      furthest away from the second set of Eyes that spawned NE.)</em></p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_01_02.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>3.</b> The third set of eyes spawn.</p>
      <p>Stack together, mitigate, and get ready to move as a group.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_01_03.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>4.</b> Hraesvelgr's Cauterize resolves. Drop first Akh Morn
      puddle.</p>
      <p>The initial Akh Morn movement will always go east-to-west or vice
      versa.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_01_04.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>5.</b> First set of eye AoEs resolve. Drop the second Akh Morn
      puddle without getting hit by the eye AoE.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_01_05.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>6.</b> Drop third and fourth Akh Morn puddles.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_01_06.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>7.</b> Move to the middle and identify whether Nidhogg is casting
      Hot Wing or Hot Tail.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_01_07.jpg"></td>
  </tr>
  <tr>
    <td colspan="2">
      <p><b>8.</b> Spreads will go towards Nidhogg (west), stacks will go
      towards Hraesvelgr (east).</p>
      <p style="text-align:center"><b>(West)</b> MT ST D1 D2 D3 D4 H1 H2
      <b>(East)</b></p>
    </td>
  </tr>
  <tr>
    <td style="text-align:center"><b>Hot Wing</b></td>
    <td style="text-align:center"><b>Hot Tail</b></td>
  </tr>
  <tr>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/dsr_mana/06/wroth_flames_ex_01_08a.jpg">
      <p>There is enough space for two "spreads" to stand side-by-side if they
      are on the sides of the safe zone.</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/dsr_mana/06/wroth_flames_ex_01_08b.jpg">
    </td>
  </tr>
</table>

Shortly after the stacks/spreads resolve, the next *Mortal Vow* pass happens.

Note that this *Mortal Vow* pass is *fast*.

<table>
  <tr>
    <td width="50%">
      <p><b>7.</b> Pass Mortal Vow from the MT to the ST in the center.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/mortal_vow_03.jpg"></td>
  </tr>
</table>

Here are some additional examples to consider:

<details>
<summary>
  <b>[Wroth Flames]</b> Hraesvelgr middle (uptime available), 2-to-1 dodge
</summary>
<table>
  <tr>
    <td width="50%">
      <p><b>1.</b> Hraesvelgr appears along either the North or South edge
      together with the first set of <em>Sable Price</em> eyes (that will
      always spawn center).</p>
      <p>Move to the East or West edge to avoid Hraesvelgr's Cauterize</p>
      <p><em>(In this example, Hraesvelgr's Cauterize will go down the center, 
      so the party moves West next to Nidhogg.)</em></p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_02_01.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>2.</b> The second set of eyes spawn.</p>
      <p>Move to the North or South corner, whichever is further from the
      second set of eyes.</p>
      <p><em>(In this example, moving North to the NW corner puts the party the 
      furthest away from the second set of Eyes that spawned SW.)</em></p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_02_02.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>3.</b> The third set of eyes spawn.</p>
      <p>Stack together, mitigate, and get ready to move as a group.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_02_03.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>4.</b> Hraesvelgr's Cauterize resolves. Drop first Akh Morn puddle.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_02_04.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>5.</b> First set of eye AoEs resolve. Drop the second Akh Morn
      puddle without getting hit.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_02_05.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>6.</b> Drop third and fourth Akh Morn puddles.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_02_06.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>7.</b> Move to the middle, identify whether Nidhogg is casting Hot
      Wing or Hot Tail.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_02_07.jpg"></td>
  </tr>
</table>
</details>

<details>
<summary>
  <b>[Wroth Flames]</b> Hraesvelgr west (forced downtime), 2-to-1 dodge
</summary>
<table>
  <tr>
    <td width="50%">
      <p><b>1.</b> Hraesvelgr appears along either the North or South edge
      together with the first set of <em>Sable Price</em> eyes (that will
      always spawn center).</p>
      <p>Move to the East or West edge to avoid Hraesvelgr's Cauterize</p>
      <p><em>(In this example, Hraesvelgr's Cauterize will go down the west 
      half, so the party moves east away from Nidhogg.)</em></p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_03_01.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>2.</b> The second set of eyes spawn.</p>
      <p>Move to the North or South corner, whichever is further from the
      second set of eyes.</p>
      <p><em>(In this example, moving North to the NE corner puts the party the 
      furthest away from the second set of Eyes that spawned SE.)</em></p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_03_02.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>3.</b> The third set of eyes spawn.</p>
      <p>Stack together, mitigate, and get ready to move as a group.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_03_03.jpg"></td>
  </tr>
  <tr>
    <td><b>4.</b> Hraesvelgr's Cauterize resolves. Drop first Akh Morn puddle.</td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_03_04.jpg"></td>
  </tr>
  <tr>
    <td><b>5.</b> First set of eye AoEs resolve. Drop the second Akh Morn
    puddle without getting hit.</td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_03_05.jpg"></td>
  </tr>
  <tr>
    <td><b>6.</b> Drop third and fourth Akh Morn puddles.</td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_03_06.jpg"></td>
  </tr>
  <tr>
    <td><b>7.</b> Move to the middle, identify whether Nidhogg is casting Hot
    Wing or Hot Tail.</td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_ex_03_07.jpg"></td>
  </tr>
</table>
</details>

---

## Second half

The second half is a rehash of the first, with slightly different twists on the
same mechanics from earlier.

### Akh Afah #2

<table>
  <tr>
    <td width="50%">
      <p><b>1.</b> This works exactly the same as the first- both dragon's HP
      must be brought to within 3% of one another for their stack to survive.</p>
      <p>However, the catch is that depending on whether the party had
      uptime/downtime earlier on Hraesvelgr or Nidhogg during the previous
      mechanics, one of the two dragons' HP may be skewed to one side.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/akh_afah.jpg"></td>
  </tr>
</table>

### Hallowed Wings #2

<table>
  <tr>
    <td width="50%">
      <p><b>2.</b> This time, Hallowed Wings will happen in combination with
      Hot Wing <em>or</em> Hot Tail from Nidhogg.</p>
      <ul>
        <li><b>MT:</b> Goes to the edge, depending on Hraesvelgr's head.
          <ul>
            <li><b>Hraesvelgr's head up:</b> West edge.</li>
            <li><b>Hraesvelgr's head down:</b> East edge.</li>
          </ul>
        </li>
        <li><b>ST: </b> Takes the center.</li>
      </ul>
      <p><em>(This example has Hot Wing with Hraesvelgr's head up.)</em></p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/hallowed_wings_02_01.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>3. Mortal Vow pass #3</b></p>
      <p>This pass goes from the ST to D1, <em>unless</em> D1 started with the
      first Mortal Vow, in which case ST passes to D2 instead.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/mortal_vow_04.jpg"></td>
  </tr>
</table>

Here are some other potential configurations to consider:

<details>
<summary><b>[Hallowed Wings #2]</b> Hot Wing, head up</summary>
<table>
  <tr>
    <td width="50%">
      <p>Hot Wing means all party members must stay near the E/W line.</p>
      <p>Heads up means the tanks are away from Hraesvelgr, and the rest of the
      party is towards Hraesvelgr.</p>
      <p>The MT takes the western-most position.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/hallowed_wings_02_01.jpg"></td>
  </tr>
</table>
</details>

<details>
<summary><b>[Hallowed Wings #2]</b> Hot Tail, head down</summary>
<table>
  <tr>
    <td width="50%">
      <p>Hot Tail means all party members must go to north <em>or</em> south
      without getting hit by Hallowed Wings' AoE.</p>
      <p>Heads down means the tanks are towards Hraesvelgr, and the rest of the
      party is away from Hraesvelgr.</p>
      <p>The MT takes the eastern-most position.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/hallowed_wings_02_02.jpg"></td>
  </tr>
</table>
</details>

### Wyrmsbreath 2 (fixed positions)

This iteration of Wyrmsbreath is different because we **do not** want to stack
opposite tethers.

All players (except the tanks) have fixed positions for this mechanic- each
tank has two possible positions, depending on whether they get a single-target,
or the shared tankbuster.

The positions are *precise*- pay attention to the markings on the ground to
help determine where to stand.

![]({{site.baseurl}}/images/ultimates/dsr_mana/06/fixed_wyrmsbreath2.jpg)

Also note that if D1 is tethered to Nidhogg, or D2 is tethered to Hraesvelgr,
the tether will indicate that it is *not* stretched out.

The melee DPS should use their personal shields to help mitigate this damage.

<div style="background-color: #200 ; padding: 10px; border: 1px solid;">
  <b>Note:</b> H1 will want to pay special attention to D2 if they are a DRG,
  as DRG is the only melee that cannot shield themselves, especially if they
  have <em>Mortal Vow</em> at this time.
</div>

---

## Cauterize

The reason why we did not stack opposite tethers in Wyrmsbreath #2 was because
we needed the fire/ice debuffs in order to survive this mechanic.

<table>
  <tr>
    <td width="50%">
      <p><b>1.</b> Nidhogg and Hraesvelgr will spawn along the north edge in a
      <b>random</b> configuration, and dive down each half.</p>
      <p>The first player hit by each dive takes additional damage, and are
      taken by the tanks with their invulns.</p>
      <ul>
        <li><b>MT:</b> West half, closest to the North edge.</li>
        <li><b>ST:</b> East half, closest to the North edge.</li>
        <li><b>Players with the Fire debuff:</b> Stand in the half in front of 
        Hraesvelgr. <em>Do not move.</em></li>
        <li><b>Players with the Ice debuff:</b> Stand in the half in front of 
        Nidhogg.</li>
      </ul>
      <p><b>Do not move</b> as Nidhogg's debuff will turn into Pyretic. The
      resulting damage will result in Hraesvelgr's Cauterize killing you and
      cause Hraesvelgr to enrage.</p>
      <div style="background-color: #200 ; padding: 10px; border: 1px solid;">
        <b>Note:</b> If you have a DRK and are using <em>Living Dead</em> here, 
        neither dragon will be targetable for the DRK to recover HP for <em>Walking Dead</em>.
      </div>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/cauterize_01.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>2. Mortal Vow pass #4</b></p>
      <p>After Cauterize, everybody gathers north to avoid Nidhogg's and
      Hraesvelgr's Touchdown damage.</p>
      <p>After Touchdown, all players move away from the stack point
      <em>except</em> the DPS with Mortal Vow and D3.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/mortal_vow_05.jpg"></td>
  </tr>
</table>

After both dragons *Touchdown*, they will each start casting their enrage,
*Revenge of the Horde*.

## Alternative End

After the two dragons are defeated, the two dragon eyes will be left behind.
Just like before, they will do raid-wide damage with a bleed (*Resentment*).

This time around, if Thordan was spared in the previous phase, he will jump
down and do another raid-wide with a bleed on the party (*Shockwave*) before
taking the eyes for his own, starting his transformation to Dragonking Thordan.

When the bleed from *Shockwave* disappears, **heavily shield and mitigate** in
order to survive *Alternative End*, the final raid-wide damage that marks the
transition to the final phase *(Dragonking Thordan will not be targetable*
*during this)*.

<table>
  <tr>
    <td><b>Alterative End</b></td>
    <td>
      <p>MT 90s, ST 90s, H2 30s, H2 120s, H2 90s, D3</p>
      <ul>
        <li>A SCH can substitute <em>Expedient</em> with <em>Fey 
        Illumination</em>.</li>
      </ul>
    </td>
  </tr>
</table>

<div style="background-color: #200 ; padding: 10px; border: 1px solid;">
  <p><b>Note:</b> Each Bleed tick deals about ~14k damage. Make sure you
  <em>do not</em> apply shields until <em>after</em> the Bleed has worn off
  completely!</p>
</div>
<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
  <p><b>Tip:</b> Thordan will announce <em>"Hahahaha! By the power of mine
  enemy's eyes..."</em> just before the second round of bleeds are applied.</p>
  <p>A DNC should start <em>Improvisation</em> when the dialogue box
  <em>disappears</em> to get the maximum value out of <em>Improvisation</em>'s
  shields.</p>
</div>

---

## Frequently Asked Questions

<details markdown=block>
<summary>
  <b>[Mortal Vow]</b> Does the final <em>Mortal Vow</em> pass still go to D3
  even if D3 started with <em>Mortal Vow</em>?
</summary>
<table>
  <tr>
    <td>
      <p>Yes. If D3 starts with <em>Mortal Vow</em>, they will be affected by 
      <em>Mortal Atonement</em> after the first pass.</p>
      <p>However, <em>Mortal Atonement</em> will expire before the final 
      <em>Mortal Vow</em> pass, allowing D3 to take it again.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Pyretic]</b> Do channeled abilities/emotes trigger Pyretic?
</summary>
<table>
  <tr>
    <td>
      <p>No. Channeled abilities like Improvisation, Meditate, Collective
      Unconsciousness, Flamethrower, Anatman, or emotes do not count as
      movement, and will not trigger Pyretic provided they're already
      in the middle of being channeled.</p>
      <p>However, <em>starting</em> to channel an ability counts.</p>
      <p><em>(You really shouldn't channel during Cauterize anyway, as the
      buildup to Alternative End is a better place to do so.)</em></p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Hallowed Wings 1]</b> Why should the party continue to attack Hraesvelgr
  after the first Hallowed Wings, even after Nidhogg returns?
</summary>
<table>
  <tr>
    <td>
      <p>This is done to prepare for the second <em>Akh Afah</em> HP check that
      happens after <em>Wroth Flames</em>.</p>
      <p>Part of what makes the second <em>Akh Afah</em> dynamic is that 
      depending on whether the party (randomly) got uptime on Nidhogg or 
      Hraesvelgr, the HP may be skewed in one direction.</p>
      <p>That being said, it is <em>more likely</em> that Hraesvelgr will have
      more HP than Nidhogg after <em>Wroth Flames</em> because:</p>
      <ul>
        <li>The party has a 1-in-2 chance of downtime on Hraesvelgr during
        <em>Hallowed Wings</em> 1, but the chance of downtime on Nidhogg during
        <em>Wroth Flames</em> is lower at 1-in-3.</li>
        <li><em>Wroth Flames</em> coincides with the party's 1-minute abilities,
        so in the more likely event the party has uptime on Nidhogg, Nidhogg 
        would take more damage.</li>
      </ul>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Wroth Flames]</b> Is there a pattern to how the debuffs are assigned?
</summary>
<table>
  <tr>
    <td>
      <p>Unfortunately not- the debuff distribution is random.</p>
      <p>Here's an example where two of the no-debuff players are both DPS.</p>
    </td>
  <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_debuffs.jpg"></td></tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Wroth Flames]</b> Why are there two marking schemes?
</summary>
<table>
  <tr>
    <td>
      <p>The short answer is "that's just the automarker configuration that got
      passed around early."</p>
      <p>One that argue that if you mark all eight players, the visual clutter
      makes it hard(er) for each player to discern their number over their
      colour, hence the "same marker-type" stack configuration.</p>
    <p>I am personally not a fan because it is harder to replicate manually
    (effectively <em>mandating</em> automarkers).</p>
    <p>The problem with manually marking each pair using the same marker type
    is that this task cannot be split between two players, because there's now
    a possibility that the two players pick the same person twice.</p>
    <p>For example, in the configuration on the right, one person can pick the
    WAR + SMN as a pair, then the other pick RDM + SMN, doubling up on the SMN
    and leaving the SAM unmarked (it also doesn't help that <em>Mortal
    Atonement</em> looks like a purple spread debuff).</p>
  </td>
  <td><img src="{{site.baseurl}}/images/ultimates/dsr/06/wroth_flames_debuffs.jpg"></td></tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Cauterize]</b> Just how large are the Cauterize AoEs? Do they extend past 
  half the arena?
</summary>
<table>
  <tr>
    <td>Each Cauterize is exactly half the arena, even though the visual
    effects make it look like the AoE is slightly larger.</td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/dsr/06/cauterize.jpg">
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Cauterize]</b> Do the tanks have to invuln Cauterize?
</summary>
<table>
  <tr>
    <td>
      <p>Technically speaking, no- <em>Cauterize</em> deals about 240k damage, 
      which <em>can</em> be mitigated with <em>Rampart</em>, a tank's 30% 
      mitigation, and the short mitigation.</p>
      <p>The problem is that <em>Wyrmsbreath</em> 2 happens right before. There
      is 14 seconds between <em>Wyrmsbreath</em> 2 and <em>Cauterize</em> which
      means that it <em>is</em> possible to catch both with a tank's 30% 
      mitigation, allowing the tank to mitigate <em>Cauterize</em> instead.</p>
      <p>The end result is that the tank has their invuln available for P7-
      this is key to the "1-1-6" style of resolving <em>Akh Morn's Edge</em>
      that you might see other groups do.</p>
      <p>However, it is tighter in execution than simply using a tank invuln,
      and provides an additional point of failure in P6 (which is already
      unforgiving enough).</p>
      <p>Prog groups <em>especially</em> should aim to get more P7 practice,
      and it is difficult to justify potentially spending more time in P6 for
      <em>both</em> tanks to consistently (and independently!) get the timing
      down.</p>
      <p>At this stage, most players in PF aren't used to resolving <em>Akh 
      Morn's Edge</em> in a 1-1-6 fashion, so trying to push 1-1-6 now may lead 
      to wipes in P7 due to players being unfamiliar with the strat.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Cauterize]</b> Can the Cauterize DoT be mitigated?
</summary>
<table>
  <tr>
    <td>No. Regardless of whether Cauterize was taken with invuln or with 
    mitigations, the DoT ticks for about 18k damage/tick.</td>
  </tr>
</table>
</details>

<details markdown=block>
<summary><b>[General]</b> Can you defeat one dragon early?</summary>
<table>
  <tr>
    <td>No. Each dragon will have a floor of 1HP until they start casting their
    enrage.</td>
  </tr>
</table>
</details>

---

## Troubleshooting

<details markdown=block>
<summary>
  <b>[Wyrmsbreath #1]</b> I took extra damage even though I wasn't tethered-
  why is that?
</summary>
<table>
  <tr>
    <td>
      <p><b>Both</b> dragon's damage are based on proximity, even if you are
      not actually tethered to them.</p>
      <p>You can think of the tethers as just directing where the breaths will 
      go; the colour change is a proximity indicator of that particular 
      player-dragon pair, but you still have to worry about proximity to the 
      other dragon.</p>
      <p>Here is a graph plotting damage vs distance (in centiyalms).</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/dsr/06/wyrmsbreath_faq.jpg">
      <em>(Credit: radrauser)</em>
    </td>
  </tr>
</table>
</details>

---

## Strategy Related Questions

<details markdown=block>
<summary>
  <b>[Wyrmsbreath 2]</b> What is the fixed Wyrmsbreath 2 strat, and why aren't we doing it?</summary>
<table>
  <tr>
    <td>
      <p>As the name implies, this is a strat that fixes all player positions
      (except for the tanks, who may have to stack in the middle).</p>
      <p>The fixed Wyrmsbreath 2 strat is popular in other regions, but has
      fallen out of favour in Elemental.</p>
      <p>However, player positioning is precise, and when things go wrong, it's
      often difficult to diagnose what went wrong.</p>
      <p style="text-align:center">
        <img src="{{site.baseurl}}/images/ultimates/dsr_mana/06/fixed_wyrmsbreath2.jpg">
      </p>
      <ul>
        <li><b>MT:</b> NW if you get the single-target tankbuster (by Nidhogg).</li>
        <li><b>ST:</b> SE if you get the single-target tankbuster (by Hraesvelgr).</li>
      </ul>
      <p><em>Tanks should stand inside the targeting circles- use where the
      outer AoE intersects the targeting circle as a reference point. You will
      kill the healers if you are not in the correct place.</em></p>
      <ul>
        <li><b>H1:</b> As far true North as you can go.</li>
        <li><b>H2:</b> As far true South as you can go.</li>
        <li><b>D1:</b> NW corner of the white tile beside Nidhogg.</li>
        <li><b>D2:</b> Between the two white tiles besides Hraesvelgr.</li>
        <li><b>D3:</b> 1/2 a tile west of the western "train track", as far
        south as you can go.</li>
        <li><b>D4:</b> 1/2 a tile east of the eastern "train track", as far
        north as you can go.</li>
      </ul>
      <p>Depending on which dragon they are tethered to, <b>D1's and/or D2's
      tether may not fully stretch. This is okay, and the damage is not
      lethal.</b></p>
      <p>This strategy is popular in other data centers- however:</p>
      <ul>
        <li>It is difficult to tell what went wrong in the event of an accident.</li>
        <li>Incoming damage is inconsistent on the two melee, leading to
        inconsistent healing requirements between pulls.</li>
        <li>The two melee are potentially taking the most damage from the
        tethers, and <em>Mortal Vow</em> is also on a melee at this point (and has
        a DoT effect).</li>
      </ul>
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
