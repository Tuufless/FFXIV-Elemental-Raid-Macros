---
layout: default
title: 1. Living Liquid
parent: Lv 80. TEA
permalink: /ultimates/tea/01_living_liquid/
---

# Living Liquid

This is a modified version of the original [Separations Living Liquid strat](http://laytina14.com/archives/20887361.html).

Notable changes are:
- The MT Provokes the Liquid Hand and invulns the first set of *Fluid Swings*
  and the *Protean Wave* from the "north" puddle.
- The first set of *Protean Waves* are baited by the MT and both healers,
  instead of both healers and D3.
- The DPS positions for the final set of *Protean Waves* are different.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Liquid Hand mechanics</b></summary>
<p>The Liquid Hand is an add that spawns when Living Liquid casts the first 
<em>Cascade</em> in the fight. It has two key mechanics:</p>
<p><b>Hand of Parting</b></p>
<ul>
  <li>The Liquid Hand will glow blue and turn into an open palm, or a closed
  fist.</li>
  <li>After a few seconds, the Liquid Hand will slam on the ground, dealing
    raid-wide damage based on its distance to Living Liquid:
    <ul>
      <li>If the Hand was <b>an open palm</b>: Stack the Hand on top of Living
      Liquid.</li>
      <li>If the Hand was <b>a closed fist</b>: Separate the Hand and Living
      Liquid.</li>
    </ul>
  </li>
  <li>Whether the Hand turns into a closed fist or an open palm <b>can be
  baited.</b>
    <ul>
      <li>If Living Liquid and the Hand are <b>separated</b>, the Hand will
      glow with an open palm.</li>
      <li>If Living Liquid and the Hand are <b>near one another</b>, the Hand
      will glow with <b>a closed fist</b>.</li>
    </ul>
  </li>
  <li>We will <em>always</em> want the Liquid Hand to turn to an open
  palm.</li>
</ul>
<p><b>Hand of Pain</b></p>
<p>The Liquid Hand will slam the ground, and deal raid-wide damage based on the
HP% difference between Living Liquid and the Liquid Hand.</p>
<ul>
  <li>Living Liquid and the Liquid Hand's HP% must be <b>within 5%</b> to not
  deal lethal damage.</li>
  <li>This damage ignores tank invulnerability.</li>
</ul>
</details>
</div>

<table>
  <tr>
    <td width="50%">
      <p><b>1.</b> Pull Living Liquid to the center of the arena.</p>
      <p>Living Liquid will auto-attack three times, before cleaving the MT
      with a <em>Fluid Swing</em>.</p>
      <p>Living Liquid then casts the first <em>Cascade</em>, which spawns the
      Liquid Hand and three water puddles.</p>
      <ul>
        <li>The party orients themselves to the three water puddles.</li>
        <li><b>MT, ST:</b> Separate Living Liquid and Hand to force Liquid Hand
        to an open palm.</li>
      </ul>
      <div style="background-color: #002 ; padding: 10px; border: 1px solid;">
      <b>Tip:</b> If the ST is having trouble taking the Liquid Hand's hate
      from the MT, the MT can momentarily turn off their tank stance when the
      Liquid Hand spawns to let the ST secure hate.</div>
      <p>As a rough guide, we split the party as such:</p>
      <ul>
        <li><b>MT, H1, D1, D3:</b> Living Liquid</li>
        <li><b>ST, H2, D2, D4:</b> Liquid Hand</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_01.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>2.</b> If Liquid Hand has been sufficiently separated from Living
      Liquid, it will now glow as an open palm.</p>
      <ul>
        <li><b>MT:</b> Provoke the Liquid Hand to stack it on top of Living Liquid.</li>
        <li><b>MT, H1, H2:</b> Bait the first set of (telegraphed) <em>Protean
        Waves</em> from the water puddles.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_02.jpg">
    </td>
  </tr>
</table>

The Liquid Hand does *not* need to be defeated to clear the phase- however, its
HP needs to be kept close to Living Liquid's because of *Hand of Pain*.

---

## Jagd Dolls

This is the first major section of the fight that introduces the Jagd Dolls,
which are a one-time mechanic, but also introduces the puddle's *Protean
Waves*.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Jagd Dolls breakdown</b></summary>
<p>The Jagd Dolls are adds that have the following mechanics:</p>
<ul>
  <li>The Jagd Dolls tether to the first player that performs any action on
  them (including auto-attacks), and lock onto that player.</li>
  <li>They periodically pulse with <em>Exhaust</em>, a point-blank AoE that
  applies a stacking <em>Luminous Aetheroplasm</em> on any player hit.
  <ul>
    <li>If any player is hit with two AoEs, they explode and wipe the raid.</li>
  </ul>
  </li>
  <li>The Jagd Dolls <b>cannot</b> be destroyed by damage- they will explode
  and wipe the raid if they reach 0% HP.
  <ul>
    <li>To destroy them, they need to be dragged near either Living Liquid
    <em>or</em> the Liquid Hand. Doing so will tether them to the boss and 
    destroy them, dealing raid-wide damage to the party <em>(Reducible
    Complexity)</em> based on its current HP.</li>
    <li>The Jagd Doll <b>must be under 25% HP</b>, or the explosion will deal 
    lethal damage.</li>
  </ul>
  </li>
</ul>
</details>
</div>

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Puddle's Protean Waves</b></summary>
<ol>
  <li>Each puddle targets the closest player to them with a cone telegraph.</li>
  <li>When the telegraph disappears, a cone <em>Protean Wave</em> fires where
  the telegraph was. This <em>Protean Wave</em> will also knockback any players
  hit (although this can be stopped with <em>Arm's Length/Surecast</em>).</li>
  <li>Finally, a second <b>untelegraphed</b> <em>Protean Wave</em> fires at the
  closest player. This <em>Protean Wave</em> cannot be avoided, but doesn't
  knockback.</li>
</ol>
<p>All <em>Protean Waves</em> also apply a 5-second <em>Water Resistance Down
II</em> debuff on the players they hit (so a player cannot get hit by more than
one).</p>
</details>
</div>

<table>
  <tr>
    <td width="50%">
      <p><b>3.</b> Jagd Dolls spawn, and first set of untelegraphed Protean
      Waves resolve.</p>
      <ul>
        <li><b>MT:</b> Invuln Living Liquid's <em>Fluid Swing</em> and the
        Liquid Hand's <em>Fluid Strike</em>.</li>
        <li><b>MT, H1, H2:</b> Bait telegraphed Protean Waves from the puddles</li>
        <li><b>DPS:</b> Take your assigned Jagd Doll.</li>
      </ul>
      <p>The Liquid Hand will also use <em>Hand of Parting</em> here. The Hand
      should've been an open palm, which will wipe the raid unless the Liquid
      Hand is stacked on top of Living Liquid.</p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_03.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>4.</b> The second set of untelegraphed Protean Waves resolve.</p>
      <ul>
        <li><b>D1, D2:</b> Stack on top of your doll to avoid getting hit by
        two Doll AoEs. Be careful not to accidentally bait the Protean Wave
        away from the MT.</li>
      </ul>
      <p>The Liquid Hand will also use <em>Hand of Pain</em> here. Living
      Liquid and the Liquid Hand's HP need to be kept within 5% HP of each
      another for the party to survive this.</p></td>
	<td><img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_04.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>5.</b> Liquid Hand casts Hand of Pain; two Embolus orbs spawn and
      slowly move towards the bosses.</p>
      <ul>
        <li><b>MT:</b> When D1's doll is under 25% HP, move to the center of
        the arena.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_05.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>6.</b> D3's and D4's Dolls pulse one more time.</p>
      <ul>
        <li><b>MT, ST:</b> Position NW and NE to prepare for Fluid Swing.</li>
        <li><b>D2:</b> Feed your doll to either boss at under 25% HP.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_06.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>7.</b> Living Liquid and the Liquid Hand both cleave their
      respective tanks with <em>Fluid Swing/Strike</em>.</p>
      <ul>
        <li><b>D3, D4:</b> Feed your dolls to the bosses when they are <b>under
        25% HP</b>. You may want to wait for the Fluid Swings to resolve first.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_07.jpg">
    </td>
  </tr>
</table>

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<b>Tip:</b> From here on, the ST will generally take more damage than the MT,
as the Liquid Hand will auto-attack more over the rest of the phase.</div>

---

## Protean Waves #1

This section of the fight now introduces Living Liquid's *Protean Waves*, which
are similar to the puddle's *Protean Waves*, with a few differences.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Living Liquid's Protean Waves</b></summary>
<ol>
  <li>Living Liquid targets each player with a cone telegraph.</li>
  <li>When the telegraphs disappear, a cone <em>Protean Wave</em> fires where
  the telegraph was. This <em>Protean Wave</em> will also knockback any players
  hit (although this can be stopped with <em>Arm's Length/Surecast</em>).</li>
  <li><p>Living Liquid then fires <b>two sets</b> of <b>five untelegraphed</b>
  <em>Protean Waves</em>, one after the other:</p>
    <ul>
      <li>The <b>four closest players</b> to Living Liquid.</li>
      <li>A fifth <em>Protean Wave</em> in front of Living Liquid, <b>in the
      direction Living Liquid is facing.</b></li>
    </ul>
  </li>
</ol>
<p>This last sets of <em>Protean Waves</em> cannot be avoided, but do not
knockback.</p>
<p>All <em>Protean Waves</em> also apply a 5-second <em>Water Resistance Down
II</em> debuff on the players they hit (so a player cannot get hit by more than
one).</p>
</details>
</div>

<table>
  <tr>
    <td width="50%">
      <p><b>8.</b> Party stacks "north/south" to bait the first set of
      telegraphed <em>Protean Waves</em> from Living Liquid.</p></td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_08.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>9.</b> First set of untelegraphed Protean Waves.</p>
      <ul>
        <li><b>MT, ST, D1, D2:</b> Stay close to take these Protean Waves.</li>
        <li><b>H1, H2, D3, D4:</b> Bait AoEs away from the bosses.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_09.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>10.</b> Second set of untelegraphed Protean Waves.</p>
      <ul>
        <li><b>MT, ST, D1, D2:</b> Move to max-melee to avoid baiting the
        <em>Protean Waves</em>.</li>
        <li><b>H1, H2, D3, D4:</b> Fan out under Living Liquid's targeting
        circle to bait the Protean Waves.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_10.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>11.</b> 6x <em>Splashes</em> from Living Liquid.</p>
      <p>Two tornados will also tether to two players, and these tethers should
      be picked up by the tanks. They will resolve with an AoE tankbuster
      centered on the tethered player.</p>
      <p>It's easy for the Liquid Hand to be out of melee range, because the
      melee do not want to get hit by the tether AoEs. Healers and ranged can
      swap over to the Liquid Hand if needed to keep the HP within range for
      <em>Hand of Pain</em>.</p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_11.jpg">
    </td>
  </tr>
</table>

---

## Protean Waves #2

This is the final phase of Living Liquid, and combines both Living Liquid's
*Protean Waves* with a set of *Protean Waves* from the puddles.

<table>
  <tr>
    <td width="50%">
      <p><b>12.</b> 2nd Cascade. The Liquid Hand also uses <em>Hand of
      Pain</em>.</p>
      <p>The party should reorient themselves to the new water puddles.</p>
      <ul>
        <li><b>MT, ST, D3, D4:</b> Stack together "north".</li>
        <li><b>H1, H2, D1, D2:</b> Stack together "south".</li>
      </ul>
      <p>Six players (at random) will get a <em>Throttle</em> debuff, which
      must be removed via <em>Esuna</em> (or <em>Warden's Paean</em>).</p>
      <ul>
        <li><b>H1, H2:</b> <em>Esuna</em> Throttled players.</li>
      </ul>
      <p>How the two healers split up the <em>Esunas</em> doesn't matter, so
      long as they agree. We go with the following priority:</p>
      <ul>
        <li><b>H1:</b> MT ST H1 H2 D1 D2 D3 D4 <b>:H2</b></li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_12.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>13.</b> Start of Protean Waves #2.</p>
      <p>Just like the first iteration, this begins with baited, telegraphed
      <em>Protean Waves</em> north and south of Living Liquid.</p>
      <div style="background-color: #002 ; padding: 10px; border: 1px solid;">
      <b>Tip:</b> If <b>both</b> Living Liquid and the Liquid Hand are around
      10-11% HP at this point, the whole party can switch to Living Liquid and
      kill it before the next <em>Hand of Pain</em> resolves.</div>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_13.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>14.</b> 1st untelegraphed <em>Protean Waves</em> from Living
      Liquid.</p>
      <p>The Liquid Hand will also do a <em>Hand of Pain</em> here.</p>
      <ul>
        <li>
          <p><b>H1, H2, D3, D4:</b> Bait AoEs next to assigned puddles.</p>
          <p>If you plan on using a gap-closer, wait until you see the
          telegraphed <em>Protean Waves</em> from the puddles as they are
          <em>slightly</em> offset.</p>
        </li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_14.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>15.</b> 1st telegraphed <em>Protean Waves</em> from the puddles.</p>
      <ul>
        <li><b>D1, D2:</b> Prepare to bait the "west" and "east" puddles.</li>
        <li><b>H1, H2, D3, D4:</b> Move in to bait Living Liquid's <em>Protean
        Waves</em> after the puddle's telegraphs appear.</li>
      </ul>
      <p><em>(The East puddle's <em>Protean Wave</em> can be baited by either
      H2 or D4.)</em></p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_15.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>16.</b> 2nd untelegraphed <em>Protean Waves</em> from Living
      Liquid.</p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_16.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>17.</b> 2nd untelegraphed <em>Protean Waves</em> from the puddles.</p>
      <ul>
        <li><b>ST:</b> If you're confident on the party's DPS, you can
        alternatively bring the Liquid Hand "south" instead, but an Embolus may
        now go through the center if DPS is low.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_17.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>18.</b> Embolus orbs spawn.</p>
      <ul>
        <li><b>MT, ST:</b> Stack Living Liquid and the Liquid Hand together for
        <em>Hand of Parting</em> once the Liquid Hand glows as an open palm.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_18.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>19.</b> The Liquid Hand does one final <em>Hand of Pain</em>. If 
      the party went "all in" on Living Liquid, you need to kill Living Liquid
      before this <em>Hand of Pain</em> resolves.</p>
      <p>After the <em>Hand of Pain</em>, Living Liquid uses <em>Splash</em>
      six times before targeting the MT with <em>Fluid Swing</em>.</p>
      <p>Living Liquid then casts one final <em>Cascade</em>, serving as the
      enrage.</p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/01/living_liquid_19.jpg">
    </td>
  </tr>
</table>

---

## Troubleshooting

<details markdown=block>
<summary>
  <b>[Hand of Pain]</b> The MT invulns the first <em>Fluid Swing/Strike</em>
  and the <em>Protean Wave</em> from the puddle, but dies shortly thereafter.
  What happened?
</summary>
<table>
  <tr>
    <td>
      <p>The MT possibly died to <em>Hand of Pain</em>, which shortly follows
      the <em>Protean Wave</em>. <em>Hand of Pain</em> ignores tank
      invulnerabilities.</p>
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
